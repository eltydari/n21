import argparse
from collections import namedtuple, deque
from copy import copy
import os.path
from pprint import pprint
import re

WORD_PATTERN = re.compile(r"([^,.:;?!\s]+)")
END = "\0"

Token = namedtuple("Token", ["line_num", "start_pos", "contents"])
Location = namedtuple("Token", ["line_num", "start_pos"])


class Tokenizer(object):
    def __init__(self, path):
        self.document = open(path)

    def __del__(self):
        self.document.close()

    def get_tokens(self):
        nline = 0
        for line in self.document:
            nline += 1
            spos = 0
            for word in WORD_PATTERN.finditer(line):
                spos += 1
                yield Token(nline, spos, word.groups()[0])


class TrieNode(object):
    def __init__(self):
        self._data = []
        self._children = {}
        self._terminal = False

    @property
    def values(self):
        return copy(self._data)

    @property
    def terminal(self):
        return self._terminal

    @property
    def children(self):
        return self._children.keys()

    def create_child(self, key, terminal=False):
        child = self._children.setdefault(key, TrieNode())
        if terminal:
            child.set_terminal()
        return child

    def add_value(self, value):
        self._data.append(value)

    def set_terminal(self):
        self._terminal = True

    def __getitem__(self, key):
        return self._children.get(key, None)

    def __repr__(self):
        keys = []
        for key in self._children.keys():
            if self[key].terminal:
                key += '*'
            keys.append(key)
        return "<TrieNode keys=[{}]>".format(','.join(keys))


class TrieParser(object):
    def __init__(self, path):
        self._root = TrieNode()
        self._queue = deque([END])
        with open(path) as config:
            for line in config:
                self._make_trie(self._root, line.split()[::-1])

    def parse(self, documentPath):
        tokens = Tokenizer(documentPath).get_tokens()
        for token in tokens:
            self._process_token(token)

    def get_stats(self):
        stats = []
        self._get_stats_recursive(self._root, stats, [])
        return stats

    def _get_stats_recursive(self, node, stats, name):
        for child in node.children:
            child_name = name + [child]
            child_node = node[child]
            if child_node.terminal:
                data = child_node.values
                str_name = " ".join(child_name)
                stats.extend(({
                    "Entry": str_name,
                    "LineNum": val.line_num,
                    "StartPos": val.start_pos
                } for val in data))
            else:
                self._get_stats_recursive(child_node, stats, child_name)

    def _make_trie(self, node, cfg_stack):
        current_stack = copy(cfg_stack)
        key = current_stack.pop()
        stack_empty = (len(current_stack) <= 0)
        child = node.create_child(key, terminal=stack_empty)
        if not stack_empty:
            self._make_trie(child, current_stack)

    def _process_token(self, token):
        word = token.contents

        rootMatch = self._root[word]
        if rootMatch is not None:
            location = Location(token.line_num, token.start_pos)

            if rootMatch.terminal:
                rootMatch.add_value(location)
            else:
                self._queue.appendleft((rootMatch, location))

        prevMatchTuple = self._queue.pop()
        while prevMatchTuple != END:
            prevMatch, loc = prevMatchTuple
            match = prevMatch[word]
            if match is not None:
                if match.terminal:
                    match.add_value(loc)
                else:
                    self._queue.appendleft((match, loc))
            prevMatchTuple = self._queue.pop()

        self._queue.appendleft(END)


def main():
    parser = argparse.ArgumentParser(description='Process a file looking for specific words/phrases.')
    parser.add_argument('documentPath', type=str, help='Path to the document to be processed.')
    parser.add_argument('--configPath', default=os.path.join(".", "config", "config.txt"),
                        help='Path to the configuration file containing words/phrases.')

    args = parser.parse_args()

    parser = TrieParser(args.configPath)
    parser.parse(args.documentPath)
    pprint(parser.get_stats())


if __name__ == "__main__":
    main()
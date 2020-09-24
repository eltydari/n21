import argparse
from collections import namedtuple
from copy import copy
import os.path
import re

WORD_PATTERN = re.compile(r"([^,.:;?!\s]+)")
END = "\0"

Token = namedtuple("Token", ["line_num", "start_pos", "contents"])


class Tokenizer(object):
    def __init__(self, path):
        self.document = open(path)

    def __del__(self):
        self.document.close()

    def get_tokens(self):
        nline = 0
        while True:
            nline += 1
            spos = 0
            line = self.document.next()
            for word in WORD_PATTERN.finditer(line):
                spos += 1
                yield Token(nline, spos, word.groups()[0])


class TrieNode(object):
    def __init__(self):
        self.__data = []
        self.__children = {}
        self.__terminal = False

    @property
    def values(self):
        return copy(self.__data)

    @property
    def terminal(self):
        return self.__terminal

    def create_child(self, key, terminal=False):
        child = self.__children.setdefault(key, TrieNode())
        if terminal:
            child.set_terminal()
        return child

    def add_value(self, value):
        self.__data.append(value)

    def set_terminal(self):
        self.__terminal = True

    def __getitem__(self, key):
        return self.__children.get(key, None)

    def __repr__(self):
        keys = []
        for key in self.__children.keys():
            if self[key].terminal:
                key += '*'
            keys.append(key)
        return "<TrieNode keys=[{}]>".format(','.join(keys))


class TrieParser(object):
    def __init__(self, path):
        self._root = TrieNode()
        with open(path) as config:
            for line in config:
                self._make_trie(self._root, line.split()[::-1])

    def _make_trie(self, node, cfg_stack):
        current_stack = copy(cfg_stack)
        key = current_stack.pop()
        stack_empty = (len(current_stack) <= 0)
        child = node.create_child(key, terminal=stack_empty)
        if not stack_empty:
            self._make_trie(child, current_stack)


def main():
    parser = argparse.ArgumentParser(description='Process a file looking for specific words/phrases.')
    parser.add_argument('documentPath', type=str, help='Path to the document to be processed.')
    parser.add_argument('--configPath', default=os.path.join(".", "config.txt"),
                        help='Path to the configuration file containing words/phrases.')

    args = parser.parse_args()

    parser = TrieParser(args.configPath)
    print(parser._root)


if __name__ == "__main__":
    main()
import argparse
import os.path
import re

WORD_PATTERN = re.compile(r"([^,.:;?!\s]+)")


class Tokenizer(object):
    def __init__(self, path):
        self.document = open(path)

    def __del__(self):
        self.document.close()

    def getTokens(self):
        while True:
            line = self.document.next()
            for word in WORD_PATTERN.finditer(line):
                yield word.groups()[0]


class TrieParser(object):
    def __init__(self, path):
        pass

    def _make_trie(self, str_in):
        pass


def main():
    parser = argparse.ArgumentParser(description='Process a file looking for specific words/phrases.')
    parser.add_argument('documentPath', type=str, help='Path to the document to be processed.')
    parser.add_argument('--configPath', default=os.path.join(".", "config.txt"),
                        help='Path to the configuration file containing words/phrases.')

    args = parser.parse_args()

    parser = TrieParser(args.configPath)
    for token in Tokenizer(args.documentPath).getTokens():
        print token


if __name__ == "__main__":
    main()
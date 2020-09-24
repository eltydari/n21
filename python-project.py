import argparse
import os.path


class Tokenizer(object):
    def __init__(self, path):
        pass

    def nextToken(self):
        pass


class TrieParser(object):
    def __init__(self, path):
        pass

    def _make_trie(self, str_in):
        pass


def main():
    parser = argparse.ArgumentParser(description='Process a file looking for specific words/phrases.')
    parser.add_argument('documentPath', type=str, help='Path to the document to be processed.')
    parser.add_argument('--configPath', default=os.path.join(".", "config.txt"),
                        help='Path to the configuration file containg words/phrases.')

    args = parser.parse_args()
    with open(args.documentPath) as f:
        print(f.read())
    print(args.documentPath)
    with open(args.configPath) as f:
        print(f.read())
    print(args.configPath)

if __name__ == "__main__":
    main()
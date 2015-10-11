#!/usr/bin/env python3

import sys

def main(argv):
    with open(argv[1], 'r') as fp:
        buf = fp.read(4096)
        while buf:
            sys.stdout.write(buf)
            buf = fp.read(4096)

if __name__ == "__main__":
    sys.exit(main(sys.argv))

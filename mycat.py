#!/usr/bin/env python3

import sys

def main(argv):
    try:
        with open(argv[1], 'r') as fp:
            buf = fp.read(4096)
            while buf:
                sys.stdout.write(buf)
                buf = fp.read(4096)
    except Exception as exc:
        print("Error:", str(exc))
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))

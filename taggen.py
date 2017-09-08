#!/usr/bin/python3

import hmac
import sys

def gen_tag(msg, key):
    hm = hmac.new(key.encode())
    hm.update(msg.encode())
    return hm.hexdigest()

def usage():
    print("Usage: {} <msg> <name>".format(sys.argv[0]))

if __name__ == '__main__':
    if not sys.argv[2:]:
        usage()
        sys.exit(0)

    msg = sys.argv[1]
    filename = sys.argv[2] + '.key'

    with open(filename) as f:
        key = f.read()

    t = gen_tag(msg, key)
    print(msg + ':' + t)


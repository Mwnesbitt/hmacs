#!/usr/bin/python3
#Mark Nesbitt
#20170901

import hmac
import sys

def validate(text, key):
    hm = hmac.new(key.encode())
    hm.update(parseline(text, 'msg').encode())
    return hm.hexdigest() == parseline(text, 'digest')

def parseline(text, desired):
    if desired == 'msg':
        return text[:text.index(":")]
    else:
        return text[text.index(":")+1:]

def main():
    if not len(sys.argv)==3:
        print("Usage: "+sys.argv[0]+" messagefile keyfile")
        sys.exit(1)

    messagefile = sys.argv[1]
    keyfile = sys.argv[2]
    k = open(keyfile, 'r')
    key = k.read()
    k.close()

    out = open("imposters", 'w')
    with open(messagefile, 'r') as f:
        for line in f.read().splitlines():
            if not validate(line, key):
                print(parseline(line, 'msg'), file = out)
    out.close()

if __name__ == '__main__':
    main()

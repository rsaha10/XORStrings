import sys

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

if len(key) > len(inp):
    key = key[:len(inp)]

if len(key) < len(inp):
    org = key
    rem = len(inp) % len(key)
    add = key[:rem]

    times = int(len(inp) / len(key))
    for i in times-1:
        key = key + org
    key = key + add

import sys

mode = sys.argv[1]
key = sys.argv[2]
inp = sys.argv[3]
#key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
#inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
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
    for i in range(times-1):
        key = key + org
    key = key + add

key0 = key.encode('utf-8')
keyy = key0.hex()
inp0 = inp.encode('utf-8')
inp1 = inp0.hex()

xor = hex(int(keyy, 16) ^ int(inp1, 16))
xor1 = (xor[2:])


if mode == "human":
    bytes_object = bytes.fromhex(xor1)
    ascii_string = bytes_object.decode("ASCII")
    print(ascii_string)

if mode == "numOut":
    print (xor1)

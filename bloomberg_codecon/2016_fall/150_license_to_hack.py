#Problem        : License to Hack
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

crypt = data[0]
N = int(data[1])
res = []
rev = True
i = 0

while i < len(crypt):
    value = crypt[i:min(i+N, len(crypt))]
    if rev:
        value = value[::-1]
    res.append(str(value))
    
    rev = not rev
    i+=N
    
print(''.join(res))

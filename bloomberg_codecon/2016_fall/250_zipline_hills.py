#Problem        : Zipline Hills
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys


def path_length(index, hills):
    val = hills[index]
    
    n_inf = float("-inf")
    ll = n_inf
    l = n_inf
    r = n_inf
    rr = n_inf
    
    if index - 2 > 0 and hills[index - 2] < val:
        ll = path_length(index - 2, hills)
    
    if index - 1 > 0 and hills[index - 1] < val:
        l = path_length(index - 1, hills)
        
    if index + 2 < len(hills) and hills[index + 2] < val:
        rr = path_length(index + 2, hills)
        
    if index + 1 < len(hills) and hills[index + 1] < val:
        r = path_length(index + 1, hills)
        
        
    if ll != n_inf or rr != n_inf or l != n_inf or r != n_inf:
        return max(ll, l, r, rr) + 1
    else:
        return 0

data = sys.stdin.read().splitlines()
        
        
N = int(data[0])

hills = data[1:]
hills = [int(x) for x in hills]

best = -1

for i in range(N):
    dist = path_length(i, hills)
    
    if dist > best:
        best = dist
        
        
print(best)
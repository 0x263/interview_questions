#Problem        : Chemistry 101
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()


N = int(data[0])
proposal = data[N+1].split(' ')

tb = {}

for i in range(1, N+1):

    cur = data[i].split(' ')
    key = cur[0]
    count = int(cur[1])
    
    reqs = []
    
    for j in range(2, count+2):
        reqs.append(cur[j])
        
    tb[key] = reqs
        
        
        
# Checking
#success = True
deposit = set()
for i in range(len(proposal)):
    if proposal[i] in tb:
        for j in tb[proposal[i]]:
            if j not in deposit:
                print("BOOM!")
                sys.exit()
    
    deposit.add(proposal[i])
    
    
print("SAFE!")
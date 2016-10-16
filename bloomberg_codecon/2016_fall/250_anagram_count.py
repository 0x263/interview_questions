#Problem        : Anagram Count
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

count = int(data[0])
tables = []

for i in range(1, count+1):
    cur = {}
    for c in data[i]:
        c = c.lower()
        if c in cur:
            cur[c] = cur[c] + 1
        else:
            cur[c] = 1
            
    tables.append(cur)

done_indices = set()
res = 0

for i in range(0, count-1):
    first = True
    if i in done_indices:
        continue
    
    for j in range(i+1, count):
        if tables[i] == tables[j]:
            done_indices.add(i)
            done_indices.add(j)
            if first:
                res += 2
                first = False
            else:
                res += 1
            
            
print(res)
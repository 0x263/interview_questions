#Problem        : Zombie Ambulance
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT


# ~~~~~~~~~~~~~~~~~~~~~~ NOTE ~~~~~~~~~~~~~~~~~~~~~~
# This solution is not correct and does not pass all cases

import sys


def calc_dist(hospital, target):
    if int(hospital[0] / 10) == int(target[0] / 10) and hospital[1] != target[1]:
        neg = hospital[0] % 10 + target[0] % 10
        pos = (10 - hospital[0] % 10) + (10 - target[0] % 10)
        
        return min(neg, pos) + abs(hospital[1] - target[1])
    elif int(hospital[1] / 10) == int(target[1] / 10) and hospital[0] != target[0]:
        neg = hospital[1] % 10 + target[1] % 10
        pos = (10 - hospital[1] % 10) + (10 - target[1] % 10)
        
        return min(neg, pos) + abs(hospital[0] - target[0])
    else:
        return abs(hospital[0] - target[0]) + abs(hospital[1] - target[1])

    
    return dist

data = sys.stdin.read().splitlines()

values = data[0].split(' ')
X = int(values[0])
Y = int(values[1])
T = int(values[2])
N = int(values[3])

patients = []

hosp = (X, Y)

for i in range(1, N+1):
    values = data[i].split(' ')
    
    xy = (int(values[1]), int(values[2]))
    dist = calc_dist(hosp, xy)
    
    patients.append((dist, values[0]))
    
    

l_pat = sorted(patients)
visited = []
time = 0

for i in range(len(l_pat)):
    cost = l_pat[i][0] * 2
    
    if time + cost <= T:
        time += cost
        visited.append(l_pat[i][1])
    else:
        break
    
    
print(str(len(visited)) + ' ' + ' '.join(visited))
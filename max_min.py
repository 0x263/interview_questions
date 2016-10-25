"""
Given a list of n integers, your task is to select k integers from the list such
that its unfairness is minimized.

the unfairness is defined as:
max(x1, x2, x3, ..., xk) - min(x1, x2, x3, ..., xk)

Input Format
The first line contains an integer N.
The second line contains an integer K.
N lines follow. Each line contains an integer that belongs to the list .

Note: Integers in the list N may not be unique.

Output Format
An integer that denotes the minimum possible value of unfairness.

Sample Input #00

7
3
10
100
300
200
1000
20
30

Sample Output #00

20

Explanation #00
Here K = 3; selecting the 3 integers such that K = 10, 20, 30, unfairness equals

max(10,20,30) - min(10,20,30) = 30 - 10 = 20

Sample Input #01

10
4
1
2
3
4
10
20
30
40
100
200

Sample Output #01

3

Explanation #01
Here K = 4; selecting the 4 integers 1, 2, 3, 4, unfairness equals

max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3

Sample Input #02

6
3
10
20
30
100
101
102

Sample Output #02

2

Explanation #02

Here K = 3; the 3 integers so that the difference between the maximum and the
minimum is the smallest are 100, 101, 102, which means unfairness equals

max(100, 101, 102) - min(100, 101, 102) = 102 - 100 = 2
"""


def minimize_unfairness(input_list, k):
    sorted_list = sorted(input_list)

    diff = sorted_list[k - 1] - sorted_list[0]
    first = 1
    last = k

    min_diff = float("inf")
    for i in range(len(input_list) - k + 1):
        min_diff = min(min_diff, sorted_list[i + k - 1] - sorted_list[i])

    return min_diff

"""
When you need to find a sequence of k numbers such that unfairness is minimized.
"""


def simple_min_unfairness(input_list, k):
    high = 0
    low = 0
    min_ndx = 0
    max_ndx = 0

    while high < k:
        if input_list[high] >= input_list[max_ndx]:
            max_ndx = high

        if input_list[high] <= input_list[min_ndx]:
            min_ndx = high

        high += 1

    low += 1
    diff = input_list[max_ndx] - input_list[min_ndx]

    while high < len(input_list):
        if min_ndx < low:
            temp = low
            min_ndx = low
            while temp < high:
                if input_list[temp] <= input_list[min_ndx]:
                    min_ndx = temp

                temp += 1

        if max_ndx < low:
            temp = low
            max_ndx = low
            while temp < high:
                if input_list[temp] >= input_list[max_ndx]:
                    max_ndx = temp

                temp += 1

        if input_list[high] >= input_list[max_ndx]:
            max_ndx = high

        if input_list[high] <= input_list[min_ndx]:
            min_ndx = high

        diff = min(input_list[max_ndx] - input_list[min_ndx], diff)

        high += 1
        low += 1

    return diff

if __name__ == '__main__':
    num_lines = int(input())
    num = int(input())

    input_list = []
    for i in range(num_lines):
        input_list.append(int(input()))

    # unfair = MinUnfairness()

    print(minimize_unfairness(input_list, num))

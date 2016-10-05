"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
"""


def get_products(numbers):
    l1 = []
    l2 = []

    for i in range(len(numbers)):
        if i == 0:
            l1.append(numbers[i])
        else:
            t = l1[len(l1) - 1]
            l1.append(t * numbers[i])

    temp = numbers
    temp.reverse()

    for i in range(len(temp)):
        if i == 0:
            l2.append(temp[i])
        else:
            t = l2[len(l2) - 1]
            l2.append(t * temp[i])

    l2.reverse()

    ans = []

    for i in range(len(numbers)):
        if i == 0:
            ans.insert(i, l2[i + 1])
        elif i == len(numbers) - 1:
            ans.insert(i, l1[i - 1])
        else:
            ans.insert(i, l1[i - 1] * l2[i + 1])

    return ans


def test():
    t = [1, 7, 3, 4]
    print(get_products(t))


if __name__ == "__main__":
    test()

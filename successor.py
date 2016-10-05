"""
Given a node in a binary search tree, return it's in order successor.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.ans = None

    def successor(self, root, node):
        self.wrapper(root, node, False)
        return self.ans

    def wrapper(self, root, node, flag):
        if not root:
            return

        self.wrapper(root.left, node, flag)

        if flag:
            self.ans = root.data
            print(self.ans)

        if root == node:
            flag = True
            print(root.data)

        self.wrapper(root.right, node, flag)

        return

    def test(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        seven = Node(7)
        eight = Node(8)

        five.left = three
        five.right = seven
        three.left = two
        three.right = four
        two.left = one
        seven.left = six
        seven.right = eight

        print(self.successor(five, three))  # should return 4.

if __name__ == "__main__":
    sol = Solution()
    sol.test()

"""
Given a node in a binary search tree, return it's in order successor.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def successor(root, node):
    ans = None
    wrapper(root, node, False, ans)
    return ans


def wrapper(root, node, flag, ans):
    if not root:
        return

    wrapper(root.left, node, flag, ans)
    if flag:
        ans = root.data

    if root.data == node.data:
        flag = True

    wrapper(root.right, node, flag, ans)
    return


def test():
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

    print(successor(five, three))

if __name__ == "__main__":
    test()

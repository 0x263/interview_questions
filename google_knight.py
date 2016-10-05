"""
Given a 8 x 8 chess board, find the minimum number of moves required to move
from source to destination given you can only move like a knight.
That is move only in L motions. The chess board is indexed from 0 to 63.
"""


def answer(src, dest):
    x, y = (int(src / 8), src % 8)
    src_coord = (x, y)
    q = [(x, y)]
    parent = {}
    curr = q.pop(0)
    visited = []
    dest_coord = (int(dest / 8), dest % 8)

    while curr != dest_coord:
        x, y = curr
        visited.append(curr)
        adj = [(x - 2, y - 1), (x - 2, y + 1), (x + 2, y - 1), (x + 2, y + 1),
               (x - 1, y - 2), (x - 1, y + 2), (x + 1, y - 2), (x + 1, y + 2)]

        for neighbor in adj:
            x1, y1 = neighbor
            if x1 < 0 or y1 < 0 or x1 > 7 or y1 > 7:
                continue

            q.append(neighbor)
            if neighbor not in parent:
                parent[neighbor] = curr

        curr = q.pop(0)
        while curr in visited:
            curr = q.pop(0)

    temp = curr
    count = 0

    while temp != src_coord:
        print(temp)
        temp = parent[temp]
        count += 1

    return count

if __name__ == "__main__":
    print(answer(0, 1))

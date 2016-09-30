def copy_ll(head):
    prev = {}       # in case our rand_next points to a node is in the back of the list
    future = {}     # our rand_next pointer is not seen yet so we keep track of
    # a list of nodes that we will eventually create and will need to go back
    # and set the rand_next for
    cur_old = head
    prev_new = None

    while cur_old is not None:
        cur_new = Node(cur_old.data)

        # Keep track of this node's mapping from old -> new
        prev[cur_old] = cur_new

        # Check if this was a rand_next that we now just created (future)
        if cur_old in future:
            for f in future[cur_old]:
                f.rand_next = cur_new

        if cur_old.rand_next is not None:
            if cur_old.rand_next in prev:
                cur_new.rand_next = prev[cur_old.rand_next]
            else:
                if cur_old.rand_next in future:
                    future[cur_old.rand_next].append(cur_new)
                else:
                    future[cur_old.rand_next] = [cur_new]

        if prev_new is not None:
            prev_new.next = cur_new

        prev_new = cur_new
        cur_old = cur_old.next


def copylist(head):
    cmap = {}
    rmap = {}

    prev = None
    curr = head
    curr_new = None

    while curr:
        curr_new = Node(curr.data)
        cmap[curr] = curr_new
        fmap[curr_new] = curr.rand

        if prev:
            prev.next = curr_new

        prev = curr_new
        curr = curr.next

    curr_new = cmap[head]

    while curr_new:
        curr_new.rand = cmap[fmap[curr_new]]
        curr_new = curr_new.next

    return cmap[head]

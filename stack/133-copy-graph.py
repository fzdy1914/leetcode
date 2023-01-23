class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        seen_old = dict()

        lst = [node]

        while len(lst) > 0:
            cur = lst[-1]
            if cur is None:
                return None

            if cur.val not in seen_old:
                # TODO: copy need to copy list, remember, always copy the list!!!!!!!!!!!
                seen_old[cur.val] = Node(cur.val, cur.neighbors.copy())

                for n in cur.neighbors:
                    if n.val not in seen_old:
                        lst.append(n)
            else:
                n = lst.pop()
                to_update = seen_old[n.val]
                for i in range(len(n.neighbors)):
                    to_update.neighbors[i] = seen_old[to_update.neighbors[i].val]

                if n == node:
                    return seen_old[node.val]
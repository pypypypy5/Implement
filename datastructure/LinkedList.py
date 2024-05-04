class LkdList:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def pop(self):
        self.prev.next = self.next
        self.next.prev = self.prev


def new_circular_Lkd(seq):
    for i in range(len(seq)):
        if i == 0:
            node_first = LkdList([i+1,seq[i]], None, None)
            node_prev = node_first
        elif i == len(seq) - 1:
            node = LkdList([i+1,seq[i]],node_prev,node_first)
            node_first.prev = node
            node_prev.next = node
        else:
            node = LkdList([i+1,seq[i]],node_prev,None)
            node_prev.next = node
            node_prev = node

    return node_first
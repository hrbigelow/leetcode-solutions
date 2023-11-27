class SparseMap:
    def __init__(self, valmap):
        self.vmap = valmap

    def dot(self, other):
        ixn = set(self.vmap.keys()).intersection(other.vmap.keys())
        return sum(self.vmap[k] * other.vmap[k] for k in ixn)


class SparseAry:
    def __init__(self, valmap):
        self.keys, self.vals = list(zip(*valmap.items()))

    def dot(self, other):
        n1 = len(self.keys)
        n2 = len(other.keys)
        i, j = 0, 0
        total = 0.0
        while i != n1 and j != n2:
            if self.keys[i] < other.keys[j]:
                i += 1
            elif other.keys[j] < self.keys[i]:
                j += 1
            else:
                total += self.vals[i] * other.vals[j]
        return total






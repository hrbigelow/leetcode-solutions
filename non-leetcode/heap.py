
# transform 'a' into a min-heap in place    
def heapify(a):
    n = len(a)
    for i in range(2, n+1):
        _bubble_up(a, i)

# 
def insert(h, v):
    h.append(v)
    _bubble_up(h, len(h))


def delete_min(h):
    if len(h) == 0:
        return None
    ret = h[0]
    h[0] = h[-1]
    h.pop()
    _bubble_down(h, len(h))
    return ret

# bubble the root down
def _bubble_down(h, n):
    u = 0
    l = 1 if n < 3 or h[1] < h[2] else 2

    while l < n and h[u] > h[l]:
        h[u], h[l] = h[l], h[u]
        u = l
        l = u * 2 + 1
        if l + 1 < n and h[l+1] < h[l]:
            l = l + 1


# bubble the last element up
def _bubble_up(h, n):
    l = n - 1
    u = (l + 1) // 2 - 1
    while u > -1 and h[l] < h[u]:
        h[u], h[l] = h[l], h[u]
        l = u
        u = (u + 1) // 2 - 1


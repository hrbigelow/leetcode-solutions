"""
Given an array a of integers, return an array l such that:
l[i] = largest j < i such that a[j] < a[i], or -1 if not exists

"""
def longestLeftCeiling(a):
    st = [(-1, float('-inf'))]
    llc = [None] * len(a)
    
    for i, el in enumerate(a):
        while st[-1][1] >= el: st.pop()
        llc[i] = st[-1][0]
        st.append((i, el))

    return llc


def longestLeftCeilingTest(a):
    # brute force approach
    n = len(a)
    l = [-1] * n
    for i in range(n):
        j = i-1
        while j != -1:
            if a[j] < a[i]:
                break
            j -= 1
        l[i] = j

    return l


# return the area of the maximum rectangle that
# would fit under the skyline defined by 'a'
# The skyline is piecewise constant, with segments
# (i, a[i]) -> (i+1, a[i])

"""
Approach:

1.  The area of the maximum rectangle fitting under the skyline must end at
some position i in [0, n).  So, instead we can find, for each i, the maximum
area rectangle that fits under the skyline which ends at i.



"""
def maxRectUnderSkyline(a):
    st = [(-1, -1)]
    a.append(0)
    m = 0
    for i, el in enumerate(a):
        while st[-1][1] > el:
            pre_i, pre_l = st.pop()
            m = max(m, pre_l * (i - pre_i))
        else:
            pre_i = i
        if st[-1][1] < el:
            st.append((pre_i, el))

    return m


def maxRectUnderSkylineTest(a):
    m = 0
    n = len(a)
    for i, h in enumerate(a):
        for j in range(i+1, n):
            h2 = a[j]
            if h > h2:
                m = max(m, h * (j - i))
                break

    return m

    

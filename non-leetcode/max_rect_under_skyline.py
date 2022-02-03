# return the area of the maximum rectangle that
# would fit under the skyline defined by 'a'
def maxRectUnderSkyline(a):
    st = [(-1, -1)]
    a.append(0)
    m = 0
    for i, el in enumerate(a):
        while st[-1][1] > el:
            pre_i, pre_l = st.pop()
            m = max(m, pre_l * (i - pre_i))
        if st[-1][1] < el:
            st.append((i, el))

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

    

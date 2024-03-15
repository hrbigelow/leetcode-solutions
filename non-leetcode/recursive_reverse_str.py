def reverse_str1(s):
    ary = [None] * len(s)
    def reverse(i):
        if i == len(ary):
            return ''.join(ary)
        ary[i] = s[-i-1]
        return reverse(i+1)
    return reverse(0)

s = 'abcde'


def reverse_str2(s):
    ary = []
    def reverse(i):
        if i == len(s):
            return ''.join(ary)
        ary.append(s[-i-1])
        return reverse(i+1)
    return reverse(0)

"""
In this case, we 
"""
def reverse_str3(s):
    def reverse(ary):
        if len(ary) == len(s):
            return ''.join(ary)
        ary.append(s[-len(ary)-1])
        return reverse(ary)
    return reverse([])


def reverse_str4(s):
    def reverse(output, input):
        if not input:
            return ''.join(output)
        output.append(input.pop())
        return reverse(output, input)
    return reverse([], list(s))

print(reverse_str1(s))
print(reverse_str2(s))
print(reverse_str3(s))
print(reverse_str4(s))




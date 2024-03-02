"""
we can solve this by knowing that a number can be decomposed into:
a * 10 ^ 0 + a2 * 10 ^ 1 + a3 * 10 ^ 2...
"""
def str_2_int(s, index = 0):
    length = len(s)
    if index == length - 1:
        return int(s[index])
    else:
        return int(s[index]) * 10**(length - index - 1) + str_2_int(s, index + 1)

ans = str_2_int('123')
print(ans, type(ans))

# Time: O(N)
# Space: O(N)
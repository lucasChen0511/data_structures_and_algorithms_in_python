def rec_find_max(S, index):
    if index == len(S) - 1:
        return S[index]
    return max(S[index], rec_find_max(S, index + 1))

def find_max(S):
    return rec_find_max(S, 0)

print(find_max([1,2,4,5,6,7,8,9]))
print(find_max([1,2,99, 3,4,5]))
print(find_max([10,7,6,4,3,2,1]))

# Time: O(N)
# Space: O(N)
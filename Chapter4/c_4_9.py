def find_min_max(S, index=0):
    if index == len(S) - 1:
        return S[index], S[index]
    else:
        min_c, max_c = find_min_max(S, index + 1)
        return min(S[index], min_c), max(S[index], max_c)

print(find_min_max([1,2,4,5,6,7,8,8,9]))
print(find_min_max([-19, 8, 883,19,28,3]))
print(find_min_max([9,8,6,5,4,3,2,1]))
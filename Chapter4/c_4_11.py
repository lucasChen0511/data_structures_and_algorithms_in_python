def unique_num(S, index= 0):
    if index == len(S) - 1:
        return True
    else:
        unique = True
        for i in range(index + 1, len(S)):
            if S[index] == S[i]: unique = False
        
        return unique and unique_num(S, index + 1)

for S in [[1,2,4,5,6,7], [3,4,5,34,6,3,2],
          [234,454,23,63,432]]:
    print(unique_num(S))
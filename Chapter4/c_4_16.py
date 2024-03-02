def reversestring(S, index=0):
    if index == len(S) -1:
        return [S[index]]
    else:
        ans = reversestring(S, index + 1)
        ans.append(S[index])
        if index == 0:
            ans = ''.join(ans)
        return ans
print(reversestring('pot&pans'))
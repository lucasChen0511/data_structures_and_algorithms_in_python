# Write a Python program that outputs all possible strings formed by using the
# characters c, a, t, d, o, and g exactly once.
ans = []

def permute(s):
    used = [False] * len(s)
    track = []
    backtrack(s, track, used)
    return ans


def backtrack(s, track, used):
    if len(track) == len(s):
        ans.append(list(track))
        return
    
    for i in range(len(s)):
        if used[i]:
            continue
        used[i] = True
        track.append(s[i])
        backtrack(s, track, used)
        used[i] = False
        track.pop()
    
print(len(permute(['c', 'a', 't', 'd', 'o', 'g'])))


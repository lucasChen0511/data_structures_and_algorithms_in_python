def query_index(s):
    n = len(s)
    for k in range(-1, -n, -1):
        j = n + k
        print(s[k], s[j])

print(query_index("hello, world"))
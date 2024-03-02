def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n - 1)

# Time: O(N)
# Space: O(N)
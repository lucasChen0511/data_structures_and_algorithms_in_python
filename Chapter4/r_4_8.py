import math

def isabel(A):
    assert math.log(len(A), 2) % 1 == 0, 'Your array must be a length that is a power of 2'

    if len(A) == 1:
        return A[0]
    else:
        B = [None] * (len(A) // 2)
        for i in range(len(B)):
            B[i] = A[2*i] + A[2*i + 1]
        print(B)
        return isabel(B)

print(isabel([0,1,2,3]))

"""
The recursion will be called log(N) times, since the array is divided in half each time

Each call will required you to access all of the remaining elements, which means it will
be n + n/2 + n/4 + ...

This is equal to n * sum(1/2**i), which is < 2n
Therefore, the running time is O(N)
"""
# Time: O(N)

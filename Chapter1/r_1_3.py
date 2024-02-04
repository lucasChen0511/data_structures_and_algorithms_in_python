def minmax(data):
    min, max = float("inf"), float("-inf")
    for val in data:
        min = val if val < min else min
        max = val if val > max else max
    return min, max

data = [-65,2,3,4,5,85,7,8,9,10]
print(minmax(data))
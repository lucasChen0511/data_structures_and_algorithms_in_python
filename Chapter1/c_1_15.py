def is_distinct(list):
    s = set(list)
    return len(list) == len(s)

print(is_distinct([1,3,6,7,4,3,0]))
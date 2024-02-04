l = [1,2,3,4]

try:
    l[8] = 5
except:
    print("Don't try buffer overflow attacks in Python!")
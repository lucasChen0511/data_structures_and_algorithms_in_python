import math

def log_2_int(n):
    if n < 2:
        return 0
    else:
        return 1 + log_2_int(n//2)

for n in [100,5, 7, 1.8, 0.1, 7]:
    print(n, log_2_int(n), math.log(n, 2))
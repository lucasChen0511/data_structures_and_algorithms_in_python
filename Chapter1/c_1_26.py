def can_add(a, b, c):
    if a == b+c:
        return True
    if b == a+c:
        return True
    if c == a+b:
        return True
def can_subtract(a, b, c):
    if a == b - c:
        return True
    if b == a - c:
        return True
    if c == a - b:
        return True

def can_multiply(a, b, c):
    if a == b * c:
        return True
    if b == a * c:
        return True
    if c == a * b:
        return True

def can_divide(a, b, c):
    if a == b/c:
        return True
    if b == a/c:
        return True
    if c == a/b:
        return True

def can_power(a, b, c):
    if a == b ** c:
        return True
    if b == a ** c:
        return True
    if c == a ** b:
        return True

def arithmetic_order(a, b, c):
    i = can_add(a, b, c)
    j = can_subtract(a, b, c)
    k = can_multiply(a, b, c)
    l = can_divide(a, b ,c)
    m = can_power(a, b, c)
    if i or j or k or l or m:
        return True
    else:
        return False
print(arithmetic_order(9, 2, 82))
def birthday_paradox(n):
    prob = 1
    for i in range(0, n):
        prob *= (365-i) / 365
    return i - prob

print(birthday_paradox(22))
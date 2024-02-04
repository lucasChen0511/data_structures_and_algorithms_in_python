def squr(n):
    data = [i * i for i in range(1, n + 1) if i % 2 != 0]
    print(data)

squr(10)
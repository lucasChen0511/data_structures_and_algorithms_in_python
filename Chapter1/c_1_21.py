def reverse_line():
    lines = []
    while True:
        print("Enter: ")
        x = input()
        if x == '':
            break
        lines.append(x)
    lines = reversed(lines)
    for line in lines:
        print(line)

reverse_line()
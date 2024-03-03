from array_stack import ArrayStack


def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.puth(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()

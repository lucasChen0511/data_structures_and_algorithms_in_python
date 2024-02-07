#--------------P2-33---------------
class Polynomial:
    def __init__(self, len=3):
        self._coords = [0] * len
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Index overflow')
        return self._coords[index]
    def __repr__(self):
        output_str = []
        for i in range(len(self)):
            output_str.append(f'{self[i]}x^{i} ')
        return ''.join(output_str)
    def __setitem__(self, index, val):
        try:
            self._coords[index] = val
        except Exception as e:
            print(e)
    def derivative(self):
        ans = Polynomial(len(self) - 1)
        for i in range(1, len(self)):
            ans[i - 1] = self[i] * i
        return ans

if __name__ == '__main__':
    p = Polynomial(10)
    for i in range(len(p)):
        p[i] = i
    print(p)

    print(p.derivative())
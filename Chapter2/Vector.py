class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            self._coords = d
    
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(self)
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords

    def __nq__(self, other):
        return not self == other
    
    def __str__(self):
        return '<' + str(self._coords)[1: -1] + '>'
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        result = Vector(self)
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(self)
        for i in range(len(self)):
            result[i] = self[i] * -1
        return result
    
    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * len(other)
        return sum(result)

    def __rmul__(self,value):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = value * self[i]
        return result

if __name__ == '__main__':
    v1 = Vector(5)
    v2 = Vector(5)

    for i in range(5):
        v1[i] = 5
        v2[i] = i
    print(v1 * v2)
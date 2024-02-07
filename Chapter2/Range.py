class Range:
    def __init__(self, start, stop= None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start
        
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step
    
    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step
    
    def __contains__(self, val):
        factor, remainder = divmod((val - self._start), self._step)
        if remainder == 0:
            if 0 <= factor < len(self): return True
            else: return False
        else:
            return False

if __name__ == '__main__':
    r1 = Range(1, 100, 2)
    print(len(r1), r1[3], 4 in r1, 5 in r1)

    r2 = Range(-100, step=-1)
    print(len(r2), r2[3], 4 in r2, 5 in r2)
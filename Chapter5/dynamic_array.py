import ctypes

class DynamicArray:
    """ A dynamic array class akin to a simplified Python list. """

    def __init__(self) -> None:
        """ Create an empty array. """
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        """ Return number of elements stored in the array"""
        return self._n
    
    def __getitem__(self, k):
        """ Return element at index k. """
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self, obj):
        """ Add object to end of the array """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def _resize(self, c):
        """ Resize internal  array to capacity c. """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self, c):
        """ Return new array with capacity c. """
        return (c * ctypes.py_object)()
    
    def insert(self, k, val):
        """ Insert value at index k, shifting subsequent values rightward. """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[k] = self._A[j - 1]
        self._A[k] = val
        self._n += 1

    def remove(self, val):
        """ Remove first occurence of value (or raise ValueError). """
        for k in range(self._n):
            if self._A[k] == val:
                for j in range(k, self._n-1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('value not found')
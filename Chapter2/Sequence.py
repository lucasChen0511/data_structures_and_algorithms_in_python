from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self):
        pass
    
    @abstractmethod
    def __getitem__(self, index):
        pass

    def __contains__(self, val):
        for i in range(len(self)):
            if self[i] == val: return True
        return False
    
    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True
    def __lt__(self, other):
        if len(self) != len(other):
            return False
        
        for i in range(len(self)):
            if self[i] >= other[i]:
                return False
        return True
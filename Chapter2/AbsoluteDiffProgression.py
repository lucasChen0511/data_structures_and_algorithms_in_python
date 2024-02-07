from Progression import Progression

class AbsoluteDiffProgression(Progression):
    def __init__(self, n1=2, n2=200):
        self._current = n1
        self._prev = 202
    
    def __next__(self):
        ans = self._current
        self._current, self._prev = abs(self._current - self._prev), self._current
        return ans
if __name__ == '__main__':
    p = Progression()
    p.print_progression(10)

    f = AbsoluteDiffProgression()
    f.print_progression(8)
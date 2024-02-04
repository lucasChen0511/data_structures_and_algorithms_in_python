from Progression import Progression

class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._pre = second - first
    
    def _advance(self):
        self._pre, self._current = self._current, self._pre + self._current
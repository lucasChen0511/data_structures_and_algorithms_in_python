from Progression import Progression

class SQRTProgression(Progression):
    def __init__(self, start=65536):
        self._current = start
    
    def __next__(self):
        ans = self._current
        self._current = self._current ** 0.5
        return ans

    def __getitem__(self, index):
        return (self._current ** (1/(2**index)))
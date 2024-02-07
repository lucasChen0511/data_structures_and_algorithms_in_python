#---------------P2-35----------------
import random

class AliceBot:
    CHANCE_OF_ACTING = 0.3
    def __init__(self):
        self._current_packet = None
    
    def act(self):
        if random.random() <= self.CHANCE_OF_ACTING:
            self._current_packet = self._create_packet()
            return True
        return False
    
    def _create_packet(self):
        length = random.randint(5, 20)
        packet = [' '] * length
        for i in range(length):
            packet[i] = chr(random.randint(ord('A'), ord('z')))
        return ''.join(packet)
    
    def get_packet(self):
        return self._current_packet
    
    def delete_packet(self):
        self._current_packet = None

class InternetBot:
    def __init__(self):
        self._new_packet = False
        self._Alice = None
    
    def check_for_packet(self):
        if self._Alice.get_packet() is not None:
            return True
        return False

    def read_packet(self):
        if self._new_packet:
            return self._Alice.get_packet()
        return None
    
    def delete_packet(self):
        self._Alice.delete_packet()
    
    def assign_Alice(self, alice):
        self._Alice = alice

class BobBot:
    def check_for_packet(self, other):
        if other.check_for_packet():
            return True
        return False
    
    def delete_packet(self, other):
        other.delete_packet()

if __name__ == '__main__':
    Alice = AliceBot()
    Inter = InternetBot()
    Inter.assign_Alice(Alice)
    Bob = BobBot()

    for i in range(30):
        print(f'Time is {i}')
        if Alice.act():
            print('Created the packet', Alice.get_packet())
        if Bob.check_for_packet(Inter):
            print('Bob detected the packet')
            Bob.delete_packet(Inter)
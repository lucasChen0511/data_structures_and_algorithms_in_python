#---------------------P2-37-------------------
from RiverEcosystem import RiverEcosystem
import random

class RiverEcosystem2(RiverEcosystem):
    class Bear:
        def __init__(self, location):
            self._location = location
            self._strength = random.random()
            self._gender = True if random.random() > 0.5 else False
    
    class Fish:
        def __init__(self, location):
            self._location = location
            self._strength = random.random()
            self._gender = True if random.random() > 0.5 else False
    
    def _attempt_move(self, obj, target_location):
        if target_location < 0 or target_location >= len(self):
            return False
        elif self[target_location] is None:
            self[obj._location], self[target_location] = self[target_location], self[obj._location]
        elif type(obj) == type(self[target_location]):
            if obj._gender == self[target_location]._gender:
                self.assign_object(type(obj), 1)
            else:
                to_delete = min(obj, self[target_location], key= lambda x: x._strength)
                object_list = self._fish if isinstance(obj, self.Fish) else self._bears
                self._delete_object(to_delete, object_list)
        elif isinstance(obj, self.Fish):
            self._delete_object(obj, self._fish)
        elif isinstance(self[target_location], self.Fish):
            self._delete_object(self[target_location], self._fish)

if __name__ == '__main__':
    Game1 = RiverEcosystem2(100)
    print('Currently playing a game with 3 bears and 10 fish')
    for _ in range(40):
        print(Game1)
        Game1.timestep()
    print('\n\n')

    Game2 = RiverEcosystem2(100, 10, 10)
    print('Currently playing a game with 10 bears and 10 fish')
    for _ in range(40):
        print(Game2)
        Game2.timestep()
    
    b1, b2 = Game2._bears[0], Game2._bears[1]
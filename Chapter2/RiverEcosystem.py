#-----------------------P2-36--------------------------
import random

class RiverEcosystem:

    class Bear:
        def __init__(self, location):
            self._location = location
        
    class Fish:
        def __init__(self, location):
            self._location = location
    
    MOVE_CHANCE = 0.3
    LR_CHANCE = 0.5

    def __init__(self, length=100, bears=3, fish=10):
        self._ecosystem = [None] * length
        self._bears = self.assign_object(self.Bear, bears)
        self._fish = self.assign_object(self.Fish, fish)
        self._time = 0
    
    def __len__(self):
        return (len(self._ecosystem))
    
    def __getitem__(self, index):
        return self._ecosystem[index]
    
    def __setitem__(self, index, val):
        self._ecosystem[index] = val
    
    def assign_object(self, obj, num):
        assigned = 0
        object_list = []
        maximum_attempts = 100
        attempts = 0
        while assigned < num and attempts < maximum_attempts:
            attempts += 1
            i = random.randint(0, len(self) - 1)
            if self[i] is None:
                new_obj = obj(i)
                assigned += 1
                self[i] = new_obj
                object_list.append(new_obj)
        return object_list

    def __repr__(self):
        output_string = []
        for element in self._ecosystem:
            if element is None:
                output_string += '-'
            elif isinstance(element, self.Bear):
                output_string += 'B'
            elif isinstance(element, self.Fish):
                output_string += 'F'
            else:
                output_string += '?'
        return ''.join(output_string)
    
    def _delete_object(self, obj, obj_list):
        target = None
        for i in range(len(obj_list)):
            if obj is obj_list[i]:
                target = i
        if target is not None:
            del (obj_list[target])
    
    def _attempt_move(self, obj, target_location):
        if target_location < 0 or target_location >= len(self):
            return False
        elif self[target_location] is None:
            self[obj._location], self[target_location] = self[target_location], self[obj._location]
        elif type(obj) == type(self[target_location]):
            self.assign_object(type(obj), 1)
        elif isinstance(obj, self.Fish):
            self._delete_object(obj, self._fish)
        elif isinstance(self[target_location], self.Fish):
            self._delete_object(self[target_location], self._fish)
    
    def determine_action(self, obj):
        if random.random() < self.MOVE_CHANCE:
            if random.random() < self.LR_CHANCE:
                self._attempt_move(obj, obj._location - 1)
            else:
                self._attempt_move(obj, obj._location + 1)
    
    def timestep(self):
        self._time += 1
        for f in self._fish:
            self.determine_action(f)
        for b in self._bears:
            self.determine_action(b)

if __name__ == '__main__':
    Game1 = RiverEcosystem(100)
    print('Currently playing a game with 3 bears and 10 fish')
    for _ in range(40):
        print(Game1)
        Game1.timestep()
    print('\n\n')

    Game2 = RiverEcosystem(100, 10, 10)
    print('Currently playing a game with 10 bears and 20 fish')
    for _ in range(40):
        print(Game2)
        Game2.timestep()
import random


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        if isinstance(other, Fire):
            return Steam()
        if isinstance(other, Earth):
            return Mud()

class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lighting()
        if isinstance(other, Earth):
            return Dust()
        if isinstance(other, Water):
            return Storm()

class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Air):
            return Lighting()
        if isinstance(other, Water):
            return Steam()

class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Mud()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Lighting):
            return Golem()

class Storm:    # Water + Air
    output = 'Вода с воздухом дают шторм'

class Steam:    # Water + Fire
    output = 'Вода с огнем дают пар'

class Mud:      # Water + Earth
    output = 'Вода с землей дают грязь'

class Lighting: # Air + Fire
    def __add__(self, other):
        if isinstance(other, Earth):
            return Golem()
    output = 'Воздух с огнем дают молнию'

class Dust:     # Air + Earth
    output = 'Воздух с землей дают пыль'

class Lava:     # Fire + Earth
    output = 'Огонь с землей дают лаву'

class Golem:    #Lighting + Earth
    output = 'Молния с землей рождают голема'



TRY = 10

def magic():
    elements = [Water(), Air(), Fire(), Earth(), Lighting()]
    try_count = 0
    while try_count < TRY:
        first_el = random.choice(elements)
        second_el = random.choice(elements)
        magic_el = first_el + second_el
        if magic_el is None:
            print('Упс, не получилось! ¯\_(ツ)_/¯')
            print('*' * 33)
            continue
        try_count += 1
        print(magic_el.output)
        print('*' * 33)


if __name__ == '__main__':
    magic()

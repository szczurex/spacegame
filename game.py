# -*- coding: UTF-8 -*-
"""
    Small game idea

    Legend:
    ▓ - Empty space (undiscovered)
    ░ - Empty space (discovered)
    ◎ - SpaceShip
    ◌ - Player
"""


from math import floor
import random, sys

LVL_SIZE_X = 10
LVL_SIZE_Y = 10
SHIP_SPAWN_COUNT = 10
LEVEL_MAP = {}

class Player:
    symbol = u"◌"
    resources = {'batteries': 0,
                 'scrap_metal': 0,
                 'oxygen_tank': 0}
    position = (0,0) #off the map
    
    def check_status(self):
        if self.resources.oxygen_tank < 1:
            return False
        return True


class Entity:
    symbol = u"░"
    name = 'Empty space'
    description = 'Empty space, no resources.'
    batteries = 0
    scrap_metal = 0
    oxygen_tank = 0
    traverse_battery_cost = 1
    traverse_oxygen_cost = 1
    discovered = False

    def scavenge(self, player):
        print "%d batteries found" % (self.batteries)
        player.resources.batteries    += self.batteries
        self.batteries = 0

        print "%d scrap metal found" % (self.scrap_metal)
        player.resources.scrap_metal += self.scrap_metal
        self.scrap_metal = 0

        print "%d oxygen tanks found" % (self.oxygen_tank)
        player.resources.oxygen_tank += self.oxygen_tank
        self.oxygen_tank = 0

    def traverse(self):
        reduce_battery = self.traverse_battery_cost
        reduce_oxygen = self.traverse_oxygen_cost

        if self.discovered:
            half_battery = int(floor(float(self.traverse_battery_cost) / float(2)))
            half_oxygen = int(floor(float(self.traverse_oxygen_cost) / float(2)))
            reduce_battery = 1 if (half_battery == 0) else half_battery
            reduce_oxygen = 1 if (half_oxygen == 0) else half_oxygen

        self.discovered = True
        player.resources.batteries   -= reduce_battery
        player.resources.oxygen_tank -= reduce_oxygen


class SpaceShip(Entity):
    symbol = u"◎"
    name = 'Spaceship wreck'
    description = 'Spaceship wreckage (small) - salvagable for resources.'
    batteries = 12
    scrap_metal = 5
    oxygen_tank = 7
    traverse_battery_cost = 2
    traverse_oxygen_cost = 2


def init_game():
    #init player
    print('Spawning player...')
    player = Player()
    player.resources = {'batteries': 10,
                        'scrap_metal': 9,
                        'oxygen_tank': 7}
    position = (5,5)

    print('Spawning 5 ships...')
    for i in range(4):
        LEVEL_MAP[(random.randint(1,10),random.randint(1,10))] = SpaceShip()
    
    print('Filling the level in...')
    for y in range(10):
        for x in range(10):
            if not LEVEL_MAP.get((x+1,y+1)):
                LEVEL_MAP[(x+1,y+1)] = Entity()
            
    #draw the level?
    for y in range(10):
        for x in range(10):
            symbol = LEVEL_MAP[(x+1,y+1)].symbol
            sys.stdout.write(symbol)
        print('')

if __name__ == '__main__':
    
    #TODO: implement
    init_game()
    print('Initialized!')
    pass

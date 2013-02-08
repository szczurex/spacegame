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

LVL_SIZE_X = 10
LVL_SIZE_Y = 10
SHIP_SPAWN_COUNT = 10
LEVEL_MAP = {}

class Player:
    resources = {'batteries': 0,
                 'scrap_metal': 0,
                 'oxygen_tank': 0}


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

    def scavenge(self):
        print "%d batteries found" % (self.batteries)
        #PLAYER.resources.batteries    += self.batteries
        self.batteries = 0

        print "%d scrap metal found" % (self.scrap_metal)
        #PLAYER.resources.scrap_metal += self.scrap_metal
        self.scrap_metal = 0

        print "%d oxygen tanks found" % (self.oxygen_tank)
        #PLAYER.resources.oxygen_tank += self.oxygen_tank
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
        #PLAYER.resources.batteries   -= reduce_battery
        #PLAYER.resources.oxygen_tank -= reduce_oxygen


class SpaceShip(Entity):
    symbol = u"◎"
    name = 'Spaceship wreck'
    description = 'Spaceship wreckage (small) - salvagable for resources.'
    batteries = 12
    scrap_metal = 5
    oxygen_tank = 7
    traverse_battery_cost = 2
    traverse_oxygen_cost = 2


def spawn_ships():
    #TODO: implement
    pass


if __name__ == '__main__':
    #TODO: implement
    pass

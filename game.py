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
import random, sys, os

LVL_SIZE_X = 10
LVL_SIZE_Y = 10
SHIP_SPAWN_COUNT = 100
LEVEL_MAP = {}

class Player:
    symbol = u"◌"
    resources = {'batteries': 0,
                 'scrap_metal': 0,
                 'oxygen_tank': 0}
    position = (0,0) #off the map
    
    def check_status(self):
        if self.resources['oxygen_tank'] < 1:
            return False
        return True

    def move(self, direction):
        moves = ['N','E','S','W']
        if direction in moves:
            moved = False # better safe then sorry.
            if direction == 'N':
                if self.position[1]-1 <= LVL_SIZE_Y and self.position[1]-1 > 0:
                    self.position = (self.position[0], self.position[1]-1)
                    moved = True
            elif direction == 'E':
                if self.position[0]+1 <= LVL_SIZE_X and self.position[0]+1 > 0:
                    self.position = (self.position[0]+1, self.position[1])
                    moved = True
            elif direction == 'S':
                 if self.position[1]+1 <= LVL_SIZE_Y and self.position[1]+1 > 0:
                    self.position = (self.position[0], self.position[1]+1)
                    moved = True
            elif direction == 'W':
                if self.position[0]-1 <= LVL_SIZE_X and self.position[0]-1 > 0:
                    self.position = (self.position[0]-1, self.position[1])
                    moved = True
            #we assume we moved.
            if moved:
                LEVEL_MAP[player.position].traverse(self)
            else:
                print("Could not move.")
                raw_input('Press Enter to continue...')
                
            
        else:
            print("ILLEGAL MOVE")
            raw_input('Press Enter to continue...')
        

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
        player.resources['batteries']    += self.batteries
        self.batteries = 0

        print "%d scrap metal found" % (self.scrap_metal)
        player.resources['scrap_metal'] += self.scrap_metal
        self.scrap_metal = 0

        print "%d oxygen tanks found" % (self.oxygen_tank)
        player.resources['oxygen_tank'] += self.oxygen_tank
        self.oxygen_tank = 0
        
        raw_input('Press any key to continue...')

    def traverse(self, player):
        reduce_battery = self.traverse_battery_cost
        reduce_oxygen = self.traverse_oxygen_cost

        if self.discovered:
            half_battery = int(floor(float(self.traverse_battery_cost) / float(2)))
            half_oxygen = int(floor(float(self.traverse_oxygen_cost) / float(2)))
            reduce_battery = 1 if (half_battery == 0) else half_battery
            reduce_oxygen = 1 if (half_oxygen == 0) else half_oxygen

        self.discovered = True
        player.resources['batteries']   -= reduce_battery
        player.resources['oxygen_tank'] -= reduce_oxygen
        
        print("Lost %s batteries and %s oxygen during travel." % (reduce_battery, reduce_oxygen))
        raw_input('Press Enter to continue...')

class SpaceShip(Entity):
    symbol = u"◎"
    name = 'Spaceship wreck'
    description = 'Spaceship wreckage (small) - salvagable for resources.'
    batteries = 12
    scrap_metal = 5
    oxygen_tank = 7
    traverse_battery_cost = 2
    traverse_oxygen_cost = 2

def draw_level(player=None):
    for y in range(10):
        for x in range(10):
            symbol = LEVEL_MAP[(x+1,y+1)].symbol
            if player:
                if player.position == (x+1,y+1):
                    sys.stdout.write(player.symbol)
                else:
                   sys.stdout.write(symbol) 
            else:
                sys.stdout.write(symbol)
        print('')


def init_game():
    #init player
    print('Spawning player...')
    player = Player()
    player.resources = {'batteries': 10,
                        'scrap_metal': 9,
                        'oxygen_tank': 7}
    player.position = (random.randint(1,10),random.randint(1,10))

    print('Spawning %s ships...' % (SHIP_SPAWN_COUNT))
    for i in range(SHIP_SPAWN_COUNT):
        LEVEL_MAP[(random.randint(1,10),random.randint(1,10))] = SpaceShip()
    
    print('Filling the level in...')
    for y in range(10):
        for x in range(10):
            if not LEVEL_MAP.get((x+1,y+1)):
                LEVEL_MAP[(x+1,y+1)] = Entity()
    
    draw_level()
        
    return player

if __name__ == '__main__':
    player = init_game()
    print('Initialized!')
    raw_input('Press any key to start...')
    
    
    while(player.check_status()):
        os.system('clear')
        '''
            1. Draw the level.
            2. Print out stats.
            3. Wait for input.
        '''
        #1
        draw_level(player)
        #2
        print('Player position: %s,%s (%s)' % (player.position[0],
                                               player.position[1],
                                               LEVEL_MAP[player.position].name))
        print('......Resources......')
        print('Batteries: %s' % (player.resources['batteries']))
        print('Scrap    : %s' % (player.resources['scrap_metal']))
        print('Oxygen   : %s' % (player.resources['oxygen_tank']))
        print('\n')
        #3
        command = raw_input('SCAVENGE or TRAVERSE?')
            
        if command == 'SCAVENGE':
            LEVEL_MAP[player.position].scavenge(player)
        if command == 'TRAVERSE':
            newpos = raw_input('N/E/S/W ?')
            player.move(newpos)
        
    if player.resources['oxygen_tank'] < 1:
        print("You ran out of oxygen to breathe.")
    if player.resources['batteries'] < 1:
        print("You ran out of batteries for life support.")
    print('GAME OVER.')

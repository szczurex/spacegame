from __init__ import GameItem
from __init__ import TYPE_RESCUE_POD_PART
import random

# might be used for part name-generating.
PREFIXES = ['Alpha','Beta','Gamma','Delta','Epsilon',
            'Zeta','Eta','Theta','Iota','Kappa','Lambda',
            'Mu','Nu','Xi','Omicron','Pi','Rho','Sigma',
            'Tau','Upsilon','Phi','Chi','Psi','Omega']

INFIXES = [
           'Air',
           'Belt','Bucket','Button',
           'Core','Cylinder','Cooler','Cell','Control','Clockwork','Cog','Component','Connector','Controller','Crank',
           'Drum','Dynamo',
           'Engine',
           'Feeder','Flywheel',
           'Gasket','Gear','Guard','Generator',
           'Heat Pump','Hydraulic',
           'Intake',
           'Jacket',
           
           'Lock',
           'Module','Mount','Mechanism','Motor',
           
           
           'Power','Plasma','Photoelectric','Piston','Plunger',
           'Radiator','Ratchet','Regulator','Remote','Reservoir',
           'Steam','Seal','Shaft','Shovel','Socket','Spindle','Sprocket','Stabiliser','Starter','Supercharger',
           'Timer','Tripwire',
           'Unit',
           'Valve',
           'Wheel']

#SUFFIX = ['Module','Mount','Valve']


def NameGenerator():
    PREFIX_CHANCE = 40
    PREFIX_DOUBLE_CHANCE = 20
    INFIX_DOUBLE_CHANCE = 100
    
    name = ''
    
    #roll 1
    if random.randint(0,100) <= PREFIX_CHANCE:
        prefix = PREFIXES[random.randint(0, len(PREFIXES)-1)]
        name += prefix
        #sub-roll 1
        if random.randint(0,100) <= PREFIX_DOUBLE_CHANCE:
            subfix = prefix
            while subfix == prefix:
                subfix = PREFIXES[random.randint(0, len(PREFIXES)-1)]
            name += '-%s' % (subfix)
            
    #roll 2
    infix = INFIXES[random.randint(0, len(INFIXES)-1)]
    if name:
        name += ' %s' % (infix)
    else:
        name += '%s' % (infix)
    #sub-roll 2
    if random.randint(0,100) <= INFIX_DOUBLE_CHANCE:
        subinfix = infix
        while subinfix == infix:
            subinfix = INFIXES[random.randint(0, len(INFIXES)-1)]
        name += ' %s' % (subinfix)
        
    return name

    

class RescuePodPart(GameItem):
    name = 'Item name'
    description = 'A part of the rescue pod required for fixing.'
    type = TYPE_RESCUE_POD_PART
    
    def __init__(self):
        self.name = NameGenerator()
        
    def __unicode__(self):
        return self.name

from items import GameItem
from items import TYPE_RESCUE_POD_PART

# might be used for part name-generating.
PREFIXES = ['Alpha','Beta','Gamma','Delta','Epsilon',
            'Zeta','Eta','Theta','Iota','Kappa','Lambda',
            'Mu','Nu','Xi','Omicron','Pi','Rho','Sigma',
            'Tau','Upsilon','Phi','Chi','Psi','Omega']

INFIXES = ['Power','Core','Generator','Engine',
           'Plasma','Steam','Air']

SUFFIX = ['Module','Mount','Valve']

class RescuePodPart(GameItem):
    name = 'Item name'
    description = 'Item description'
    type = TYPE_RESCUE_POD_PART
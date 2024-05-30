#-----------------------------------------------------------------------------
# Module: User
#-----------------------------------------------------------------------------
'''User Class'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
class User:
    def __init__(self, name, xpos, zpos, needs, phone_number):
        self.name = name
        self.xpos = xpos
        self.zpos = zpos
        self.needs = needs
        self.phone_number = phone_number
        self.summary = [self.name, [self.xpos, self.zpos], self.needs, self.phone_number]

    def save(self):
        with open(f'{self.name}.txt', 'w') as f:
            f.write(tabulate(self.summary))
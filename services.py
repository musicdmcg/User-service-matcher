#-----------------------------------------------------------------------------
# Module: Services
#-----------------------------------------------------------------------------
'''Service Class'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
class Service:
    def __init__(self, name, xpos, zpos, services, phone_number):
        self.name = name
        self.xpos = xpos
        self.zpos = zpos
        self.services = services
        self.phone_number = phone_number
        self.summary = [[self.name], [f'({self.xpos}, {self.zpos})'], [self.services], [self.phone_number]]

    def __str__(self):
        return tabulate(self.summary)
    def save(self):
        with open(f'Services/{self.name}.txt', 'w') as f:
            f.write(tabulate(self.summary))

Apple = Service('Apple', 3, 1, ['phones', 'OS', 'PCs', 'laptops'], 2348094923)
Apple.save()
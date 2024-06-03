#-----------------------------------------------------------------------------
# Module: Services
#-----------------------------------------------------------------------------
'''Service Class'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
master_list = []
class Service:
    def __init__(self, name, xpos, zpos, services, phone_number, tags):
        self.name = name
        self.xpos = xpos
        self.zpos = zpos
        self.services = services
        self.phone_number = phone_number
        self.tags = tags
        self.summary = [[self.name], [f'Location : ({self.xpos}, {self.zpos})'], ['Services: ' + str(', '.join(map(str, self.services)))], [f'Phone Number: {self.phone_number}']]

    def __str__(self):
        return tabulate(self.summary)
        
    def save(self):
        with open(f'Services/{self.name}.txt', 'w') as f:
            f.write(tabulate(self.summary))
        master_list.append(self)

Apple = Service('Apple', 3, 1, ['phones', 'OS', 'PCs', 'laptops'], 2348094923, ['tech'])
Apple.save()
Windows = Service('Windows', 3, 0, ['OS', 'PCs'],  2348022222, ['tech'])
Windows.save()
Safeway = Service('Safeway', 1, 1, ['groceries'], 3069999999, ['fresh food'])
Safeway.save()
Costco = Service('Costco', 4, 5, ['phones', 'PCs', 'laptops', 'groceries', 'TVs'], 3061112222, ['bulk'])
Costco.save()
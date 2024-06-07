#-----------------------------------------------------------------------------
# Module: Services
#-----------------------------------------------------------------------------
'''Service Class'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
master_service_list = []
existing_tags = []
class Service:
    def __init__(self, name, xpos, zpos, services, phone_number, tags):
        self.name = name
        self.xpos = xpos
        self.zpos = zpos
        self.services = services
        self.phone_number = phone_number
        self.tags = tags
        self.summary = [[self.name], 
                    [f'Location : ({self.xpos}, {self.zpos})'], 
                    ['Services: ' + str(', '.join(map(str, self.services)))], 
                    [f'Phone Number: {self.phone_number}'], 
                    ['Tags: ' + str(', '.join(map(str, self.tags)))]]
        master_service_list.append(self)

    def __str__(self):
        return tabulate(self.summary)
        
    def save(self):
        global existing_tags
        with open(f'Services/{self.name}.py', 'w') as f:
            f.write(f'import services as s \n {self.name} = s.Service({self.name}, {self.xpos}, {self.zpos}, {self.services}, {self.phone_number}, {self.tags})')
        for tag in self.tags:
            if tag not in existing_tags:
                existing_tags.append(tag)

Service1 = Service('Apple', 3, 1, ['phones', 'OS', 'PCs', 'laptops'], 
                2348094923, ['tech'])
Service1.save()
#Service2 = Service('Windows', 3, 0, ['OS', 'PCs'],  2348022222, ['tech'])
#Service2.save()
#Service3 = Service('Safeway', 1, 1, ['groceries'], 3069999999, ['fresh food'])
#Service3.save()
#Service4 = Service('Costco', 4, 5, ['phones', 'PCs', 'laptops', 
#                                  'groceries', 'TVs'], 
#                 3061112222, ['bulk', 'tech'])
#Service4.save()
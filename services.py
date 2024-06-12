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
        var_name = self.name.replace("'", '')
        var_name.replace('"', '')
        with open('service_objects.py', 'a') as f:
            f.write(f'\n{var_name} = '
                    + f's.Service("""{self.name}""", {self.xpos}, '
                    + f'{self.zpos}, {self.services}, {self.phone_number}, '
                    + f'{self.tags})')
        for tag in self.tags:
            if tag not in existing_tags:
                existing_tags.append(tag)
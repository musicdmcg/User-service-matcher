#-----------------------------------------------------------------------------
# Module: User
#-----------------------------------------------------------------------------
'''User Class'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
import math as m
import services as s

class User:
    def __init__(self, name, xpos, zpos, needs, phone_number):
        self.name = name
        self.xpos = xpos
        self.zpos = zpos
        self.needs = needs
        self.phone_number = phone_number
        self.summary = [self.name, [self.xpos, self.zpos], self.needs, self.phone_number]

    def save(self):
        with open(f'Users/{self.name}.txt', 'w') as f:
            f.write(tabulate(self.summary))
    def distance_from_user(self, service):
        distance = m.sqrt((self.zpos - service.zpos)**2 + (self.xpos - service.xpos)**2)
        return distance

    def get_services(self):
        print_list = []
        for need in self.needs:
            for service in s.master_list:
                if need in service.services:
                    print_list.append(service)
        print_list = [s.Apple, s.Windows]
        print_list.sort(key = self.distance_from_user)
        return print_list

bob = User('Bob', 4, 0, ['OS'], 3065643223)




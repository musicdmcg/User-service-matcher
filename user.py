#-----------------------------------------------------------------------------
# Module: User
#-----------------------------------------------------------------------------
'''User Class'''
#-----------------------------------------------------------------------------
#-Imports and Global Variables------------------------------------------------
from tabulate import tabulate
import math as m
import services as s

master_user_list = []
class User(s.Service):
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
        master_user_list.append(self)

    def save(self):
        with open(f'Users/{self.name}.txt', 'w') as f:
            f.write(tabulate(self.summary))
    
    def distance_from_user(self, service):
        distance = m.sqrt((self.zpos - service.zpos)**2 
                        + (self.xpos - service.xpos)**2)
        return round(distance, 6)

    def get_services(self):
        service_matching = []
        tag_matching = []
        for service in s.master_service_list:
            for product in service.services:
                if product in self.services:
                    service_matching.append(service)
                    break
            for tag in service.tags:
                if tag in self.tags and service not in service_matching:
                    tag_matching.append(service)
                    break
        service_matching.sort(key = self.distance_from_user)
        for service in service_matching:
            service.summary.append([f'Distance from current location: \
            {self.distance_from_user(service)}'])
            print(tabulate(service.summary))
        print('Matched tags')
        tag_matching.sort(key = self.distance_from_user)
        for service in tag_matching:
            service.summary.append([f'Distance from current location: \
            {self.distance_from_user(service)}'])
            print(tabulate(service.summary))
        return None

user1 = User('Bob', 4.0, 0.0, ['phones', 'laptops'], 3065643223, 'tech')
user2 = User('Alice', -1, 0, ['TVs', 'groceries'], 3067771818, 'bulk')



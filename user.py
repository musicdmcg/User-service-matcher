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
                    ['Needs: ' + str(', '.join(map(str, self.services)))], 
                    [f'Phone Number: {self.phone_number}'], 
                    ['Tags: ' + str(', '.join(map(str, self.tags)))]]
        master_user_list.append(self)

    def save(self):
        '''Saves a user to user_objects.py as a user object'''
        var_name = self.name.replace("'", ' apostrophe ')
        var_name = var_name.replace('"', ' quotation mark ')
        var_name = var_name.replace(' ', '_')
        var_name = var_name.replace('&', 'and')
        var_name = s.r.sub('\d', '_number_', var_name)
        with open('user_objects.py', 'a') as f:
            f.write(f'\n{var_name} = '
            + f'u.User("""{self.name}""", {self.xpos}, {self.zpos}, '
            + f'{self.services}, {self.phone_number}, {self.tags})')

    def distance_from_user(self, service):
        '''Returns distance between self and service. '''
        distance = m.sqrt((self.zpos - service.zpos)**2 
                        + (self.xpos - service.xpos)**2)
        return round(distance, 6)

    def get_services(self):
        '''Searches s.master_service_list for services that match 
        needs or tags, then prints them'''
        service_matching = []
        tag_matching = []
        # Finding matches
        for service in s.master_service_list:
            for product in service.services:
                if product in self.services:
                    service_matching.append(service)
                    break
        for service in s.master_service_list:
            for tag in service.tags:
                if tag in self.tags and service not in service_matching:
                    tag_matching.append(service)
                    break
        # Printing results
        if len(service_matching) == 0 and len(tag_matching) == 0:
            print('\nNo services matched your request')
            return None
        if len(service_matching) == 0:
            print('\nNo services matched your needs')
        else:
            print('\nMatched Needs')
            service_matching.sort(key = self.distance_from_user)
            for service in service_matching:
                service.summary.append(['Distance from current location: '
                                    + f'{self.distance_from_user(service)}'])
                print(tabulate(service.summary))
        if len(tag_matching) == 0:
            print('No services matched your tags')
        else:
            print('Matched tags')
            tag_matching.sort(key = self.distance_from_user)
            for service in tag_matching:
                service.summary.append(['Distance from current location: '
                                    + f'{self.distance_from_user(service)}'])
                print(tabulate(service.summary))
            return None

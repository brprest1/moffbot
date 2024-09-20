import datetime
from datetime import datetime
import time

# check if daylight savings is active
dst = time.daylight

# detect day of the week
weekday = datetime.now().strftime('%A')

# detect date
date_today = int(datetime.today().strftime('%d'))

# realm cycle
realm_cycle = ['Daylight Prairie', 'Hidden Forest', 'Valley of Triumph', 'Golden Wasteland', 'Vault of Knowledge']
realm = realm_cycle[(date_today - 1) % len(realm_cycle)]

# group cycle
group_cycle = [2, 1, 3, 0, 4, 1, 2, 0, 3, 1, 4, 0]
group = group_cycle[(date_today - 1) % len(group_cycle)]

# areas
areas = {
    'Daylight Prairie': ['Butterfly Fields', 'Village Islands', 'Prairie Caves', 'Bird Nest', 'Sanctuary Islands'],
    'Hidden Forest': ['Forest Brook', 'Boneyard', 'Forest End', 'Treehouse', 'Elevated Clearing'],
    'Valley of Triumph': ['Ice Rink', 'Ice Rink', 'Village of Dreams', 'Village of Dreams', 'Hermit Valley'],
    'Golden Wasteland': ['Broken Temple', 'Battlefield', 'Graveyard', 'Crab Fields', 'Forgotten Ark'],
    'Vault of Knowledge': ['Starlight Desert', 'Starlight Desert', 'Jellyfish Cove', 'Jellyfish Cove', 'Jellyfish Cove']
}

class Groups:
    def __init__(self, weekday, areas, realm, dst):
        self.weekday = weekday
        self.realm = realm
        self.areas = areas
        self.dst = dst

    def group0(self):
        self.color = 'Black'
        if self.dst == '0':
            pass
        self.timing = '1:58 AM - 5:58 AM, 9:58 AM - 1:58 PM, 5:58 PM - 9:58 PM'
        if self.weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            self.availability = True
        else:
            self.availability = False
        self.reward = '200 wax'
        self.area = self.areas[self.realm][0]

    def print_info(self):
        print(f"Color: {self.color}")
        print(f"Realm: {self.realm}")
        print(f"Area: {self.area}")
        print(f"Timing: {self.timing}")
        print(f"Availability: {self.availability}")
        print(f"Reward: {self.reward}")


groups = Groups(weekday, areas, realm, dst)
groups.group0()
groups.print_info()
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
todays_realm = realm_cycle[(date_today - 1) % len(realm_cycle)]
print(todays_realm)

# timing cycle
timing_cycle = [2, 1, 3, 0, 4, 1, 2, 0, 3, 1, 4, 0]
todays_time_num = timing_cycle[(date_today - 1) % len(timing_cycle)]
print(todays_time_num)

# areas
areas = {
    'Daylight Prairie': ['Butterfly Fields', 'Village Islands', 'Prairie Caves', 'Bird Nest', 'Sanctuary Islands'],
    'Hidden Forest': ['Forest Brook', 'Boneyard', 'Forest End', 'Treehouse', 'Elevated Clearing'],
    'Valley of Triumph': ['Ice Rink', 'Ice Rink', 'Village of Dreams', 'Village of Dreams', 'Hermit Valley'],
    'Golden Wasteland': ['Broken Temple', 'Battlefield', 'Graveyard', 'Crab Fields', 'Forgotten Ark'],
    'Vault of Knowledge': ['Starlight Desert', 'Starlight Desert', 'Jellyfish Cove', 'Jellyfish Cove', 'Jellyfish Cove']
}

# group 0
class Group0:
    def __init__(self, todays_realm):
        todays_color = 'Black'
        todays_rewards = '200 wax'
        todays_timings = '1:58'
        todays_area = areas[todays_realm][0]

if todays_time_num == 0:
    today = Group0(todays_realm)

print(f'{todays_color} {todays_rewards} {todays_timings} {todays_area}')
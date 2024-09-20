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

# group 0
class Group0:
    def __init__(self, color, area, rewards, timings, availability):
        self.color = 'Black'
        
        if todays_realm == 'Daylight Prairie':
            self.area = 'Butterfly Fields'
        elif todays_realm == 'Hidden Forest':
            self.area = 'Forest Brook'
        elif todays_realm == 'Valley of Triumph':
            self.area = 'Ice Rink'
        elif todays_realm == 'Golden Wasteland':
            self.area = 'Broken Temple'
        elif todays_realm == 'Vault of Knowledge':
            self.area = 'Starlight Desert'

        self.rewards = '200 wax'

        if weekday == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
            self.availability == True
        elif weekday == 'Saturday' or 'Sunday':
            self.availability == False

if todays_time_num == 0:
    todays_group = Group0()
    print(todays_group)
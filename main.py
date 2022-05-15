import argparse, sys
import os
from datetime import datetime


parser = argparse.ArgumentParser()

parser.add_argument('--duration_in_minutes')
parser.add_argument('--minimum_people')
parser.add_argument('--calendars')
args = parser.parse_args()

duration = args.duration_in_minutes
minimumPeople = args.minimum_people
calendarsDirectory = args.calendars

busyTime = dict()

for calendar in os.listdir(calendarsDirectory):
    f = open(f"{calendarsDirectory}/{calendar}", 'r')
    name=os.path.basename(f"{calendarsDirectory}/{calendar}").split('.')[0]
    content = f.readlines()
    for lines in content:
        splitted=lines.partition(' - ')
        if(splitted[2]==''):
            date= datetime.strptime(splitted[0], '%Y-%m-%d')
            busyTime[name]=((date,datetime.strptime(splitted[0]+ '23:59:59', '%Y-%m-%d %H:%M:%S')))

        else:
            date1= datetime.strptime(splitted[0], '%Y-%m-%d %H:%M:%S')
            date2= datetime.strptime(splitted[2], '%Y-%m-%d %H:%M:%S')
            busyTime[name]=((date1,date2))
    f.close()

print(busyTime)
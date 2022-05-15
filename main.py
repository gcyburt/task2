import argparse, sys
import datefinder
import os


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--duration_in_minutes')
    parser.add_argument('--minimum_people')
    parser.add_argument('--calendars')
    args = parser.parse_args()

    duration = args.duration_in_minutes
    minimumPeople = args.minimum_people
    calendarsDirectory = args.calendars

    for calendar in os.listdir(calendarsDirectory):
        f = open(calendar, 'r')
        content = f.read()
        dates = list(datefinder.find_dates(content))

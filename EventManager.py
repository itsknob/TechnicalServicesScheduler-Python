from TechStuff import Event
from TechStuff import Employee
from HoursParser import FileParser
import pprint

'''
file_parser = FileParser()
file_parser.choose_file()
upcoming_events = file_parser.parse_file()
'''
"""
f = FileParser()
f.choose_file()
new_shifts = f.parse_file()
"""
"""
# Currently Working
for shift in new_shifts:
    print(shift.get_event_name())
    print(shift.get_event_start_time())
    print(shift.get_event_end_time())
    print(shift.get_event_number_employees())
    print()
"""
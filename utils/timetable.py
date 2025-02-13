# utils/timetable.py

import json

def load_timetable(json_path):
    """Load the college timetable from a JSON file."""
    with open(json_path, 'r') as f:
        timetable = json.load(f)
    return timetable

def get_current_class(timetable, current_time):
    """
    Get the class details for the current time.
    Assuming timetable is a dict with keys as "start-end" time slots.
    """
    for time_slot, class_info in timetable.items():
        start, end = time_slot.split('-')
        if start <= current_time <= end:
            return class_info
    return None

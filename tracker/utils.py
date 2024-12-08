from datetime import datetime
from icalendar import Calendar, Event

def generate_ics(tasks):
    cal = Calendar()
    cal.add('prodid', '-//Goal Tracker//mxm.dk//')
    cal.add('version', '2.0')

    for task in tasks:
        event = Event()
        event.add('summary', task.title)
        event.add('description', task.description)
        event.add('dtstart', task.due_date)
        event.add('dtend', task.due_date)
        event.add('dtstamp', datetime.now())
        cal.add_component(event)

    return cal.to_ical()

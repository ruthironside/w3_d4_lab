from app.models.event import *

event1 = Event("March", "Birthday", 10, "Pub", "Party")
event2 = Event("February", "Wedding", 200, "Castle", "Milestone")
events = [event1, event2]

def add_new_event(event):
    events.append(event)
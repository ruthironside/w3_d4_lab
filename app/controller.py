from flask import render_template, request
from app import app
from app.models.event_list import *
from app.models.event import *

@app.route('/')
def index():
    return render_template('index.html', title="Events", events=events)


@app.route('/create-event', methods=['POST'])
def add_task():
    event_name = request.form['title']
    # new_event = Event(name_of_event=event_name)
    new_event = Event(date=None, name_of_event=event_name, number_of_guests=None, room_location=None, description=None)
    add_new_event(new_event)
    return render_template('index.html', title="Events", events=events)
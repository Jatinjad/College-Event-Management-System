import json


def load_data():

    with open("data/events.json", "r") as file:
        events = json.load(file)

    with open("data/students.json", "r") as file:
        students = json.load(file)

    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    with open("data/attendance.json", "r") as file:
        attendance = json.load(file)

    return events, students, registrations, attendance


def save_data(events, students, registrations, attendance):

    with open("data/events.json", "w") as file:
        json.dump(events, file, indent=4)

    with open("data/students.json", "w") as file:
        json.dump(students, file, indent=4)

    with open("data/registrations.json", "w") as file:
        json.dump(registrations, file, indent=4)

    with open("data/attendance.json", "w") as file:
        json.dump(attendance, file, indent=4)
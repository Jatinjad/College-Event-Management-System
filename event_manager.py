# EVENT MANAGEMENT MODULE


# CREATE EVENT

def create_event(events, save_data):

    print("\n------------- CREATE EVENT -------------")

    event_id = input("Enter event ID: ").strip()

    # Check whether event already exists
    for event in events:

        if event["id"] == event_id:
            print("Event already exists.")
            return

    event_name = input("Enter event name: ").strip()
    event_date = input("Enter event date: ").strip()
    event_time = input("Enter event time: ").strip()
    event_venue = input("Enter venue: ").strip()
    event_organizer = input("Enter organizer: ").strip()

    event_capacity = int(
        input("Enter event capacity: ")
    )

    event = {
        "id": event_id,
        "name": event_name,
        "date": event_date,
        "time": event_time,
        "venue": event_venue,
        "organizer": event_organizer,
        "capacity": event_capacity,
        "status": "Upcoming"
    }

    events.append(event)

    save_data()

    print("\nEvent created successfully!")


# VIEW EVENTS

def view_events(events):

    print("\n------------- ALL EVENTS -------------")

    if len(events) == 0:
        print("No events available.")
        return

    for event in events:

        print("\nEvent ID:", event["id"])
        print("Event Name:", event["name"])
        print("Date:", event["date"])
        print("Time:", event["time"])
        print("Venue:", event["venue"])
        print("Organizer:", event["organizer"])
        print("Capacity:", event["capacity"])
        print("Status:", event["status"])

        print("----------------------------------------")


# UPDATE EVENT

def update_event(events, save_data):

    print("\n------------- UPDATE EVENT -------------")

    event_id = input(
        "Enter event ID to update: "
    ).strip()

    selected_event = None

    for event in events:

        if event["id"] == event_id:
            selected_event = event
            break

    if selected_event is None:
        print("Event not found.")
        return

    print("\nEnter new details.")

    selected_event["name"] = input(
        "Enter event name: "
    ).strip()

    selected_event["date"] = input(
        "Enter event date: "
    ).strip()

    selected_event["time"] = input(
        "Enter event time: "
    ).strip()

    selected_event["venue"] = input(
        "Enter venue: "
    ).strip()

    selected_event["organizer"] = input(
        "Enter organizer: "
    ).strip()

    selected_event["capacity"] = int(
        input("Enter event capacity: ")
    )

    save_data()

    print("\nEvent updated successfully!")


# CANCEL EVENT

def cancel_event(events, save_data):

    print("\n------------- CANCEL EVENT -------------")

    event_id = input(
        "Enter event ID to cancel: "
    ).strip()

    for event in events:

        if event["id"] == event_id:

            if event["status"] == "Cancelled":
                print("Event is already cancelled.")
                return

            event["status"] = "Cancelled"

            save_data()

            print("\nEvent cancelled successfully!")
            return

    print("Event not found.")
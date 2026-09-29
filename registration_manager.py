# REGISTRATION MANAGEMENT MODULE


# REGISTER STUDENT FOR EVENT


def register_for_event(students, events, registrations, save_data):

    print("\n EVENT REGISTRATION ")

    student_id = input("Enter student ID: ").strip()

    # Find student
    selected_student = None

    for student in students:

        if student["id"] == student_id:

            selected_student = student
            break

    if selected_student is None:

        print("Student not found,try again.")
        return

    event_id = input("Enter event ID: ").strip()

    # Find event
    selected_event = None

    for event in events:

        if event["id"] == event_id:

            selected_event = event
            break

    if selected_event is None:

        print("Event not found.")
        return

    # Check whether event is cancelled
    if selected_event["status"] == "Cancelled":

        print("Cannot register for a cancelled event.")
        return

    # Check duplicate registration
    for registration in registrations:

        if (
            registration["student_id"] == student_id
            and registration["event_id"] == event_id
            and registration["status"] == "Registered"
        ):

            print("Student is already registered for this event.")
            return

    # Count active registrations
    registration_count = 0

    for registration in registrations:

        if (
            registration["event_id"] == event_id
            and registration["status"] == "Registered"
        ):

            registration_count += 1

    # Check event capacity
    if registration_count >= selected_event["capacity"]:

        print("Event is full. Registration cannot be completed.")
        return

    # Create registration
    registration = {
        "student_id": student_id,
        "event_id": event_id,
        "event_name": selected_event["name"],
        "status": "Registered",
    }

    registrations.append(registration)

    save_data()

    print("\nRegistration successful!")
    print("Student:", selected_student["name"])
    print("Event:", selected_event["name"])


# VIEW MY REGISTRATIONS


def view_my_registrations(students, registrations):

    print("\n------------- MY REGISTRATIONS -------------")

    student_id = input("Enter student ID: ").strip()

    # Check whether student exists
    student_exists = False

    for student in students:

        if student["id"] == student_id:

            student_exists = True
            break

    if not student_exists:

        print("Student not found.")
        return

    found = False

    for registration in registrations:

        if (
            registration["student_id"] == student_id
            and registration["status"] == "Registered"
        ):

            print("\nEvent Name:", registration["event_name"])
            print("Event ID:", registration["event_id"])
            print("Status:", registration["status"])
            print("----------------------------------------")

            found = True

    if not found:

        print("No active registrations found.")


# CANCEL REGISTRATION


def cancel_registration(students, registrations, save_data):

    print("\n------------- CANCEL REGISTRATION -------------")

    student_id = input("Enter student ID: ").strip()
    event_id = input("Enter event ID: ").strip()

    # Check student
    student_exists = False

    for student in students:

        if student["id"] == student_id:

            student_exists = True
            break

    if not student_exists:

        print("Student not found.")
        return

    # Find registration
    for registration in registrations:

        if (
            registration["student_id"] == student_id
            and registration["event_id"] == event_id
            and registration["status"] == "Registered"
        ):

            registration["status"] = "Cancelled"

            save_data()

            print("\nRegistration cancelled successfully!")
            return

    print("Active registration not found.")

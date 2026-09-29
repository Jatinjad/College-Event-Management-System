# ATTENDANCE MANAGEMENT MODULE


def mark_attendance(students, events, registrations, attendance, save_data):

    print("\n------------- MARK ATTENDANCE -------------")

    student_id = input("Enter student ID: ").strip()

    event_id = input("Enter event ID: ").strip()

    # Check whether the student exists
    student_exists = False

    for student in students:

        if student["id"] == student_id:
            student_exists = True
            break

    if not student_exists:
        print("Student not found.")
        return

    # Check whether the event exists
    event_exists = False

    for event in events:

        if event["id"] == event_id:
            event_exists = True
            break

    if not event_exists:
        print("Event not found.")
        return

    # Check whether student is registered
    registered = False

    for registration in registrations:

        if (
            registration["student_id"] == student_id
            and registration["event_id"] == event_id
            and registration["status"] == "Registered"
        ):
            registered = True
            break

    if not registered:
        print("Student is not registered for this event.")
        return

    # Get attendance status
    status = input("Enter attendance status (Present/Absent): ").strip()

    # Check if attendance was already marked
    for record in attendance:

        if record["student_id"] == student_id and record["event_id"] == event_id:
            record["status"] = status

            save_data()

            print("\nAttendance updated successfully!")
            return

    # Create new attendance record
    attendance_record = {
        "student_id": student_id,
        "event_id": event_id,
        "status": status,
    }

    attendance.append(attendance_record)

    save_data()

    print("\nAttendance marked successfully!")

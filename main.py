from database import load_data, save_data as database_save_data

from event_manager import ( create_event,view_events,update_event,cancel_event,)

from student_manager import add_student

from registration_manager import (register_for_event,view_my_registrations,cancel_registration,)

from attendance_manager import mark_attendance

events = []
students = []
registrations = []
attendance = []
events, students, registrations, attendance = load_data()


def save_data():
    database_save_data(events, students, registrations, attendance)

def pause():
    input("\nPress Enter to continue...")

def view_registrations():
    print("\nALL REGISTRATIONS ")

    if len(registrations) == 0:
        print("No registrations available.")
        return

    for registration in registrations:
        print("\nStudent ID:", registration["student_id"])
        print("Event ID:", registration["event_id"])

        if "event_name" in registration:
            print("Event Name:", registration["event_name"])

        print("Status:", registration["status"])

# ADMINISTRATOR MENU

def administrator_menu():

    while True:

        print("\nWELCOME TO THE ADMINISTRATOR MENU")
        print("1. Create Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Cancel Event")
        print("5. View Registrations")
        print("6. Mark Attendance")
        print("7. Back")

        admin_choice = input("Enter your choice: ").strip()

        # CREATE EVENT

        if admin_choice == "1":

            create_event(events, save_data)
            pause()

        # VIEW EVENTS

        elif admin_choice == "2":

            view_events(events)
            pause()

        # UPDATE EVENT

        elif admin_choice == "3":

            update_event(events, save_data)
            pause()

        # CANCEL EVENT

        elif admin_choice == "4":

            cancel_event(events, save_data)
            pause()

        # VIEW REGISTRATIONS

        elif admin_choice == "5":

            view_registrations()
            pause()

        # MARK ATTENDANCE

        elif admin_choice == "6":

            mark_attendance(students, events, registrations, attendance, save_data)

            pause()

        # BACK

        elif admin_choice == "7":

            print("Going back...")
            break

        else:

            print("Invalid choice!")
            pause()


# STUDENT MENU


def student_menu():

    while True:

        print("\nWELCOME TO THE STUDENT MENU")
        print("Please select an option:")
        print("1. View Events")
        print("2. Add Student")
        print("3. Register for Event")
        print("4. My Registrations")
        print("5. Cancel Registration")
        print("6. Back")

        student_choice = input("Enter your choice: ").strip()

        # VIEW EVENTS

        if student_choice == "1":

            view_events(events)
            pause()

        # ADD STUDENT

        elif student_choice == "2":

            add_student(students, save_data)
            pause()

        # REGISTER FOR EVENT

        elif student_choice == "3":

            register_for_event(students, events, registrations, save_data)

            pause()

        # MY REGISTRATIONS

        elif student_choice == "4":

            view_my_registrations(students, registrations)

            pause()

        # CANCEL REGISTRATION

        elif student_choice == "5":

            cancel_registration(students, registrations, save_data)

            pause()

        # BACK

        elif student_choice == "6":

            print("Going back...")
            break

        else:

            print("Invalid choice!")
            pause()


# MAIN PROGRAM

running = True

while running:

    print("\nWELCOME TO THE COLLEGE EVENT MANAGEMENT SYSTEM")
    print("1. Student")
    print("2. Administrator")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    # STUDENT

    if choice == "1":

        student_menu()

    # ADMINISTRATOR

    elif choice == "2":

        administrator_menu()

    # EXIT

    elif choice == "3":

        print("\nThank you for using the system!")
        running = False

    # INVALID CHOICE

    else:

        print("Invalid choice!")
        pause()

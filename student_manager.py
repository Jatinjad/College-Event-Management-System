# STUDENT MANAGEMENT MODULE


# ADD STUDENT

def add_student(students, save_data):

    print("\n------------- ADD STUDENT -------------")

    student_id = input("Enter student ID: ").strip()

    # Check whether student already exists
    for student in students:

        if student["id"] == student_id:
            print("Student already exists.")
            return

    student_name = input("Enter student name: ").strip()

    student_email = input("Enter student email: ").strip()

    student_course = input("Enter course: ").strip()

    student_year = input("Enter year: ").strip()

    student = {
        "id": student_id,
        "name": student_name,
        "email": student_email,
        "course": student_course,
        "year": student_year
    }

    students.append(student)

    save_data()

    print("\nStudent added successfully!")
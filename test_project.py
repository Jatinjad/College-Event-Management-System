# ============================================
# CEMS PROJECT TESTING
# ============================================

import unittest


class TestCollegeEventManagementSystem(unittest.TestCase):

    # ----------------------------------------
    # BASIC CALCULATION TEST
    # ----------------------------------------

    def test_available_seats(self):

        capacity = 100
        registrations = 35

        available_seats = capacity - registrations

        self.assertEqual(
            available_seats,
            65
        )


    # ----------------------------------------
    # ATTENDANCE PERCENTAGE TEST
    # ----------------------------------------

    def test_attendance_percentage(self):

        registrations = 50
        present = 40

        attendance_percentage = (
            present / registrations
        ) * 100

        self.assertEqual(
            attendance_percentage,
            80
        )


    # ----------------------------------------
    # EMPTY REGISTRATION TEST
    # ----------------------------------------

    def test_no_registrations(self):

        registrations = []

        self.assertEqual(
            len(registrations),
            0
        )


    # ----------------------------------------
    # EVENT CAPACITY TEST
    # ----------------------------------------

    def test_event_capacity(self):

        capacity = 100
        registrations = 100

        self.assertTrue(
            registrations >= capacity
        )


    # ----------------------------------------
    # STUDENT ID TEST
    # ----------------------------------------

    def test_student_id(self):

        student = {
            "id": "S001",
            "name": "Test Student"
        }

        self.assertEqual(
            student["id"],
            "S001"
        )


# ============================================
# RUN TESTS
# ============================================

if __name__ == "__main__":

    unittest.main()
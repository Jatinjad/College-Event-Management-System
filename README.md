# College Event Management System

## Overview

The College Event Management System (CEMS) is a Python-based project
designed to simplify the management of college events, student
registrations, attendance, and event reports.

The system provides separate options for students and administrators.
Students can view events and manage their registrations, while
administrators can manage events, registrations, attendance, and reports.

---

## Features

### Student Features

- View available events
- Add student information
- Register for an event
- View personal registrations
- Cancel event registration

### Administrator Features

- Create events
- View events
- Update events
- Cancel events
- View all registrations
- Mark student attendance
- Generate event reports

### Validation

The system provides input validation for:

- Empty inputs
- Positive numbers
- Email addresses
- Attendance status
- Invalid menu choices

### Reporting

The system can display:

- Total number of events
- Total number of students
- Active registrations
- Cancelled registrations
- Attendance records
- Upcoming events
- Cancelled events
- Event-wise registrations
- Available seats
- Attendance percentage
- Most registered event

---

## Project Structure

```text
College Event Management System/
│
├── main.py
├── database.py
├── validation.py
├── event_manager.py
├── student_manager.py
├── registration_manager.py
├── attendance_manager.py
│
├── data/
│   ├── events.json
│   ├── students.json
│   ├── registrations.json
│   └── attendance.json
│
├── tests/
│   └── test_project.py
│
├── README.md
└── statement.md
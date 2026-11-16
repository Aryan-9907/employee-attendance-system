## About the Project

This project is a console-based application that helps manage employee attendance.

Users can add employees, mark their daily attendance, and view attendance reports. All employee data is saved in a text file so that it is available even after closing the program.

## Features

- Add new employees.
- Automatically generate employee IDs starting from E101.
- Mark attendance as Present (P), Absent (A), or Leave (L).
- View individual employee attendance reports.
- Calculate attendance percentage.
- Prevent duplicate attendance entries for the same date.
- Save and load employee data using file handling.
- Validate employee IDs, dates, and attendance status.

## Technologies Used

- Python 3
- Lists
- Dictionaries
- Functions
- Conditional Statements
- Loops
- File Handling

## Menu Options

1. Add Employee
2. Mark Attendance
3. View Attendance Report
4. Exit

## Attendance Status

| Code | Meaning |
|------|---------|
| P | Present |
| A | Absent |
| L | Leave |

## Attendance Percentage

The attendance percentage is calculated using:

**Attendance % = (Present Days / Total Marked Days) × 100**

## Project Structure

```text
employee-attendance-system/
│
├── employee_attendance.py
├── attendance.txt
└── README.md
```

Note: `attendance.txt` is created automatically when employee data is saved.

## Learning Outcomes

Through this project, I learned about:

- Python functions and loops.
- Lists and dictionaries.
- Conditional statements.
- Basic file handling.
- Input validation.
- Building a simple console application.

## Author

**Aryan Kumar**

B.Tech CSE (AI & ML) Student

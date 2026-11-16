
# Employee Attendance System

# Function to save data in file
def save_data():
    file = open("attendance.txt", "w")

    for emp in employees:
        data = emp["id"] + "|" + emp["name"] + "|"

        for date in emp["records"]:
            data = data + date + "," + emp["records"][date] + ";"

        file.write(data + "\n")

    file.close()


# Function to load data from file
def load_data():
    try:
        file = open("attendance.txt", "r")

        for line in file:
            parts = line.strip().split("|")

            if len(parts) == 3:
                emp = {
                    "id": parts[0],
                    "name": parts[1],
                    "records": {}
                }

                if parts[2] != "":
                    records = parts[2].split(";")

                    for record in records:
                        if record != "":
                            details = record.split(",")
                            emp["records"][details[0]] = details[1]

                employees.append(emp)

        file.close()

    except FileNotFoundError:
        pass


# Function to add employee
def add_employee():
    name = input("Enter employee name: ")

    if len(employees) == 0:
        emp_id = "E101"
    else:
        emp_id = "E" + str(int(employees[-1]["id"][1:]) + 1)

    emp = {
        "id": emp_id,
        "name": name,
        "records": {}
    }

    employees.append(emp)

    save_data()

    print("Employee added:", emp_id, "|", name)


# Function to mark attendance
def mark_attendance():
    emp_id = input("Enter employee ID: ")

    found = False

    for emp in employees:
        if emp["id"] == emp_id:
            found = True

            date = input("Enter date (YYYY-MM-DD): ")

            # Check date
            try:
                from datetime import datetime
                d = datetime.strptime(date, "%Y-%m-%d")

                if d.strftime("%Y-%m-%d") != date:
                    print("Invalid date. Use YYYY-MM-DD.")
                    return

            except ValueError:
                print("Invalid date. Use YYYY-MM-DD.")
                return

            # Check duplicate date
            if date in emp["records"]:
                print("Attendance for", date, "is already marked.")
                return

            status = input("Enter status (P/A/L): ").upper()

            if status == "P" or status == "A" or status == "L":
                emp["records"][date] = status
                save_data()
                print("Attendance marked successfully.")

            else:
                print("Invalid status. Enter P, A or L.")

            return

    if found == False:
        print("Employee", emp_id, "not found.")


# Function to show attendance report
def show_report():
    emp_id = input("Enter employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            present = 0
            absent = 0
            leave = 0

            for date in emp["records"]:
                if emp["records"][date] == "P":
                    present = present + 1

                elif emp["records"][date] == "A":
                    absent = absent + 1

                elif emp["records"][date] == "L":
                    leave = leave + 1

            total = present + absent + leave

            if total == 0:
                percentage = 0
            else:
                percentage = (present / total) * 100

            print(emp["name"] + ": Present", present,
                  "| Absent", absent, "| Leave", leave)

            if total == 0:
                print("Attendance: 0.00% (no records)")
            else:
                print("Attendance: {:.2f}%".format(percentage))

            return

    print("Employee", emp_id, "not found.")


# Main program
employees = []

load_data()

while True:

    print("\n===== EMPLOYEE ATTENDANCE SYSTEM =====")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        show_report()

    elif choice == "4":
        save_data()
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")

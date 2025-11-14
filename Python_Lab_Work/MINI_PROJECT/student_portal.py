# ---------------------- Student Portal Mini Project ----------------------

students = {} 


def register_student():
    print("\n-------- Student Registration ------")
    
    sid = input("Student id : ")
    name = input("Name : ")
    std = input("Standard : ")
    roll = input("Roll No. : ")
    att = float(input("Attendance (%) : "))

    students[sid] = {
        "name": name,
        "standard": std,
        "roll": roll,
        "attendance": att
    }

    print("\nStudent Registered successfully.\n")


def student_profile():
    print("\n-------- Student Profile ------")
    sid = input("Enter Student ID: ")

    if sid in students:
        print("\nStudent Details:")
        print("ID:", sid)
        print("Name:", students[sid]["name"])
        print("Standard:", students[sid]["standard"])
        print("Roll No.:", students[sid]["roll"])
        print("Attendance:", students[sid]["attendance"])
    else:
        print("\nStudent not found!")


def delete_student():
    print("\n-------- Delete Student ------")
    sid = input("Enter Student ID to delete: ")

    if sid in students:
        del students[sid]
        print("Student deleted successfully.\n")
    else:
        print("Student not found!\n")


def list_sorted_by_standard():
    print("\n-------- List of Students Sorted by Standard ------")

    sorted_list = sorted(students.items(), key=lambda x: x[1]["standard"])

    if not sorted_list:
        print("No student data available.\n")
        return

    for sid, data in sorted_list:
        print(f"{sid} - {data['name']} - Standard {data['standard']} - Roll {data['roll']} - Att {data['attendance']}%")


def list_particular_standard():
    print("\n-------- List of Students of Particular Standard ------")
    std = input("Enter Standard: ")

    found = False
    for sid, data in students.items():
        if data["standard"] == std:
            print(f"{sid} - {data['name']} - Roll {data['roll']} - Att {data['attendance']}%")
            found = True

    if not found:
        print("No students found in this standard.\n")


def list_attendance_above_50():
    print("\n-------- Students With Attendance > 50% (Standard Wise) ------")
    
    for sid, data in students.items():
        if data["attendance"] > 50:
            print(f"{sid} - {data['name']} - Std {data['standard']} - Att {data['attendance']}%")

    print()


# ----------------------------- Main Program -----------------------------

while True:

    print("\n-------------------------------- Student Portal --------------------------------")
    print("1. Registration of New Student")
    print("2. Student Profile")
    print("3. Delete Student")
    print("4. List of All Students Sorted as per Standard")
    print("5. List of Students of Particular Standard")
    print("6. List of Students with Attendance greater than 50% standard wise")
    print("--------------------------------------------------------------------------------")

    choice = input("Select any one operation : ")

    if choice == "1":
        register_student()
    elif choice == "2":
        student_profile()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        list_sorted_by_standard()
    elif choice == "5":
        list_particular_standard()
    elif choice == "6":
        list_attendance_above_50()
    else:
        print("Invalid Option! Please try again.")

    cont = input("\nPress 0 to exit, any other key to continue: ")
    if cont == "0":
        print("\nExiting Student Portal... Thank you!\n")
        break

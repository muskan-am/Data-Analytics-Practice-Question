import mysql.connector

# connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",     # your MySQL password
    database="lab"
)

cursor = db.cursor()

print("--------- INSERT MENU ---------")
print("1. Insert Course")
print("2. Insert Faculty")
print("3. Insert Module")
ch = int(input("Enter your choice: "))

if ch == 1:
    sql = """INSERT INTO course 
    (course_id, course_name, description, duration, min_enrollment, max_enrollment)
    VALUES (%s, %s, %s, %s, %s, %s)"""

    data = (
        input("Course ID: "),
        input("Course Name: "),
        input("Description: "),
        int(input("Duration: ")),
        int(input("Min Enrollment: ")),
        int(input("Max Enrollment: "))
    )

    cursor.execute(sql, data)
    db.commit()
    print("Course inserted successfully!")

elif ch == 2:
    sql = """INSERT INTO faculty 
    (faculty_id, faculty_name, age, dob, qualification)
    VALUES (%s, %s, %s, %s, %s)"""

    data = (
        input("Faculty ID: "),
        input("Faculty Name: "),
        int(input("Age: ")),
        input("DOB (YYYY-MM-DD): "),
        input("Qualification: ")
    )

    cursor.execute(sql, data)
    db.commit()
    print("Faculty inserted successfully!")

elif ch == 3:
    sql = """INSERT INTO modules 
    (module_id, module_name, description, duration, course_id)
    VALUES (%s, %s, %s, %s, %s)"""

    data = (
        input("Module ID: "),
        input("Module Name: "),
        input("Description: "),
        int(input("Duration: ")),
        input("Course ID (must exist): ")
    )

    cursor.execute(sql, data)
    db.commit()
    print("Module inserted successfully!")

else:
    print("Invalid choice")

cursor.close()
db.close()

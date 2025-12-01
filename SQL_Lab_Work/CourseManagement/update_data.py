import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="lab"
)

cursor = db.cursor()

print("--------- UPDATE MENU ---------")
print("1. Update Course Name")
print("2. Update Faculty Name")
print("3. Update Module Name")

ch = int(input("Enter choice: "))

if ch == 1:
    cid = input("Enter Course ID to update: ")
    new_name = input("New Course Name: ")
    cursor.execute("UPDATE course SET course_name=%s WHERE course_id=%s", (new_name, cid))
    db.commit()
    print("Course updated!")

elif ch == 2:
    fid = input("Enter Faculty ID to update: ")
    new_name = input("New Faculty Name: ")
    cursor.execute("UPDATE faculty SET faculty_name=%s WHERE faculty_id=%s", (new_name, fid))
    db.commit()
    print("Faculty updated!")

elif ch == 3:
    mid = input("Enter Module ID to update: ")
    new_name = input("New Module Name: ")
    cursor.execute("UPDATE modules SET module_name=%s WHERE module_id=%s", (new_name, mid))
    db.commit()
    print("Module updated!")

cursor.close()
db.close()

-- LAB: MySQL queries for Students & Marks
-- Created for Muskan's assignment
-- Date : 21 November 2025 

DROP DATABASE IF EXISTS lab;
CREATE DATABASE lab;
USE lab;

-- PART 1: Create students table and insert records (Q1, Q2)
CREATE TABLE students (
    stdid INT PRIMARY KEY,
    stdname VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

INSERT INTO students (stdid, stdname, age, city) VALUES
(1,'Rohan',20,'Pune'),
(2,'Meera',22,'Mumbai'),
(3,'Arjun',21,'Delhi'),
(4,'Kavya',23,'Pune'),
(5,'Neha',22,'Kolkata');

-- Q3. Display all student records
 SELECT * FROM students;

-- Q4. Display only name and age of all students.
 SELECT stdname, age FROM students;

-- Q5. Display students who are from Pune
 SELECT * FROM students WHERE city = 'Pune';

-- Q6. Display students whose age is greater than 21
 SELECT * FROM students WHERE age > 21;

-- Q7. Display students in descending order of age
  SELECT * FROM students ORDER BY age DESC;

-- Q8. Count how many students belong to each city (GROUP BY)
 SELECT city, COUNT(*) AS total_students FROM students GROUP BY city;

-- Q9. Display students whose name starts with 'K' (LIKE)
 SELECT * FROM students WHERE stdname LIKE 'K%';

-- Q10. Delete student whose stdid = 5
  DELETE FROM students WHERE stdid = 5;


-- PART 2 — ALTER COMMAND QUESTIONS
-- Q11. Add a new column contact VARCHAR(15) to the students table.
 ALTER TABLE students ADD contact VARCHAR(15);

-- Q12. Modify the data type of city column to VARCHAR(100).
 ALTER TABLE students MODIFY city VARCHAR(100);

-- Q13. Rename the column stdname to student_name.
 ALTER TABLE students RENAME COLUMN stdname TO student_name;

-- Q14. Drop the column contact from the table.
 ALTER TABLE students DROP COLUMN contact;

-- Q15. Add a new column gender ENUM('M','F').
 ALTER TABLE students ADD gender ENUM('M','F');

-- PART 3 — JOIN PRACTICE
-- Create marks table

CREATE TABLE marks (
    stdid INT,
    subject VARCHAR(50),
    marks INT
);

INSERT INTO marks (stdid, subject, marks) VALUES
(1,'Maths',88),
(2,'Maths',76),
(3,'Maths',92),
(5,'Maths',67);



-- Q16. INNER JOIN: Display student name and marks of only those students who have matching IDs in both tables.

 SELECT s.stdname, m.marks FROM students s INNER JOIN marks m ON s.stdid = m.stdid;

-- Q17. LEFT JOIN: Display all students and their marks (NULL if no marks)
 SELECT s.stdname, m.marks FROM students s LEFT JOIN marks m ON s.stdid = m.stdid;

-- Q18. RIGHT JOIN: Display all marks records along with student names (NULL if student doesn't exist)
 SELECT s.stdname, m.marks FROM students s RIGHT JOIN marks m ON s.stdid = m.stdid;

-- Q19. CROSS JOIN:
-- Display all possible combinations of students and subjects
 SELECT s.stdname, m.subject FROM students s CROSS JOIN marks m;

-- Q20. INNER JOIN with filtering (marks > 80)
 SELECT s.stdname, m.marks FROM students s INNER JOIN marks m ON s.stdid = m.stdid WHERE m.marks > 80;



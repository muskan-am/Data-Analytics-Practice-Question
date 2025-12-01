USE lab;

CREATE TABLE student_crud (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(100)
);

-- Insert(CREATE)
INSERT INTO student_crud (id, name, age, city)
VALUES (1,'Muskan',20,'Prayagraj');

-- Read(SELECT)
SELECT * FROM student_crud;

-- Update
UPDATE student_crud
SET name = 'Muskan Kesharwani' , age=21
WHERE id = 1;

DELETE FROM student_crud WHERE id = 1;
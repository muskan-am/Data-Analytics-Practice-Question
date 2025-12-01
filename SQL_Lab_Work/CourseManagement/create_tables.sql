
USE lab;

DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS faculty;
DROP TABLE IF EXISTS course;

-- COURSE TABLE
CREATE TABLE course (
    course_id VARCHAR(30) PRIMARY KEY,
    course_name VARCHAR(300) NOT NULL,
    description VARCHAR(2000) NOT NULL,
    duration INT NOT NULL,
    min_enrollment INT NOT NULL,
    max_enrollment INT NOT NULL
);

-- FACULTY TABLE
CREATE TABLE faculty (
    faculty_id VARCHAR(30) PRIMARY KEY,
    faculty_name VARCHAR(300) NOT NULL,
    age INT NOT NULL,
    dob DATE NOT NULL,
    qualification VARCHAR(200) NOT NULL
);

-- MODULES TABLE
CREATE TABLE modules (
    module_id VARCHAR(30) PRIMARY KEY,
    module_name VARCHAR(300) NOT NULL,
    description VARCHAR(3000) NOT NULL,
    duration INT NOT NULL,
    course_id VARCHAR(30) NOT NULL,
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

-- Day 4: SQL Basics

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);

INSERT INTO students VALUES (1, 'Arun', 20, 'CSE');
INSERT INTO students VALUES (2, 'Karthik', 21, 'ECE');
INSERT INTO students VALUES (3, 'Priya', 19, 'IT');

SELECT * FROM students;

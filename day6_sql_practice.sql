-- Day 6: SQL Practice Queries

SELECT COUNT(*) FROM students;

SELECT MAX(age) FROM students;

SELECT MIN(age) FROM students;

SELECT department, COUNT(*) 
FROM students 
GROUP BY department;

SELECT * FROM students WHERE name LIKE 'A%';

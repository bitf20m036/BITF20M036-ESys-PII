CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    roll_number TEXT NOT NULL,
    email_address TEXT NOT NULL,
    gender TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    city TEXT NOT NULL,
    interest TEXT NOT NULL,
    department TEXT NOT NULL,
    degree_title TEXT NOT NULL,
    subject TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE

);
CREATE TABLE register (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    confirm_password VARCHAR(255) NOT NULL
);
CREATE TABLE interests (
    id INT PRIMARY KEY AUTO_INCREMENT,
    interest VARCHAR(255) NOT NULL
);
INSERT INTO student (full_name, roll_number, email_address, gender, date_of_birth, city, interest, department, degree_title, subject, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
INSERT INTO interests (interest) VALUES (%s)
SELECT interest FROM interests
SELECT id FROM interests WHERE interest = %s
SELECT id,full_name, roll_number, email_address, gender, date_of_birth, city, interest, department, degree_title, subject, start_date, end_date
FROM student
SELECT id, full_name, roll_number, email_address, gender, date_of_birth, city, interest, department, degree_title, subject, start_date, end_date
FROM student WHERE id = %s
DELETE FROM student WHERE id = %s
UPDATE student
SET full_name = %s, roll_number = %s, email_address = %s, gender = %s,date_of_birth = %s, city = %s, interest = %s, department = %s, degree_title= %s, subject= %s, start_date= %s, end_date= %s
WHERE id = %s
SELECT COUNT(*) FROM student
SELECT id, full_name, roll_number, email_address, gender, date_of_birth, city, interest, department, degree_title, subject, start_date, end_date FROM student ORDER BY {sort_column} {sort_order} LIMIT %s OFFSET %s
INSERT INTO register (username, password, confirm_password) VALUES (%s, %s, %s)
SELECT id FROM register WHERE username = %s
SELECT id FROM register WHERE username = %s AND password = %s
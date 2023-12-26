from models import Student
import pymysql
class databaseHelper:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def Add_Student(self, student):
        mydb = None
        mydbCursor = None
        inserted = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "INSERT INTO student (full_name, roll_number, email_address, gender, date_of_birth, city, interest, department, degree_title, subject, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            args = (student.full_name, student.roll_number, student.email_address, student.gender,student.date_of_birth,student.city,student.interest,student.department,student.degree_title,student.subject,student.start_date,student.end_date)
            mydbCursor.execute(sql, args)
            mydb.commit()
            inserted = True
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()
            if mydb != None:
                mydb.close()
            return inserted

    def add_interest(self, interest):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Add the new interest to the interests table
            sql_insert = "INSERT INTO interests (interest) VALUES (%s)"
            mydbCursor.execute(sql_insert, (interest,))
            mydb.commit()

        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def get_interests(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Retrieve interests from the interests table
            sql_select = "SELECT interest FROM interests"
            mydbCursor.execute(sql_select)
            interests = [row[0] for row in mydbCursor.fetchall()]

            return interests

        except Exception as e:
            print(str(e))
            return []

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()


    def get_interest_id(self, interest_name):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Retrieve the interest ID for the given interest name
            sql_select = "SELECT id FROM interests WHERE interest = %s"
            mydbCursor.execute(sql_select, (interest_name,))
            result = mydbCursor.fetchone()

            if result:
                return result[0]
            else:
                return None

        except Exception as e:
            print(str(e))
            return None

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def get_students(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Execute a SELECT query to fetch all students with their interests
            sql_select = """
                  SELECT id,full_name, roll_number, email_address, gender, date_of_birth, 
                      city, interest, department, degree_title, subject, start_date, end_date
                  FROM student
              """
            mydbCursor.execute(sql_select)
            rows = mydbCursor.fetchall()
            # Convert rows to Student objects
            students = [Student(id=row[0], full_name=row[1], roll_number=row[2], email_address=row[3],
                                gender=row[4], date_of_birth=row[5], city=row[6], interest=row[7],
                                department=row[8], degree_title=row[9], subject=row[10], start_date=row[11],
                                end_date=row[12]) for row in rows]

            return students

        except Exception as e:
            print(f"Error fetching students: {str(e)}")
            return []

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def get_student_by_id(self, student_id):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Execute a SELECT query to fetch a student with the given id
            sql_select = """
                  SELECT id, full_name, roll_number, email_address, gender, date_of_birth, 
                      city, interest, department, degree_title, subject, start_date, end_date
                  FROM student
                  WHERE id = %s
              """
            mydbCursor.execute(sql_select, (student_id,))
            row = mydbCursor.fetchone()

            if row:
                # Convert the row to a Student object
                student = Student(id=row[0], full_name=row[1], roll_number=row[2], email_address=row[3],
                                  gender=row[4], date_of_birth=row[5], city=row[6], interest=row[7],
                                  department=row[8], degree_title=row[9], subject=row[10], start_date=row[11],
                                  end_date=row[12])
                return student
            else:
                return None

        except Exception as e:
            print(f"Error fetching student by id: {str(e)}")
            return None

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def delete_student_by_id(self, student_id):
        mydb = None
        mydbCursor = None
        deleted = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Execute a DELETE query to remove a student with the given id
            sql_delete = """
                  DELETE FROM student
                  WHERE id = %s
              """
            mydbCursor.execute(sql_delete, (student_id,))
            mydb.commit()

            deleted = True

        except Exception as e:
            print(f"Error deleting student by id: {str(e)}")

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

            return deleted

    def update_student(self, student):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Execute an UPDATE query to update the student in the database
            sql_update = """
                   UPDATE student
                   SET full_name = %s, roll_number = %s, email_address = %s, gender = %s,
                       date_of_birth = %s, city = %s, interest = %s, department = %s, degree_title= %s, subject= %s, start_date= %s, end_date= %s
                   WHERE id = %s
               """
            mydbCursor.execute(sql_update, (
                student.full_name, student.roll_number, student.email_address, student.gender,
                student.date_of_birth, student.city, student.interest,student.department,student.degree_title,student.subject,student.start_date,student.end_date, student.id
            ))
            mydb.commit()

            return True  # Return True on successful update

        except Exception as e:
            print(f"Error updating student: {str(e)}")
            return False  # Return False on failure

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def get_paginated_students(self, page, page_size, sort_column, sort_order):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Build and execute the SQL query to get the total count of students
            count_query = "SELECT COUNT(*) FROM student"
            mydbCursor.execute(count_query)
            total_count = mydbCursor.fetchone()[0]
            # Calculate total number of pages
            total_pages = (total_count + page_size - 1) // page_size
            # Ensure the current page is within valid bounds
            page = max(1, min(page, total_pages))

            # Calculate offset
            offset = (page - 1) * page_size

            # Build and execute the SQL query to fetch paginated students
            query = query = f"SELECT id, full_name, roll_number, email_address, gender, date_of_birth, city, interest, department, degree_title, subject, start_date, end_date FROM student ORDER BY {sort_column} {sort_order} LIMIT %s OFFSET %s"

            mydbCursor.execute(query, (page_size, offset))
            # Fetch the results
            students = []
            for student_data in mydbCursor.fetchall():
                # Create a Student object using the fetched data
                student = Student(*student_data)
                students.append(student)

            return students, total_pages

        except Exception as e:
            # Handle exceptions, log errors, etc.
            print(f"Error in get_paginated_students: {str(e)}")
            return [], 0
        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def get_total_pages(self, mydbCursor, page_size):
        try:
            # Execute the query to get the total count of students
            count_query = "SELECT COUNT(*) FROM student"
            mydbCursor.execute(count_query)
            total_count = mydbCursor.fetchone()[0]

            # Calculate total number of pages
            total_pages = (total_count + page_size - 1) // page_size

            return total_pages

        except Exception as e:
            # Handle exceptions, log errors, etc.
            print(f"Error in get_total_pages: {str(e)}")
            return 0

    def register_user(self, username, password, confirm_password):
        mydb = None
        mydbCursor = None
        inserted = False

        try:
            # Check if the username already exists
            if self.is_username_exists(username):
                return False, 'Username already exists. Please choose a different username.'

            # Check if the password and confirm_password match
            if password != confirm_password:
                return False, 'Passwords do not match. Please enter the same password and confirm password.'

            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Insert the new user into the register table
            sql_insert = "INSERT INTO register (username, password, confirm_password) VALUES (%s, %s, %s)"
            mydbCursor.execute(sql_insert, (username, password, confirm_password))
            mydb.commit()

            inserted = True
            return True, 'Registration successful. You can now login.'

        except Exception as e:
            print(str(e))
            return False, 'Error during registration. Please try again.'

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def is_username_exists(self, username):
        mydb = None
        mydbCursor = None

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Check if the username already exists in the register table
            sql_select = "SELECT id FROM register WHERE username = %s"
            mydbCursor.execute(sql_select, (username,))
            result = mydbCursor.fetchone()

            return result is not None

        except Exception as e:
            print(str(e))
            return False

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()

    def authenticate_user(self, username, password):
        mydb = None
        mydbCursor = None

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            # Check if the username and password match a registered user
            sql_select = "SELECT id FROM register WHERE username = %s AND password = %s"
            mydbCursor.execute(sql_select, (username, password))
            result = mydbCursor.fetchone()

            if result:
                return True, 'Login successful.'
            else:
                return False, 'Invalid username or password.'

        except Exception as e:
            print(str(e))
            return False, 'Error during login. Please try again.'

        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()
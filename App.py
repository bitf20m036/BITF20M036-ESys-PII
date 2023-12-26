# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from models import Student
from databaseHelper import databaseHelper

app = Flask(__name__)

# Route to render the add student form
@app.route('/AddStudentform')
def AddStudentform():
    hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
    interests = hdlr.get_interests()
    return render_template("add_student.html", interests=interests)

# Route to add a new student
@app.route('/add_student', methods=["GET", "POST"])
def Add_student():
    try:
        if request.method == "POST":
            # Process form data and add a new student
            full_name = request.form["full_name"]
            roll_number = request.form["roll_number"]
            email_address = request.form["email_address"]
            gender = request.form["gender"]
            date_of_birth = request.form["date_of_birth"]
            city = request.form["city"]
            interest = request.form["interest"]

            if interest == "add_new":
                new_interest = request.form["new_interest"]
                # Save the new interest to the database
                hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
                hdlr.add_interest(new_interest)
                interest = new_interest  # Use the new interest name directly

            department = request.form["department"]
            degree_title = request.form["degree_title"]
            subject = request.form["Subject"]
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]

            # Placeholder: Add logic to create Student object
            student = Student(
                id=None,  # Assuming 'id' is generated automatically or set to None for a new student
                full_name=full_name,
                roll_number=roll_number,
                email_address=email_address,
                gender=gender,
                date_of_birth=date_of_birth,
                city=city,
                interest=interest,
                department=department,
                degree_title=degree_title,
                subject=subject,
                start_date=start_date,
                end_date=end_date
            )

            # Placeholder: Add logic to insert student into the database
            hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
            flag = hdlr.Add_Student(student)

            if flag:
                return render_template("add_student.html", message="Successfully added", interests=hdlr.get_interests())
            else:
                message = "Adding student failed"
                return render_template("add_student.html", message=message, interests=hdlr.get_interests())

    except Exception as e:
        message = "Adding failed " + str(e)
        return render_template("add_student.html", message=message, interests=hdlr.get_interests())
@app.route('/display_students', methods=['GET', 'POST'])
def display_students():
    # Get page, page_size, sort_column, and sort_order from request args
    page = int(request.args.get('page', 1) or 1)
    page_size = int(request.args.get('page_size', 10))
    sort_column = request.args.get('sort_column', 'id')
    sort_order = request.args.get('sort_order', 'asc')

    hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
    students, total_pages = hdlr.get_paginated_students(page, page_size, sort_column, sort_order)

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None

    return render_template(
        'display_students.html',
        students=students,
        total_pages=total_pages,
        page=page,
        page_size=page_size,
        sort_column=sort_column,
        sort_order=sort_order,
        prev_page=prev_page,
        next_page=next_page
    )

@app.route('/view_student/<int:id>')
def view_student(id):
    # Assuming you have a method to retrieve a single student by ID
    hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
    student = hdlr.get_student_by_id(id)
    return render_template('view_student.html', student=student)

@app.route('/edit_student/<int:id>', methods=["GET", "POST"])
def edit_student(id):
    # Assuming you have a method to retrieve a single student by ID
    hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
    student = hdlr.get_student_by_id(id)
    interests = hdlr.get_interests()

    if request.method == "POST":
        # Process the form data and update the student
        updated_student = Student(
            id=id,
            full_name=request.form.get("full_name"),
            roll_number=request.form.get("roll_number"),
            email_address=request.form.get("email_address"),
            gender=request.form.get("gender"),
            date_of_birth=request.form.get("date_of_birth"),
            city=request.form.get("city"),
            interest=request.form.get("interest"),
            department=request.form.get("department"),
            degree_title=request.form.get("degree_title"),
            subject=request.form.get("Subject"),
            start_date=request.form.get("start_date"),
            end_date=request.form.get("end_date"),  # Added comma here

            # Add other fields
        )

        # Update the student in the database
        if hdlr.update_student(updated_student):
            # Fetch the updated student from the database
            updated_student = hdlr.get_student_by_id(id)
            message = "Student updated successfully!"

            return render_template('edit_student.html', student=updated_student, interests=hdlr.get_interests(), message=message)

    return render_template('edit_student.html', student=student, interests=hdlr.get_interests())

@app.route('/delete_student/<int:id>')
def delete_student(id):
    # Assuming you have a method to delete a student by ID
    hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
    success = hdlr.delete_student_by_id(id)

    if success:
        # Fetch the updated list of students and render the template
        students = hdlr.get_students()
        return render_template('display_students.html', students=students)
    else:
        # Handle the case where deletion fails
        return render_template("Deletion failed")
@app.route('/dashboard')
def dashboard():
    # You can perform any necessary data processing here
    # For simplicity, I'm passing an empty dictionary to render_template
    # Pass interests data to the template

    hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
    interests = hdlr.get_interests()
    return render_template('dashboard.html', interests=interests)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")

        # Register the user
        success, message = hdlr.register_user(username, password, confirm_password)
        if success:
            message="Successfully Registered";
            return render_template('Register.html', message=message)
        else:
            return render_template('Register.html', message=message)

    return render_template('Register.html')
@app.route('/')
def loginform():
    return render_template('login.html')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hdlr = databaseHelper("localhost", "root", "Asma123@", "student_interest_system")
        # Check if the username and password match a registered user
        success, message = hdlr.authenticate_user(username, password)

        if success:
            interests = hdlr.get_interests()
            return render_template('dashboard.html',interests=interests)
        else:
            return render_template('login.html', message=message)

    return render_template('login.html')

if __name__ == '__main__':
    app.run()

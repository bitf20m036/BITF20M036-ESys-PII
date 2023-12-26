class Student:
    def __init__(self, id, full_name, roll_number, email_address, gender,date_of_birth,city,interest,department,degree_title,subject,start_date,end_date):
        self.id = id
        self.full_name = full_name
        self.roll_number = roll_number
        self.email_address = email_address
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.city = city
        self.interest = interest
        self.department = department
        self.degree_title = degree_title
        self.subject = subject
        self.start_date = start_date
        self.end_date = end_date

    def print(self):
        print(self.full_name, self.roll_number, self.email_address, self.gender,self.date_of_birth,self.city,self.interest,self.department,self.degree_title,self.subject,self.start_date,self.end_date)

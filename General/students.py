class Students:
    def __init__(self,fname,lname,rollno,email):
        self.fname = fname
        self.lname = lname
        self.rollno = rollno
        self.email = email

class Course:
    def __init__(self,name,student,marks):
        self.name = name
        self.student = student
        self.students = []
        self.marks  = marks
    
    def add_student(self,student):
        if len(self.students) < (self.student):
            self.students.append(student)
            return True
        return False
   
    
    def percentage(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (len(self.marks) * 100)) * 100
        return percentage
    def cgpa(self):
        total_cgpa = self.percentage()/9.5
        return total_cgpa 

    def __str__(self):
        return f"{self.name} has {self.student} no of students with {self.percentage()} with {self.cgpa()}"

        
    
std1 = Students("musa","rehman",33,"musa@gmail.com")
course = Course("c++",8,[85,90,75,80])
course.add_student(std1)
course.percentage()
print(course)
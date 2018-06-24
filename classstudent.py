class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print("student information")
        print("Name-",self.name)
        print("roll no-",self.rollno)

name=input("enter the name of student")
rollno=int(input("enter the roll no"))
c1=student(name,rollno)
c1.display()

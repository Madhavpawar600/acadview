class employee:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empcount+=1

    def displaycount(self):
        print("total employee",employee.empcount)

    def displayemployee(self):
        print("name:",self.name, ",salary:",self.salary)

emp1=employee("zara",65000)
emp2=employee("vadhma",890000)

emp1.displaycount()
emp1.displayemployee()
#emp1.displayemployee()
#emp2.displaycount()

print("total",employee.empcount)

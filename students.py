class Student:
    def __init__(self, name, reg_number, course):
        self.name = name
        self.reg_number = reg_number
        self.course = course

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_number}")
        print(f"course: {self.course}")

student1 = Student("Nicho Sssentongo", "M23B13/013","Computer Science")
student2 = Student("Bash Mickey", "M23B13/019", "Information technology")
student3 = Student("Hajarah Ssentongo", "M23B13/016", "Data analysis")
student4 = Student("kemi Musa", "M23B13/015","Computer Science")

student1.display_info()
print()  
student2.display_info()
student3.display_info()
student4.display_info()
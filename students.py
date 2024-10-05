class Student:
    def __init__(self, name, reg_number):
        self.name = name
        self.reg_number = reg_number

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Registration Number: {self.reg_number}")

student1 = Student("Nicho Sssentongo", "M23B13/013")
student2 = Student("Bash Mickey", "M23B13/019")
student3 = Student("Hajarah Ssentongo", "M23B13/016")
student4 = Student("kemi Musa", "M23B13/015")

student1.display_info()
print()  
student2.display_info()
student3.display_info()
student4.display_info()

class Student:
    """ Các sinh viên nhóm ES Python """
    count = 0
 
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university
        Student.count = Student.count + 1
    
    def say_hi(self, favourite = ""):
        print(f"Hi, I am {self.name}, {self.age} years old.")
        print(f" Now I am studying at {self.university}.")
        if favourite != "":
            print(" My favourite is: ", favourite)
        else:
            print(" I don't know what I really like!")
        print(" Nice to meet you here!\n")
        
s1 = Student("Liên", 22, "Mokwon")
s2 = Student("Ba", 20, "FPT")
s3 = Student("An",20, "Kinh tế quốc dân")

s1.say_hi("book reading")
s2.say_hi("No avata")
s3.say_hi()

print("Số lượng sinh viên là:", Student.count)

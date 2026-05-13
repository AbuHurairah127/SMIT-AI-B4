# class Student:
#     name:str
#     age:int
#     def study(self):
#         print(self.name, "Studying")

# student1 = Student()
# student1.name = "Abu Hurairah"
# student1.age = 23
# print(student1.name)
# print(student1.age)
# student1.study()


# student2 = Student()
# student2.name = "Ahmad"
# student2.age = 23
# print(student2.name)
# print(student2.age)
# student2.study()




class Student:
    name:str
    age:int
    email:str
    __password:str
    def __init__(self,_name,_age,_email,_password):
        self.email = _email
        self.name = _name
        self.age = _age
        self.__password = _password
    
    @property
    def passwordBtao(self):
        print("Password is being accessed")
        if self.isloggedIn == True:
            return self.__password
        else:
            return "You are not authorized to access the password"



student1 = Student("Abu Hurairah",23,"abu@gmail.com","password")
student2 = Student("Ahmad",24,"ahmad@gmail.com","123456789")
student3 = Student("Ali",25,"ali@gmail.com","123456789")

print(student1.name,student1.age,student1.email)
print(student1.passwordBtao)
print(student2.passwordBtao)




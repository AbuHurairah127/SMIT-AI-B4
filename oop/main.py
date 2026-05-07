# name:str = "Abu Hurairah"
# age:int = 23
# city:str = "Faisalabad"
# country:str = "Pakistan"
# country2:str =38000

# print(name)
# print(age)
# print(city)
# print(country)
# print(country2)


# car:dict[str,Any] = {
#     model:"M5 Competition",
#     year:2026,
#     color:"Black",
#     price:38000,
#     owner:"Abu Hurairah",
#     interiorColor:["Black","Brown","White"],
#     isRegistered:True,
# }


# bankuser1 = {
#     deposit:lambda x: x * 1.05,
# }



# class Car:
#     id:int = 1
#     model:str = "M5 Competition"
#     def drive(self):
#         print("Driving the car")
#         print("Driving the M5 Competition")
#         print("Driving the BMW")
#         print("Driving the",self.model)


# car1 = Car()
# car2 = Car()
# car1.model = "7 series"
# car2.model = "X7"

# print(car1.drive())
# print(car2.drive())




class Car:
    id: int
    model: str
    company: str
    def __init__(self,_id,_model,_company):
        self.id = _id
        self.model = _model
        self.company = _company

   

car1 = Car(1,"M5 Competition","BMW")
car2 = Car(2,"7 series","BMW")

print(car1.id)
print(car1.model)
print(car1.company)

print(car2.id)
print(car2.model)
print(car2.company)
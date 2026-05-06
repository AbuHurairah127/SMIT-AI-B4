# myCar = {
#     "brand":"BWM",
#     "model":"M5 Competition",
#     "year":2026,
#     "color":"Black",
#     "price":"price",
#     "owner":"Abu Hurairah",
#     "interiorColor":["Black","Brown","White"],
#     "isRegistered":True,
# }


# # print(myCar["interiorColor"])
# # print(myCar.get("engineType","V8"))


# # myCar["ownerLastName"] = "Ahmad"
# for key in myCar.items():
#     print(key)
#     # print(myCar[key])
#     print("--------------------------------")





# students = [{"name":"Abu Hurairah","age":23,"city":"Faisalabad","country":"Pakistan"},
#             {"name":"Ahmad","age":24,"city":"Lahore","country":"Pakistan"},
#             {"name":"Ali","age":25,"city":"Karachi","country":"Pakistan"},
#             {"name":"Usman","age":26,"city":"Islamabad","country":"Pakistan"},
#             {"name":"Hassan","age":27,"city":"Peshawar","country":"Pakistan"},
#             {"name":"Bilal","age":28,"city":"Quetta","country":"Pakistan"},
#             {"name":"Zahid","age":29,"city":"Multan","country":"Pakistan"},
#             {"name":"Rizwan","age":30,"city":"Faisalabad","country":"Pakistan"},
#             {"name":"Zahid","age":29,"city":"Multan","country":"Pakistan"},
#             {"name":"Rizwan","age":30,"city":"Faisalabad","country":"Pakistan"},]



# student = {"name":"Abu Hurairah","age":23,"city":"Faisalabad","country":"Pakistan"}

# print(student.pop("car",None))
# print(student.clear())
# print(student.popitem())
# print(student)


# Tuple

# numT = (5,4,6,7,8,1,2,3)
# numList = [5,4,6,7,8,1,2,3]
# print(numT.count(5))
# print(numT.index(5))
# print(len(numT))
# # numList[0] = 10
# # print(numT[0])
# # print(numList[0])


# roles = ("admin","user","guest","superadmin")
# # a, b, c = roles
# # print(a,b,c)

# a, b,c,d = roles
# e,*f = roles
# print(a,b,c,d)
# print(e,f)


# a = {1,2,3,2,2,6,7,8,9,10}
# print(a.add(11))
# # print(a.remove(23))
# print(a.discard(10))
# print(a.pop())
# print(len(a))
# # print(a.copy())
# # print(a.clear())
# # print(a)

b = {11,12,13,4,3,1,1,8,19,20}
print("b",b)

# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.isdisjoint(b))
# print(a.isdisjoint(b))

# abc = (1,2,3,4,5) * 3
# print(abc)
# abc = ()



my_list = [1,2,3,4,5,5,5,5,9,10]
my_set = set(my_list)
print(my_set)
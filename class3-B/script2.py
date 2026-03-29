obtainedMarks = 75
totalMarks = 100
percentage = (obtainedMarks/totalMarks)*100

# if percentage >=90 and percentage <=100:
#     print("A+ Grade")

# if percentage >=80 and percentage <90:
#     print("A Grade")

# if percentage >=70 and percentage <80:
#     print("B Grade")

# if percentage >=60 and percentage <70:
#     print("C Grade")

# if percentage >=50 and percentage <60:
#     print("D Grade")

# if percentage >= 33 and percentage <50:
#     print("E Grade")

# if percentage>=0 and percentage <33:
#     print("Fail")

# if percentage>100 or percentage <0:
#     print("Invalid Percentage/Marks")



if percentage >=90 and percentage <=100:
    print("A+ Grade")
elif percentage >=80 and percentage <90:
    print("A Grade")
elif percentage >=70 and percentage <80:
    print("B Grade")
elif percentage >=60 and percentage <70:
    print("C Grade")
elif percentage >=50 and percentage <60:
    print("D Grade")
elif percentage >= 33 and percentage <50:
    print("E Grade")
elif percentage>=0 and percentage <33:
    print("Fail")
elif percentage>100 or percentage <0:
    print("Invalid Percentage/Marks")


if obtainedMarks % 2 == 0:
    print("Even")
else:
    print("Odd")
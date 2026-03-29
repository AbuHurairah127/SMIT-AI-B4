obtainedMarks = 45
totalMarks = 75

percentage = (obtainedMarks/totalMarks)*100
print(percentage,"Percentage - functionName - class3-B/script.py") 
# best practice 👇
if percentage > 33:
    print("Pass")

resp = percentage > 33
print(resp,"resp")

if resp:
    print("pass")
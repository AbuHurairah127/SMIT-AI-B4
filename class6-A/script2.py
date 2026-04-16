# def sum2(a,b):
#     return a + b

# x = lambda a,b: a + b
# print(x(10,20))

# def evenOrOdd(n):
#     if n % 2 ==0 :
#         return "Even"
#     return "Odd"

# print(evenOrOdd(10))

evenOdd = lambda num: "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(evenOdd(10))


def checkNum(num):
    if num> 0:
        return "positive"
    else:
        if num< 0:
            return "Negative"
        else:
            return "Zero"

print(checkNum(10))

nums = [10,20,30,40,50,60]
newNums = [x//10 for x in nums if x > 20]
print(newNums)
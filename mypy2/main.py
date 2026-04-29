# a = 10
# b = 20
# print(a,b)
# a = b
# b = 15
# print(a,b)



# num1 = [1,2,3,4,5]
# num2 = num1.copy()
# num2[3] = 45
# print(num1,num2)




def func1(x):
    a = 10
    x(a)
    print("This is function 1")

def func2(num):
    print("This is function 2",num)

func1(func2)



nums = [9,78,85,74,25,36,45,14,51,78,99,89,8,87,5]
# [odd,even,odd,even,odd,even,even, ....]


def oddOrEven(num):
    if num % 2 == 0:
        return "even"
    return "odd"
    


ans = map(oddOrEven,nums)
print(list(ans))


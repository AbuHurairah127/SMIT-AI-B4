students = ["Ali","Ahmad","Anas","Rizwan","Zahid","Bilal"]

# print(students.pop())
# print(students)
# print(students)
# print(students.pop(2))
# print(students)

# i = 0
# while i < len(students):
#     print(students[i].upper())
#     i = i + 1


# nums = [13,89,85,75,-45,-44,47,63,-9,5,3,-2,100,0,-100]
# print(nums)
# i = 0
# while i < len(nums):
#     if nums[i]<0:
#         print(nums.pop(i)) 
#     else:   
#         i = i + 1


# nums = [13,89,85,75,-45,-44,47,63,-9,5,3,-2,100,0,-100]
# newList = []
# print(nums)
# i = len(nums) - 1
# while i >= 0:
#     if nums[i] < 0:
#         newList.append(nums.pop(i))
#     i = i - 1

# print(nums)
# print(newList)

#  * * * * *
# i = 0
# while i < 5:
#     print("*", end=" ")
#     i = i + 1


#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *

# i = 0
# while i < 5:
#     print("* * * * *")
#     i = i + 1


# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# i = 1
# while i < 6:
#     print(i, i, i, i, i)
#     i = i + 1


# a a a a a
# b b b b b
# c c c c c
# d d d d d
# e e e e e

# list = ['a', 'b', 'c', 'd', 'e']
# i = 0
# while i < len(list):
#     print(list[i], list[i], list[i], list[i], list[i])
#     i += 1   


# * 
# * *
# * * *
# * * * *
# * * * * *


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i: # j = 1, i = 1
#         print("*", end=" ")
#         j += 1 # j = 2,3
#     print()
#     i += 1 # i = 2



# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# i = 1
# while i < 6:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1

# print(list(range(1,51,2)))
# for elem in range(1,10):
#     print(elem)


# sum = 1
# for abc in range(0,19,2):
#     sum = sum * abc

# print(sum)



for elem in range(1,10):
    if elem == 5:
        break
    print(elem)


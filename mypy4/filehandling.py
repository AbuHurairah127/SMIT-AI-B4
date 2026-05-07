# data1 = open('./../myfile.txt', 'w')
# print(data1.write("This is magic"))
# data1.close()
# data2 = open('./../myfile.txt', 'r')
# print(data2.read())
# data2.close()


# data1 = open('./../myfile.txt', 'a')
# data1.write("\nThis is magic")
# data1.close()


data2 = open('myfile.txt', 'x')
data2.write("This is magic")
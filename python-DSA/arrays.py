
list = [1,2,3,4,5]

list.append(1)


length = len(list)
index = int(input("what position do you want to insert the number into: "))
number = int(input("enter number: "))

list.insert(index-1,number)

print(list)




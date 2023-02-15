# lists in python 
# create a list using square brackets

a = [1, 3 , 354 ,32,324 ,4 , 4]
print(a)

# # # type
print(type(a))

# # # access using index
print(a[:-2])



a.remove(3)
print(a)


# # change the valus of the list

a[0] = 78
print(a)

# # we can also create a list using different data type

a = [1 , True , "Shailesh" , 98.6]
print(a)

# # list slicing

names = ["Shailesh" , "Shashant" , "Durvesh" , "Tufel" , "Divya"]
print(names[0:4])

print(names[-5:])

#                         # ------- list methods ----------- #

list1 = [1 , 2, 544 , 3, 8, 7 , 9 , 10 ]
list1 = ["shailesh", "Gaddam" , "bhai"]
print(list1)


# # sort the list
list1.sort()
print(list1)

# # reversed the list
list1.reverse()
print(list1)

# # append the list means add something
list1.append(76)
print(list1)

# # insert the value using index
list1.insert(2 , 789)
print(list1)

# # pop method delete the function using index
list1.pop(2)
print(list1)

# # clears all the emelemts from the list
list1.clear()
print(list1)

list1.remove(3)
print(list1)

names = ["Muskan" , "Shailesh" , "Umer" , "Tufel"]

names_with_o = [item for item in names if "S" in item]

# print(names)
print(names_with_o)

numbers = ["1" , "79" , "99" , "7", "9"]

vi = [item for item in numbers if "9" in item]
print(vi)




# # Practice
# 1. 
f1 = input("Enter the fruit name! ")
f2 = input("Enter the fruit name! ")
f3 = input("Enter the fruit name! ")
f4 = input("Enter the fruit name! ")
f5 = input("Enter the fruit name! ")
f6 = input("Enter the fruit name! ")
f7 = input("Enter the fruit name! ")


fruits = [f1,f2 , f3 , f4 , f5 , f6 , f7]
print(fruits)

# # 2. take input from the student and sort the marks

m1 = int(input("Enter the Student Marks! "))
m2 = int(input("Enter the Student Marks! "))
m3 = int(input("Enter the Student Marks! "))
m4 = int(input("Enter the Student Marks! "))
m5 = int(input("Enter the Student Marks! "))
m6 = int(input("Enter the Student Marks! "))
m7 = int(input("Enter the Student Marks! "))

Marks = [m1 , m2 ,m3 , m4 , m5 , m6]
Marks.sort()
print(Marks)

# addition of list items
l1 = [234, 5, 25,55]
print(l1[0] + l1[1] +l1[2] +l1[3])
print(sum(l1))

L2 = [876 , 787 , 789]
print(sum(L2))
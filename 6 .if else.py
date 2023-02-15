age = int(input("Enter your Age: "))

if age >= 18:
    print("YES , You're eligible for driving license.")
else:
    print("NO, Sorry you're not eligible")


age = int(input("Enter your Age: "))
if (age>30) and (age<50):
    print("Yes, you can work with us!")

else:
    print("Sorry! your cant work with us!")

# relation operators
# ==
# >=
# <=

# logical operators
# and
# or 
# not


# in and is 
# in
list = [87 , 67 , 9 , 4]
print(67 in list)

# is
a = 55 
if a is 55:
    print("Yes")
else:
    print("No!")


# practice 
# 1. 

num1 = int(input("Enter your Number 1 : "))
num2 = int(input("Enter your Number 2 : "))
num3 = int(input("Enter your Number 3 : "))
num4 = int(input("Enter your Number 4 : "))

if (num1 > num4):
    f1 = num1
else:
    f1 = num4

if (num2 > num3):
    f2 = num2
else:
    f2 = num3

if (f1>f2):
    print(str(f1) + " f1 is Greater")
else:
    print(str(f2) +  " f2 is Greater")


# 2.
sub1 = int(input("Enter your marks \n : "))
sub2 = int(input("Enter your marks \n : "))
sub3 = int(input("Enter your marks \n : "))

if (sub1<33 or sub2<33 or sub3<33):
    print("You're failed because of not scoring 33 marks in one of these exam")
elif (sub1 + sub2 + sub3)/3 < 40:
    print("Youre fail because of less percentage")
else:
    print("Congrats you're passed!")

# 3.
text = input("Enter your text: \n")

if ("make money in" in text):
    spam = True
elif ("subscribe this" in text):
    spam = True
elif ("congrats you have won reward" in text):
    spam = True
elif ("buy now" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is Spam")
else:
    print("This is not spam!")

# 4.
username = input("Enter your username: ")

if len(username) >= 10:
    print("This name contains greater than 10 char")
else:
    print("This username contains less than 10 char")

# 5.
names = ["shailesh" , "harsh" , "shashant"]
name = input("Enter your name")

if name in names:
    print("Yes, this name is present in the list")

else:
    print("Sorry! this name is not present in the list")

# 6.
marks = int(input("Enter your marks"))

if marks >= 90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"


print("Your grade is " + grade)
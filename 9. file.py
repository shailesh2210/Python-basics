# use open function to read the file
# by default mode is r

# reading the file

# f = open("./sample.txt" , "r")
# data = f.read()
# print(data)
# f.close()


# f = open("./sample.txt" , "r")
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)

# # writing the file
# f = open("Another.txt" , "w")
# f.write("Shailesh Bhai kya bolte tum")
# f.close()

# # with statement
# with open("Another.txt" ,"r") as f:
#     a = f.read()
# print(a)


# practise

# f = open("sample.txt", "r")
# t = f.read()
# if "Shailesh" in t:
#     print("Yes! , Shailesh is present")
# else:
#     print("Shailesh is not present")

# f.close()

# 2. 

# def game():
#     return 7898687

# score = game()

# with open("highscore.txt", "r") as f:
#     highscore = f.read()

# if highscore ==" ":
#     with open("highscore.txt" , "w") as f:
#         f.write(str(score))

# elif int(highscore)<score:
#     with open("highscore.txt" , "w") as f:
#         f.write(str(score))

# 3.

# for i in range(2 , 21):
#     with open(f"tables/tables_of_{i}.txt" , "w") as f:
#         for j in range(1 , 11):
#             f.write(f"{i}x{j} = {i*j}\n")


# 4.

# with open("sample.txt" , "r") as f:
#     content = f.read()

# content = content.replace("lavde" , "???")
# with open("sample.txt" , "w") as f:
#     f.write(content)


# 5.

content = True
i = 1
with open("hey.txt") as f:
    while content:
        content = f.readline()
        if "Shailesh" in content.lower():
            print(content)
            print(f"Yes", "Shailesh is present in line no")
        i+=1

f = open("hey.txt" , "r")
data = f.read()
print(data)

# copy file
f = open("hey.txt" , "r")
content = f.read()

f = open("copy.txt" , "w")
f.write(content)


# 6. identical files

file1 = "hey.txt"
file2 = "copy.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("files are not identical")
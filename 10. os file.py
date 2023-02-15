import os

files = os.listdir("tables")

for i in files:
    print(i)

data = os.rename("./tables/hey.txt" , "./tables/heyyyy.txt")
print(data)

files = os.listdir("tables")
for i in files:
    if i.endswith(".png"):
        print(i)

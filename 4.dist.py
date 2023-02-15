mydict = { 
   "Name" : "Shailesh Gaddam",
    "Age" : "20",   
}

print(mydict)
print(type(mydict))
print(mydict["Name"])
print(mydict.items())


# deleting key values from the dict
del mydict["Age"]
print(mydict)

# adding key values into dict

mydict["Marks"] = 20
print(mydict)

# update the dict

mydict.update({"Marks" : 22})
print(mydict)

# clearing the dict
# print(mydict.clear())

# copying the dict
newdict = mydict.copy()
print(newdict)

# getting values
print(mydict.values())

# getting keys
print(mydict.keys())

print(mydict.items())




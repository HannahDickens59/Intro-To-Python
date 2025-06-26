#Lists
# Apple = 0, banana = 1 ...
fruits = ["apple", "banana", "peach", "kiwi", "cherry"] 
print(fruits[0])

print(fruits)

fruits[2] = "kiwi" #Changing a value in the list: 
print(fruits)

fruits.append("strawberry") #Adding a value to the end of a list
print(fruits)

fruits.insert(2, "naartjie") #To insert a value in the middle of the list
print(fruits) 

fruits.remove("kiwi") #To remove an item - if there is a repitition, it removes only the first.
print(fruits)

fruits.sort() #Sort in alphabetical order
print(fruits)

fruits.sort(reverse= True)
print(fruits)



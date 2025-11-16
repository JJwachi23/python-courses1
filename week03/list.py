# List 

# List count like index [0]
sports = ["football", "basketball", "table-tennis", "golf"]

print(len(sports))

list1 = [1 ,3 ,5, 7, 9]
list2 = [True, False, True]

print(type(list1))
print(type(list2[2]))

# list() || []
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# golf
print(sports[-1])

# (ค่าที่เริ่มนับ) : (ค่าที่ไม่นับ)
# cherry, orange, kiwi
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mongo"]
print(fruits[2:5])
# 
print(fruits[:4])
# 
print(fruits[2:])

# 
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")

# ----------------------------- Change Item in List ---------------------------------------
fruits[1] = "coconut"
# apple, coconut, cherry, orange, kiwi, mongo
print(fruits)

# ----------------------------- Added Item in List ---------------------------------------
# .append() 
fruits.append("grape")
print(fruits)

# .insert()
fruits.insert(1, "watermelon")
print(fruits)

# .extend()
fruits2 = ["watermelon", "grape", "coconut"]
fruits.extend(fruits2)
print(fruits)

# ----------------------------- Remove Item in List ---------------------------------------
# .remove()
fruits.remove("orange")
print(fruits)

# .pop()
fruits.pop(1)
print(fruits)

fruits.pop()
print(fruits)
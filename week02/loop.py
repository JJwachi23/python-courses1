# Week02 Loop

# for
# while
# while...else

fruits = ["apple", "banana", "cherry", "grape"]

i = 0

# A function for loop is used for interating 
# over a sequence (list, dictonary)
for x in fruits:
    print(x)

for y in "banana":
    print(y)

for z in fruits:
    print(z)
    if z == "banana":
        break

for q in range(10):
    print(q)


# A function whie loop will continue until 
# the statement is FALSE
while i < 9:
    print(i)
    i += 1 # i = i + 1

# while and break statement
while i < 7:
    print(i)
    if i == 6:
        break
    i += 1

while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)


# while..else
while i < 20:
    print(i)
    i += 1
else:
    print(" i is no longer less than 20")
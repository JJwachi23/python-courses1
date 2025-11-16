# 1. ให้ดึงค่าตัวอักษร HelLoEDco ออกมาทีละตัวพร้อมบอกว่ามีทั้งหมดกี่ตัวอักษร 

hello = "HelLoEDco"
total = 0

for x in hello:
    total += 1
    print(x)

print("Total of character",total)

# len() = นับค่าความยาวของตัวอักษร

# 2. ทำสามเหลี่ยมกลับด้านโดยความสูงให้รับมาจากค่า input() 
# input = 5
# **********
#  *******
#   *****
#    ***
#     *

height = int(input("Please enter your height of triangle: "))

for n in range(height, 0, -1):
  spaces = height - n
  triangle = 2*n - 1
  print(' ' * spaces + '*' * triangle)

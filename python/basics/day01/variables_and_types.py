# Day 1 - Variables and Types

name = "Elad"
age = 29
height = 1.78
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

age_str = str(age)
height_int = int(height)

print(age_str, type(age_str))
print(height_int, type(height_int))

user_age = input("Enter your age: ")
user_age = int(user_age)

print("In 5 years you will be:", user_age + 5)

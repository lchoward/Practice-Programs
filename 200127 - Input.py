# gather inputs on name and age
name = raw_input("Please enter your name: ")
str_age = raw_input("How old will you be at the end of 2020? ")
age = int(str_age)

#quick maths
year100 = 100-age+2020
str_year100 = str(year100)

print(name + ", you will be 100 years old in " + str_year100)
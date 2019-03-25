from math import *

character_name = "Tom"
character_age = 35
is_male = True

print("There once was a man named \"" + character_name + "\",")
print("he was " + str(character_age) + " years old.\n")

character_age = character_age - 10

print("He really liked the name \"" + character_name.replace("Tom", "Mike") + "\",")
print("but his name was \"" + character_name + "\",")
print("and he wished he was " + str(character_age) + ".\n")

print(character_name.upper().isupper())
print(len(character_name))
print(character_name[0])
print(character_name.index("T"))

print((12 - (4 + 2) * 7) / -5)
print(10 % 3)
my_num = -5
print(abs(my_num))
print(pow(3, 2))
print(max(3, 2))
print(min(3, 2))
print(round(3.7))
print(round(3.2))
print(floor(3.2))
print(ceil(3.2))
print(sqrt(36))


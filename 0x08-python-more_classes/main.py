#!/usr/bin/python3
###################################################################################
print("-----------------------------------[0]------------------------------------")
Rectangle = __import__("0-rectangle").Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
###################################################################################
print("-----------------------------------[1]------------------------------------")
Rectangle = __import__("1-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
###################################################################################
print("-----------------------------------[2]------------------------------------")
Rectangle = __import__("2-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
###################################################################################
print("-----------------------------------[3]------------------------------------")
Rectangle = __import__("3-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

###################################################################################
print("-----------------------------------[4]------------------------------------")
Rectangle = __import__("4-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

###################################################################################
print("-----------------------------------[5]------------------------------------")


###################################################################################
print("-----------------------------------[6]------------------------------------")


###################################################################################
print("-----------------------------------[7]------------------------------------")

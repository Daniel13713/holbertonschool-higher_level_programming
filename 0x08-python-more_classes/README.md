# Python - Python - More Classes and Objects

### Resources
##### Read or watch:

- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s&ab_channel=Socratica)
- [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk&ab_channel=MITOpenCourseWare)
- [verify a type of a varible in a class](https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not)
- [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

## Tasks
#### 0. Simple rectangle
Write an empty class Rectangle that defines a rectangle:

#### 1. Real definition of a rectangle
Private instance attribute: width:
property **def width(self):** to retrieve it
property setter **def width(self, value):** to set it:
width must be an integer, otherwise raise a **TypeError** exception with the message **width must be an integer**
if width is less than 0, raise a **ValueError** exception with the message **width must be >= 0**
Private instance attribute: height:
property **def height(self):** to retrieve it
property setter**def height(self, value):** to set it:
height must be an integer, otherwise raise a **TypeError** exception with the message **height must be an integer**
if height is less than 0, raise a **ValueError** exception with the message **height must be >= 0**
Instantiation with optional width and height: **def __init__(self, width=0, height=0):**

#### 2. Area and Perimeter
Public instance method: **def area(self):** that returns the rectangle area
Public instance method: **def perimeter(self):** that returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0

#### 3. String representation
print() and str() should print the rectangle with the character #: (see example below)
if width or height is equal to 0, return an empty string
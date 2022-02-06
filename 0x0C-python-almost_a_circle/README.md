# Python - Almost a circle


### Background Context
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
  - How to update private attributes?? :
    - [setattr Method](https://docs.python.org/3/library/functions.html#setattr)
    - [getattr](https://docs.python.org/3/library/functions.html#getattr)
    - [Use setattr to update](https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python)
- Class method
- Static method
- Inheritance

- Unittest
  - [About testing in general, about __init__py file too](https://realpython.com/python-testing/)
    - What do you want to test=
    - Are you writing a unit test or an integration test?
    - How to Write Assertions:
  - [Documentation oficial](https://docs.python.org/3/library/unittest.html)
  - [Side Effects]()
    - [Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)
  - [catch a raise error with unittest](https://www.youtube.com/watch?v=cdxRMjYDrmg&ab_channel=ParisNakitaKejser)
  - [Test exception, asserRiase, error_code](https://www.youtube.com/watch?v=LxbiAHGkPhk&ab_channel=AnInsightfulTechie)
  - [assertRaise and AssertRaiseRegex](https://www.tutorialspoint.com/unittest_framework/unittest_framework_exceptions_test.htm)

- Read/Write file

- Zip Method
  - [Use for Looping Over Multiple Iterables](https://realpython.com/python-zip-function/)

- args and kwargs
  - [blog](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
  - [Optional Arguments in Python With *args(unpack iterables) and **kwargs(unpack dictionaries)](https://www.youtube.com/watch?v=WcTXxX3vYgY&ab_channel=RealPython)
  - [more about * and **](https://realpython.com/python-kwargs-and-args/)
  - [Wrapper functions??](https://www.geeksforgeeks.org/function-wrappers-in-python/)

- Serialization/Deserialization

- JSON
![Serialitation - Deserialitation](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/images/Serialization.PNG)

commits:
- :stop_sign: some don't work
- :rotating_light: Priority
- :construction: review test cases
- :wilted_flower: Doubts, not sure
- :deciduous_tree: working!!
- :arrows_counterclockwise: update a script

## Parts of the Project

#### [1. Base class](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)

#### [2. Rectangle](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)
  - Attributes
    - [Width](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/5002134d000a267c20418bf98496e0f2dd6ae277/0x0C-python-almost_a_circle/models/rectangle.py#L89)
    - [Height](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/5002134d000a267c20418bf98496e0f2dd6ae277/0x0C-python-almost_a_circle/models/rectangle.py#L59)
    - [x](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/5002134d000a267c20418bf98496e0f2dd6ae277/0x0C-python-almost_a_circle/models/rectangle.py#L69)
    - [y](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/5002134d000a267c20418bf98496e0f2dd6ae277/0x0C-python-almost_a_circle/models/rectangle.py#L79)
  - Methods
    - [Area](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/5002134d000a267c20418bf98496e0f2dd6ae277/0x0C-python-almost_a_circle/models/rectangle.py#L89)
    - [Display](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/5002134d000a267c20418bf98496e0f2dd6ae277/0x0C-python-almost_a_circle/models/rectangle.py#L93)
    - [__str__](https://github.com/Daniel13713/holbertonschool-higher_level_programming/blob/5002134d000a267c20418bf98496e0f2dd6ae277/0x0C-python-almost_a_circle/models/rectangle.py#L102)

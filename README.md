# Python-Week-1


# Intro:
Started the week with a brief explanation of how computers store, retriev and diseminate data as far as storage or computer memory is concerned.
Jumped into an introduction to python, whcih involved downloading python, pip and jupyter notebook using the command prompt.
I used the "import" command which is used to fetch a module you want to utilize, in this instance i fetched the "this" module.
I wrote my first python program, "Hello World" using the visual studio code text editor and ran it in the command prompt by typing the file's directory.
Jupyter Notebook is new to me; which is a web application that lets you write and execute Python programs in your browser rather than through the command line. It's a tool created by Project Jupyter which is a non-profit organization that develops Python tools for programming and data science.

# Variables & Types:
A variable is the basic unit of a program and should be assigned a value by using an "=" sign(asignment operator).
Variable names can't be used if they start with a number. Lower & upper cases are acceptible as well as underscores. 
In python variables traditionally start with lowercase letters.
Types of variables include - Integers(whole numbers)
                           - Floats(decimal numbers)
                           - Complex numbers(used for complex mathematical calculations)
                           - strings(collection of characters and can be concatenated by the "+" sign and repeated by using the "*" operatror)
                           - Booleans(True or False)

# Data structures:
They allow the storage of a list of items or values within a single variable.The length of a list can be determined by using the length function(Len()).
The order of items within a set is not important, unlike in a list.
Types of data structures include - List(can store any data type and a list within a list)
                                 - Set(can only store unique elements and is declared within curly braces)
                                 - Tuple(similar to a list except that it can not be modified once declared and are useful for storing large amounts of data more effeciently)
                                 - Dictionary(a collection of key-value pairs, can only be accessed by a key and are declared within curly braces)

# Operators:
They are instructions that carry out/perform operations/manipultion of the variables and values.
Types include:

               Arithmetic operators(perform mathematical operations)
               Examples - addition "+"
                        - subtraction "-"
                        - multiplication "*"
                        - division "/"
                        - modulus(output is the remainder) "%"
                        - exponent("**")

               Comparison operators(evaluates two variables and produce a boolean result)
               Examples - equality "=="
                        - greater than ">"
                        - less than "<"
                        - greater than or equal to ">="
                        - less than or equal to "<="

               Logical operators(operate on Boolean values)
               Examples - and(returns true only if both operands are true)
                        - or(returns true if at least one operand is true)
                        - not(negates the Boolean value it operates on)

               Membership operators(check whether a value is present in a sequence or not)
               Exampes - in
                       - not in

# Control flow:
Types - The if statement(allows you to execute a block of code only if a certain condition is met)
      - For loop(used to iterate over a list or any iterable object eg for item in my_list: print item)
      - while loop(loops until a condition is false)

# Functions:
Is a block of code that performs a specifc function.
It's defined by the "def" keyword followd by the function name and arguments(value accepted by the function) in parenthesis.
The "return" keyword is used to specify the output.
A recursive function is a function that is called within a function
Example: A recursive function for finding the factorial of 5 that accepts user input:

      
      def getFact(x):

 
        if x < 2:
          return 1
        else:
          return x * getFact(x-1)
    
      x = int(input("enter number: "))
      print(getFact(x))
    
     


# Classes and Objects:
An object(an instance of a class) is a collection of data (variables) and functions. A class is a blueprint for that object(collection of related functions).
Example:
## define a class
class Bike:
    name = ""
    gear = 0

## create object of class
bike1 = Bike()

## access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
When we define a class, we use an uppercase letter for the class name, and we start defining all the functions and attributes inside the class definition. 

# Basic data types
## Ints and Floats
Ints and Floats are two fundamental number types in Python.
Python automatically returns a float to accommodate non-whole numbers. Adding a float to an int or multiplying or using exponents with both also returns a float. 

        Example: 20/4 = 5.0

We can use a method called "casting"to convert one datatype to the other. You can convert a float to an integer or inteher to string, etc.
Python doesn't round when casting floats to ints.
To round a float to the nearest int, we can use the round function. We can also specify how many decimal places to round to, such as rounding 4.67 to 5.

        Example: round(14/3, 2)
        output: 4.67 - *rounds the result to 2 decimal places*

## Alternative number types
If you pass a number as a string, the int class will convert it to an integer.

        Example: "50" becomes the integer 50
If you pass a second argument as a number, it will convert the first argument from that base to base 10.

## Decimals
To use the decimal module, you need to import the decimal class and the getcontext function at the top of your code.

        Example: from decimal import Decomal, getcontext

## Booleans
Python casts integers to booleans - 1 is true and 0 is false. In fact, anything except 0 is true.
with strings, anything other than an empty string is true.
An empty data structure (list or dictionary, etc) is false.

## Strings
### Slicing 
refers to taking a portion of a string and returning it. 

        Example: name = "My name is Lorraine"
                 name[0] = M
                 name[0:7] = My name
                 name[:7] = My name
                 len(name) = 19 *the len() function is used to find the length of the elements within a variable*

### Formatting
There are various ways to create/manipulate strings in python. This include but not limited to concatenation and f-strings.
F-strings allow us to insert variables or expressions inside curly braces in a string, ounding and number formatting. 

        Example: f'My name is Lorraine. My age is {28}'
        outout: My name is Lorraine. My age is 28.

### Multi-line strings
In python you can create multi-line strings by using triple quotes. If we need to include literal triple quotes in the string, we can escape them with a backslash.

        Example: string = """here is a block of strings
                             i can add new lines
                             the text will stop when it sees this \'"""
                        print(string)
We use '\n' to go to a new line.
        Example: print("My name\nis Lorraine.")
        output: My name
                is Lorraine.

### Bytes
Computers store information as ones and zeros(binary numbers). 
The bytes object is commonly used for streaming files or transmitting texts without knowing the encoding.
Each byte has eight bits. 
A byte object can be identfied by a 'b' in front of it.

        Example: bytes(4)
        output: b'\x00\x00\x00\x00'

Bytes objects are immutable, like tuples, but you can use a byte array if you need to modify the data.

              

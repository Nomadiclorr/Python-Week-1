# Python-Week-1

DAY 1

Intro:
Started the week with a brief explanation of how computerstore, retriev and diseminate data as far as storage or computer memory is concerned.
Jumped into an introduction to python, whcih involved downloading python, pip and jupyter notebook using the command prompt.
I used the "import" command which is used to fetch a module you want to utilize, in this instance i fetched the "this" module.
I wrote my first python program, "Hello World" using the visual studio code text editor and ran it in the command prompt by typing the file's directory.
Jupyter Notebook is new to me; which is a web application that lets you write and execute Python programs in your browser rather than through the command line. It's a tool created by Project Jupyter which is a non-profit organization that develops Python tools for programming and data science.

Variables & Types:
A variable is the basic unit of a program and should be assigned a value by using an "=" sign(asignment operator).
Variable names can't be used if they start with a number. Lower & upper cases are acceptible as well as underscores. 
In python variables traditionally start with lowercase letters.
Types of variables include - Integers(whole numbers)
                           - Floats(decimal numbers)
                           - Complex numbers(used for complex mathematical calculations)
                           - strings(collection of characters and can be concatenated by the "+" sign and repeated by using the "*" operatror)
                           - Booleans(True or False)

Data structures:
They allow the storage of a list of items or values within a single variable.The length of a list can be determined by using the length function(Len()).
The order of items within a set is not important, unlike in a list.
Types of data structures include - List(can store any data type and a list within a list)
                                 - Set(can only store unique elements and is declared within curly braces)
                                 - Tuple(similar to a list except that it can not be modified once declared and are useful for storing large amounts of data more effeciently)
                                 - Dictionary(a collection of key-value pairs, can only be accessed by a key and are declared within curly braces)

Operators:
They are instructions that carry out/perform operations/manipultion of the variables and values.
Types include: Arithmetic operators(perform mathematical operations)
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

Control flow:
Types - The if statement(allows you to execute a block of code only if a certain condition is met)
      - For loop(used to iterate over a list or any iterable object eg for item in my_list: print item)
      - while loop(loops until a condition is false)

Functions:
Is a block of code that performs a specifc function.
It's defined by the "def" keyword followd by the function name and arguments(value accepted by the function) in parenthesis.
The "return" keyword is used to specify the output.

Classes and Objects:
An object(an instance of a class) is a collection of data (variables) and functions. A class is a blueprint for that object(collection of related functions).
Example:
# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
      
              

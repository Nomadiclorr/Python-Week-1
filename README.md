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

# Data structrures
## Lists
### List slicing
Uses the same syntax as the strings slicing
Slicing can be used to extract a range of values from a list or string, and you can also add a third value to control the step size.

              Example: myList = [1, 2, 3, 4, 5]
              myList[start:stop:step]
              myList[0:5:2]
              output: 1 3 5
              
### Add item to list
To add an item to the end of a list, we can use the append() method.

              Example: thislist = ["apple", "banana", "cherry"]
              thislist.append("orange")
              print(thislist)
              output: apple banana cherry orange

If we want to insert an item at a specific position in the list, we can use the insert() method. 

              Example: thislist = [1, 3, 4, 5]
              thislist.insert(1, 2)
              print(thislist)
              output: 1 2 3 4 5

### Remove item from list
There are two ways to remove items from a list. 
The first method is called remove(), which removes an item based on its value, not its index. 

              Example: thislist = [1, 2, 3, 4, 5]
              thislist.remove(1)
              print(thislist)
              output: 2 3 4 5

The second method to remove items from a list is pop(). This method removes and returns the item at the end of the list. For example, if we type myList.pop() and then print myList, the last item will be removed from myList.

             Example: myList = [1, 2, 3, 4, 5]
             myList.pop()
             print(myList)
             output: 1, 2, 3, 4

## Sets
A set is defined using curly brackets.

             Example: mySet = {'a', 'b', 'c'}

Sets only contain unique values.
You can convert a list to a set by using the set() function like so: *mySet = list(set(mylist))*
You can also check if an element is in a set using the membership operator (in)
You can add elements to a set by using the add() function and discard() to remove elements.

## Tuples
They're similar to lists but are declared with parentheses instead of square brackets.
They are immutable, meaning you can't modify them.
You can retrieve elements from a tuple using indexing.

## Dictionaries
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values.
The values in dictionary items can be of any data type

              Example: thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }
              print(thisdict)

You can use the dict() constructor to make a dictionary.

              Example: thisdict = dict(name = "John", age = 36, country = "Norway")
              print(thisdict)

### Accessing items
You can access the items of a dictionary by referring to its key name, inside square brackets or by using the get() function.

              Example: thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }
              x = thisdict["model"]
              or 
              x = thisdict.get("model")

The keys() method will return a list of all the keys in the dictionary. *x = thisdict.keys()*
The values() method will return a list of all the values in the dictionary. *x = thisdict.values()*
The items() method will return each item in a dictionary, as tuples in a list. *x = thisdict.items()*
To determine if a specified key is present in a dictionary use the "in" keyword.

              Example: thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }
              if "model" in thisdict:
              print("Yes, 'model' is one of the keys in the thisdict dictionary")

### Modifying items
You can change the value of a specific item by referring to its key name.

              Example: thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }
              thisdict["year"] = 2018

The update() method will update the dictionary with the items from the given argument.

              Example: thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }
              thisdict.update({"year": 2020})

Adding an item to the dictionary is done by using a new index key and assigning a value to it.

              Example:  thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }
              thisdict["color"] = "red"
              print(thisdict)

The pop() method removes the item with the specified key name.

              Example: thisdict = {
              "brand": "Ford",
              "model": "Mustang",
              "year": 1964
              }
              thisdict.pop("model")
              print(thisdict)

The popitem() method removes the last inserted item. *thisdict.popitem()*
The del keyword removes the item with the specified key name and can delete the whole dictionary. *del thisdict["model"]*
The clear() method empties the dictionary. *thisdict.clear()*

## List comprehensions
A list comprehension allows you to create a for loop in one line while also returning a copy of the list you're iterating over. It also enables you to filter or apply functions to every item in a list.

              Example: fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

              newlist = [x for x in fruits if "a" in x]

              print(newlist)

## Dictionaries and comprehensions
You can use dictionary comprehensions to create a new dictionary from an iterable structure.


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

# Control Flow
Flow control is the order in which statements or blocks of code are executed at runtime based on a condition.
### There are three categories of flow control statements: 
        1. Conditional statements - act depending on whether a given condition is true or false (if, if-else, if-elif-else, nested if-else & switch)
        2. Transfer statements - are used to alter the program’s way of execution in a certain manner (break, continue & pass)
        3. Iterative statements / Loops - iterative statements allow us to execute a block of code repeatedly as long as the condition is True (for & while)

### If statement
It takes a condition and evaluates to either True or False.
If the condition is True, then the True block of code will be executed, and if the condition is False, then the block of code is skipped, and The controller moves to the next line.

        Example: number = 6
                 if number > 5:
                     print(number * number)
                 print('This is an if statement')

### If-else
The if-else statement checks the condition and executes the if block of code when the condition is True, and if the condition is False, it will execute the else block of code.

        Example: password = input('Enter password ')

                 if password == "Password@1":
                      print("Correct password")
                 else:
                      print("Incorrect Password")

       output 1: Enter password (user inputs "PASSWORD")
                 Incorrect Password
       output 2: Enter password (user inputs "Password@1")
                 Correct Password

### If-elif-else
The elif statement checks multiple conditions one by one and if the condition fulfills, then executes that code.

        Example: def user_check(choice):
                        if choice == 1:
                            print("Admin")
                        elif choice == 2:
                            print("Editor")
                        elif choice == 3:
                            print("Guest")
                        else:
                            print("Wrong entry")
                    
                    user_check(1)
                    user_check(2)
                    user_check(3)
                    user_check(4)
        output: Admin
                Editor
                Guest
                Wrong entry 

### Nested if-else statement
The nested if-else statement is an if statement inside another if-else statement.

          Example: num1 = int(input('Enter first number '))
                  num2 = int(input('Enter second number '))
                  
                  if num1 >= num2:
                      if num1 == num2:
                          print(num1, 'and', num2, 'are equal')
                      else:
                          print(num1, 'is greater than', num2)
                  else:
                      print(num1, 'is smaller than', num2)

### While statement
The while loop statement repeatedly executes a code block while a particular condition is true.

          Example: count = 1
           *condition: Run loop till count is less than 3*
                   while count < 3:
                      print(count)
                      count = count + 1
                      
You can use the break statement to exit a loop and move on to the next line of code outside of the loop. 
You can use the continue statement to skip over any lines that come after it and jump back to the top of the loop to start the next iteration.

### For loop
The for loop is used to iterate over a sequence such as a list, string, tuple, other iterable objects such as range for a "fixed" number of times.
You can declare a new variable, like "item," to hold the value of each element in your list as you iterate through it.
Pass can be used to write a stub for a for loop, continue can be used to skip the rest of a loop during a specific iteration, and break can be used to stop the loop early if you've found what you're looking for. 

          Example: numbers = [10, 20, 30, 40, 50]
                  # definite iteration
                  # run loop 5 times because list contains 5 items
                  sum = 0
                  for i in numbers:
                      sum = sum + i
                  list_size = len(numbers)
                  average = sum / list_size
                  print(average)

### Break statement
The break statement is used to terminate the loop.

          Example: Example: break the loop if number a number is greater than 15
                   In this program, for loop iterates over each number from a list.
                   Next, the if statement checks if the current is greater than 15. If yes, then break the loop else print the current number.
                   numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
                   for i in numbers:
                        if i > 15:
                            # break the loop
                            break
                        else:
                            print(i)

### Continue statement
The continue statement skips the current iteration of a loop and immediately jumps to the next iteration.

          Example: Count the total number of ‘m’ in a given string.
          name = "mariya mennen"
          count = 0
          for char in name:
              if char != 'm':
                  continue
              else:
                  count = count + 1
          
          print('Total number of m is:', count)


# Week 1
# Anatomy of a function
Functions are composed of a name and parameters, which are denoted by the *def* statement.

          Example: def performOperation (num1, num2, operation):
                        if operation == 'sum':
                            return num1 + num2
                        if operation == 'multiplication':
                            return num1 * num2
                   performOperation(2, 3, 'sum')
          output: 5

## locals()
These are the variable names that are only accessible locally within the function.
Referencing a variable outside its scope will result in an error. 

          Example: def performOperation(num1, num2, operation = 'sum'):
                        print(locals())
                  performOperation(2,3, operation = 'multiply')
          output: {'num1': 2, 'num2': 3, 'operation': 'multiply'}

## globals()


                    
                                                                  
                  
                                

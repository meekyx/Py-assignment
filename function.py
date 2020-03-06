#fixed length arguements/positional
def greet(name,msg):
   """This function greets to
   the person with the provided message"""
   print("Hello",name + ', ' + msg)

greet("Massa morning!")

#Try
greet("Something")
greet()

#what results do you get ?
#Why?


def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Jed")
greet("Karl","with a K as in Karl Max!!!!")

'''

In this function, the parameter name does not
have a default value and is required (mandatory) during a call.

On the other hand, the parameter msg has a default
 value of "Good morning!".
 So, it is optional during a call.
 If a value is provided, it will overwrite the default value.

Any number of arguments in a function can have a default value.
But once we have a default argument, all the arguments to its right
 must also have default values.
'''

#
def greet(msg = "Good morning!", name):
    pass

#SyntaxError: non-default argument follows default argument


'''
Python allows functions to be called using
keyword arguments.
When we call functions in this way,
the order (position) of the arguments can be changed.
Following calls to the above function are all valid and
produce the same result.
'''

#Arbitrary Arguments
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","Steve","John")


Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
   for arg in argv:
       print (arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')



# Python program to illustrate
# *args with first extra argument
def myFun(arg1, *argv):
    print ("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')d

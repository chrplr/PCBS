# Functions


A *function* is a block of code that is given a name. 

    !python
    def one_two():  #  definition of a functoin names 'one_two'
        print(1)
        print(2)
        print('...')

    one_two()  # function call
    one_two()
    one_two()


Run this code in a terminal in python, 

then in http://pythontutor.com/

---

# Remarks 


- calling a function is like substituting the function call by *its body*, that is, the block of lines within the definition.

- Using functions avoids duplicating code which is good as it facilitate the modification and correction of a program. 

- Using functions typically serves to make the code more readable (and maybe shorter). 

- if you do not call the function, it will never be executed.


---

# functions must be defined before called

    !python
    one_two()  # function call
    one_two()
    one_two()

    def one_two():  # function definition
        print(1)
        print(2)
        print('...')


---

# Functions can call other functions

One can define several functions and they can call each other:

    !python
    def func1():
        print(1)
    
    def func2():
        func1()
        print(2)
        func1()
    
    func2()

---

# Arguments

    !python
    def hello(name):
        print('Hello, ' + name)

    hello('Alice')
    hello('Bob')


During the call `hello('Alice')`, the argument `Alice` is stored in the variable `name`.

See http://pythontutor.com/

Note: the variable `name` is created only during the execution of the function `hello()` (it is *local* to hello())

---

# Multiple arguments

    ! python
    def check_divisible(a, b):
        if a % b == 0:
            print(a, ' is a divisible by ', b)

    check_divisible(10, 5)
    check_divisible(11, 5)


Exercise: using the above function, write code that writes all the divisors of 840, 747, 833, 997.

---

# Return values

The functions we have seen so far executed actions. 

A function can also return the result(s) of a computation

    !python
    def func(x):
        y = x * x + x + 1
        return y
    
    print(func(0.0))
    print(func(1.0))
    print(func(2.5))




---

# Boolean Functions

    !python
    def isDivisible(x, y):
        if x % y == 0:
            result = True
        else:
            result = False

        return result

    print(isDivisible(10, 5))


Other examples: `os.path.isdir`, `os.path.isfile`

Question: how could one "simplify" (shorten) the function `isDivisible` ?

---



# Returning "complex" objets

A function can return a t-uple, a list, a dictionary, ...

    !python
    def f(x): 
        y1 = x + 1 
        y2 = x * 3 
        y3 = x ** 2 + 3 
        return (y1, y2, y3)
        
    f(2.0)

---

# Use of position or keyword 

In a function call, parameters are assigned to arguments based either on the position or on their names: 

   !python
   def f(a, b):
       print('a=', a)
       print('b=', b)
   
   f(1 ,2)
   f(2, 1)
   f(b=2, a=1)
 
---

# Default values for arguments

It is possible to provide defaults values for arguments.

    !python
    def message(name, msg='Hello'):
        print(msg + ' ' + name + '!')
        
    message("Anna")
    message("Anna", "Gooodbye")    




# Scope of variables
 
Try the following code in http://pythontutor.com/


    !python
    name = 'chris'
    
    def hello(name):
        print('Hello, ' + name)

    print(name)
    hello('Alice')
    hello('Bob')
    print(name)
    
    
---

# scope of variables

**local variables**

Arguments or variables defined inside the body of a function only exist while the function is executed. They are destroyed ant the associated memory is freed.

**non-local variables***

- variables that have been created in the environment where the variable was called. functions can access them (if they are not shadowed)

Yet, this is *bad practice* and must be avoided except in a few cases. 

Why ? Because one should be able to understand what a function is going to do only based on its call. 


Read section ""Local and Global Scope"" in Automate the Boring stuff (from p. 67)



---


# Call stack

function calls can be nested.

see p. 63 of *Automate the boring stuff*


---

# Exercises:


(1) Define a function which takes 2 arguments: a string `msg` and a number `nrepetitions`, and print `msg`, `nrepetition` times.

(2) Read <https://en.wikipedia.org/wiki/Fahrenheit> and write a function that converts from Fahenheit to Celsius, and another one that converts from Celsius to Fahrentheit

(3) Define a function `isPrime(x)` which return `True` if `x` is a prime number, else `False` 


---

# More exercices


---


# Modules

Functions defined in a file "myfunc.py" in the current folder can be called from another python script.


    !python
    ### file "mymodule.py"
    def  hello(name):
        print("Hello ", name "!")

    ### file "myscript.py"
    import mymodule
    
    mymodule.hello("Chris")


See Chapter 3 of *Automate the boring stuff*, p.57


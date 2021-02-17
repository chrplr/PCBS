# Functions


A *function* is a block of instructions that is given a name.

    !python
    #  definition of a function named 'one_two'
    def one_two():
        print(1)
        print(2)
        print('...')

    # function calls
    one_two()
    one_two()
    one_two()


Calling a function is like substituting the function call by *its body*.

If you do not call the function, it will never be executed.

-> Run this code inside a terminal with `python` (or in <https://repl.it/languages/python3>), then in http://pythontutor.com/

*What, in your opinion, is the interest of functions?* 

---

# Usefulness of functions


1. Using functions avoids to duplicate code (i.e. by cutting and pasting).

   -> This facilitates the modification and correction of a program (errors are at a single place!)

2. Using functions typically serves to make the code more readable (and maybe shorter). 


---

# definitions first!


functions must be defined before they are called

    !python
    one_two()  # function call
    one_two()
    one_two()

    def one_two():  # function definition
        print(1)
        print(2)
        print('...')

-> Run this code in python.

Remarks:

- A given script can contain several function definitions.

- As a convention, all functions definitions must be at the beginning of the script.


---

# Arguments


    !python
    def hello(name):
        print('Hello, ' + name)

    hello('Alice')
    hello('Bob')


During the call `hello('Alice')`, the argument `Alice` is stored in the variable `name`.

-> run it in http://pythontutor.com/

Note: the variable `name` is created only during the execution of the function `hello()` (it is *local* to hello())

---

# Multiple arguments

    !python
    def check_divisible(a, b):
        if a % b == 0:
            print(a, ' is a divisible by ', b)

    check_divisible(10, 5)
    check_divisible(11, 5)


-> **Exercise:** using the above function, find the divisors of ``840, 747, 833, 997`.

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

    xs = range(-10, 10)
    values = [func(x) for x in xs] 
    print(values)
    
    import matplotlib.pyplot as plt
    plt.plot(xs, values)
    plt.show()


---

# Boolean Functions

Boolean functions return `True` or `False`

    !python
    def isDivisible(x, y):
        if x % y == 0:
            result = True
        else:
            result = False

        return result

    print(isDivisible(10, 5))


Other examples: `os.path.isdir`, `os.path.isfile`

-> Question: how could one "simplify" (shorten) the function `isDivisible` ?

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

---


# Scope of variables
 
-> Try the following code in http://pythontutor.com/


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

# functions can call other functions

Note that functions can call each other.

    !python
    def func1():
        print(1)
    
    def func2():
        func1()
        print(2)
        func1()
    
    func2()

-> Predict the output of this script.

---

# Recursive functions

Recursive functions are function that contains calls to themselves:

For example:

    !python
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)

---


# Modules

Functions defined in a file `myfunc.py` in the current folder can be called from another python script.


    !python
    ### file "mymodule.py"
    def  hello(name):
        print("Hello ", name "!")

    ### file "myscript.py"
    import mymodule
    
    mymodule.hello("Chris")


- modules (aka libraries) allow to reuse functions.

- Python comes with many modules, e.g. `random`, `math`, `os`.

- Anaconda adds scientific libraries`numpy`, `scipy`

To know more about modules, read *Automate the boring stuff*, chap.3, p.57


#     if __name__ == '__main__':

Many scripts will contain a series of functions and then the line

    !python
    if __name__ == '__main__':
         
    
The condition is true only if the script is executed as a python script. 

The functions in it can be reused with `import script`


# Exercises:


(1) Define a function with two arguments --- a string `msg` and a number `nrepetitions` --- that prints `msg`, `nrepetition` times.

(2) Read <https://en.wikipedia.org/wiki/Fahrenheit> and write a function that converts from Fahenheit to Celsius, and another one that converts from Celsius to Fahrentheit

(3) Define a function `isPrime(x)` which return `True` if `x` is a prime number, else `False` 

(4) Two taxi companies propose differents pricing schemes:

        Company A charges 4.80€ plus 1.15€ by km travelled.
        Company B charges 3.20€ plus 1.20€ by km travelled.

Write a first function which, given a distance, returns the costs of both companies, and a second function that returns 'company A' and 'company B', the cheapest company for a given distance.

(5) Write a function `areAnagram(word1, word2)` that tests if two words are anagrams, that is contain the same letters in different orders.



---

# More exercices

- https://pcbs.readthedocs.io/en/latest/representing-numbers-images-text.html
- https://pcbs.readthedocs.io/en/latest/building_abstractions_with_functions.html


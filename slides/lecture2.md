# Menu of the day

1. Short **Quizz** about Python on Schoology 

2. Depending on the outcome:

    - **Lecture** on Python fundamentals: objects, control flow (tests, loops), functions
 
    OR

    - **Self-training*** on Regular expressions (+ extra on register machines)

3. At noon, **debriefing** on zoom (Q & A session)

Remark: You can always use http://cogmaster-pcbs.slack.com/ to ask questions. 


---

# Self-training *Regular Expressions*

It is common to have to search for strings of characters that conform to certain patterns. For example:

- All French verbs that end in '-er'.
- all possible consonant clusters (strings of consonants) in a given language (French, Japanese, English) to study the phonotactics of the language.

Regular expressions are the tools of choice for this type of task.

The activity is at <https://pcbs.readthedocs.io/en/latest/regular_expressions.html>

---

# Extra bonus on Register Machines 


A register machine is a universal computational model (as a Turing machine). 

- Check out [The seven secrets of computer power revealed](../documents/Dan_Dennett-The_seven_secrets_of_computers_revealed.pdf)

- try the simulator at <http://proto.atech.tufts.edu/RodRego/>

- (if you dare) Implement a Rodrego interpreter in Python: a script that will take as input a Rodrego source code, 10 integer values representing the initial state of registers, and will execute the program step by step.

- Compare with a solution at <https://raw.githubusercontent.com/chrplr/PCBS/master/solutions-to-exercices/rodrego.py>

---

# Python fundamentals

---

# Editing and running Python code

Using a text editor (e.g., SublimeText) and a Terminal (e.g., Git Bash) side by side. (Check out <https://www.youtube.com/watch?v=2yhcWvBt7ZE>)

If you still have issues,  you can use an on-line python interpreter <https://repl.it/languages/python3>

---

# A question:

what happens when one types:

      python mycode.py

on a line in a Terminal?

---

Answer:


A program, called "python", is started that reads ``mycode.py``'s lines ("instructions") and executes them one by one, from top to bottom (pipeline).


    # compute the area of a circle
    pi = 3.1415
    radius = .4
    area = pi * (radius ** 2) 
    print("radius=", radius, " area=", area)
    
    print("The solution is", 42)  # reference to The Hitchiker's Guide to the Galaxy
     
    # give greetings
    print("hello")
    var = input("your name?")
    print("Hello " + var + "!")


Instructions typically:

- perform computations and may save them in the memory (variables)
- perform input/ouput operations

---


# Python basic objects


    # integer
    -6
    2**64
    
    # float
    3.1415
    float('inf')
    
    # Boolean
    True
    False
    1 == 2
    
    # strings
    
    'hello'
    "hello"

    """hello.
    Did you
    sleep well?
    """

    None  # a special object


---

# Complex objects



     # tuples

     red = (255, 0 , 0)
     print(red[0])

     # lists

     simple = [5, 7, 8, 0]
     complex = ['abc', 5, (4, 5), ['hello', 6]]
     print(complex[3][1])

     # dictionaries
     d= {'alpha':1, 'beta':2}
     print(d['alpha'])


---
# Control flow: loops

To repeat the same line several times

    for _ in range(5):
        print("boring!")



    for _ in range(20):
        print("boring!")


Note the **indentation** !!!


    for _ in range(10):
        print('a', end='')
        print('b', end='')
    
    print('c')


Notice the notion of **block of instructions**

# Doing something with the loop index


    for i in range(10):
        print(2 * i)



    for name in ['Jim', 'John', 'Donald']:
        print('Hello ' + name)

Nested loops


    for i in range(1, 6):
        for j in range(1, 6):
            print(i, "*", j, "=", i * j)



---


# Exercises

- Write codes that print 20 times the string ``All work no play makes Jack a dull boy``

- Write code that prints the squares of numbers between 1 and 100.


---

# 'While' loops



    while condition:
       code



'condition' is an expression that evaluate to ``True`` or ``False`` (a Boolean)

As long as it evaluates to ``True``, code is executed 



    x = 1
    while x * x < 132:
        x = x + 1

    print(x, x ** 2 )
    print(x + 1, (x + 1) ** 2)


---

# Exercises:

- Given a list of numbers, print their sum

- Given a list of numbers, print their product

- Given a list of numbers, print the sum of their squares

- Given a list of numbers, print the largest one.

---

# conditional (branching)


    if condition:
        code1
    else:
        code2



    a = 4
    if a % 2 == 0:   # '%' is the 'modulo' operator
        print(a, " is even")
    else:
        print(a, " is odd")


---

# Breaking a loop


    N = 72239
    for i in range(2, 300):
        if N % i == 0:
            print(i)
            # break  # uncomment and see the result



    passwd = 'sesame'

    while True:
        code = input('Password? ')
        if code == passwd:
            break
        else:
            print('invalide password')

    print("You are in!")


---

# Exercise

Write code that prints all the numbers between 1 and 1000 that are multiples of 7

---

# Case study: "Guess the number"

Visualize the following code at <http://pythontutor.com/visualize.html#mode=display>


    import random

    guessesTaken = 0
 
    print('Hello! What is your name?')
    myName = input()

    number = random.randint(1, 20)
    print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

    for guessesTaken in range(6):
        print('Take a guess.') # Four spaces in front of "print"
        guess = input()
        guess = int(guess)

        if guess < number:
            print('Your guess is too low.') # Eight spaces in front of "print"

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

    if guess == number:
        guessesTaken = str(guessesTaken + 1)
        print('Good job, ' + myName + '! You guessed my number in ' +
          guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')



(taken from https://inventwithpython.com/invent4thed/chapter3.html)


---

Recommended reading (for later)

Check out Chapter 2 of *Automate the boring stuff* "Flow control" from page 21 to 47


---

# Functions


A function is a block of code that is given a name. 



    def hello():  # function definition
        print('Howdy!')
        print('Howdy!!!')
        print('Hello there.')

    hello()  # function call
    hello()
    hello()




Let's run the previous code in http://pythontutor.com/


---

# Parameters

    def hello(name):
        print('Hello, ' + name)

    hello('Alice')
    hello('Bob')


Note: the variable ``name`` is only defined within the *scope* of the function ``hello``


---


# multiple parameters


    def is_divisor(a, b):
        if b % a == 0:
            print(a, ' is a factor of', b)


    is_divisor(5, 11)
    is_divisor(5, 10)


---

# Return values



    def func(x):
        y = x * x + x + 1
        return y
    
    func(1.0)
    func(2.5)




    def func(x):
        return x * x + x + 1


---

Exercise

Write a function the converts from Fahenheit to Celsius, and another one that converts from Celsius to Fahrentheit

See <https://en.wikipedia.org/wiki/Fahrenheit>

---

# Call stack

function calls can be nested.

see p. 63 of *Automate the boring stuff*


---


# Modules

Functions defined in a file "myfunc.py" in the current folder can be called from another python script.


myfunc.py:

   def hello(name):
       print("Hello ", nam, "!")


myscript.py:

    import myfunc
    
    myfunc.hello("Chris")





See Chapter 3 of *Automate the boring stuff*, p.57








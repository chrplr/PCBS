****************************************
Introduction to Programming, with Python
****************************************

The only prequisite is to have installed Sublime, Anaconda Python and Git bash following the instructions at `<https://pcbs.readthedocs.io/en/latest/software-installation.html>`_


Course 1
########

Skills to acquire
-----------------

* be able to download and execute from the command line simple Python scripts found on the web (require ability to navigate folders from the command line)
* be able to open an editor (e.g. Sublime), type in a series of Python statements, and execute it from the command line.

(see `<https://pcbs.readthedocs.io/en/latest/running-python.html>`_)

Programming concepts
--------------------

* Python objects: numbers, strings, lists, and basic operations on them)
* Constants vs. Variables
* a program normally executes *sequentially* from top to bottom
* but some instructions can change the flow: ``if`` and ``for`` loops (notion of the  interpretation pointer keeping track of the current line of execution) 

Examples of exercices
----------------------
* download a script from the internet and execute it
* Type the line "print('Hello')" in a ``hello.py`` file and execute it
* Write code that asks the user for his/her name and prints "Hello <user_name>!".
* Write code that prints the string ``"All work no play makes Jack a dull boy"`` 50 times
* Write code that prints the squares of all integers between 1 and 100.
* Write code that asks the user to enter a number and prints the square of it. IF the input is '0', then stop.
* Write code that computes the factorial of an integer (no function, no recursion, just a loop)


Course 2
########

Skills
------

* Use `<http://pythontutor.com/>`_ to visualize the step by step execution of a program
(show an example. EXplain that sutdents must try to simulate programs in their head or on paper)

Programming
-----------

* random numbers 
* More Python objects: dictionaries, sets
* List extensions  ([2 * x for x in range(10) if x != 3])

Exercices
---------

* Lists:
  -  Given a list of numbers, print their sum
  -  Given a list of numbers, print their product
  -  Given a list of numbers, print the sum of their squares
  -  Given a list of numbers, print the largest one.
  -  Given a list of numbers, print the second largest
* Write a program that prints the first N rows of Pascal’s triangle (see `<https://www.youtube.com/watch?v=XMriWTvPXHI>`_). 
* Given a list of words, count the number of times each word appears in the list.
* Monte Carlo estimation of Pi: one way to estimate the value of the π is to generate a large number of random points in the unit square and see how many fall within the unit circle; their proportion is an estimate of the area of the circle. See `<https://academo.org/demos/estimating-pi-monte-carlo>`_. Implement the proposed algorithm to estimate the value of π.


Course 3
########

Programming
-----------

* Functions, functions, functions. (see `<https://rawgit.com/chrplr/PCBS/master/slides/lecture3.html>`_)
* pure functions (returning a value) vs. procedures (having side effects) 

Exercices
---------

* Define a function with two arguments --- a string msg and a number nrepetitions --- that prints msg, nrepetition times.
* Read `<https://en.wikipedia.org/wiki/Fahrenheit>`_ and write a function that converts from Fahrenheit to Celsius, and another one that converts from Celsius to Fahrenheit
* Two taxi companies propose differents pricing schemes: Company A charges 4.80€ plus 1.15€ by km travelled. Company B charges 3.20€ plus 1.20€ by km travelled. Write a first function which, given a distance, returns the costs of both companies, and a second function that returns 'company A' and 'company B', the cheapest company for a given distance.

 

Course 4
########

Programming
-----------

* function's keywords arguments
* scope of variables: local vs. global. Use pythontutor.com

Exercices
---------

* Define a function ``is_prime(x)`` which returns ``True`` if ``x`` is a prime number, else ``False``. Use it to list all prime numbers below 1000.
* recursion `<https://pcbs.readthedocs.io/en/latest/building_abstractions_with_functions.html>`_
* 

Course 5
########

Skills
------

* be able to launch ipython and test python code interactively.


Programming
-----------

* Querying and navigating the file system `<https://automatetheboringstuff.com/2e/chapter10/>`_
* Reading and writing text files.
* Manipulating strings (split, join, ...).


Exercices
---------

* Write a script that prints the first 10 lines of a file
* Write a script that prints the last 10 lines of a file (or the whole file is it is less than 10 lines long).
* Write a script that opens and read a text file, and print all the lines that contain a given target word
* compute the number of the number of words (removing punctuation) in a text file
* compute the number of occurences of each word in a text file
* read a matrix in a text file and return the mean of each row (not using pandas, ...)
* find and list all ``*.csv`` files in a folder and its subfolders. 
* rename all files in a folder by adding the last modification date and the end of the name (before the extension)  


Course 6
########

Skills
------

*  installing an additional python module with ``conda install`` or  ``pip install`` and testing it. E.g. nilearn, pygame...

Programming
-----------

* How to write clean Code. See `<https://rawgit.com/chrplr/PCBS/master/slides/lecture5.html>`_



Resources
#########


* `<https://automatetheboringstuff.com/>`_



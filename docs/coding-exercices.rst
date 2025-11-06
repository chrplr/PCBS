****************
Coding Exercises
****************

.. contents::


(Note: Solutions to most exercises are available in https://github.com/chrplr/PCBS/tree/master/coding-exercises )


Flow control
------------

You can read about  `loops in Python <https://wiki.python.org/moin/ForLoop>`__, and more generally about `flow control <https://automatetheboringstuff.com/chapter2/>`__. 


Shining
~~~~~~~

Write a python script that prints 1000 times the line ``All work and no play makes Jack a dull boy.``

Check a solution at :download:`shining.py  <../coding-exercises/shining.py>`

Multiplication tables
~~~~~~~~~~~~~~~~~~~~~

Write a script that displays the tables of multiplication from 1 to 10 as a table::

    1   2   3   4   5   6   7   8   9  10 
    2   4   6   8  10  12  14  16  18  20 
    3   6   9  12  15  18  21  24  27  30 
    4   8  12  16  20  24  28  32  36  40 
    5  10  15  20  25  30  35  40  45  50 
    6  12  18  24  30  36  42  48  54  60 
    7  14  21  28  35  42  49  56  63  70 
    8  16  24  32  40  48  56  64  72  80 
    9  18  27  36  45  54  63  72  81  90 
   10  20  30  40  50  60  70  80  90 100 


Check out  :download:`multiplication_table.py  <../coding-exercises/multiplication-table.py>` for a solution.


Taxis
~~~~~

Two taxi companies propose differents pricing schemes:

 - Company A charges 4.80€ plus 1.00€/km
 - Company B charges 3.20€ plus 1.20€/km

Write code to find which company is the cheapest as a function of the distance to travel.

Check out :download:`taxis.py  <../coding-exercises/taxis.py>`


Estimation of PI by a Monte-Carlo method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One way to estimate the value of the π is to generate a large number of *random points* in the unit square and see how many fall within the unit circle; their proportion is an estimate of the area of the circle. See https://academo.org/demos/estimating-pi-monte-carlo/

Implement the proposed algorithm to estimate the value of π.

Check out  :download:`pi_monte_carlo.py  <_static/pi_monte_carlo.py>`


Computer-guess-a-number
~~~~~~~~~~~~~~~~~~~~~~~

Read `chapter 3 of Invent your own games with
Python <https://inventwithpython.com/invent4thed/chapter3.html>`__ where
the author presents a game where the computer chooses a random number
that the user must guess. Study the code.

Now, your task is to write another program, where the roles are
inverted: the computer tries to guess a number that the user has in
mind. The computer proposes a number and the user answers with ‘+’ (the
number he has is mind is larger), ‘-’ (if it is smaller), ‘y’ (if the
guess is correct)

Check a solution at :download:`computer-guess-a-number.py <../coding-exercises/computer-guess-a-number.py>`


Lists
-----

These exercises require list manipulations. If you do not know Lists in Python, you can read:

   -  `Python Lists <https://www.w3schools.com/python/python_lists.asp>`__
   -  `List comprehensions <https://www.pythonforbeginners.com/basics/list-comprehensions-in-python>`__
   -   https://automatetheboringstuff.com/2e/chapter4/


Try to solve the following exercices:

- Given a list of numbers, print their sum

- Given a list of numbers, print their product

- Given a list of numbers, print the sum of their squares

- Given a list of numbers, print the largest one.

- Given a list of numbers, print the second largest one.


After you have tried to solve these problems, you can check  :download:`lists.py <../coding-exercises/lists.py>`


Prime numbers
~~~~~~~~~~~~~

Write a script that lists all prime numbers between 1 and 10000 (A prime
number is a integer that has no divisors except 1 and itself). You can
use the following function:

.. code:: python

    def is_factor(d, n):
        """ True if `d` is a divisor of `n` """
        return n % d == 0

Check a solution at :download:`prime-numbers.py <../coding-exercises/prime-numbers.py>`



Pascal triangle
~~~~~~~~~~~~~~~

Write a program that prints the first N rows of Pascal’s triangle (see
https://www.youtube.com/watch?v=XMriWTvPXHI). For example::

   1 
   1   1 
   1   2   1 
   1   3   3   1 
   1   4   6   4   1 
   1   5  10  10   5   1 
   1   6  15  20  15   6   1 
   1   7  21  35  35  21   7   1 
   1   8  28  56  70  56  28   8   1 
   1   9  36  84 126 126  84  36   9   1 


To solve this problem, one solution is to store the values
of the current line in a Python list, and write a function that
given a list as an argument, calculates and returns the following line
in a new list.

Proposed solutions:

  - :download:`Pascal-triangle_v1.py <../coding-exercises/Pascal-triangle_v1.py>` 
  - :download:`Pascal-triangle_v2.py <../coding-exercises/Pascal-triangle_v2.py>` 


Functions
---------

Read about *functions* in Python:
- https://www.w3schools.com/python/python_functions.asp
- https://automatetheboringstuff.com/2e/chapter3/).


Convert temperatures from Fahrenheit to Celcius and vice-versa.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Read https://en.wikipedia.org/wiki/Fahrenheit and write a function that converts a temperature from Fahrenheit to Celsius, and another one that converts from Celsius to Fahrenheit

- Add code that reads temperatures from the standard input and print the
  converted numbers.

A solution is available here: :download:`Fahrenheit_celsius.py <../coding-exercises/Fahrenheit_celsius.py>`.


Permutations
~~~~~~~~~~~~

Generate all the permutations of a set, e.g. (1..n).

Note: This is an advanced exercise, which requires mastery of recursive functions (functions that call themselves)

A solution is proposed at :download:`generate_all_permutations.py <../coding-exercises/generate_all_permutations.py>`.

To run it::

   python generate_all_permutations.py 4


Eight queens puzzle
~~~~~~~~~~~~~~~~~~~

The eight queens puzzle is the problem of placing eight chess queens on an 8×8
chessboard so that no two queens threaten each other; thus, a solution requires
that no two queens share the same row, column, or diagonal. See
https://en.wikipedia.org/wiki/Eight_queens_puzzle

As there can be only one queen per column and per row, a winning solution can
be represented by a set of 8 numbers, one per line, which represent the column
in which there is a queen. Because the columns must be different, the solutions
are a subset of the permutations of 8 numbers. We just have to check that no
two queens are in the same diagonal.

In Python, you can get all the permutations of a set, with the ``permutations`` function from the ``itertools`` module ::

    from itertools import permutations
    list(permutations(range(3))

For a solution to the eight queens problem, check out https://code.activestate.com/recipes/576647-eight-queens-six-lines/

The code is available at :download:`eight_queens.py <../coding-exercises/eight-queens.py>`.


Strings
-------

Pseudowords
~~~~~~~~~~~

- Search the internet to find out how to generate a random integer number in a interval in Python

- Read about strings in Python at https://realpython.com/python-strings/

- Write functions that generate pseudowords from words. The first function will delete a character in a random position from a string passed as argument. The second will insert a random character at a random position. The third will swap two characters at random location.

- If you know about file input/output (see https://automatetheboringstuff.com/2e/chapter9/), you can read a dictionary (e.g. http://www.pallier.org/extra/liste.de.mots.francais.frgut.txt) and use it to filter out any actual words.



Dictionaries
------------


unique
~~~~~~

Given a list of words, print how many different words are in that list (hint: use a dictionary or a set)

.. code-block:: python

   liste = ['bonjour', 'chat', 'chien', 'bonjour']

   n = 0
   d = dict()
   for e in liste:
      if not e in d.keys():
         d[e] = 1
         n = n + 1
   print(n)

   print(len(set(liste)))  # shortest solution using a set



word count
~~~~~~~~~~

Given a list of words, count the number of times each word appears in
the list. Eg. ``[Jim, Alan, Jim, Joe]`` -> ``Jim:2, Alan:1, Joe:1``
(hint: use a dictionary)

.. code-block:: python

   liste = ['Jim', 'Alan', 'Jim', 'Joe']
   counts = dict()
   for word in liste:
       if word in counts.keys():
            counts[word] += 1
       else:
            counts[word] = 1
   print(counts)



Anagrams
~~~~~~~~

Two words are anagrams if they contain the same letters in different orders, e.g., *binary* and *brainy*.

- write a function that take two strings as arguments and returns True if they are anagrams.

- Given a list of words, print all subsets that form anagrams.

Check my solution at :download:`anagrams.py <../coding-exercises/anagrams.py>`. Running::

   python anagrams.py < liste.de.mots.francais.frgut.txt 

will list *all* anagrams in French! (:download:`liste.de.mots.francais.frgut.txt <../coding-exercises/liste.de.mots.francais.frgut.txt>` contains a list of French words)





File reading and writing
------------------------

Read the chapter about files reading and writing at https://automatetheboringstuff.com/2e/chapter9/


head
~~~~

Write a script that prints the first 10 lines of a file (or the whole file is it is less than 10 lines long).

.. code-block:: python

    with open('aga.txt', 'r', encoding='utf-8') as f:
       for l in f.readlines()[:10]:
           print(l, end='')


tail
~~~~

Write a script that prints the last 10 lines of a file (or the whole
file is it is less than 10 lines long).

.. code-block:: python

   with open('aga.txt', 'r', encoding='utf-8') as f:
       all_lines = f.readlines()
       for l in all_lines[-10:]:
           print(l, end='')


string-detector
~~~~~~~~~~~~~~~

Read  `Chap. 8 of Automate the boring stuff <http://automatetheboringstuff.com/chapter8/>`__.

Write a script that opens and read a text file, and print all the lines that contain a given target word,  say, ``cogmaster``.

Check out :download:`search-file.py <../coding-exercises/search-file.py>`


Kaprekar numbers
~~~~~~~~~~~~~~~~

A Kaprekar number is a number whose decimal representation of the
square can be cut into a left and a right part (no
nil) such that the sum of these two parts gives the number
initial. For example:

- 703 is a number of Kaprekar in base 10 because 703² = 494 209 and that
   494 + 209 = 703.
- 4879 is a number of Kaprekar in base 10 because 4879² = 23 804 641 and
   04641 + 238 = 4879

Write a program that returns all Kaprekar numbers between 1 and N.

Solution: :download:`Kaprekar-numbers.py <../coding-exercises/Kaprekar-numbers.py>`


RPN Calculator
~~~~~~~~~~~~~~

Write a reverse Polish arithmetic expression evaluator (See
https://en.wikipedia.org/wiki/Reverse_Polish_notation).

E.g. ``3 4 * 5 -`` evaluate to ``7``.

Solution: :download:`rpn-calculator.py <../coding-exercises/rpn-calculator.py>`


Rodrego-simulator
~~~~~~~~~~~~~~~~~


Write a Python script that simulates a `RodRego machine <http://sites.tufts.edu/rodrego/>`__ with 10 registers.
The program is stored in a string or in
file that is read and then executed. Your program must contain
a function which, given the 10 initial values of the registers, and
the program, returns the new register values when
the END command is reached.

Check two possible solutions:
- :download:`rodrego_maxime_caute.py <../coding-exercises/rodrego/rodrego_maxime_caute.py>`
- :download:`rodrego_christophe_pallier.py <../coding-exercises/rodrego/rodrego_christophe_pallier.py>`


Cellular automata
~~~~~~~~~~~~~~~~~

Implement a 1-dimension `elementay cellular automata <https://en.wikipedia.org/wiki/Elementary_cellular_automaton>`__. (Further reading: https://en.wikipedia.org/wiki/A_New_Kind_of_Science)

Solution: :download:`1d-ca.py <../simulations/cellular-automata/1d-ca.py>`


Analysis of a Signal Detection Experiment 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a signal detection experiment, a faint stimulus (e.g. a faint sound or a faint visual target) is presented or not at each trial and the participant must indicate whether he has perceived it or not. There are four possible outcomes for each trial:

  - A *hit* occurs when the participant correctly detects the target.
  - A *miss* occurs when the target was there but the participant did not detect it.
  - A *false alarm* occurs when the participant reports the presence of the target when it was not actually there.
  -  A *correct rejection* occurs when the participant correctly reports that the target was not present.

One defines;

  -  The *hit rate*, equal to #hits / (#hits + #misses)
  -  The *false alarm rate*, equal to #false alarms / (#false alarms + # correct rejections)

Let us first suppose that the data from a participant is represented as a string. This string represents a series of trials, each trial being represented by two characters indicating the trial type (1=target present, 0=target absent) and the participant's response (Y=target perceived, N=No target perceived). For example:

.. code-block:: python

  data = "0Y,0N,1Y,1Y,0N,0N,0Y,1Y,1Y"

Exercise:

 - Write a function which, given such a string, returns the Hit rate and the False rate.
 - Now, the results from different participants are stored in different files ``subj*.dat`` (download the files from https://github.com/chrplr/PCBS/tree/master/coding-exercises/subjdat.zip`) Write a script that computes the hit rates and false alarms for each subject, and displays the group averages and standard deviations. 

Solution :download:`sdt.py <../coding-exercises/sdt.py>`




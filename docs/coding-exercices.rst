=======================
 Programming Exercices
=======================

(Note: Solutions are available in https://github.com/chrplr/PCBS/tree/master/solutions-to-exercices)


Flow control
------------

You can read about  `loops in Python <https://wiki.python.org/moin/ForLoop>`__, and more generally about `flow control <https://automatetheboringstuff.com/chapter2/>`__. 


Shining
~~~~~~~

Write code that prints 1000 times the line ``All work and no play makes Jack a dull boy.``
(a solution is at :download:`shining.py  <../solutions-to-exercices/shining.py>`


prime numbers
~~~~~~~~~~~~~

Write a script that lists all prime numbers between 1 and 10000 (A prime
number is a integer that has no divisors except 1 and itself). You may
use the following function:

.. code:: python

   def is_divisor(a, b):
       """ Args: a, b integers;
            Return True if b is a divisor of a, else False"
       return a % b == 0

Check a solution at :download:`prime-numbers.py <../solutions-to-exercices/prime-numbers.py>`


Multiplication tables
~~~~~~~~~~~~~~~~~~~~~

Write a script that displays the tables of multiplication from 1 to 10, e.g.:
, either individually, or in a table like that::

       1:  2:  3:  4:  5:  6:  7:  8:  9: 10:
  1:   1   2   3   4   5   6   7   8   9  10 
  2:   2   4   6   8  10  12  14  16  18  20 
  3:   3   6   9  12  15  18  21  24  27  30 
  4:   4   8  12  16  20  24  28  32  36  40 
  5:   5  10  15  20  25  30  35  40  45  50 
  6:   6  12  18  24  30  36  42  48  54  60 
  7:   7  14  21  28  35  42  49  56  63  70 
  8:   8  16  24  32  40  48  56  64  72  80 
  9:   9  18  27  36  45  54  63  72  81  90 
 10:  10  20  30  40  50  60  70  80  90 100 


- Note: it can be useful read https://pyformat.info/#number_padding to pretty-print the numbers.

Check out  :download:`multiplication_table.py  <../solutions-to-exercices/multiplication-table.py>`


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

Check a solution at :download:`computer-guess-a-number.py <../solutions-to-exercices/computer-guess-a-number.py>`


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


After you have tried to solve these problems, you can check  :download:`lists.py <../solutions-to-exercices/lists.py>`


Pascal triangle
~~~~~~~~~~~~~~~

Write a program that prints the first N rows of Pascal’s triangle (see
https://www.youtube.com/watch?v=XMriWTvPXHI). For example::

   ```
   %run triangle-de-Pascal.py
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
   ```

To solve this problem, one solution is to store the values
of the current line in a Python list, and write a function that
given a list as an argument, calculates and returns the following line
in a new list.

Proposed solutions: :download:`Pascal-triangle_v1.py <../solutions-to-exercices/Pascal-triangle_v2.py>` and
:download:`Pascal-triangle_v2.py <../solutions-to-exercices/Pascal-triangle_v2.py>`




Functions
---------

Read about Python's functions: https://automatetheboringstuff.com/2e/chapter3/).

Convert temperatures from Fahrenheit to Celcius and vice-versa.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Read https://en.wikipedia.org/wiki/Fahrenheit and write a function that converts a temperature from Fahrenheit to Celsius, and another one that converts from Celsius to Fahrenheit

- Add code that reads temperatures from the standard input and print the converted numbers. 

A solution is available here: :download:`Fahrenheit_celsius.py <../solutions-to-exercices/Fahrenheit_celsius.py>`.


Taxis
~~~~~

Two taxi companies propose differents pricing schemes:

 * Company A charges 4.80€ plus 1.15€ by km travelled.

 * Company B charges 3.20€ plus 1.20€ by km travelled.

Write some code to find which company is the cheapest as a function of the distance to travel. Compare it to :download:`taxis.py  <../solutions-to-exercices/taxis.py>`


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

- Given a list of words, print all subsets that form anagrams. You use the file :download:`liste.de.mots.francais.frgut.txt <../solutions-to-exercices/liste.de.mots.francais.frgut.txt>`__ 

Check my solution at :download:`anagrams.py <../solutions-to-exercices/anagrams.py>`


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

Solution: :download:`Kaprekar-numbers.py <../solutions-to-exercices/Kaprekar-numbers.py>`


RPN Calculator
~~~~~~~~~~~~~~

Write a reverse Polish arithmetic expression evaluator (See
https://en.wikipedia.org/wiki/Reverse_Polish_notation).

E.g. ``3 4 * 5 -`` evaluate to ``7``.

Solution: :download:`rpn-calculator.py <../solutions-to-exercices/rpn-calculator.py>`


Rodrego-simulator
~~~~~~~~~~~~~~~~~

Write a program that simulates a RodRego machine with 10 registers
(http://sites.tufts.edu/rodrego/). The program is stored in a string or in 
file that is read and then executed. Your program must contain
a function which, given the 10 initial values of the registers, and
the program, returns the new register values when
the END command is reached.

Solution: :download:`rodrego.py <../solutions-to-exercices/rodrego.py>`


Cellular automata
~~~~~~~~~~~~~~~~~

Implement a 1-dimension `elementay cellular automata <https://en.wikipedia.org/wiki/Elementary_cellular_automaton>`__. (Further reading: https://en.wikipedia.org/wiki/A_New_Kind_of_Science)

Solution: :download:`1d-ca.py <../cellular-automata/1d-ca.py>`


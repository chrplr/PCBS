=====================
Programming Exercices
=====================


Basics
------

Read about  `loops in Python <https://wiki.python.org/moin/ForLoop>`__.

- Write code that prints 1000 times the line ``All work and no play makes Jack a dull boy.``


If you do not know Lists in Python, read:

   -  `Python Lists <https://www.w3schools.com/python/python_lists.asp>`__
   -  `List comprehensions <https://www.pythonforbeginners.com/basics/list-comprehensions-in-python>`__
   -   https://automatetheboringstuff.com/2e/chapter4/


Then, try to solve the following exercices:

- Given a list of numbers, print their product

- Given a list of numbers, print the sum of their square

- Given a list of numbers, print the largest one.

- Given a list of numbers, print the second largest one.


After you have tried to solve these problems, you can check  :download:`my proposed answers <../solutions-to-exercices/basic-examples.py>`.


Convert temperature from Fahrenheit to Celcius
----------------------------------------------

- Read https://en.wikipedia.org/wiki/Fahrenheit and write a function that converts a temperature from Fahrenheit to Celsius, and another one that converts from Celsius to Fahrenheit (if necessary, read about Python's functions: https://automatetheboringstuff.com/2e/chapter3/).

- Add code that reads temperatures from the standard input and print the converted numbers. 

Here is :download:`my version <../solutions-to-exercices/Fahrenheit_celsius.py>`.


Multiplication tables
---------------------

- Write a script that displays the tables of multiplication from 1 to 10, e.g.:
::

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


- Note: you may need to read https://pyformat.info/#number_padding to format the numbers)

Check out  :download:`multiplication_table.py  <../solutions-to-exercices/multiplication-table.py>`


Taxis
-----

Two taxi companies propose differents pricing schemes:

 * Company A charges 4.80€ plus 1.15€ by km travelled.

 * Company B charges 3.20€ plus 1.20€ by km travelled.

Write some code to find which company is the cheapest as a function of the distance to travel. Compare it to :download:`taxis.py  <../solutions-to-exercices/taxis.py>`



Pascal triangle
---------------

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

Pour résoudre ce problème, une solution consiste à stocker les valeurs
de la ligne courante dans une liste Python, et d’écrire une fonction qui
étant donnée une liste en argument, calcule et renvoit la ligne suivante
dans une nouvelle liste.


Anagrams
--------

Two words are anagrams if they contain the same letters in different orders, e.g., *binary* and *brainy*.

- write a function that take two strings as arguments and returns True if they are anagrams.

- Given a list of words, print all items that have anagrams (in this list) 



Pseudowords
-----------

- Search the internet to find out how to generate a random integer number in a interval in Python

- Read about strings in Python at https://realpython.com/python-strings/

- Write functions that generate pseudowords from words. The first function will delete a character in a random position from a string passed as argument. The second will insert a random character at a random position. The third will swap two characters at random location.

- If you know about file input/output (see https://automatetheboringstuff.com/2e/chapter9/), you can read a dictionary (e.g. http://www.pallier.org/extra/liste.de.mots.francais.frgut.txt) and use it to filter out any actual words.


Compputer-guess-a-number
-----------------------

Read `chapter 3 of Invent your own games with
Python <https://inventwithpython.com/invent4thed/chapter3.html>`__ where
the author presents a game where the computer chooses a random number
that the user must guess. Study the code.

Now, your task is to write another program, where the roles are
inverted: the computer tries to guess a number that the user has in
mind. The computer proposes a number and the user answers with ‘+’ (the
number he has is mind is larger), ‘-’ (if it is smaller), ‘y’ (if the
guess is correct)


unique
------

Given a list of words, print how many different words are in that list (hint: use a dictionary or a set)


word count
----------

Given a list of words, count the number of times each word appears in
the list. Eg. ``[Jim, Alan, Jim, Joe]`` -> ``Jim:2, Alan:1, Joe:1``
(hint: use a dictionary)




head
----

Read the chapter about files at https://automatetheboringstuff.com/2e/chapter9/

Write a script that prints the first 10 lines of a file (or the whole
file is it is less than 10 lines long).

tail
----

Write a script that prints the last 10 lines of a file (or the whole
file is it is less than 10 lines long).


string-detector
---------------

Read  `Chap. 8 of Automate the boring stuff <http://automatetheboringstuff.com/chapter8/>`__.

Write a script that opens and read a text file, and print all the lignes that contain a given target word,  say, ``cogmaster``.


prime numbers
-------------

Write a script that lists all prime numbers between 1 and 10000 (A prime
number is a integer that has no divisors except 1 and itself). You may
use the following function:

.. code:: python

   def is_divisor(a, b):
       """ Args: a, b integers;
            Return True if b is a divisor of a, else False"
       return a % b == 0
   

Kaprekar numbers
----------------

Un nombre de Kaprekar est un nombre dont la représentation décimale du
carré peut être découpée en une partie gauche et une partie droite (non
nulle) telles que la somme de ces deux parties redonne le nombre
initial. Par exemple:

-  703 est un nombre de Kaprekar en base 10 car 703² = 494 209 et que
   494 + 209 = 703.
-  4879 est un nombre de Kaprekar en base 10 car 4879² = 23 804 641 et
   04641 + 238 = 4879

Ecrire un programme qui renvoit tous les nombres de Kaprekar entre 1 et N.

Solution: :download:`Kaprekar-numbers.py <../solutions-to-exercices/Kaprekar-numbers.py>`


RPN Calculator
--------------

Write a reverse Polish arithmetic expression evaluator (See
https://en.wikipedia.org/wiki/Reverse_Polish_notation).

E.g. ``3 4 * 5 -`` evaluate to ``7``.

Solution: :download:`rpn-calculator.py <../solutions-to-exercices/rpn-calculator.py>`


Rodrego-simulator
-----------------

Ecrire un programme qui simule une machine RodRego à 10 registres
(http://sites.tufts.edu/rodrego/). Le programme est stocké dans une chaine de caractère ou dans 
fichier qui est lu, puis executé. Votre programme doit contenir
une fonction qui, étant donnée les 10 valeurs initiales des registres, et
le programme, renvoit les nouvelles valeurs des registres quand
l’instruction END est atteinte.

Solution: :download:`rodrego.py <../solutions-to-exercices/rodrego.py.py>`




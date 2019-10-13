=====================
Programming Exercices
=====================


Basics
------

- prints 1000 times the lines ``All work and no play makes Jack a dull boy.``

- Given a list of numbers, print their product

- Given a list of numbers, print the sum of their square

- Given a list of numbers, print the largest one.

- Given a list of numbers, print the second largest one.


References:

   -  `Python Lists <https://www.w3schools.com/python/python_lists.asp>`__
   -  `List comprehensions <https://www.pythonforbeginners.com/basics/list-comprehensions-in-python>`__
   -   https://automatetheboringstuff.com/chapter4/


Convert temperature from Fahrenheit to Celcius
----------------------------------------------

- Read https://en.wikipedia.org/wiki/Fahrenheit and write a script that converts
  temperature from one scale to the other.

- Create a new repository  on github.com to house your conversion script, and write the
  documentation inside the README.md using Markdown format.


Multiplication tables
---------------------

- Write a script that displays the tables of multiplication from 1 to 12.

- Read https://pyformat.info/#number_padding and improve the format of the
  multiplication tables.


Taxis
-----

Two taxi companies propose differents pricing schemes:

 * Company A charges 4.80€ plus 1.15€ by km travelled.

 * Company B charges 3.20€ plus ##20€ by km travelled.

Write a script that finds which company is the cheapest as a function of the distance to travel.



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






computer-guess-a-number
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


RPN Calculator
--------------

Write a reverse Polish arithmetic expression evaluator (See
https://en.wikipedia.org/wiki/Reverse_Polish_notation).

E.g. ``3 4 * 5 -`` evaluate to ``7``.


Rodrego-simulator
-----------------

(optionnel: seulement pour ceux qui se sentent capables et sont motivés)
Ecrire un programme qui simule une machine RodRego à 10 registres
(http://sites.tufts.edu/rodrego/). Le programme est stocké dans une chaine de caractère ou dans 
fichier qui est lu, puis executé. Votre programme doit contenir
une fonction qui etant donnée les 10 valeurs initiales des registres, et
le programme, renvoit les nouvelles valeurs des registres quand
l’instruction END est atteinte.




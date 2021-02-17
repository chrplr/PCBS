=========================================================================
Building abstractions with recursive functions and higher-order functions
=========================================================================

In programming, we control the intellectual complexity of our programs
by **building abstractions** that hide details when appropriate.
You already know of one such means to build abstractions in Python:
the ability to **define your own functions**.
This allows you to chunk compound operations as conceptual units, give them a name and manipulate them.
In this module, you will explore two other means to build abstractions with functions: **recursive functions** and **higher-order functions**.


Recursive functions
-------------------


**1. Watch the introduction video and read the following summary paragraph.**

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/jHENcWPGLoc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Summary.**
Recursive definitions allow us to describe many complex concepts in a simple and elegant way.
Likewise, *recursive functions* in Python allow us to define methods for solving problems in a simple and elegant way.
When doing so, we think in terms of *base cases*, for which there is an immediate solution,
and *recursive cases*, for which we can define the solution to our problem in terms of solutions to smaller versions of the same problem.
Once the solution has been defined in such a way, translating it into Python code is a snap.
This frees us from without having to worry about a whole series of questions that would arise if we were to solve the problem iteratively
(how to traverse sub-problems, how to keep track of intermediate results, what the iteration variable is, what the stop conditions are…).
In other words, we have abstracted the solution from the nitty-gritty details of control flow, memory, etc.

**2. Read section 16.1 to 16.6 of the interactive book thinkcspy at:** https://runestone.academy/runestone/books/published/thinkcspy/IntroRecursion/toctree.html

Sections 16.5. and 16.6 use the ``turtle`` graphics module which you may not be familiar with, but you should still be able to grasp the code easily.
You can skip them if you want, but visualization is a powerful way to learn about recursion.

**3. Do some of the following practice exercises.**

You can move to the next section whenever you feel ready to learn more, but make sure to do at least two exercises (like any other programming concepts/techniques, recursive functions cannot be understood without practice).

**Time to complete.** [\*]: short, [\*\*]: medium, [\*\*\*]: long.


**Exercise 1.** [\*] Write a recursive function to reverse a list. (Hint: to concatenate two lists, use the '+' operator).

.. A solution: TBD

**Exercise 2.** [\*] Write a recursive function to reverse a list.

.. A solution: TBD

**Exercise 3.** [\*\*] Write a script that displays the Koch snowflake (`see on wikipedia <https://en.wikipedia.org/wiki/Koch_snowflake>`__) using a recursive function.
You can use the ``turtle`` graphics module to draw on screen
(as shown in `section 16.5 of thinkcspy <https://runestone.academy/runestone/books/published/thinkcspy/IntroRecursion/intro-VisualizingRecursion.html>`__).

A solution: `link to code <https://github.com/chrplr/PCBS/blob/9a9ebc54b5a03c4e58311cb0d0bd20ea12d0ec02/games/koch.py>`__.

**Exercise 4.** [\*\*] Write a script that returns the pathnames of all the files ending in ``.txt`` contained inside a directory (at any depth of the hierarchy). You will need to use ``os.listdir()`` and ``os.path.isdir()``.

**Exercise 5.** [\*\*] Write a recursive function to generate all permutations of a list of values. (This could be useful, e.g., to do a permutation test for statistical analyses.)

**Exercise 6.** [\*\*\*] Write a recursive function to evaluate an arithmetic expression given in Polish notation (i.e. prefix notation, `see on wikipedia <https://en.wikipedia.org/wiki/Polish_notation>`__)

.. A solution: TBD

**Exercise 7.** [\*\*\*] Produce strings from the MIU formal grammar and investigate the MU puzzle. See :ref:`detailed explanations on the MU Puzzle <mupuzzle>`.

.. A solution: TBD


Side remark: in some cases, recursive functions can take a prohibitive amount of time and/or memory. This happens when the same computations are performed many times. This issue can be addressed using *memoization*. If you are curious, you can read the article `Memoization in Python <https://towardsdatascience.com/memoization-in-python-57c0a738179a>`__



Higher-order functions
----------------------


**1. Watch the introduction video.**

.. raw:: html

	<iframe width="560" height="315" src="https://www.youtube.com/embed/X98wQvjqplk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


**2. Read section 1.6 Higher-Order Functions of the online textbook at:**
https://wizardforcel.gitbooks.io/sicp-in-python/content/6.html

This textbook is an adaptation for Python of the textbook cited at the bottom of the page. (Author’s note: I haven’t checked out the rest of this adaptation. I recommend to read the original book if you want to learn more.)

**Stop and think:** In the section of the book you have read, the functions ``summation`` and ``iter_improve`` were implemented iteratively, using a ``while`` statement. Can you think of how to implement them recursively?

**3. Do some of the following practice exercises.**

**Time to complete.** [\*]: short, [\*\*]: medium, [\*\*\*]: long.

**Exercise 1.** [\*]
Write a ``product`` function to compute the product of the values of a function at points over a given range (the function should be an argument of ``product``).
Then, define a function to compute the factorial in terms of ``product``.
Finally, use ``product`` to compute an approximation to pi using the Wallis product formula (`see on wikipedia <https://en.wikipedia.org/wiki/Wallis_product>`__).

**Exercise 2.** [\*\*]
The ``summation`` function (from the textbook section you read)
and the ``product`` function (defined above)
can be defined as special cases of an even more general ``reduce`` function
which has two more arguments:
``binary_operator`` (which specifies what operation should be applied to reduce all the values to a single one)
and ``neutral_element`` (which specifies what base value should be used when the range is empty).
Write such a ``reduce`` function, and then define ``summation`` and ``product`` functions in terms of ``reduce``.
Make sure to test your functions. 

**Exercise 3.** [\*\*]
Write a function that finds a fixed point of a function
(`see on wikipedia <https://en.wikipedia.org/wiki/Fixed_point_(mathematics)>`__)
starting from an initial guess value, which could be defined as:
``find_fixed_point(f, initial_value, error_margin)``.
The returned value, ``x``, should be such that ``abs(f(x) - x) < error_margin``. Then, define a function to calculate the square root of a positive number, using the property that the square root of x is a fixed point
for the function y -> 1/2 (y + x/y).
Make sure to test your square root function.

**Exercise 4.** [\*\*]
Write a function to numerically compute any statistic of an arbitrary random variable.
The statistic and the random variable should both be functions which are given as argument.

(Hints. A statistic can be defined as a function of a collection of samples, e.g. sample mean, sample variance. A random variable can be defined as a function that, when it is called, generates one sample.)


Reference
----------

This module was inspired by:
Abelson, Harold, and Gerald Jay Sussman. *Structure and interpretation of computer programs*. The MIT Press, 1996.

It is an excellent computer science textbook. If you are curious, go check it out, it is freely available online `as pdf <https://web.mit.edu/alexmv/6.037/sicp.pdf>`__ and `as a web document <https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html>`__.


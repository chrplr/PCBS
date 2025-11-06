.. _tips:

==================
Writing clean code
==================

.. contents::


Most of these recommendations are copied verbatim from the book  `Clean Code <https://www.goodreads.com/book/show/3735293-clean-code>`__  by Robert C. Martin.


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Names
-----

-  A function name should describes what the function does. Don’t be
   afraid to make a name long. A long descriptive name is better than a short
   enigmatic name. A long descriptive name is better than a long
   descriptive comment.

-  Don’t be afraid to spend time choosing a name. Indeed, you should try
   several different names and read the code with each in place.

-  Be consistent in your names. Use the same phrases, nouns, and verbs
   in the function or variables names.


Functions
---------

-  The first rule of functions is that they should be small. The second
   rule of functions is that they should be smaller than that. Between 1
   and 10 lines is usually good.

-  A function must do one thing, and do it well. This is because we want
   each function to be transparently obvious. For example, passing a
   boolean into a function is a truly terrible practice. It loudly
   proclaims that this function does more than one thing: It does one
   thing if the flag is true and another if the flag is false!

-  A function should have no side effects. If it does, your function
   promises to do one thing, but it also does other hidden things.
   Sometimes it will make unexpected changes to the variables passed as
   parameters or to system globals. In either case they are devious and
   damaging mistruths that often result in strange temporal couplings
   and order dependencies.

-  Functions should either do something or answer something, but not
   both. Either your function should change the state of an object, or
   it should return some information about that object. Doing both often
   leads to confusion.


Successive refinement
---------------------

-  Writing software is like any other kind of writing. When you write a
   paper or an article, you get your thoughts down first, then you
   massage it until it reads well. The first draft might be clumsy and
   disorganized, so you wordsmith it and restructure it and refine it
   until it reads the way you want it to read.

-  In R. Martin’s words:

..

   "When I write functions, they come out long and complicated. They
   have lots of indenting and nested loops. They have long argument
   lists. The names are arbitrary, and there is duplicated code. But I
   also have a suite of unit tests that cover every one of those clumsy
   lines of code.

   So then I massage and refine that code, splitting out functions,
   changing names, eliminating duplication.

..

   In the end, I wind up with functions that follow the rules I’ve laid
   down. I don’t write them that way to start. I don’t think anyone
   could."


General
-------

- We want the code to read like a top-down narrative. Each function must tell a
  story. And each function should led you to the next in a compelling order.

- Don’t Repeat Yourself. Duplicating the same code at, say four locations in
  your program, is a problem because it bloats the code and will require
  four-fold modification should the algorithm ever have to change. It is also a
  four-fold opportunity for an error of omission. Structured programming and
  Object-oriented programming were invented in part as strategies to avoid
  duplication.

Comments
--------

- Comments are, at best, a necessary evil. If our programming languages were
  expressive enough, we would not need comments very much—perhaps not at all.
- Comments should say things that the code cannot say for itself.
- A comment worth writing is worth writing well. If you are going to write a
  comment, take the time to make sure it is the best comment you can write.
  Choose your words carefully. Use correct grammar and punctuation. Don’t
  ramble. Don’t state the obvious. Be brief.
-  Learn about `docstrings in Python <https://www.datacamp.com/community/tutorials/docstrings-python>`__
- Learn about automatic generation of documentation with sphinx and readthedocs at https://www.pythonforthelab.com/blog/documenting-with-sphinx-and-readthedocs/


Testing
-------

It is an excellent idea to write tests that check your that your modules and
function keep working as they should. It can be as simple as having scripts that
just run your code on some examples and check that it does not crash after an
upgrade, or following a unit testing methodology (see `Getting Started With
Testing in Python <https://realpython.com/python-testing/>`__)



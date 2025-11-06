*********************
Starting from Scratch
*********************


To begin our journey into programming, we will use Scratch_, a system developed the MIT media lab to teach how to program to kids.

.. _Scratch: http://scratch.mit.edu

A great advantage of Scratch_ is that programs are created using a graphical interface,
preventing *syntactic errors*. Thus, you can learn the language without having to 
learn its grammar!

One can either work online at https://scratch.mit.edu/projects/editor/?tip_bar=home or offline, by
downloading Scratch_ at

-  https://scratch.mit.edu/scratch_1.4/ (version 1)
-  https://scratch.mit.edu/scratch2download/ (version 2)

We recommend the reader to run the tutorial `“Getting Started with Scratch” <https://scratch.mit.edu/projects/editor/?tip_bar=home>`__


First steps
===========

Program 001
-----------

In the ``motion`` group, take the instruction ``turn 15 degrees`` and drag
it onto the ``Scripts`` panel.

|image1|

Double-Click repeatedly on the block ``turn 15 degrees``, you should see
the cat (``sprite 1``) rotate.

In Scratch, when one double-clicks an instruction in the ``Scripts``
panel, the computer **executes** it.

Program 002
-----------

Drag the instruction ``move 10 steps`` from the motion group, and add it
to the bottom of the instruction ``turn 15 degrees``. Change the value
``10`` into ``50``.

|image2|

You have just created a **block** of instructions, that is, your first
**program** or **script**, Bravo!

-  Double-Click on the block and see the sprite moving.
-  Note that inside a block, instructions are exectuted *sequentially*,
   one after the other. **Can you prove it**?
-  Experiment with changing the **argument** of the instruction ``move``
   (Tip: to clear the drawing area, move the instruction ``pen/clear`` to
   the script window and execute it)

Program 003
-----------

Click on the ``pen`` group, and add ``pen down`` at the top of the block.

|image3|

Run it.

Program 004
-----------

Construct the following scripts and play with them until you are sure to
understand the behavior of the computer..

|image4|

Concepts learned so far
=======================

-  Instruction
-  Argument of an instruction (change ``10`` in ``move 10 steps``)
-  Block of instructions and sequential execution

Loops
=====

repeat (``for`` loop)
---------------------

Computers are good at doing tasks repeatedly (as they do not get tired).

Click on the “Control” group, and try to construct the following script:

|image5|

-  Clicking on the ``green`` flag will execute the block of instructions
-  The ``Repeat`` instruction executes the inner block of instruction a
   number of times specified as an argument. This is called a **loop**
-  Adjust the parameter of the Repeat instruction so that the sprite
   draws a full circle when you click once on the green flag.
-  Replace the repeat instruction by ``forever``.

Repeat until
------------

Modify the script as follows:

|image6|

Tip: the condition ``key space pressed?`` is in the ``Sensing`` group.

This illustrates a **repeat…until loop**: the inner block is executed
until the **condition** is satisfied.

Two sprites
===========

Add a new sprite, and duplicate the script from sprite1. Click on the
green flag. You should see the two sprites running in circles.

|image7|

Remark that the scripts associated to the two sprites run in *parallel*
(rather than sequentially).

Conditional execution or branching
==================================

Create a new scratch project, and change the costume of the sprite into
a ball.

Then write and execute the following script.

|image8|

You should see the ball bounce on the edges.

First series of exercices
=========================

1. With Scratch, use the instructions “pen down” and “move” and “turn”
   to (a) make the cat draw a square (with sides measuring 100 steps)
   (b) draw an hexagon (c) draw a circle

2. Using the Control/Forever, make the cat turn continuously along a
   circle.

3. Bouncing ball

-  Delete the cat. Using new sprite/open, add a ball.
-  Make the ball move automatically horizontally from left to right and
   bounce when it touches an edge (tip: use Control/forever)
-  Make the ball follow the mouse.
-  Add a second ball that follows the first.

4. Create a script that asks for your name and then displays “Hello !”.
   Tip: use the instructions ``sensing/ask``, ``looks/say`` and
   ``operator/join`` and the variable ``sensing/answer``.

. . .

|image9|

. . .

Variables
=========

Using the group ``variable``, we are going to create a **variable** ``a``
and make it display continuously the x-coordinate of the ball.

|image10|

The concept of **variable** is very important. You can think of it as a
name for a object that can change (here the object is a number).

Now study the following script:

|image11|

The loop is executed 100 times. Each time, the value of the variable
``a`` is incremented by 1, and is used to compute new ``x`` and ``y``
coordinates where to sprite is instructed to moved to.

|image12|


Second series of exercices
==========================

Multiplication
--------------

“Multiply by adding”: Write a program that reads in two integer numbers and
displays their sum.



|image13|



Guess a number
--------------

“Guess a number”. Make Scratch pick up a random number in the interval [1,100],
and loop asking you for a guess and reply either ``too low``, ``too high``, or
``you win!`` depending on your answer.


|image14|



Estimate PI
-----------

3. We are going to estimate the number PI by a Monte Carlo method.:

-  Repeatly (e.g. 2000 times) picks up two random numbers on the
   interval [-1, 1]. This corresponds to a dot inside a square of size
   2x2.
-  Count how many times the dot falls within the circle of radius 1
   centered on the origin (Pythagore helps you here: the dot is within
   the circle iff ``(x * x + y * y) < 1``.)
-  The proportion of dots falling within the circle, multiplied by four
   (the area of the square), is an estimate of teh area of the disk,
   that is, the number pi.


|image15|




.. |image0| image:: img/marr.jpg
.. |image1| image:: img/scratch_001.png
.. |image2| image:: img/scratch_002.png
.. |image3| image:: img/scratch_003.png
.. |image4| image:: img/scratch_004.png
.. |image5| image:: img/scratch_repeat.png
.. |image6| image:: img/repeat_until.png
.. |image7| image:: img/two_sprites.png
.. |image8| image:: img/condition_001.png
.. |image9| image:: img/hello.png
.. |image10| image:: img/condition_002.png
.. |image11| image:: img/function_001.png
.. |image12| image:: img/xy-function.png
.. |image13| image:: img/multiply.png
.. |image14| image:: img/guess-a-number.png
.. |image15| image:: img/pi_by_montecarlo.png
.. |image16| image:: img/Spirograph.jpg


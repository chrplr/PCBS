==============
Running Python
==============

.. contents::


They are several ways to work with Python, each of which is best adapted to a certain type of task:

  * To quickly test short pieces of code in an interactive manner, or to access the documentation of some functions or mudles, open a terminal and run ``ipython``

  * To write reusable python scripts, use a text editor or an Integrated Development Environment, save the script and run it from a command line in a Terminal.

  * To write a data analysis report, or a lecture, use a jupyter notebook.



Running a python script from the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run a python script, that is, a text file containing python code, you need to:

1. Open a Terminal

MacOS
   Type ``terminal`` in the Spotlight search field.

Windows
   Start ``Git Bash`` (This assumes that you have installed
   ``Git for windows`` as described in `Instructions for software
   installation <#instructions-for-software-installation>`__)

Linux
   Launch ``Terminal`` from your application menu or use
   ``Ctrl-Alt-T`` (gnome, xfce), or ``Win+Return`` (i3)).

2. If the script is not located in the current working directory (the user's home directory), use the `cd command <http://linuxcommand.sourceforge.net/lc3_lts0020.php>`__ to navigate to the relevant directory

3. Type ``python`` followed by the script's filename, then press the ``return`` key.

For example, let us suppose that you want to execute a script named ``matches.py`` located in a subdirectory ``PCBS/games`` of your home directory. Open a terminal and type::

   cd PCBS/games
   python matches.py


Remarks:

  * When the script has run to completion, you will be back interacting with the shell (see http://linuxcommand.sourceforge.net/lc3_learning_the_shell.php).

  * It you need to interrupt a running python script, you can press ``Ctrl-C`` in the Terminal.

  * You can specify `absolute or relative pathnames <https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/>`__ to specify the location of the scripts::

     python ~/PCBS/games/matches.py

  * A good practice is to always take a glance to the code *before* running it. Depending on your system, you might be able to do this with the commands ``cat filename.py`` or ``less filename.py`` or ``micro filename.py``, ...



Testing a short piece of python code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To quickly test some Python code, type ``ipython`` on a command line.

.. figure:: figures/ipython_terminal1.png

Then press 'Return'; you should obtain a should display  like the following:

.. figure:: figures/ipython_terminal2.png

A blinking cursor after ``[1]:`` indicates that ipython is ready and waiting for you to enter a Python statement that it will execute as soon as you press the "Return" key. For example, try:

.. code:: python

   2 ** 5
   2 ** 64


.. code:: python

       import turtle
       turtle.circle(50)
       turtle;forward(100)
       turtle.circle(50)

       turtle.right(90)
       turtle.forward(100)
       turtle.right(90)
       turtle.heading()


.. code:: python

        import matplotlib.pyplot as plt
        import numpy as np
        t = np.linspace(0, 30, num=3001)
        plt.plot(t, np.sin(t))

A Window should open with a graphical representation of the sine function,
You can press ‘q’ in this Window to close it.

It is possible to  execute a python script from within ipython. While in ipython, try:

.. code:: python

   pwd
   cd PCBS/games
   %run matches.py


Finally, To quit ipython, type ``quit()`` or press ``Ctrl-D`` .

This approach is fine if you need to quickly test an idea. But as soon as you quit ``ipython``, you lose
all what you have done (technically, this is not entirely true: ipython saves the history of commands that you have typed).

To keep track of your work, you need to use a text editor and the
*Edit-run* approach.






Write code inside a text editor (Edit-run cycle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


A script is nothing but a pure text file, that is, a sequence of characters.

A Python script is written with a **text editor**, saved on the disk, and then executed

1. Open a Text-Editor (e.g. Sublime Text) and a Terminal window side-by-side:

.. figure:: figures/editor-terminal.png
   :alt: Using Atom and a Terminal side by side


2. Create a ``New File`` in the Editor and enter the following text:

.. code:: python

       import turtle
       turtle.forward(50)
       turtle.left(120)
       turtle.forward(100)
       turtle.left(120)
       turtle.forward(100)
       turtle.left(120)
       turtle.forward(50)

3. Using ‘File/Save as’, save the this text under the filename
   ``myscript.py`` in your personal (home) directory

-  *run* with a python interpreter, by typing ``python myscript.py`` on
   a command line of the Terminal. Try it now.

Important: you must make sure that the *current working directory* of
the terminal is the same directory where the file ``myscript.py`` has
been saved. Otherwise, you will get an error message such as ‘No such
file or directory’. To fix this problem, you must use the ``cd`` command
to navigate the directory structure.

Remarks:

-  You can learn more about Turtle graphics by reading the documentation
   at https://docs.python.org/2/library/turtle.html


Using an Integrated Development Environment like Spyder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some people like to work within a single application and avoid going
back and forth from the text editor to the terminal. A nice application
for Python developement is ``spyder``, which provides an environment
somewhat similar to the MATLAB IDE.

.. figure:: figures/spyder.png
   :alt: The “spyder” Integrated Development Environment

   The “spyder” Integrated Development Environment


Spyder, PyCharm, ... are very nice IDEs but you should not use them to run python scripts that open new graphics windows (e.g. scripts using ``tkinter``, ``pygame``, ...) because, when such scripts crash, they can leave the IDE in an unstable state. It is always safer to run a script directly from the command line in a terminal windows.

One commendable approach is to use an IDE to edit python code, but then  use the command line to run the scripts.



Perform an interactive data analysis with jupyter-notebook or jupyter-lab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To perform a data analysis and produce a nicely formatter report, it is recommended to use  ``jupyter-notebook`` or ``jupyter-lab``  (see https://jupyter.org/).

In practice, launch Jupyter Notebook from the Start Menu/Anaconda3 (in Windows) or
type ``jupyter-notebook`` in a terminal (Linux, MacOS). The "Jupyter homepage" should then open in your browser:

.. figure:: figures/jupyter1.png
   :alt: Jupyter homepage


Clicking ``New`` and selecting ``Python [root]`` will open a new tab containing a
notebook where you can enter python code inside so-called ‘cells’. To execute
the code in a cell, just move the cursor there and press ``Ctrl+Enter``

.. figure:: figures/jupyter2.png
   :alt: Jupyter notebook

A nice feature of the Jupyter notebooks is persistence, i.e. they are
saved automatically (in ``.ipynb`` files) and you can go on working on
the same notebook whn you reopen it. This is also very handy, for
example, to send a data analysis report by email.

Jupyter’s documentation is available at
http://jupyter.readthedocs.io/en/latest/index.html


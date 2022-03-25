==============
Running Python
==============

.. contents::


They are several ways to work with Python, each of which is best adapted to a certain type of task:

  * To write reusable python scripts, use a code editor (e.g. `subl`` (Sublime Text)), or an Integrated Development Environment (e.g. ``spyder``), save the script and run it from a shell command line inside a Terminal.

  * To quickly test short pieces of code in an interactive manner, or to access the documentation of some functions or mudles, open a terminal and run ``ipython``

  * To write a data analysis report use ``jupyter notebook``


Running a python script from the command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run a python script, that is, a text file containing python code, you need to:

1. Open a Terminal

  * MacOSX: Search for ``terminal`` in Spotlight.
  * Windows: Launch ``Git Bash`` (This assumes that you have installed
   ``Git for windows`` as described in `Instructions for software
   installation <#instructions-for-software-installation>`__)
  * Linux: Launch ``Terminal`` from your application menu or use
   ``Ctrl-Alt-T`` in Gnome, Xfce or ``Win+Return`` in i3.

2. If the script is not located in your home directory, use the ``cd`` command to navigate to the directory that contains the script (to learn about this, read `Navigation in the shell <http://linuxcommand.sourceforge.net/lc3_lts0020.php>`__). 

3. Type ``python`` followed by the script's filename, then press the ``return/enter`` key.

For example, let us suppose that you want to execute a script named ``matches.py`` located in a subdirectory ``PCBS/games`` of your home directory. Open a terminal and type::

   cd PCBS/games
   python matches.py


Remarks:

  * When the script has run to completion, you will be back to interacting with `the shell <http://linuxcommand.sourceforge.net/lc3_learning_the_shell.php)>`_.

  * It you need to interrupt a running python script, you can press ``Ctrl-C`` in the Terminal.

  * You can specify `absolute or relative pathnames <https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/>`__ to specify the location of the script::

     python ~/PCBS/games/matches.py

   Note: The directory from which you started the script is the **current working directory**: it will be the root for any relative path names that may be used within the script.

  * A good practice is to systematically take a glance to the code *before* running it. Depending on your system, you might be able to do this with the commands ``cat filename.py`` or ``less filename.py`` or ``micro filename.py``.


Testing a short piece of python code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To quickly test some Python code, type ``ipython`` (“interactive Python”) on a command line.

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
all what you have done.

To keep track of your work, you need to use a code editor and the *Edit-Run* approach.



Write code with a text editor (Edit-run cycle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


A script is nothing but a pure text file, that is, a sequence of characters.

A Python script is written with a **text editor**, saved on the disk, and then executed.

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
to `navigate the directory structure <http://linuxcommand.sourceforge.net/lc3_lts0020.php>`_. 
  

Remarks:

-  You can learn more about Turtle graphics by reading the documentation
   at https://docs.python.org/2/library/turtle.html


-  WINDOWS Only: To be able to start 'Sublime Text' from the command line by just typing ``subl``, copy the following command:

           export PATH="/c/Program Files/SublimeText 3/":"$PATH"

  in the file ``$HOME/.bash_profile`` (create it if necessary)


Using an Integrated Development Environment (IDE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some people like to work within a single application and avoid going
back and forth from the text editor to the terminal. The Anaconda Python distribution comes with and integrated development environment (IDE), Spyder_, which provides an environment somewhat similar to the MATLAB IDE. PyCharm_ and `Microsoft Visual Code`_ are two other popular (and more powerful) IDEs. 


.. _Spyder: https://www.spyder-ide.org/
.. _PyCharm: https://www.jetbrains.com/pycharm/
.. _Microsoft Visual Code: https://code.visualstudio.com/

.. figure:: figures/spyder.png
   :alt: The “spyder” Integrated Development Environment

   The “Spyder” Integrated Development Environment


Visual Code, PyCharm, Spyder... are very nice IDEs but you should not use them to run python scripts that open new graphics windows (e.g. scripts using ``tkinter``, ``pygame``, ...) because, when such scripts crash, they can leave the IDE in an unstable state. It is always safer to run a script directly from the command line in a terminal windows.

One commendable approach is to use an IDE to edit python code, but use the command line to run the scripts.


Perform an interactive data analysis with jupyter-notebook or jupyter-lab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To perform data analyses and produce nicely formatted reports, one can use  ``jupyter-notebook`` or ``jupyter-lab``  (see https://jupyter.org/).

In practice, launch Jupyter Notebook from the Start Menu/Anaconda3 (in Windows) or
type ``jupyter notebook`` in a terminal (Linux, MacOS). The "Jupyter homepage" should then open in your browser:

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


Developping in Python with Emacs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Action
     - Shortcut
     - Function

   * - Comment or Uncomment cleverly
     - ``M-;``
     - comment-dwim

   * - Indent
     - ``C->`` 
     - python-indent-shift-right
     
   * - Unindent 
     - ``C-<``
     - python-indent-shift-left
     
   * - Navigate the function definitions
     - ``C-c C-j``
     - imenu
     
   * - Move backward to block
     - ``M-a`` 
     - python-nav-backward-block
     
   * - Move forward to block
     - ``M-e``
     - python-nav-forward-block
     

   * - Checking for errors, etc.
     -
     - flymake
     
   * - Checking for errors, etc.
     -
     - flycheck
   
   * - Reformat code to best practices
     -
     - yapify
     
   * - Launch the Python Debugger (Pdb_)
     -
     - pdb
     

.. Note::
   I am actually using Spacemacs_ with the `python layer`_

   See also https://realpython.com/emacs-the-best-python-editor/


.. _Pdb: https://realpython.com/python-debugging-pdb/#essential-pdb-commands
.. _Spacemacs: https://www.spacemacs.org/
.. _`python layer`: https://develop.spacemacs.org/layers/+lang/python/README.html

.. _first:

==================
First things first
==================

.. contents::


Course description
------------------


Objectives
~~~~~~~~~~

Students in Cognitive-(Neuro)-science need to learn programming:

1. to understand how computers work, because of the importance of the
   Computational Theory of Mind in Cognitive Science.
2. to automate the boring stuff (e.g. repetitive work on files, web
   scrapping,)
3. to do reproducible science: simulating models, designing experiments, running
   them, analysing data, ...


The purpose of the PCBS course is to make students able to write clean code in
order to solve the tasks that are typically encountered in cognitive or
neurosciences (data manipulation and analysis, creation of stimuli, programming
of real-time experiments, simulations...). The first half (6 weeks) of the
course consists of lectures with hands-on exercises, then, during the last 6
weeks, students have to realize a project publicly available on github.


Learning outcomes
~~~~~~~~~~~~~~~~~
                    
On successful completion of this course, students should be able to write
readable, well- documented, Python programs, and use system such as git that
promote reproducible science.

                    
Pedagogy, class organization and homework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first classes are CM with hands-on exercices. The remaining classes, I and
the teaching assistant are present for individual support to help the students
accomplish their project. I also give weekly assignments to be done *before* the
next lecture.
                    
Assessment
~~~~~~~~~~

The projects will be graded on a 20 points scale. The main criterion is *clarity*
(see :ref:`projects` for more details).



Textbook and readings
~~~~~~~~~~~~~~~~~~~~~

All the materials are available on the course’s web site at http://github.com/chrplr/PCBS.
                    

Course policies
~~~~~~~~~~~~~~~
                    
Laptops: Students must bring there own laptop (preferably fully charged!) with
the specified software preinstalled.
                    
Participation. You are strongly encouraged to participate in lectures and on the
slack discussion forum. The more advanced students are expected to help the
beginners.


Prerequisites
-------------

Students are expected to know how to open a terminal and `navigate in the file system <http://linuxcommand.org/lc3_lts0020.php>`__ and to know how to view and edit text files with a text editor such as `Sublime Text <https://www.sublimetext.com>`__.

They should  acquainted with basic programming concepts: instructions, variables, tests (if..then..else), loops (while and for). Check out  starting-from-scratch_ or the pointers listed in resources_:  


Software Installation
---------------------

These instructions explain how to install  *Anaconda Python 3*, *Expyriment*, *Git*, a text editor, 
*R* and *R Studio*.


Warnings:
~~~~~~~~~

-  You will need to download about 1GB of software from the Internet.
   Therefore, make sure to have a decent connection.
-  Make sure that you have at least 5GB of free space on your hard drive
   to unpack the various software.
-  You might need to have administrator rights to install some of the
   softwares. If you are using a computer from an Institution, this is
   not always the case. Check with your IT team.
-  If you are using Windows 10, make sure your user name doesn’t include
   spaces or characters that don’t belong to the English alphabet
   (accents, ideograms,…). If you do, better create a new user with a
   simple identifier.


Anaconda Python3
~~~~~~~~~~~~~~~~

Among various python distributions, we recommend the `Anaconda
distribution <https://www.anaconda.com/distribution>`__ because it comes
with most of the packages needed for the lectures.

1. Go to <https://www.anaconda.com/> and among the "Products", search for the "Individual Edition";
   Select your OS — Windows, MacOS or Linux — and download the 64 bits
   installer for the latest version of Python (3.8 at the time of writing this).
2. Execute the Anaconda3 installer.
3. In the Anaconda Setup Wizard.
    * If you are on a Mac, accept all the default option.
    * If you are under Windows, pay attention to the following options:

       -  verify that you Install for ``Just Me (recommended)``, then click on ``Next``
       -  Accept the default Destination folder and click on ``Next``
       -  VERY IMPORTANT: Check the boxes in front ``Add Anaconda to my PATH`` (ignore the warning that this is not recommended) and ``Register Anaconda as my default Python`` and click on ``Install``
       -  upon completion, click on ``Next``, then ``Finish``


Expyriment
~~~~~~~~~~

We will make use of Python library `Expyriment <http://www.expyriment.org>`__

1. Open a Terminal, following the instructions specific to your operating system:

Windows
    Launch ``Anaconda Prompt`` (use the "Search box")

MacOS
   Type ``terminal`` in the Spotlight search field (Or, open a ``Finder`` window, select the
   ``Application`` folder, then the ``Utilities`` folder, then double-click on the ``Terminal`` icon)

Linux
   launch ``Terminal`` from your applications menu (or use ``Ctrl-Alt-T``).


2. Inside the terminal, type the following command::

       pip install expyriment

3. Test that the installation went fine. In the terminal, type::

      ipython

This should display something like::

   Python 3.7.4 (default, Aug  9 2019, 18:51:30) 
   Type 'copyright', 'credits' or 'license' for more information
   IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.

It means that you are interacting with the ipython programme. Now type::

      import expyriment

If all went well, you should see a message such as::

   pygame 1.9.6
   Hello from the pygame community. https://www.pygame.org/contribute.html
   Expyriment 0.9.0 (Python 3.7.4) 

Finally, press ‘Ctrl-D’ to exit ipython, then ``y`` for 'yes', and type ``exit`` to close the
terminal.


The Git version control system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git is a version control tool for software development, an indispensable
tool to do reproducible science.

Linux
   execute the command ``sudo apt install git``

MacOSX
   Download the ``Git for Mac`` installer from https://git-scm.com/download/mac and execute it. Accept all the
   defaults.

Windows
   Download the 64 bit version of ``Git for windows`` from https://git-scm.com/download/win and
   launch it.
   1. When the GNU Licence is displayed, press ``Next``;
   2. Accept the default installation folder and press ``Next``;
   3. Accept all the Components selected by default and press ``Next``
   4. Accept the creation of a start menu folder named 'Git': press ``Next``;
   5. VERY IMPORTANT: When proposed a default editor, select 'Use the nano editor' (unless you want to learn Vim) 
   6. VERY IMPORTANT: When proposed to adjust your Path environnement,  tick the box "Use Git and optional unix tools from the command line prompt". 

   Then accept all other defaults.  (Note: if you are hesitant, check the graphical instructions provided at
   https://hackernoon.com/install-git-on-windows-9acf2a1944f0)


Now, open *Git Bash* if you are under Windows, or a standard terminal if you are under MacOS or Linux, and type::

    git config --global user.name "your_first_and_last_names_here" 
    git config --global user.email your_email_here 
    git config --global core.editor nano


You can exit the terminal by typing `Ctrl-D`, or `exit`.

A Text file Editor
~~~~~~~~~~~~~~~~~~

A text editor is a program that allows you to edit pure text files such
as python scripts, markdown documents,...

Unless you already use a text editor that you are happy with, we
recommend that you download and install *Sublime Text* from
https://www.sublimetext.com/. Follow the instructions specific for your
Operating System.

If you prefer opensource software, try `Atom <http://atom.io>`__, but be
aware that it is slower and more buggy than sublime text.

Finally, if you like small and simple things, you can instead use the
lightweight editor `micro <https://micro-editor.github.io/>`__

If you can afford to spend a few weeks of your life to learn a text editor,
learn Emacs (see https://realpython.com/emacs-the-best-python-editor/).

An alternative is to install Visual Studio Code from https://code.visualstudio.com


The R statistical software
~~~~~~~~~~~~~~~~~~~~~~~~~~

R is a programming language specialized for statistical data analyses.

Windows
   Download and install the latest version of R from
   https://cran.rstudio.com/bin/windows/base/

MacOS
   Download and install the latest version of R from
   https://cran.rstudio.com/bin/macosx/

Linux
   Find the version relevant for your distribution at
   https://cran.rstudio.com/bin/linux/ and follow the instructions in
   the ``README.html`` file.


Rstudio Desktop
~~~~~~~~~~~~~~~

Rstudio is an Integrated Developpement Environment for R which greatly
simplifies the use of \__RMarkdown_. You can download and install the
latest version of \__RStudio Desktop\_ from
https://www.rstudio.com/products/rstudio/download/. Make sure to select
the correct Operating System!


Learn how to open a Terminal
----------------------------

MacOS
   Type ``terminal`` in the Spotlight search field.
   Alternatively, you can open a ``Finder`` window and select the
   ``Application`` folder, then the ``Utilities`` folder, then
   double-click on the ``Terminal`` icon..

Windows
   Start ``Git Bash`` (This assumes that you have installed
   ``Git for windows`` as described in `Instructions for software
   installation <#instructions-for-software-installation>`__)

   1. Click the Windows or Start icon.
   2. In the Programs list, open the Git folder.
   3. Click the option for Git Bash.

Linux
   Launch ``Terminal`` from your application menu or use
   ``Ctrl-Alt-T`` (gnome, xfce), or ``Win+Return`` (i3)).


Inside a terminal, you interact with a program that expects you to type
commands. This program is called a *shell* (see
http://linuxcommand.sourceforge.net/lc3_learning_the_shell.php).

You only need
to know three commands in order to navigate in the filesystem:

-  *ls*: list the content of the current working directory
-  *pwd*: path of current working directory
-  *cd*: change directory

Read http://linuxcommand.sourceforge.net/lc3_lts0020.php to learn about them.


Download the course materials
------------------------------

Once Git is installed  on your computer, you can download the
course materials. To this end, open a terminal and type::

       git clone https://github.com/chrplr/PCBS.git

This should download, the course materials at from http://githb.com/chrplr/PCBS
inside a subfolder named ``PCBS``.

Be aware that if a folder with that name already
exists, git will stop and not download the content of the website. In that case,
delete or move the existing PCBS folder before running the ``git clone`` command
above.

I do often update the materials. To synchronize your local copy with the
latest version, you just need to open a terminal and type::

      cd PCBS
      git pull


Important: do not manually modify or create new files in the PCBS folder.
If you do so, git will notice it and might prevent an automatic upgrade
and ask you to ‘resolve conflicts’. If you get such a message, the
simplest course of action, for beginners, is to delete the PCBS folder (or
move it if you wnat to keep a copy of your modifications) and reissue the
``git clone`` command above to reload the full folder.


 

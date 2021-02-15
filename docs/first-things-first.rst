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

They should  acquainted with basic programming concepts: instructions, variables, tests (if..then..else), loops (while and for). 

Students are expected to know how to open a terminal and `navigate in the file system <http://linuxcommand.org/lc3_lts0020.php>`__ and to know how to view and edit text files with a text editor such as `Sublime Text <https://www.sublimetext.com>`__.


Resources
---------

Basic programming concepts
~~~~~~~~~~~~~~~~~~~~~~~~~~

A fun way to get acquainted to learn the bases of programming is to play with the MIT language **Scratch**. Check out my document :doc:`scratch/Starting-from-Scratch`


Programming skills
~~~~~~~~~~~~~~~~~~

*  `Software Carpentry <https://software-carpentry.org/lessons/>`__
   provides nice lessons about writing software for science.
*  :doc:`tips-to-write-clean-code`



Resources to learn Python
~~~~~~~~~~~~~~~~~~~~~~~~~

-  I **strongly recommend** the freely available book `Automate the
   boring stuff with Python: Practical programming for total
   beginners. <https://automatetheboringstuff.com/>`__ to total novices
   (as well as the other books by the author). For those who dislike
   reading, there are videos on the site.

-  See :download:`Python in a Nutshell <../02_Python_in_a_nutshell/Python_in_a_nutshell-doc.html>`


*  Books:

   -  `Automate the boring stuff with
      Python <https://automatetheboringstuff.com/>`__ (highly
      recommended!)
   -  `Apprendre à Programmer avec
      Python3 <https://inforef.be/swi/python.htm>`__
   -  `Think Python <http://greenteapress.com/thinkpython2/>`__


*  MOOCs:

   -  `Udemy’s Python programming for absolute
      beginners <https://www.udemy.com/python-programming-for-absolute-beginners/>`__
   -  `Code Academy’s Learn Python
      module <https://www.codecademy.com/learn/learn-python>`__
   -  `Openclassrooms’ Apprendre à programmer en
      Python <https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python>`__
   -  `Python 3 : des fondamentaux aux concepts avancés du
      langage <https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/eb326b60bec3461ba2621fd4d6bd95b8/>`__.



Books relevant to Cognitive and Brain Sciences Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*  `Programming Visual Illusions for
   Everyone <https://www.programmingvisualillusionsforeveryone.online/>`__
   by Marco Bertamini:
*  *Neural Data Science: A Primer with MATLAB and Python* by von Erik
   Lee Nylen and Pascal Wallisch
*  *Matlab for Brain and Cognitive Scientists* and *Analyzing neural
   time series data* by Mike X Cohen
*  `Python in Neuroscience <https://www.frontiersin.org/research-topics/8/python-in-neuroscience>`__
*  *Modeling Psychophysical Data in R* by Kenneth Knoblauch & Laurence
   T. Maloney



Stimulus/Experiment generation modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  http://www.pygame.org (See `PyGame Drawing
   Basics <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>`__)
-  http://www.lexique.org
-  http://www.expyriment.org (See `Get started with
   Expyriment <https://docs.expyriment.org/Tutorial.html>`__
-  http://psychopy.org (See `Programming with
   PsychoPy <https://www.socsci.ru.nl/wilberth/nocms/psychopy/print.php>`__)
-  http://psychtoolbox.org/ (See `Psychtoolbox
   demos <http://peterscarfe.com/ptbtutorials.html>`__)
-  https://www.jspsych.org/ (See intro at https://blog.s-m.ac/using-jspsych/)



Data analyses, Statistics in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Modules: numpy, scipy, pandas, seaborn, statsmodel, sklearn

   -  Data manipulation:

      -  http://pandas.pydata.org/pandas-docs/stable/tutorials.html

   -  Plotting:

      -  http://matplotlib.org/users/pyplot_tutorial.html
      -  https://seaborn.pydata.org/tutorial.html

-  *Scipy Lecture Notes*: http://www.scipy-lectures.org/
-  *Think Stats* by Allen B. Downey:
   http://greenteapress.com/thinkstats2/
-  *Python Data Science Handbook* by Jake VanderPlas:
   https://jakevdp.github.io/PythonDataScienceHandbook
-  *Introduction to Data Science in Python*: notebook from a 2 day workshop organized by the Paris-Saclay Center for Data Science: https://github.com/paris-saclay-cds/data-science-workshop-2019


Simulations
~~~~~~~~~~~

-  `Think
   Complexity <http://greenteapress.com/wp/think-complexity-2e/>`__ by
   Allen B. Downey
-  The `Brian spiking neural network
   simulator <http://briansimulator.org/>`__
-  `Deep Learning for Natural Language Processing with
   Pytorch <https://pytorch.org/tutorials/beginner/deep_learning_nlp_tutorial.html>`__


Resources to learn the command shell
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Why learn the command shell?

   “What is a command shell? To properly understand the role of a shell,
   it’s necessary to visualize what a computer does for you. Basically,
   a computer is a tool; in order to use that tool, you must tell it
   what to do—or give it “commands.” These commands take many forms,
   such as clicking with a mouse on certain parts of the screen. But
   that is only one form of command input.

..

   By far the most versatile way to express what you want the computer
   to do is by using an abbreviated language called script. In script,
   instead of telling the computer, “list my files, please”, one writes
   a standard abbreviated command word—‘ls’. Typing ‘ls’ in a command
   shell is a script way of telling the computer to list your files.1

   The real flexibility of this approach is apparent only when you
   realize that there are many, many different ways to list files.
   Perhaps you want them sorted by name, sorted by date, in reverse
   order, or grouped by type. Most graphical browsers have simple ways
   to express this. But what about showing only a few files, or only
   files that meet a certain criteria? In very complex and specific
   situations, the request becomes too difficult to express using a
   mouse or pointing device. It is just these kinds of requests that are
   easily solved using a command shell.

..

   For example, what if you want to list every Word file on your hard
   drive, larger than 100 kilobytes in size, and which hasn’t been
   looked at in over six months? That is a good candidate list for
   deletion, when you go to clean up your hard drive. But have you ever
   tried asking your computer for such a list? There is no way to do it!
   At least, not without using a command shell.

   The role of a command shell is to give you more control over what
   your computer does for you. Not everyone needs this amount of
   control, and it does come at a cost: Learning the necessary script
   commands to express what you want done. A complicated query, such as
   the example above, takes time to learn. But if you find yourself
   using your computer frequently enough, it is more than worthwhile in
   the long run. Any tool you use often deserves the time spent learning
   to master it."

..

   (Extract from Emacs’ eshell documentation)

-  `The Linux Command Line <http://linuxcommand.org/tlcl.php>`__ by
   Williams Shotts.
-  `Openclassrooms
   MOOC <https://openclassrooms.com/courses/reprenez-le-controle-a-l-aide-de-linux>`__

Remarks:

- Under Windows, after having installed Git, you have access to ``git bash``, which provides a terminal with the bash shell and emulates many unix commands.

- Under Windows 10, Microsoft has recently made available the “Windows Subsystem for Linux”, which provides a virtual Linux system running inside Windows. (See https://itsfoss.com/install-bash-on-windows/, and https://itsfoss.com/windows-linux-kernel-wsl-2/).

-  Under MacOSX, when you open a terminal, you may be interacting withthe bash shell or the zsh shell (to know which, type ``echo $SHELL``).



Resources to learn Git
~~~~~~~~~~~~~~~~~~~~~~

To understand why you need to learn git, see :doc:`tools-for-reproducible-science`

*  Openclassrooms’ MOOC `Manage your code with Git and Github <https://openclassrooms.com/en/courses/5671626-manage-your-code-project-with-git-github>`__
*  https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners
*  https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
*  The `Git Book <https://git-scm.com/book/en/v2>`__
*  My own `git cheat page <http://www.pallier.org/version-control-at-your-fingertips-a-quick-start-with-git.html#version-control-at-your-fingertips-a-quick-start-with-git>`__




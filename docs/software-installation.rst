.. _install:

*********************
Software Installation
*********************


.. contents::


These instructions explain how to install  *Anaconda Python 3*, *Expyriment*, *Git*, a text editor, *R* and *R Studio*.

Warnings:

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


SublimeText code editor
-----------------------

A code editor is a program that allows you to edit pure text files such
as Python programs, `Markdown <https://daringfireball.net/projects/markdown/>`__  or `LaTeX <https://www.latex-project.org/>`__ documents, ...

Unless you already use an editor that you are happy with, we
recommend that you download and install `Sublime Text <https://www.sublimetext.com/>`__. Follow the instructions specific to your Operating System.

If you prefer opensource software, you can try `Atom <http://atom.io>`__, but be
aware that it is slower and more buggy than Sublime Text.


Anaconda Python3 distribution
-----------------------------

There exists various Python distributions. Among them, we recommend the `Anaconda3 distribution <https://www.anaconda.com/distribution>`__ as it already contains most of the packages needed for the lectures.

1. Go to  <https://www.anaconda.com/products/individual> and  click on ``Download``. Then, select the 64-bit installer for your operating system (Windows, MacOS or Linux).
2. Execute the Anaconda3 installer. During the installation. 
    * If you are on a Mac, you can accept all the default for the proposed options.
    * If you are under Windows, pay close attention to the following options:

       -  verify that you Install for ``Just Me (recommended)``, then click on ``Next``
       -  Accept the default Destination folder and click on ``Next``
       -  VERY IMPORTANT: Check the boxes in front ``Add Anaconda to my PATH`` (ignore the warning that this is not recommended) and ``Register Anaconda as my default Python`` and click on ``Install``
       -  upon completion, click on ``Next``, then ``Finish``



The Git version control system
------------------------------

Git is a version control tool for software development, an indispensable
tool to do reproducible science.

Linux
   execute the command ``sudo apt install git``

MacOSX
   Download and install `Xcode <https://developer.apple.com/xcode/>`__, which provides ``git``, either from the App store, or by using the command line ``xcode-select --install``.

Windows
   Download the 64 bit version of `Git for Windows <https://git-scm.com/download/win>`__ and
   launch it.

   1. When the GNU Licence is displayed, press ``Next``;
   2. Accept the default installation folder and press ``Next``;
   3. Accept all the Components selected by default and press ``Next``
   4. Accept the creation of a start menu folder named 'Git': press ``Next``;
   5. VERY IMPORTANT: When proposed a default editor, select 'Use the nano editor' (unless you want to learn Vim) 
   6. VERY IMPORTANT: When proposed to adjust the PATH environment variable,  tick the box "Use Git and optional unix tools from the command line prompt". 

   You can accept all other defaults.  (Note: if you are hesitant, check the graphical instructions provided at https://hackernoon.com/install-git-on-windows-9acf2a1944f0)

Open a Terminal window, following the instructions specific to your operating system:

Windows
    Launch ``Git bash`` (use the "Search box")

MacOS
   Type ``terminal`` in the Spotlight search field (Or, open a ``Finder`` window, select the
   ``Application`` folder, then the ``Utilities`` folder, then double-click on the ``Terminal`` icon)

Linux
   launch ``Terminal`` from your applications menu (or use ``Ctrl-Alt-T``).


Then, type the following command lines, making sure to replace ``your_first_and_last_name_here``  and ``your_email_here`` by the relevant personal information::

    git config --global user.name "your_first_and_last_names_here" 
    git config --global user.email your_email_here 
    git config --global core.editor nano


You can exit the Terminal by typing `Ctrl-D`, or `exit`, or just closing its window.



The Pygame and Expyriment python modules
----------------------------------------

We will rely on the `Pygame module <https://www.pygame.org>`__ to create stimuli and the `Expyriment Python Library <http://www.expyriment.org>`__  to program behavorial experiments.

First you need to install the modules [#f1]_:

Linux
    Open a Terminal (``Ctrl-Alt-T``) and type ``pip install expyriment[all]``

Windows
    Starts **Git bash**. This opens a terminal, where you can type ``pip install expyriment[all]``

MacOS
    1. Install `XQuartz <https://www.xquartz.org/>`__. Download the .dmg from the official website and open it to install.

    2. Open a Terminal and type ``pip install expyriment[all]``

    3. In the same Terminal, type ``pip install -U pygame``

       This upgrade the version of pygame (1.9) installed along expyriment to pygame (2.0), which is required by recent versions of macOS. (As of 2021-02-23.)


Whetever your operating systems, you now need to test your installation:

1. run this command in a terminal to test ``pygame``::

      python -m pygame.examples.aliens

   You should see a window with moving spaceships.

2. To test ``expyriment``, type the following in the terminal::

          python

     Then, at the the prompt ``>>>``, type the following lines::

         import expyriment
         expyriment.control.run_test_suite()

       You should see a screen with ``Test suite``. There are various tests that you can run. Pressing ``Esc`` will stop the program.

Finally, in the terminal running ``python``, at the ``>>>`` prompt, press ``Ctrl-D``  then ``y``. You are out of python and you can type ``exit`` to close the terminal.



The R statistical software
--------------------------

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
---------------

Rstudio is an *Integrated Developpement Environment* for R which greatly
simplifies the use of RMarkdown. You can download and install the
latest version of **RStudio Desktop** from https://www.rstudio.com/products/rstudio/download/. Make sure to select
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

Other resources to learn more about how to control your computer from a terminal:

     - Learning the Shell  http://linuxcommand.org/lc3_learning_the_shell.php
     - OpenClassRoom : https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/37813-la-console-ca-se-mange

     

Download course materials
-------------------------

This document is available in pdf format at https://pcbs.readthedocs.io/_/downloads/en/latest/pdf/

Once Git is installed  on your computer, you can download the
course materials (python scripts, data files, ...) from http://github.com/chrplr/PCBS) with the command::

       git clone https://github.com/chrplr/PCBS.git

Everything will be downloaded in a subfolder  ``PCBS`` inside the current working directory .

Be aware that if a folder with that name already exists, git will stop and not download the content of the website. In that case, delete or move the existing PCBS folder before running the ``git clone`` command above.

I do often update the materials. To synchronize your local copy with the
latest version at http://github.com/chrplr/PCBS), you just need to open a terminal and type::

      cd PCBS
      git pull


Important: do not manually modify or create new files in the PCBS folder.
If you do so, git will notice it and might prevent an automatic upgrade
and ask you to ‘resolve conflicts’. If you get such a message, the
simplest course of action, for beginners, is to delete the PCBS folder (or
move it if you wnat to keep a copy of your modifications) and reissue the
``git clone`` command above to reload the full folder.


 
.. [#f1] (advanced students only). To avoid potential clashes betwen modules, it is a good idea to create a conda environment before installing the modules: 

          .. code::

                  conda create --name pcbs
                  conda activate pcbs
   
          But then, you must not forget to activate the environment (``conda activate pcbs``) before working on the materials presented here.

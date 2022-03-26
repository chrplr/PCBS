.. _install:

*********************
Software Installation
*********************

We explain below how to install a code editor (*sublime text*), a version control system (*git*), the statistical programming language *R* and the associated integrated development environement (*R Studio*), the *Anaconda3 Python* distribution and the *Expyriment* python module. (In addition, we provide a link to instructions on how to install the *Psychtoolbox* and *Psychopy* experiment generators, an optional step as this book does not rely on these modules). 


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
as Python programs, `Markdown <https://daringfireball.net/projects/markdown/>`__  or `LaTeX <https://www.latex-project.org/>`__ documents, etc.

Unless you already master a code editor,  we recommend that you download and install `Sublime Text <https://www.sublimetext.com/>`__. Follow the instructions specific to your Operating System.

[Note: If you prefer to stick to opensource software, you can try `Atom <http://atom.io>`__, but be
aware that it is slower and more buggy than Sublime Text.]


The Git version control system
------------------------------

Git is a version control tool for software development, an indispensable
tool to do reproducible science. To install it:

Linux
   execute the command ``sudo apt install git``

MacOSX
   Download and install `Xcode <https://developer.apple.com/xcode/>`__, either from the App store, or by using the command line ``xcode-select --install``. This will provide git.

Windows
   Download the 64 bit version of `Git for Windows <https://git-scm.com/download/win>`__ and
   launch it.

   1. When the GNU Licence is displayed, press ``Next``;
   2. Accept the default installation folder and press ``Next``;
   3. Accept all the Components selected by default and press ``Next``
   4. Accept the creation of a start menu folder named 'Git': press ``Next``;
   5. VERY IMPORTANT: When proposed a default editor, select 'Use the nano editor' (unless you want to learn Vim) 
   6. VERY IMPORTANT: When proposed to adjust the PATH environment variable,  tick the box "Use Git and optional unix tools from the command line prompt". 

   You can accept all other defaults.  

Now, to finish the installation of git, open a Terminal window (see `survival`_) and type the following command lines, making sure to replace ``your_first_and_last_name_here``  and ``your_email_here`` by the relevant personal information::

    git config --global user.name "your_first_and_last_names_here" 
    git config --global user.email your_email_here 
    git config --global core.editor nano


You can then close the Terminal window by typing the command `exit` or, faster, by pressing `Ctrl-D`, or by just closing its window.



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
latest version of **RStudio Desktop** from https://www.rstudio.com/products/rstudio/download/.
Make sure to select the correct Operating System!


Anaconda Python3 distribution
-----------------------------

There exists various Python distributions. Among them, we highly recommend the `Anaconda3 distribution <https://www.anaconda.com/distribution>`_ as it already contains most of the packages needed for cognitive science.

1. Go to  <https://www.anaconda.com/products/individual> and  click on ``Download``. Then, select the 64-bit installer for your operating system (Windows, MacOS or Linux).
2. Execute the Anaconda3 installer. During the installation. 
    * If you are on a Mac, you can accept all the default for the proposed options.
    * If you are under Windows, pay close attention to the following options:

       -  verify that you Install for ``Just Me (recommended)``, then click on ``Next``
       -  Accept the default Destination folder and click on ``Next``
       -  VERY IMPORTANT: Check the boxes in front ``Add Anaconda to my PATH`` (ignore the warning that this is not recommended) and ``Register Anaconda as my default Python`` and click on ``Install``
       -  upon completion, click on ``Next``, then ``Finish``



The Pygame and Expyriment python modules
----------------------------------------

We will rely on the `Pygame module <https://www.pygame.org>`__ to create stimuli and the `Expyriment Python Library <http://www.expyriment.org>`__  to program behavorial experiments [#f1]_.

Linux
    Open a Terminal (``Ctrl-Alt-T``) and type::

        sudo apt-get install build-essential libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
        pip install expyriment[all]

Windows
    Launch the program ``Git bash`` and enter the command ``pip install expyriment[all]`` on the command line (see `survival`_).


MacOS
    1. Install `XQuartz <https://www.xquartz.org/>`__. Download the .dmg from the official website and open it to install.

    2. Open a Terminal and type ``/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`` to install `Homebrew <https://brew.sh/>`__ (which is needed to install SDL).

            - If you see "Password: ", this means the Terminal is prompting you to type your computer's administrator account password. Type your password and press the return key to continue.
            - If you see an error message such as "Error: /usr/local/Cellar is not writable. You should change the ownership and permissions of /usr/local/Cellar back to your user account: sudo chown -R $(whoami) /usr/local/Cellar", run in the Terminal the command that was suggested (here ``sudo chown -R $(whoami) /usr/local/Cellar``), and then run the previous command to try installing Homebrew once again

    3. In the same Terminal, type ``brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config`` to install SDL (which is needed to install expyriment). This may take a while.

    4. In the same Terminal, type ``pip install "expyriment[all]"`` to install expyriment.

    5. In the same Terminal, type ``pip install -U pygame`` to upgrade pygame (version >= 2.0 is required on recent versions of macOS, but this must be done *after* installing expyriment otherwise the install of expyriment will fail).

Install Psychopy and Psychtoolbox on Linux (optional)
-----------------------------------------------------

If you want to install the [Psychtoolbox](http://psychtoolbox.org/) and [Psychopy](https://www.psychopy.org) experiments generators (which are not needed in this course), you can find instructions for Linux at https://gist.github.com/chrplr/61ec2de7f0e001ebf65aec89e6f6ddc9 (For Windows or MacOSX instructions, follow the instructions on the psychtoolbox and the psychopy websites).


Check your installation
-----------------------

Test Python
~~~~~~~~~~~

Watch the video at   https://www.youtube.com/watch?v=2yhcWvBt7ZE&t and try to reproduce the activities.

Remarks:
- if you have a Mac or Linux, the only difference is how to open a terminal. Check `survival`_ for help on this.
- The ``games.zip`` file mentioned in the video is available at https://github.com/chrplr/PCBS/tree/master/games/games.zip


Download the course material
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open a Terminal (see `survival`_) and enter the following command line: 

.. code-block:: bash

    git clone https://github.com/chrplr/PCBS.git

This should download all the course materials (python scripts, data files, ...) in a subfolder  ``PCBS`` inside your home directory (If a folder named ``PCBS`` already exists in the current working directory, git will stop and not download the content of the website. In that case, you must delete or move the existing PCBS folder before running the ``git clone`` command above).

You should be able to move inside the PCBS directory and list its content: 

.. code-block:: bash

    cd PCBS
    ls

If you get any error messages, check  `Navigating the file system <http://linuxcommand.sourceforge.net/lc3_lts0020.php>`_ to understand how to set the correct current working directory.

.. code-block:: bash

    cd games
    python human-guess-a-number.py          

This should play a guessing game with you.

.. image:: images/guess-number.png

Test pygame
~~~~~~~~~~~

.. code-block:: bash

   cd ~/PCBS/stimuli/visual-illusions/
   python kanizsa_triangle.py

This should open a window displaying the Kanizsa triangle.

.. image:: images/ktri.png

Test expyriment
~~~~~~~~~~~~~~~

.. code-block:: bash

   cd ~/PCBS/experiments/expyriment/parity_decision
   python parity_feedback.py

This should run an experiment where you have to judge the parity of digits.

.. class:: center

   **If everything works, you are done !**


Annexes
-------


Keep your local copy of the course material up to date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The course materials are often updated. To make sure you have the latest version, you can synchronize your local copy with the github repository http://github.com/chrplr/PCBS, with the commands:

.. code-block:: bash

      cd ~/PCBS
      git pull

Notes:
- if the PCBS iis not in your home directory (``~``), you will need to use the appropriate path in the first cd command.
- do not manually modify or create new files in the ``PCBS`` folder.
If you do so, git will notice it and might prevent an automatic upgrade
and ask you to ‘resolve conflicts’. If you get such a message, the
simplest course of action, for beginners, is to delete the PCBS folder (or
move it if you wnat to keep a copy of your modifications) and reissue the
``git clone`` command above to reload the full folder.)


Potential issues
~~~~~~~~~~~~~~~~

    - ``python: command not found``: the folder containing anaconda3's python is missing (or shadowed) from the PATH environment variable that lists all the folders where commands can be located. It is very likely that you did not follow exactly the above installation instructions for either Anaconda3 or Git Bash (Windows only), that is, you did not check the correct options. If you know how to do it, modify the PATH environment variable, else reinstall.  

    - ``expyriment or pygame : module not found``. There are many potential causes for that one. Check that you followed the instructions precisely and contat us on the #general channel of the Slask forum.


    - If you see error messages (in red) when importing the expyriment module, it is likely due to issues with the version of Python. If this is the case (and only if this is the case), you should create an [Anaconda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) as follows:

    .. code-block:: bash

       conda create --name expyriment python=3.8
       conda activate expyriment
       pip install expyriment[all]

Then, to run python scripts using the expyriment module, you will need to activate this environment with the command::

        conda activate expyriment

  Read more about Python Anaconda environments [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).


Creating a conda environment
----------------------------
 
.. [#f1] (advanced students only). To avoid potential clashes betwen modules, it may be a good idea to create a conda environment before installing the modules: 

          .. code:: bash

                  conda create --name pcbs
                  conda activate pcbs
   
          But then, you must not forget to activate the environment (``conda activate pcbs``) before working on the materials presented here.


.. _survival:

Basic surviving skill: how to enter command lines in a Terminal
---------------------------------------------------------------

If you do not already have an open Terminal window, you need to open one:

Linux
   Launch ``Terminal`` from your application menu or use
   ``Ctrl-Alt-T`` (gnome, xfce) or ``Win+Return`` (i3).

MacOS
   Type ``terminal`` in the Spotlight search field.
   Alternatively, you can open a ``Finder`` window and select the
   ``Application`` folder, then the ``Utilities`` folder, then
   double-click on the ``Terminal`` icon..

Windows
   Start ``Git Bash`` (This assumes that you have installed
   ``Git for windows`` as described above)

   1. Click the Windows or Start icon.
   2. In the Programs list, open the Git folder.
   3. Click the option for Git Bash.


Inside the terminal, you interact with a program --- the `shell <http://linuxcommand.sourceforge.net/lc3_learning_the_shell.php>`_ --- that prints a prompt (typically a dollar sign) and shows a blinking cursor, expecting *you* to type a command and press the ``Return`` key. Then, it will (try to)  execute the command.

For the moment, you mostly need to know the following three commands:

-  ``ls``: list the content of the current working directory
-  ``pwd``: path of current working directory
-  ``cd``: change directory

Read about them in http://linuxcommand.sourceforge.net/lc3_lts0020.php

Here are some resources to learn more about how to control your computer from a terminal:

     - Learning the Shell  http://linuxcommand.org/lc3_learning_the_shell.php
     - OpenClassRoom : https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/37813-la-console-ca-se-mange




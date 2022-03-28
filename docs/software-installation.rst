.. _install:


*********************
Software Installation
*********************

We explain below how to install:

- a code editor: *Sublime text*
- a version control system: *Git*
- the statistical programming language: *R*
- its integrated development environment: *R Studio*
- Python and several useful modules, including *Expyriment*,
- the *Psychtoolbox-3* for vision and neural sciences. 

Warnings:

-  You will need to download several GB of software from the Internet.
   Therefore, make sure to have a decent connection.
-  Make sure that you have at least 5GB of free space on your hard drive
   to unpack the various software.
-  You will need to have administrator rights to install some of the
   softwares. If you are using a computer from an institution, check with the IT support team.



Instructions for Windows (WSL)
------------------------------

This is the recommended method in terms of simplicity. 

You are going to install Ubuntu Linux on your Windows system, using the *Windows
Subsystem for Linux* (aka WSL). The instructions are detailed `here
<https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps>`_. In a
nutshell, you have to

#. Install the vGPU drivers for your graphics card (Intel, AMD or Nvidia) [1]_.  
#. Launch “Windows PowerShell” as administrator, and execute the command::

        wsl --install -d ubuntu


This downloads the full Ubuntu linux which may take a while. At some point
during the install, a new Terminal window titled “Ubuntu” will open and will ask
for a user name and password. You can put anything but it is crucial that you
note down the password as it will be needed to install software under Ubuntu.

Once the installation is finished, open the “Ubuntu” App and follow the
instructions for Linux below.

Instructions for Windows (Native, without WSL)
----------------------------------------------

This is not recommended unless WSL does not work on your machine, or if you want to get the best timing perfromance from your hardware. The 


R and Rstudio
~~~~~~~~~~~~~

R is a programming language specialized for statistical data analyses.

Download and install the latest version of R from https://cran.rstudio.com/bin/windows/base/

Rstudio is an *Integrated Developpement Environment* for R which greatly
simplifies the use of RMarkdown. You can download and install the
latest version of RStudio Desktop from https://www.rstudio.com/products/rstudio/download/.



SublimeText code editor
~~~~~~~~~~~~~~~~~~~~~~~

Download and install `Sublime Text <https://www.sublimetext.com/>`__.

[Note: If you prefer to stick to opensource software, you can try `Atom <http://atom.io>`__, but be
aware that it is slower and more buggy than Sublime Text.]


Anaconda Python3 distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There exists various Python distributions. Under Windows, we recommend the `Anaconda3 distribution <https://www.anaconda.com/distribution>`__ as it already contains most of the packages needed for cognitive science.

1. Go to  <https://www.anaconda.com/products/individual>, click on ``Download`` and select the 64-bit installer for iWindows. 
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

Download the 64 bit version of `Git for Windows <https://git-scm.com/download/win>`__ and launch it.

   1. When the GNU Licence is displayed, press ``Next``;
   2. Accept the default installation folder and press ``Next``;
   3. Accept all the Components selected by default and press ``Next``
   4. Accept the creation of a start menu folder named 'Git': press ``Next``;
   5. VERY IMPORTANT: When proposed a default editor, select 'Use the nano editor' (unless you want to learn Vim) 
   6. VERY IMPORTANT: When proposed to adjust the PATH environment variable,  tick the box "Use Git and optional unix tools from the command line prompt". 

   You can accept all other defaults.  

Now, to finish the installation of git, start ``Git bash`` (use the "Search box")

Then, type the following command lines, making sure to replace ``your_first_and_last_name_here``  and ``your_email_here`` by the relevant personal information::

    git config --global user.name "your_first_and_last_names_here" 
    git config --global user.email your_email_here 
    git config --global core.editor nano


You can close the Terminal by typing the command `exit` or, faster, by pressing `Ctrl-D`, or by just closing its window.



The Pygame and Expyriment python modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will rely on the `Pygame module <https://www.pygame.org>`__ to create stimuli and the `Expyriment Python Library <http://www.expyriment.org>`__  to program behavorial experiments.

Start **Git bash** and, in the openned Terminal, type::

   pip install expyriment[all]

Learn to use Sublime Text and Git Bash Terminal to create Python scripts 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Watch the video at   https://www.youtube.com/watch?v=2yhcWvBt7ZE&t and try to perform the activities in it (the insturctions walso work for Mac or Linux: you just need to open a standard Terminal when in Windows you need to start 'Gih Bash'). Note: the game scripts mentioned in the video are available at https://github.com/chrplr/PCBS/tree/master/games/games.zip




Instructions for Linux (Ubuntu 20.04)
-------------------------------------

Open a Terminal [2]_.


Then, for each software section below, copy and paste in the terminal the lines
that are in the boxes and press ``Enter`` to execute them.

Python3
~~~~~~~

`Python <https://www.python.org/>`_ is the main programming language used in
these courses. The following commands install various modules that will be
needed.

.. code-block:: bash

    sudo apt install -y python3 ipython3 python3-dev python-is-python3 python3-future \
              python3-opengl python3-pip python3-ipython python3-pygame python3-numpy \
              python3-matplotlib python3-skimage python3-pandas python3-scipy \
              python3-imageio python3-ipython

    sudo pip install expyriment[all]

    sudo apt-get install -y python3-dev libasound2-dev
    sudo pip install simpleaudio


Git
~~~

`Git <https://git-scm.com/>`_ is a free distributed version control system.

.. code-block:: bash

   sudo apt install git

Now, type the following command lines, making sure to replace
``your_first_and_last_name_here`` and ``your_email_here`` by the relevant
personal information:

.. code-block:: bash

  git config --global user.name "your_first_and_last_names_here" 
  git config --global user.email your_email_here 
  git config --global core.editor nano


Sublime code editor
~~~~~~~~~~~~~~~~~~~

`Sublime Text <https://www.sublimetext.com/>`_ is a powerful text editor with a good Python mode. 

.. code-block:: bash

  wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
  sudo apt-get install apt-transport-https
  echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
  sudo apt-get update
  sudo apt-get install sublime-text

(from https://www.sublimetext.com/docs/linux_repositories.html)


R language for statistics
~~~~~~~~~~~~~~~~~~~~~~~~~

`R <https://www.r-project.org/>`_ is a free software environment for statistical computing and graphics.

.. code-block:: bash

  sudo apt update -qq
  sudo apt install --no-install-recommends software-properties-common dirmngr
  wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
  sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
  sudo apt install --no-install-recommends r-base
  sudo add-apt-repository ppa:c2d4u.team/c2d4u4.0+

(from https://cran.rstudio.com/bin/linux/ubuntu/)


Rstudio Desktop
~~~~~~~~~~~~~~~

Rstudio is an *Integrated Developpement Environment* for R which greatly
simplifies the use of RMarkdown. You can download and install the latest version
of **RStudio Desktop** from https://www.rstudio.com/products/rstudio/download/.
Make sure to select the ubuntu version!

.. code-block:: bash

  wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-2022.02.1-461-amd64.deb
  sudo apt install ./rstudio-2022.02.1-461-amd64.deb


Psychtoolbox
~~~~~~~~~~~~

`Psychtoolbox-3 <http://psychtoolbox.org/>`_ is a set Octave functions which is
very popular in vision and neuroscience research. This installation is optional
as the Psychtoolbox is **not used** in this book.


.. code-block:: bash

    ## Add Neurodebian repository 
    ## Select the neurodebian repository on  [Neurodebian](https://neuro.debian.net/), and copy the command lines, e.g.:

    wget -O- http://neuro.debian.net/lists/focal.de-m.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
    sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9

    ## activate sources and install  required packages

    sudo sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list
    sudo apt update

    sudo apt build-dep octave-psychtoolbox-3
    sudo apt install subversion libdc1394-22-dev libfreenect* libgstreamer1.0-dev libgstreamer-plugins-*

    ## download psychtoolbox

    wget https://raw.github.com/Psychtoolbox-3/Psychtoolbox-3/master/Psychtoolbox/DownloadPsychtoolbox.m.zip
    unzip DownloadPsychtoolbox.m.zip 

    mkdir ~/PTB3

Now, start ``octave`` on the command line and type::

      DownloadPsychtoolbox('/home/neurostim/PTB3')
      PsychLinuxConfiguration()

      # test 
      DrawingSpeedTest()


Instructions for MacOS X
------------------------


SublimeText code editor
~~~~~~~~~~~~~~~~~~~~~~~

A code editor is a program that allows you to edit pure text files such
as Python programs, `Markdown <https://daringfireball.net/projects/markdown/>`__  or `LaTeX <https://www.latex-project.org/>`__ documents, etc.

Unless you already master a code editor,  we recommend that you download and install `Sublime Text <https://www.sublimetext.com/>`__. Follow the instructions specific to MacOS.



The Git version control system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Download and install `Xcode <https://developer.apple.com/xcode/>`__, either from the App store, or by using the command line ``xcode-select --install``. This will provide git.


To finish the installation of git, open a Terminal window (see `survival`_) and type the following command lines, making sure to replace ``your_first_and_last_name_here``  and ``your_email_here`` by the relevant personal information::

    git config --global user.name "your_first_and_last_names_here" 
    git config --global user.email your_email_here 
    git config --global core.editor nano


The R statistical software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and install the latest version of **R** from https://cran.rstudio.com/bin/macosx/


Rstudio Desktop
~~~~~~~~~~~~~~~

Download and install the latest version of **RStudio Desktop** from https://www.rstudio.com/products/rstudio/download/. Make sure to select the MacOS version!

Python
~~~~~~

Download and install **Anaconda3 Python** from https://www.anaconda.com/products/individual
 


The Pygame and Expyriment python modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


 1. Install `XQuartz <https://www.xquartz.org/>`__. Download the ``.dmg`` file from the official website and open it to install.

 2. Open a Terminal and type ``/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`` to install `Homebrew <https://brew.sh/>`__ (which is needed to install SDL).

            - If you see "Password: ", this means the Terminal is prompting you to type your computer's administrator account password. Type your password and press the return key to continue.
            - If you see an error message such as "Error: /usr/local/Cellar is not writable. You should change the ownership and permissions of /usr/local/Cellar back to your user account: sudo chown -R $(whoami) /usr/local/Cellar", run in the Terminal the command that was suggested (here ``sudo chown -R $(whoami) /usr/local/Cellar``), and then run the previous command to try installing Homebrew once again

  3. In the same Terminal, type ``brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf pkg-config`` to install SDL (which is needed to install expyriment). This may take a while.

  4. In the same Terminal, type ``pip install "expyriment[all]"`` to install expyriment.

  5. In the same Terminal, type ``pip install -U pygame`` to upgrade pygame (version >= 2.0 is required on recent versions of macOS, but this must be done *after* installing expyriment otherwise the install of expyriment will fail).


Check that everything works
---------------------------

Test Git
~~~~~~~~

To download the course materials using Git, enter the following command line in a Terminal:: 

    git clone https://github.com/chrplr/PCBS.git

This should download all the course materials (python scripts, data files, ...) in a directory  ``PCBS`` inside your home directory (If a folder named ``PCBS`` already exists in the current working directory, git will stop and not download the content of the website. In that case, you must delete or move the existing PCBS folder before running the ``git clone`` command above).

You can move inside the PCBS directory and list its content: 

.. code-block:: bash

    cd PCBS
    ls
    
If you get any error messages, check  `Navigating the file system <http://linuxcommand.sourceforge.net/lc3_lts0020.php>`_ to understand how to set the correct current working directory.


Test Python
~~~~~~~~~~~

.. code-block:: bash

    cd ~/PCBS/games
    python human-guess-a-number.py          

This should play a guessing game with you.

.. image:: images/guess-number.png

Test matplotlib
~~~~~~~~~~~~~~~

.. code-block::

    cd ~/PCBS/stimuli/visual

    python bullseye.py
    python contrast_modulated_grating.py
    python gabor.py
    python image-manipulation.py
    python wedgering.py



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

Sublime Text
~~~~~~~~~~~~

.. code-block:: bash

   subl


This should open the sublime text editor. If you get a message ``command not found``, ask the instructor to fix your path.

Then, check out https://www.youtube.com/watch?v=SVkR1ZkNusI for a short tutorial.

Annexes
-------


Keep your local copy of the course material up to date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The course materials are often updated. To make sure you have the latest version, you can synchronize your local copy with the github repository http://github.com/chrplr/PCBS, with the commands:

.. code-block:: bash

      cd ~/PCBS
      git pull

Notes:

- if the PCBS directory is not in your home directory (``~``), you will need to use the appropriate path in the first cd command.
- do not manually modify or create new files in the ``PCBS`` folder.
  If you do so, git will notice it and might prevent an automatic upgrade
  and ask you to ‘resolve conflicts’. If you get such a message, the
  simplest course of action, for beginners, is to delete the PCBS folder (or
  move it if you wnat to keep a copy of your modifications) and reissue the
  ``git clone`` command above to reload the full folder.)


.. _survival:


Basic surviving skill: how to enter command lines in a Terminal
---------------------------------------------------------------

Inside the terminal, you interact with a program --- the `shell <http://linuxcommand.sourceforge.net/lc3_learning_the_shell.php>`_ --- that prints a prompt (typically a dollar sign) and shows a blinking cursor, expecting *you* to type a command and press the ``Return`` key. Then, it will (try to)  execute the command.

For the moment, you mostly need to know the following three commands:

-  ``ls``: list the content of the current working directory
-  ``pwd``: path of current working directory
-  ``cd``: change directory

Read about them in http://linuxcommand.sourceforge.net/lc3_lts0020.php

Here are some resources to learn more about how to control your computer from a terminal:

     - Learning the Shell  http://linuxcommand.org/lc3_learning_the_shell.php
     - OpenClassRoom : https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/37813-la-console-ca-se-mange



------------

.. [1] To determine which type of GPU (Intel, AMD, Nvidia) is installed on your computer, under Windows, open the *Task Manager*, e.g. with ``Ctrl-Alt-Del``, and search for GPU under the *Performance* tab.

.. [2] To open a Terminal:

        - Windows with the WSL: launch the “Ubuntu” app.
        - Windows with Git for Windows: launch “Git bash”.
        - Linux: Launch ``Terminal`` or press ``Ctrl-Alt-T`` (Gnome or Xfce) or ``Win-Return`` (i3).
        - MacOS: Type ``terminal`` in the Spotlight search field.
          Alternatively, you can open a ``Finder`` window and select the
          ``Application`` folder, then the ``Utilities`` folder, then
          double-click on the ``Terminal`` icon..


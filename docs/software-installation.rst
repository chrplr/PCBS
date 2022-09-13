.. _install:


*********************
Software Installation
*********************

We explain below how to install:

- a code editor: *Sublime text*
- a version control system: *Git*
- the statistical programming language: *R*
- its integrated development environment: *RStudio*
- Python and several useful modules, including *Expyriment*,
- the *Psychtoolbox-3* for vision and neural sciences. 

After the installation, `check`_ that everything works. 

.. warning::
   -  You will need to download several GB of software from the Internet.
      Therefore, make sure to have a decent connection.
   -  Make sure that you have at least 5GB of free space on your hard drive
      to unpack the various software.
   - You will need to have administrator rights to install some of the
     software. If you are using a computer from an institution, check with the IT support team.


.. contents:: :depth: 2



Instructions for Windows (with WSL)
-----------------------------------

If the *Windows Subsystem for Linux* (aka WSL) is installed on your Windows PC, with an Ubuntu Linux distribution, you can open Ubuntu and jump to the linux_ section in order to install the required software.

If you want to install Linux under Windows using the WSL, follow the instructions at https://docs.microsoft.com/en-us/windows/wsl/install but be aware that thre download is large (several GB) and the installation can be lengthy (30min-1h) 

Here is an overview of the process:


- If you have Windows 11:

  #. Install the vGPU driver for your graphics card (`Intel
     <https://www.intel.com/content/www/us/en/download/19344/intel-graphics-windows-dch-drivers.html?>`__,
     `AMD <https://www.amd.com/en/support/kb/release-notes/rn-rad-win-wsl-support>`__
     or `Nvidia <https://developer.nvidia.com/cuda/wsl>`__) [2]_ if it not already
     installed.
  #. Launch “Windows PowerShell” as administrator, and execute
     the command::

       wsl --install -d ubuntu

- If you have Windows 10, follow `these instructions <https://omgubuntu.co.uk/how-to-install-wsl2-on-windows-10>`__.
  (You may have to enable `Hyper-V <https://www.zdnet.com/article/windows-10-tip-find-out-if-your-pc-can-run-hyper-v/>`__)

This downloads the full Ubuntu Linux distribution which may take a while. Some versions of Windows may even ask you to reboot during the installation process. At some point during the install, a new Terminal window entitled “Ubuntu” will open and will require a new user name and password. You can type anything but it is crucial that you note down the password as it will be needed to install software under Ubuntu.


.. note::
  If anything goes wrong during the installation check the `Troubleshoting WSL <https://docs.microsoft.com/en-us/windows/wsl/troubleshooting>`__ section. 


When the WSL installation is finished, go to the linux_ section in order to install the required software.


Instructions for native Windows (without WSL)
---------------------------------------------

This approach has several pitfalls. For example, if  you do not carefully follow the instructions, many things will not work correclty. Yet, there are two reasons why one may want to follow this path:

- WSL does not work on your machine (for example, your CPU does not allow `virtualization <https://www.zdnet.com/article/windows-10-tip-find-out-if-your-pc-can-run-hyper-v/>`__). 
- You are concerned by potential overheads of the WSL (yet, read `this <https://www.techradar.com/news/windows-11-wsl-2-is-almost-as-quick-as-running-linux-natively>`__).


R and Rstudio
~~~~~~~~~~~~~

R is a programming language specialized for statistical data analyses; Download and install it from https://cran.rstudio.com/bin/windows/base/ (accepting all the default options proposed by the installer)


Rstudio is an *Integrated Developpement Environment* for R which greatly
simplifies the use of RMarkdown. You can download and install the
free version of RStudio Desktop from https://www.rstudio.com/products/rstudio/download/ (accepting all the default options)

Lauch RStudio, go to the  "Tools" menu, select "install packages" and in the dialog window that opens, in the  'packages' box, type::

     tidyverse lme4 ez


This will take a while to download packages from the internet and install them. Do not close rstudio until the process is finished (no more scrolling messages in the console).


SublimeText code editor
~~~~~~~~~~~~~~~~~~~~~~~

Download and install `Sublime Text <https://www.sublimetext.com/>`__. (accepting the default options proposed by the installer)


Anaconda Python3 distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There exists various Python distributions. Under Windows, we recommend the `Anaconda3 distribution <https://www.anaconda.com/distribution>`__ as it already contains many of the packages needed for cognitive science (but it is very large. If you you lack disk space, you can install `miniconda <docs.conda.io/en/latest/miniconda.html>`__, but later you will need to install many python packages manually)

1. Go to  <https://www.anaconda.com/products/individual>, click on ``Download`` and select the 64-bit installer for iWindows.
2. Execute the Anaconda3 installer. Pay special attention to the options:

       -  To the question 'Install for', select ``Just Me (recommended)``
       -  Accept the default Destination folder and click on ``Next``
       -  VERY IMPORTANT: Check the boxes in front ``Add Anaconda to my PATH`` (ignore the warning that this is not recommended) and ``Register Anaconda as my default Python`` and click on ``Install``
       -  upon completion, click on ``Next``, then ``Finish``

 
	  

The Git version control system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git is a version control tool for software development, an indispensable
tool to do reproducible science.

IMPORTANT: you must wait for the installation of Anaconda to finish *before* trying to install Git.

Download the installer of `Git for Windows <https://git-scm.com/download/win>`__ and launch it.

   1. When the GNU Licence is displayed, press ``Next``;
   2. Accept the default installation folder and press ``Next``;
   3. Accept all the Components selected by default and press ``Next``
   4. Accept the creation of a start menu folder named 'Git': press ``Next``;
   5. VERY IMPORTANT: When proposed a default editor, select 'Use the nano editor' (unless you want to learn Vim) 
   6. VERY IMPORTANT: When proposed to adjust the PATH environment variable,  tick the box "Use Git and optional unix tools from the command line prompt". 

   You can accept all other defaults.  

Now, to finish the installation of git, launch ``Git bash`` (use the "Search box").


Start Git Bash again, and type the following commands, making sure to replace ``your_first_and_last_name_here``  and ``your_email_here`` by the relevant personal information::

    git config --global user.name "your_first_and_last_names_here" 
    git config --global user.email your_email_here 
    git config --global core.editor nano


You can close Git Bash by typing the command `exit` or, faster, by pressing `Ctrl-D`, or by just closing its window.



The Pygame and Expyriment python modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will rely on the `Pygame module <https://www.pygame.org>`__ to create stimuli and the `Expyriment Python Library <http://www.expyriment.org>`__  to program behavorial experiments.

Start **Git bash** and, in the openned Terminal, type::

   conda create -n expyriment python=3.7

And press 'Return' to accept the installation.

Then, type::

   conda activate expyriment
   conda install ipython
   pip install expyriment[all]

To check the installation, type::

   ipython

and then::

   import expyriment

If a message `Experiment 0.10.0 ...` is displayed and no error message, the installation worked. Press `Ctrl-D` to quit ipython, and `Ctrl-D` again to qui Git Bash.



Learn to use Sublime Text and Git Bash Terminal to create Python scripts 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Watch the video at   https://www.youtube.com/watch?v=2yhcWvBt7ZE&t and try to perform the activities in it (the insturctions walso work for Mac or Linux: you just need to open a standard Terminal when in Windows you need to start 'Gih Bash'). Note: the game scripts mentioned in the video are available at https://github.com/chrplr/PCBS/tree/master/games/games.zip


Now you should check if everything works, following the instructions in chapter :doc:`testing-tour`.



Instructions for MacOS X
------------------------


SublimeText code editor
~~~~~~~~~~~~~~~~~~~~~~~

A code editor is a program that allows you to edit pure text files such
as Python programs, `Markdown <https://daringfireball.net/projects/markdown/>`__  or `LaTeX <https://www.latex-project.org/>`__ documents, etc.

Unless you already use a code editor that you are familiar and happy with,  we recommend that you download and install `Sublime Text <https://www.sublimetext.com/>`__. Follow the instructions specific to MacOS.


The Git version control system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and install `Xcode <https://developer.apple.com/xcode/>`__, either from the App store, or by using the command line ``xcode-select --install``. This will provide git.


To finish the installation of git, open a Terminal window [1]_ and type the following command lines, making sure to replace ``your_first_and_last_name_here``  and ``your_email_here`` by the relevant personal information::

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


Now you should check if everything works, following the instructions in chapter :doc:`testing-tour`.


.. _linux:

Instructions for Linux (Ubuntu 20.04)
-------------------------------------

Open a Terminal [1]_.


Then, for each software section below, copy and paste in the terminal the lines
that are in the boxes and press ``Enter`` to execute them.

Python3
~~~~~~~

`Python <https://www.python.org/>`_ is the main programming language used in
these courses. The following commands install various modules that will be
needed.

.. code-block:: bash

    sudo apt  install -y python3 ipython3 python3-dev python-is-python3 python3-future \
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

   sudo apt install git -y

Now, type the following command lines, making sure to replace
``your_first_and_last_name_here`` and ``your_email_here`` by the relevant
personal information:

.. code-block:: bash

  git config --global user.name "your_first_and_last_names_here" 
  git config --global user.email your_email_here 
  git config --global core.editor nano


Sublime code editor
~~~~~~~~~~~~~~~~~~~

`Sublime Text <https://www.sublimetext.com/>`_ is a powerful text editor with a good Python mode. To install it:

.. code-block:: bash
                
  wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

.. code-block:: bash

  sudo apt-get install apt-transport-https -y
  echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
  sudo apt-get update
  sudo apt-get install sublime-text -y

(if this does not work, check the latest instructions from https://www.sublimetext.com/docs/linux_repositories.html)

.. note::
   `Visual Studio Code <https://code.visualstudio.com/>`__ is another fine code editor too. If you prefer to use it instead of Sublime Text, this is perfectly fine. 

R language for statistics
~~~~~~~~~~~~~~~~~~~~~~~~~

`R <https://www.r-project.org/>`_ is a free software environment for statistical computing and graphics.

.. code-block:: bash

  sudo apt update -qq

.. code-block:: bash

  sudo apt install --no-install-recommends software-properties-common dirmngr -y
  wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
  sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
  sudo apt install --no-install-recommends r-base -y
  sudo add-apt-repository ppa:c2d4u.team/c2d4u4.0+

(in case of trouble, check the latest instructions at https://cran.rstudio.com/bin/linux/ubuntu/)


Rstudio Desktop
~~~~~~~~~~~~~~~

Rstudio is an *Integrated Developpement Environment* for R which greatly
simplifies the use of RMarkdown. You can download and install the latest version
of **RStudio Desktop** from https://www.rstudio.com/products/rstudio/download/.
Make sure to select the ubuntu version!

.. code-block:: bash

  wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-2022.02.1-461-amd64.deb
  sudo apt install ./rstudio-2022.02.1-461-amd64.deb -y


Psychtoolbox
~~~~~~~~~~~~

`Psychtoolbox-3 <http://psychtoolbox.org/>`_ is a set Octave functions which is
very popular in vision and neuroscience research. This installation is optional
as the Psychtoolbox is **not used** in this book.

First, add the [Neurodebian](https://neuro.debian.net/) repository.

.. code-block:: bash

    wget -O- http://neuro.debian.net/lists/focal.de-m.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list

.. code-block:: bash

    sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9

Then activate the sources and install the required packages::

    sudo sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list
    sudo apt update

    sudo apt build-dep octave-psychtoolbox-3 -y
    sudo apt install subversion libdc1394-22-dev libfreenect* libgstreamer1.0-dev libgstreamer-plugins-* -y

Download the psychtoolbox installation script::

    wget https://raw.github.com/Psychtoolbox-3/Psychtoolbox-3/master/Psychtoolbox/DownloadPsychtoolbox.m.zip
    unzip DownloadPsychtoolbox.m.zip 

    mkdir ~/PTB3

Finally, start ``octave`` and, on Octave's command line, type::

      DownloadPsychtoolbox('/home/neurostim/PTB3')
      PsychLinuxConfiguration()

      # test 
      DrawingSpeedTest()

Now you should check if everything works, following the instructions in chapter :doc:`testing-tour`.


------------

.. [1] To open a Terminal:

        - Windows with the WSL: launch the “Ubuntu” app.
        - Windows with Git for Windows: launch “Git bash”.
        - Linux: Launch ``Terminal`` or press ``Ctrl-Alt-T`` (Gnome or Xfce) or ``Win-Return`` (i3).
        - MacOS: Type ``terminal`` in the Spotlight search field.
          Alternatively, you can open a ``Finder`` window and select the
          ``Application`` folder, then the ``Utilities`` folder, then
          double-click on the ``Terminal`` icon..

.. [2] To determine which type of GPU (Intel, AMD, Nvidia) is installed on your computer, under Windows, open the *Task Manager*, e.g. with ``Ctrl-Alt-Del``, and search for GPU under the *Performance* tab.

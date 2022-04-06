.. _check:

**********************
Check your installation  
**********************

.. contents:: :depth: 2


Test Git
--------

Download the course materials using Git by entering the following command line in a Terminal:: 

    git clone https://github.com/chrplr/PCBS.git

You should see a message ``Cloning into 'PCBS'...`` and, if everything goes well, all
course materials (python scripts, data files, ...) should be downloaded in a new subdirectory, ``PCBS``, in the current working directory.

.. image:: images/term-git-clone-pcbs.png
  :width: 400
  :alt: Terminal showing the results of git clone...

You now can move inside the PCBS directory and list its content: 

.. code-block:: bash

    cd PCBS
    pwd
    ls


.. note::
   If a folder named ``PCBS`` already exists in the current working
   directory, git will stop and will not download the content of the remote PCBS
   repository. In that case, you must delete or move the existing ``PCBS`` folder
   before running the ``git clone`` command above.

   When you open a Terminal, the current working directory is your “home”, or
   “user”, directory, until you start navigating in the filesystem with the ``cd
   (change directory)`` command. If you are lost at this point, read `Navigating
   the file system <http://linuxcommand.sourceforge.net/lc3_lts0020.php>`_.


Test Python
-----------

This tests if Python3 is installed and correclty configured.

.. code-block:: bash

    cd ~/PCBS/games
    python human-guess-a-number.py
    python matches.py

.. image:: images/term-python-guess-a-number.png
     :width: 400


.. note::
  If you receive an error message such as ``bash: python: No such file or directory``, and you are sure that python is installed, the most likely reason is that the problems lies with the [PATH environment variable](https://linuxhint.com/path_in_bash/) listing all the directories: the directory containing the python executable may be missng from hte list. This happens for example, if one did not check the right box during Anaconda installation.  

Test basic graphics
-------------------

.. code-block:: bash

  cd ~/PCBS/simulations/fractals
  python koch0.py
  python tree.py

.. image:: images/koch.png
     :width: 600

.. image:: images/tree.png
     :width: 200


Test matplotlib
---------------

matplotlib is a python library to create and display graphics.

.. code-block:: bash

    cd ~/PCBS/stimuli/visual
    python bullseye.py
    python contrast_modulated_grating.py
    python gabor.py
    python image-manipulation.py
    python wedgering.py

.. image: images/contrast-modulated.png
     :width: 400

.. image: images/gabor.png
     :width: 400

.. image: images/image-manip.png
     :width: 400
        





Test pygame
-----------

[Pygame](http://www.pygame.org) is a Python library to create simple audio visual games.

.. code-block:: bash

   cd ~/PCBS/stimuli/visual-illusions/
   python kanizsa_triangle.py
   python hering.py
   python lilac_chaser_blurred.py


Test expyriment
---------------

[Expyriment](http://expyriment.org) is a Python library for designing and conducting behavioural and neuroimaging experiments. 

.. code-block:: bash

   cd ~/PCBS/experiments/Posner-attention
   python posner_task.py 

   cd ~/PCBS/experiments/parity_decision
   python parity_feedback.py

   cd ~/PCBS/experiments/mental_logic_card_game
   python mental_logic_card_game.py             

Note: the programs can be interrupted at any time by pressing the ``Esc`` key.



Sublime Text
------------

.. code-block:: bash

   subl


This should open a new window with the sublime text editor. If you get a message ``command not found``, ask the instructor to fix your path.

Then, check out https://www.youtube.com/watch?v=SVkR1ZkNusI for a short tutorial.

Appendices
----------


Keep your local copy of the course material up to date
------------------------------------------------------

The course materials are often updated. To make sure you have the latest version, you can synchronize your local copy with the github repository http://github.com/chrplr/PCBS, with the commands:

.. code-block:: bash

      cd ~/PCBS
      git pull

Notes:

- if the PCBS directory is not in your home directory (``-``), you will need to use the appropriate path in the first cd command.
- do not manually modify or create new files in the ``PCBS`` folder.
  If you do so, git will notice it and might prevent an automatic upgrade
  and ask you to ‘resolve conflicts’. If you get such a message, the
  simplest course of action, for beginners, is to delete the PCBS folder (or
  move it if you wnat to keep a copy of your modifications) and reissue the
  ``git clone`` command above to reload the full folder.)


.. _survival:


Basic surviving skill: how to enter command lines in a Terminal
---------------------------------------------------------------


For the moment, you mostly need to know the following three commands:

-  ``ls``: list the content of the current working directory
-  ``pwd``: path of current working directory
-  ``cd``: change directory

Read about them in http://linuxcommand.sourceforge.net/lc3_lts0020.php

Here are some resources to learn more about how to control your computer from a terminal:

     - Learning the Shell  http://linuxcommand.org/lc3_learning_the_shell.php
     - OpenClassRoom : https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/37813-la-console-ca-se-mange



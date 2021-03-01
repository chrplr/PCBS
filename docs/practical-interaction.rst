===========================================
Interacting with a computer (in a Nutshell)
===========================================

.. contents::



How to open a Terminal
----------------------

Linux
   Ctrl-Alt-T (see
   https://help.ubuntu.com/community/UsingTheTerminal)

MacOSX
   Open Finder/Applications/Utilities/Terminal (see
   http://www.wikihow.com/Get-to-the-Command-Line-on-a-Mac)

Windows
   Launch ``Git Bash`` (This assumes that you have installed Git for windows)



The shell
---------

Inside the terminal, you are interacting with a program called a **Shell**.

Various *Shells* exists:  under MacOSX or Linux: bash, zsh,... under standard Windows, cmd or powershell; they speak slighlty different languages.

The shell displays a prompt and waits for you to type a *command* that it will execute. For example, if you type ``ipython``, it will start the ipython program.

One issue is that you have to know the available commands and the language. By contrast with a Graphical User Interface shell with Windows/Icons/Menus, **Textual shells** have a very poor ergonomy. Yet, there are more powerful. They provides variables, loops,... to facilitate the automation of tasks.

For example, to create 20 directories in a single bash command under linux::

   for f in 01 02 03 04 05 06 07 08 09 10; do mkdir -p subject_$f/data subject_$f/results; done


The good news is: in these lectures, you will need to use only three shell commands:
* ``cd`` (change directory)
* ``ls`` (list)
* ``pwd`` (path of working directory).

I recommand that you read about them at http://linuxcommand.org/lc3_lts0020.php 

To learn more about how to control the computer from your Terminal, by interacting with the shell, I can only highly recommend two resources:

     - Learning the Shell  http://linuxcommand.org/lc3_learning_the_shell.php
     - OpenClassRoom  https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/37813-la-console-ca-se-mange



Disks, Directories and files
----------------------------

Most computers (not all) have two kinds of memories: - volatile, fast, memory, which is cleared when the computer is switched off (processor’s caches, RAM) - ‘permanent’, slow, memory, which is not erased when the computer is switched off (DISKS, Flashdrives (=solid-state drives))

The unit of storage is the **file**.

Files are nothing but blobs of bits stored “sequentially” on disks.

A first file could be stored between location 234 and 256, a second file could be stored at location 456.


filenames, directory structure
------------------------------

To access a file, one would need to know its location on the disk. To simplify human users’ life, the OS provide a system of “pointers”, that is **filenames** , organised in directories.

To help users further, the directories are organised in a hierarchical structure: a directory can contain filenames and other (sub)directories. The top-level directory is called the **root**.

.. figure:: images/linux_directory_structure.png
   :alt: Linux directory structure

   Linux directory structure

To locate a file, you must know:

-  its location in the directory structure
-  its basename

See `absolute or relative pathnames <https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/>`__ 

Remark: a given file can have several names in the same or various directories (remember: a filename is nothing but a link between a human readable charachter string to a location on the disk)

Working directory. Absolute pathnames vs. relative pathnames (..)
-----------------------------------------------------------------

It would be tedious to always have to specify the full path of a files (that is,
the list of all subdirs from the root)

Here comes the notion of **working directory**: A running program has a working
directory and filenames can specified **relative** to this directory.

Suppose you want to access the file pointed to by ``/users/pallier/documents/thesis.pdf``. If the current working directory is ``/users/pallier``, you can just use ``documents/thesis.pdf`` (notice the absence of ‘/’ at the beginning).

To determine the current working directory, list its content, and change it:

-  under bash::

        pwd
        ls
        cd Documents

-  under python (or ipython)::

       import os
       os.getcwd()
       os.listdir('.')
       os.chdir('documents')
       os.getcwd()


What is the PATH?
-----------------

A command can simply consists of a program's name. Typing it and pressing ``Enter`` will start the program.

The shell knows where to look for programs thanks to an *environment variable* called the **PATH**.

The ``PATH`` variable lists all the directories that contains programs. Try the following commands::

       echo $PATH
       which ls
       which python


It is possible to add new directories to the PATH variable, to access new programs::

      export PATH="newdirectory":"$PATH"


 
What is a library (or module/package)?
--------------------------------------

A set of new functions that extend a language (.DLL (Windows);.a or .so (Linux); framework bundles (MacOs))

Dynamic libraries can be used simultaneously by several processes.

Eg. the function @@sqrt@@ can be defined once, and called by several programs, saving memory.

In Python, use @@import library::

   import math
   math.srqt(2)

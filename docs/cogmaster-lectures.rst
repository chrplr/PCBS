.. _cogmaster:


******************
Cogmaster Lectures
******************

.. .. .. contents::
..
   ::

**Ateliers de Programmation pour les (Neuro)Sciences Cognitives / Programming for Cognitive and Brain Sciences**

This year (2023-2024) the lecture is split in two:

1. PROG101 Introduction to Programming with Python (first semester)

   This series of lectures targets students with little or no prior
   knowledge of programming. It will introduce the fundamentals concepts
   of coding : variables, expressions, functions, control structures,
   input/ouput. The course will make use of https://pythontutor.com/

2. PCBS Programming Experiments for Cognitive and Brain Sciences (second semester)

   The purpose of this module is to train students to program cognitive psychology experiments. During the first 7 lectures, the course starts with an introduction and is follwoed by hands-on exercises. In the second part of the semester, 
   Each student chooses an experiment to implement. The project’s development should be public on github.

Instructors


   - Henri van den Driessche <henri.vandendriessche@ens.fr> (PROG101)

   - Christophe Pallier <christophe@pallier.org> (PROG201)
   - Maxime Cauté  <maxime.caute@ens-rennes.fr> (PROG201)


Moodle

   https://moodle.u-paris.fr/course/view.php?id=7378

Slides

   http://github.com/chrplr/PCBS/tree/master/slides




Course description
==================


Objectives
----------


The purpose of the PCBS course is to make students able to write clean code in
order to solve the tasks that are typically encountered in cognitive or
neurosciences (data manipulation and analysis, creation of stimuli, programming
of real-time experiments, simulations...). The first half (6 weeks) of the
course consists of lectures with hands-on exercises, then, during the last 6
weeks, students have to realize a project publicly available on http://github.com


Learning outcomes
-----------------
                    
On successful completion of this course, students should be able to write
readable, well- documented, Python programs, and use system such as git that
promote reproducible science.

                    
Pedagogy, class organization and homework
-----------------------------------------

The first classes are lectures with hands-on exercices. The remaining classes, I and the teaching assistant are present for individual support to help the
students accomplish their project. I also give weekly assignments to be done
*before* the next lecture.
                    
Assessment
----------

The projects will be graded on a 20 points scale. The main criterion is *clarity* (see :ref:`projects` for more details).



Textbook and readings
---------------------

All the materials are available on the course’s web site at http://github.com/chrplr/PCBS.
                    

Course policies
---------------
                    
Laptops: Students must bring there own laptop (preferably fully charged!) with
the specified software preinstalled (see https://pcbs.readthedocs.io/en/latest/software-installation.html)
                    
Participation: You are strongly encouraged to participate in lectures and on the
discord discussion forum. The more advanced students are expected to help the
beginners.


Prerequisites
=============

They should  acquainted with basic programming concepts: instructions, variables, tests (if..then..else), loops (while and for). 

Students are expected to know how to open a terminal and `navigate in the file system <http://linuxcommand.org/lc3_lts0020.php>`__ and to know how to view and edit text files with a text editor such as `Sublime Text <https://www.sublimetext.com>`__.

.. projects

Projects
========

The project should try to replicate an experiment related to cognitive (neuro-) science.

An example of the kind of things that we expect is provided at http://chrplr.github.io/PCBS-LexicalDecision


- All documents (scripts, stimuli, documentation, data files) related to the project should be on a github.com repository with a name starts with ``PCBS-``  followed by a label that gives an idea of what the project is about.

- The main page of the repository (``README.md``) should :
    * describe the aim of the project (explain the experiment or the simulation 
    * explain how to install and run the experiment on one's computer (which command line, which options if any).
    * if the project involves analyses, the README.md should point to a documents (html, pdf, not Word!!!) containing the report.
    
- It is highly recommended to use the ‘Pages’ system of github to generate a nice looking page (see https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site ).

- It should be possible to clone your repository and execute your code without modifying anything. This implies that you should absolutely avoid absolute pathnames. Also your code must be portable and run on MacOS, Windows and Linux.

- Send us a link to your github project as soon as possible so that we can check your progress. 

- The readability of the code, and of the main page are of the main criteria of evaluation.

- Do not be overambitious: a well written project that does a simple thing but well will receive a better score than one that has an unreadble code that does complicated things.

-  You can work in binomes to read, check and criticize each other code
   regularily. it is very useful to have someone else check that the
   documentation and code that you write is readable.

-  use the discord channel to ask questions

- At the end of the `README.md` file, you must include a section detailling:
    - your previous coding experience
    - what you have learned since then, by following the lecture, coding the project or working by yourself
    - what you missed in this course.  




Programming for Cognitive and Brain Sciences
============================================

% Time-stamp: <2019-10-11 19:10:44 christophe@pallier.org>


Companion documents
===================

Must read!

-  `How to solve problems <how-to-solve-problems.md>`__
-  `Tips for writing clean code <tips.md>`__
-  `Tools for reproducible
   science <tools-for-reproducible-science.md>`__
-  Projects towards validation:

   -  `Example of past years’ projects <projects.md>`__
   -  `Some ideas of potential projects <ideas-for-projects.md>`__

--------------

.. raw:: html

   <!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->

**Table of Contents**

-  `Programming for Cognitive and Brain
   Sciences <#programming-for-cognitive-and-brain-sciences>`__
-  `Objectives <#objectives>`__
-  `First things first <#first-things-first>`__
-  `Companion documents <#companion-documents>`__
-  `Prerequisites <#prerequisites>`__

   -  `Software Installation <#software-installation>`__
   -  `Know how to open a Terminal <#know-how-to-open-a-terminal>`__
   -  `Downloading the course
      materials <#downloading-the-course-materials>`__
   -  `Basic programming concepts <#basic-programming-concepts>`__
   -  `Basic skills <#basic-skills>`__

      -  `how to download a Python script from the Internet and execute
         it from a command
         line <#how-to-download-a-python-script-from-the-internet-and-execute-it-from-a-command-line>`__
      -  `how to start
         [ipython](http://ipython.org) <#how-to-start-ipythonhttpipythonorg>`__
      -  `create and/or modify scripts with a text
         editor <#create-andor-modify-scripts-with-a-text-editor>`__
      -  `Use Git to keep your project
         clean <#use-git-to-keep--your-project-clean>`__

-  `Starting from Scratch # <#starting-from-scratch->`__
-  `Automata, Turing Machines and
   Computers <#automata-turing-machines-and-computers>`__
-  `Python in a Nutshell <#python-in-a-nutshell>`__
-  `Creating static visual stimuli <#creating-static-visual-stimuli>`__

   -  `Kanizsa illusory contours <#kanizsa-illusory-contours>`__
   -  `Herman grid <#herman-grid>`__
   -  `Ebbinghaus-Titchener <#ebbinghaus-titchener>`__
   -  `Honeycomb and Extinction
      illusions. <#honeycomb-and-extinction-illusions>`__
   -  `Random-dot stereograms <#random-dot-stereograms>`__

-  `Creating dynamic visual
   stimuli <#creating-dynamic-visual-stimuli>`__

   -  `Wertheimer line-motion
      illusion. <#wertheimer-line-motion-illusion>`__
   -  `Flash-lag illusion <#flash-lag-illusion>`__
   -  `Dynamic version of the
      Ebbinghaus-Titchener <#dynamic-version-of-the--ebbinghaus-titchener>`__

-  `Creating and playing sounds <#creating-and-playing-sounds>`__

   -  `Sound localisation from binaural
      dephasing <#sound-localisation-from-binaural-dephasing>`__
   -  `Pulsation (Povel & Essen, 1985) <#pulsation-povel--essen-1985>`__

-  `Experiments <#experiments>`__

   -  `Simple reaction times <#simple-reaction-times>`__
   -  `Posner’s attentional cueing
      task <#posners-attentional-cueing-task>`__
   -  `Stroop Effect <#stroop-effect>`__
   -  `Lexical Decision Task <#lexical-decision-task>`__
   -  `A general audio visual stimulus presentation
      script <#a-general-audio-visual-stimulus-presentation-script>`__
   -  `More examples using
      expyriment.org <#more-examples-using-expyrimentorg>`__

-  `Data Analyses <#data-analyses>`__

   -  `Basic Data Analysis with R <#basic-data-analysis-with-r>`__
   -  `Comparing means using Easy ANOVA (Analysis of
      Variance) <#comparing-means-using-easy-anova-analysis-of-variance>`__
   -  `Permutation tests <#permutation-tests>`__
   -  `Bootstrap <#bootstrap>`__
   -  `Frequency Analysis <#frequency-analysis>`__

-  `Lexical Statistics <#lexical-statistics>`__

   -  `Zipf law <#zipf-law>`__
   -  `Benford’s law. <#benfords-law>`__

-  `Simulations <#simulations>`__

   -  `Monte Carlo Estimation <#monte-carlo-estimation>`__
   -  `Fractals <#fractals>`__
   -  `Cellular Automata <#cellular-automata>`__
   -  `Artificial Neural networks <#artificial-neural-networks>`__
   -  `Natural Language Parsing <#natural-language-parsing>`__
   -  `Neuroimaging <#neuroimaging>`__

-  `License <#license>`__
-  `Appendices <#appendices>`__

   -  `Instructions for Software
      installation <#instructions-for-software-installation>`__

      -  `Warnings <#warnings>`__
      -  `Anaconda Python3 <#anaconda-python3>`__
      -  `Expyriment <#expyriment>`__
      -  `Git <#git>`__
      -  `A Text Editor <#a-text-editor>`__
      -  `R <#r>`__
      -  `Rstudio Desktop <#rstudio-desktop>`__

   -  `Resources to learn Python <#resources-to-learn-python>`__
   -  `Resources to learn the command
      shell <#resources-to-learn-the-command-shell>`__
   -  `Resources to learn Git <#resources-to-learn-git>`__
   -  `Stimulus/Experiment generation
      modules <#stimulusexperiment-generation-modules>`__
   -  `Data analyses, Statistics <#data-analyses-statistics>`__
   -  `Simulations <#simulations-1>`__
   -  `Books relevant to Cognitive and Brain Sciences
      Programming <#books-relevant-to-cognitive-and-brain-sciences-programming>`__
   -  `Programming skills <#programming-skills>`__
   -  `Coding exercices <#coding-exercices>`__

.. raw:: html

   <!-- markdown-toc end -->

--------------

--------------

Prerequisites
=============


Know how to open a Terminal
---------------------------

-  **Linux**: Launch ``Terminal`` from your application menu or use
   \`Ctrl-Alt-T*\* (gnome, xfce), or Win+Enter (i3)).

-  **MacOS**: Type ``terminal`` in the Spotlight search field.
   Alternatively, you can open a ``Finder`` window and select the
   ``Application`` folder, then the ``Utilities`` folder, then
   double-click on the ``Terminal`` icon..

-  **Windows**: Start ``Git Bash`` (This assumes that you have installed
   ``Git for windows`` as described in `Instructions for software
   installation <#instructions-for-software-installation>`__)

1. Click the Windows or Start icon.
2. In the Programs list, open the Git folder.
3. Click the option for Git Bash.

Inside a terminal, you interact with a program that expects you to type
commands. This program is called a *shell*. You need to know the
following commands in order to navigate the filesystem.

-  *ls*: list the content of the current working directory
-  *pwd*: path of current working directory
-  *cd*: change directory

This will be sufficient for this lecture, but if you want to learn more
about how to use the Terminal/Shell, check out the section `Resources to
learn the command shell <#resources-to-learn-the-command-shell>`__.

Downloading the course materials
--------------------------------

Once you have installed Git on your computer, you can download the
course materials: Open a terminal and type:

::

       git clone https://github.com/chrplr/PCBS.git

This should download the course materials in a folder named ‘PCBS’
(Remark: if a folder with that name already exists, git will stop and
not download the content of the website. In that case, delete or move
the existing PCBS folder before running the ``git clone`` command above)

I do often update the materials. To synchronize your local copy with the
latest version, you just need to open a terminal and type:

::

      cd PCBS
      git pull

Remark: do not manually modify or create new files in the PCBS folder.
If you do so, git will notice it and might prevent an automatic upgrade
and ask us to ‘resolve conflicts’. If you get such a message, the
simplest course of action for beginner, is to delete the PCBS folder (or
move it if you wnat to keep a copy of your modifications) and reuse the
git clone command above to reload the full folder.

Basic programming concepts
--------------------------

If you are a complete beginner, to get acquainted with some basic
programming concepts (instructions, variables, tests (if…then…else) and
loops (while and for)), I recommend that you learn to play with Scratch
`Starting-from-scratch <01_Starting-from-Scratch/Starting-from-Scratch.md>`__

Basic skills
------------

Beyond knowing how to open a terminal (see above), there are few skills
that you need to acquire:

how to download a Python script from the Internet and execute it from a command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try the following:

1. Download the script, e.g. `games/matches.py <games/matches.py>`__.
   Make sure you know in which directory the file has been saved.
2. Open a terminal and use the ``cd``, ``pwd`` , and ``ls`` commands to
   navigate to the directory containing the file that you have just
   downloaded; Then, type:

::

         python matches.py

how to start `ipython <http://ipython.org>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Try it:

-  Open a Terminal, type ``ipython`` and press “Return”,
-  After the prompt ``In [1]:``, type ``2**64`` and ‘Return’
-  Then, type the following lines in the ipython shell:

::

        import matplotlib.pyplot as plt
        import numpy as np
        t = np.linspace(0, 30, num=3001)
        plt.plot(t, np.sin(t))

If a Window open with a graphical representation of the sine function,
Congratulations! (you can press ‘q’ in the Window to close it)

-  Type ``quit()`` to quit ipython, then ``exit`` to quit the shell and
   close the terminal.

create and/or modify scripts with a text editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use a text editor like
`micro <https://micro-editor.github.io/>`__, `Sublime
Text <https://www.sublimetext.com/>`__ or `Atom <http://atom.io>`__, or
an Integrated Development Environment like Spyder or PyCharm.

To work you will basically need two windows side by side: one with a
text editor displaying the code, and one with ipython to test it (add
maybe a browser when you need to google for help about Python).

See `running python <running-python.md>`__

Use Git to keep your project clean
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Git <https://www.gitbook.com/>`__ is a software that allow you to keep
track of the modifications of your files, to test alternatives, to share
the work.

Git is a quite complex tool, but for this lecture, you will only need to
know very few commands (`git clone, git pull, git init, git add, git
status, git commit and git push``)

Check out `Resources to learn Git in the
Appendix <#resources-to-learn-git>`__

--------------

Starting from Scratch
=====================

See
`Starting-from-scratch <01_Starting-from-Scratch/Starting-from-Scratch.md>`__

Automata, Turing Machines and Computers
=======================================

See `Automata, Turing Machines and
Computers <Automata-Turing-Machines-and-Computers.md>`__

Python in a Nutshell
====================

-  See `Python in a
   Nutshell <02-Python_in_a_nutshell/Python_in_a_nutshell.md>`__

-  Read the Python scripts in the `games <games/>`__ folder.

-  I **strongly recommend** the freely available book `Automate the
   boring stuff with Python: Practical programming for total
   beginners. <https://automatetheboringstuff.com/>`__ to total novices
   (as well as the other books by the author). For those who dislike
   reading, there are videos on the site.

-  Check out `Resources to learn Python in the
   Appendix <#resources-to-learn-python>`__

Creating static visual stimuli
==============================

We are going to use `pygame <http://www.pygame.org>`__.

Please read this `quick introduction on drawing with
pygame <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>`__
and run and study the scripts
`square.py <visual-illusions/square.py>`__,
`circle.py <visual-illusions/circle.py>`__ and
`triangle.py <visual-illusions/triangle.py>`__.

Kanizsa illusory contours
-------------------------

0. Starting from the ``square.py`` and ``circle.py`` scripts, create a
   new script to display the Kanizsa squares:

   .. figure:: images/Kanizsa-square.jpeg
      :alt: Kanizsa square

      Kanizsa square

   .. figure:: images/Kanizsa1.png
      :alt: Kanizsa triangle

      Kanizsa triangle

   Check out my solution:
   `visual-illusions/kanizsa-square.py <visual-illusions/kanizsa-square.py>`__

   To find out more, google ``illusory contours``.\`

Herman grid
-----------

-  Starting from `square.py <visual-illusions/square.py>`__, write a
   program to display the `Herman
   grid <https://en.wikipedia.org/wiki/Grid_illusion>`__

   .. figure:: images/HermannGrid.png
      :alt: Hermann Grid

      Hermann Grid

   Hints:

   -  use paper and pencil to draw the figure
   -  find out the formulas to compute the left top of the square in the
      ith row and jth column
   -  in your python scripts, use nested for loops over rows and columns
      to display each square one by one

-  Check out `my solution <visual-illusions/grid.py>`__

-  Optional: Read
   https://stackabuse.com/command-line-arguments-in-python/ and use the
   ``sys.argv[]`` array from the ``sys`` module (or use the ``argparse``
   module) to get from the command lines the number of columns, rows,
   the size of square and the size of the margins. Play with those
   parameters to see if you can make the illusion come and go.

Ebbinghaus-Titchener
--------------------

-  Create the static `Ebbinghaus–Titchener
   stimulus <http://www.abc-people.com/illusion/illusion-3.htm#axzz5SqeF15yC>`__.

   .. figure:: images/ebbinghaus-titchener.png
      :alt: Ebbinghaus illusion

      Ebbinghaus illusion

Hint: - a bit of
`trigonometry <https://en.wikipedia.org/wiki/Unit_circle>`__ can help:
if you want to draw a circle at angle ``alpha`` from the horizontal line
and at distance ``R`` from the origin, the coordinates of its center are
``(R * cos(alpha), R * sin(alpha))``

-  Check out my solution
   `visual-illusions/ebbinghaus.py <visual-illusions/ebbinghaus.py>`__

Honeycomb and Extinction illusions.
-----------------------------------

The extinction illusion is a variant of the Herman grid:

.. figure:: images/extinction.png
   :alt: Extinction illusion

   Extinction illusion

-  Program the stimulus (the lines can be horizontal and vertical rather
   than oblique)

-  Check out `my solution <visual-illusions/extinction.py>`__

Here is the Honeycom illusion:

.. figure:: images/honeycomb.png
   :alt: Honeycomb illusion

   Honeycomb illusion

-  Watch `this video <https://www.youtube.com/watch?v=fDBYSFDXsuE>`__
-  Check out `Bertamini, Herzog, and Bruno (2016). “The Honeycomb
   Illusion: Uniform Textures Not Perceived as
   Such.” <https://doi.org/10.1177/2041669516660727.%20https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5030753/pdf/10.1177_2041669516660727.pdf>`__

-  Optional: Try to program the honeycomb stimulus above. A `solution
   using psychopy <visual-illusions/Honeycomb.py>`__ is available on
   `Bertamini’s web
   site <https://www.programmingvisualillusionsforeveryone.online/scripts.html>`__.
   To run it you might need to install “wxpython” (beware: it can be
   troublesome)

   ::

        conda install wxPython
        pip install psychopy

Random-dot stereograms
----------------------

A random-dot stereogram is stereo pair of images of random dots which,
when viewed with the eyes focused on a point in front of or behind the
images, produces a sensation of depth. See
https://en.wikipedia.org/wiki/Random_dot_stereogram.

.. figure:: images/stereogram.jpg
   :alt: stereogram

   stereogram

-  Write a script that generate random-dot stereograms.

-  Check out my solution:
   `random_dot_stereogram.py <random-dot-stereograms/random_dot_stereogram.py>`__

--------------

Creating dynamic visual stimuli
===============================

Wertheimer line-motion illusion.
--------------------------------

-  Check out `Jancke et al (2004) Imaging cortical correlates of
   illusion in early visual
   cortex <http://www.cnbc.cmu.edu/cns/papers/nature02396.pdf>`__.

-  Program the stimulus.

-  Check out my solution
   `visual-illusions/line-motion.py <visual-illusions/line-motion.py>`__

Flash-lag illusion
------------------

-  Read about the `Flash-lag
   illusion <https://en.wikipedia.org/wiki/Flash_lag_illusion>`__.

-  Program the stimulus.

-  Check out my solution
   `visual-illusions/flash-lag.py <visual-illusions/flash-lag.py>`__

Dynamic version of the Ebbinghaus-Titchener
-------------------------------------------

-  Watch `this video <https://www.youtube.com/watch?v=hRlWqfd5pn8>`__.

-  Program a version where the outer circles (inducers) grow and shrink
   in size.

-  Check out my solution
   `visual-illusions/ebbinghaus-dynamic.py <visual-illusions/ebbinghaus-dynamic.py>`__

--------------

Creating and playing sounds
===========================

-  Install the *simpleaudio* module if it is not already installed on
   your computer (check with ipython: ``import simpleaudio``) :

   ::

        pip install simpleaudio

   Run the quick check with ipython:

   ::

        import simpleaudio.functionchecks as fc 
        fc.LeftRightCheck.run() 

-  Check out `simpleaudio
   tutorials <https://simpleaudio.readthedocs.io/en/latest/tutorial.html>`__

-  Study `sound_synth.py <sound/sound_synth.py>`__.

-  Write a script that loads the wav file ``cymbal.wav`` and plays it 10
   times, at a rhythm of one per seconds.

   Hint:

   -  use the following functions:

      ::

         import scipy.io.wavfile  # for scipy.io.wavfile.read
         import simpleaudio  # to play sound


         def load_sound_as_array(filename):
            [sample_rate, audio_data] = scipy.io.wavfile.read(filename)
            return [sample_rate, audio_data]

         def play_mono(nparray, sample_rate=22050, normalize=True):
             audio = nparray[:]
             if normalize:  # normalize to 16-bit range
                audio *= 32767 / np.max(np.abs(audio))
             # convert to 16-bit data
             audio = audio.astype(np.int16)
             play_obj = simpleaudio.play_buffer(audio, 1, 2, sample_rate)
             # wait for playback to finish before exiting
             play_obj.wait_done()

Sound localisation from binaural dephasing
------------------------------------------

Take a mono sound and create a stereo sound by progressively dephasing
the two channels.

Hints: \* load the sound file into a one dimensional numpy array \* make
a copy of the array and shift it \* assemble the two arrays in a
bidimensional array (matrix) and save it as a stereo file

Pulsation (Povel & Essen, 1985)
-------------------------------

3. Create rhythmic stimuli such as the ones described in `Povel and
   Essen (1985) Perception of Temporal
   Patterns <http://www.cogsci.ucsd.edu/~creel/COGS160/COGS160_files/PovelEssens85.pdf>`__

Experiments
===========

Simple reaction times
---------------------

1. Write a script that presents a series of trials in which a dot or a
   cross is presented at the center of the screen and the participant
   must click on the mouse as quickly as possible. The reaction times
   must be recorded in a file for further analyses.

2. Here is a `solution using
   pygame <reaction-times/simple-detection-visual-pygame.py>`__. Run it
   and check ``reaction_times.csv``.

3. Here is a `solution using
   expyriment <reaction-times/simple-detection-visual-expyriment.py>`__.

Run the previous script. Check the results file in the folder ``data``.
Launch ipython in the ``data`` folder and type:

import pandas as pd d = pd.read_csv(‘simple-detection…
.xpd’,comment=‘#’) d.RT.mean() d.RT.std() d.RT[1:].mean()

import matplotlib.pyplot as plt plt.hist(d.RT)

4. Read https://docs.expyriment.org/Tutorial.html to understand the
   basic principles of expyriment. See \`PCBS/expyriment_template.py`\`

5. Modify ``simple-detection-visual-expyriment.py`` to play a short
   sound (``click.wav``) in lieu of displaying a cross. Thus you have
   created a simple detection audio experiment.

6. Modify the script to have 3 blocks of trials: one in which the target
   is visual, one in which it is audio, and one in which it is randomly
   visual or auditory. Are we slowed down in the latter condition?

Posner’s attentional cueing task
--------------------------------

Program `Posner’s attentional cueing
task <https://en.wikipedia.org/wiki/Posner_cueing_task>`__ See solution
in
`Posner-attention/posner_task.py <Posner-attention/posner_task.py>`__.

Stroop Effect
-------------

The `Stroop Effect <https://en.wikipedia.org/wiki/Stroop_effect>`__
demonstrates the automaticity of reading. Write a python script to
create 4x8 cards for the task, avoiding repetitions of colors.

.. figure:: images/stroop.png
   :alt: Stroop card

   Stroop card

You can read a tutorial on `how to display text with
pygame <https://nerdparadise.com/programming/pygame/part5>`__

-  After trying to program it yourself, you can compare with `my
   solution <Stroop-effect/create_stroop_cards.py>`__

-  Run `stroop_task.py <Stroop-effect/stroop_task.py>`__ and check the
   naming times in ``data``. Compute the average reading times as a
   function of the language (you can use R or Python).

Lexical Decision Task
---------------------

In a lexical decision experiment, a string of characters is flashed at
the center of the screen and the participant has to decide if it is real
word or not, indicating his/her decision by pressing a left or right
button. Reaction time is measured from the word onset, providing an
estimate of the speed of word recognition.

-  Visit the web site http://www.lexique.org
-  To learn to use lexique with R, follow the document
   http://chrplr.github.io/PCBS/lexique/interroger-lexique-avec-R.nb.html
-  Using [lexical-decision/select-words-from-lexique.py] as an example,
   select 20 high frequency nouns, 20 low frequency nouns, 20 high
   frequency verbs and 20 low frequency verbs, from Lexique382.txt —
   from http://www.lexique.org/public/Lexique382.zip. They must all have
   a length of 5 to 8 characters.
-  Generate 50 pseudowords using either `Lexique
   tools <http://www.lexique.org/toolbox/toolbox.pub/>`__ or
   `Wuggy <http://crr.ugent.be/programs-data/wuggy>`__
-  Program a lexical decision using expyriment.
-  Run it and compute the average decision times using pandas

A general audio visual stimulus presentation script
---------------------------------------------------

In some experiments, we know in avdvance the precise timing of all
stimuli (the program flow does not depends on external events). I wrote
a script that reads the timing of audiovisual stimuli and present them
at the expected times — Its code is available at
https://www.github.com/chrplr/audiovis

More examples using expyriment.org
----------------------------------

-  See http://docs.expyriment.org/old/0.9.0/Examples.html
-  Fork https://github.com/expyriment/expyriment-stash and contribute by
   adding new scripts!

--------------

Data Analyses
=============

Basic Data Analysis with R
--------------------------

See
http://www.pallier.org/examples-of-basic-data-analyses-with-r.html#examples-of-basic-data-analyses-with-r

Comparing means using Easy ANOVA (Analysis of Variance)
-------------------------------------------------------

See http://www.pallier.org/easy-anova-with-r.html#easy-anova-with-r

Permutation tests
-----------------

-  Read about the principle odf `permutation
   tests <https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests>`__

-  Implement a python script that uses a permutation test to compare two
   samples.

-  Check out my solution:
   `permutation_test/permutation_test.py <permutation_test/permutation_test.py>`__

Bootstrap
---------

-  Implement the
   `bootstrap <https://en.wikipedia.org/wiki/Bootstrapping_(statistics)>`__
   to obtain confidence intervals on the means of a sample.

Frequency Analysis
------------------

-  See
   `data-analysis/short-intro-fourier <data/analysis/short-intro-fourier>`__
   and the associated jupyter notebook `data-analysis/short intro to
   frequency analysis (Fourier
   series).ipynb <data-analysis/short%20intro%20to%20frequency%20analysis%20(Fourier%20series).ipynb>`__

--------------

Lexical Statistics
==================

Zipf law
--------

-  The script (word-count.py])[Zipf/word-count.py] computes the
   distribution of frequencies of occurences in a list of words. Use it
   to compute the distribution of word frequencies in `Alice in
   Wonderland <http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt>`__.

   Note: To remove the punctuation, you can use the following function:

   import string def remove_punctuation(text): punct =
   string.punctuation + chr(10) return
   text.translate(str.maketrans(punct, " " \* len(punct)))

-  Zipf law states that the product rank X frequency is roughly
   constant. This ‘law’ was discovered by Estoup and popularized by
   Zipf. See http://en.wikipedia.org/wiki/Zipf%27s_law. Create the Zipf
   plot for the text of `Alice in Wonderland <Zipf/alice.txt>`__
   showing, on the y axis, the log of the frequency and on the x axis
   the word rank (sorting words from the most frequent to the least
   frequent).

-  Display the relationship between word length and word frequencies
   from the data in
   `lexical-decision/lexique382-reduced.txt <lexical-decision/lexique382-reduced.txt>`__

-  Generate random text (each letter from a-z being equiprobable, and
   the spacecharacter being 8 times more probable) of 1 million
   characters. Compute the frequencies of each ‘pseudowords’ and plot
   the rank/frequency diagram.

-  To know more about lexical frequencies:

   -  Read Harald Baayen (2001) *Word Frequency Distributions* Kluwer
      Academic Publishers.
   -  Read Michel, Jean-Baptiste, Yuan Kui Shen, Aviva P. Aiden, Adrian
      Veres, Matthew K. Gray, The Google Books Team, Joseph P. Pickett,
      et al. 2010. “Quantitative Analysis of Culture Using Millions of
      Digitized Books.” Science, December.
      https://doi.org/10.1126/science.1199644. (use scholar.google.com
      to find a pdf copy). Check out **google ngrams** at
      https://books.google.com/ngrams. (Note that at the bottom of the
      page, there is a message “Raw data is available for download
      here”).

Benford’s law.
--------------

Learn about `Benford’s
law <https://brilliant.org/wiki/benfords-law/>`__. Write a Python script
that displays the distribution of the most significant digit in a set of
numbers. Apply it to the variables in
`Benford-law/countries.xlsx <Benford-law/countries.xlsx>`__.

A solution: `Benford-law/Benford.py <Benford-law/Benford.py>`__

--------------

Simulations
===========

Monte Carlo Estimation
----------------------

-  Read about `Monte Carlo estimation of
   PI <https://academo.org/demos/estimating-pi-monte-carlo/>`__

-  Write a script that estimate pi using this method (then check my
   solution:
   `simulations/estimate_PI_by_MonteCarlo.py <simulations/estimate_PI_by_MonteCarlo.py>`__)

Fractals
--------

`Fractals <https://en.wikipedia.org/wiki/Fractal>`__ are figures that
are self-similar at several scales.

-  Write a script that displays the `Koch
   snowflake <https://en.wikipedia.org/wiki/Koch_snowflake>`__

   Hints:

   -  use the turtle module
   -  use recursion

   My solution: `games/koch.py <games/koch.py>`__

Cellular Automata
-----------------

Learn about Conway’s `Game of
Life <https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>`__. Watch
`this <https://www.youtube.com/watch?v=S-W0NX97DB0>`__ and
`that <https://www.youtube.com/watch?v=C2vgICfQawE>`__ videos.

-  Implement an `Elementary cellular
   automaton <https://en.wikipedia.org/wiki/Elementary_cellular_automaton>`__.
   The aim is to reproduce the graphics shown at the bottom on the
   previous page. you can take inspiration from the excellent `Think
   Complexity <http://greenteapress.com/wp/think-complexity-2e/>`__ by
   Allen B. Downey. My solution is at
   `cellular-automata/1d-ca.py <cellular-automata/1d-ca.py>`__.

-  Implement the Game of Life in 2D.

-  Going futher: If you enjoy Cellular Automata, you can read Stephen
   Wolfram’s `A New Kind of
   Science <https://en.wikipedia.org/wiki/A_New_Kind_of_Science>`__. A
   more general book about Complexity is Melanie Mitchell’s *Complexity:
   a guided tour*.

Artificial Neural networks
--------------------------

To understand the basics of artificial neural networks, I recommend that
you first read https://victorzhou.com/blog/intro-to-neural-networks/ and
then watch the four excellent videos at
https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
. The last two of them focus on the backpropagation algorithm that allow
to train network to learn mapping.

Next, you can read and try to understand this
`implementation <https://visualstudiomagazine.com/articles/2017/06/01/back-propagation.aspx>`__
of the backpropagation algorithm.

Then, see a modern and efficient implementation of neural networks:
https://pytorch.org/tutorials/beginner/deep_learning_nlp_tutorial.html

More readings:

-  `The Unreasonable Effectiveness of Recurrent Neural
   Networks <http://karpathy.github.io/2015/05/21/rnn-effectiveness/>`__
   on Andrej Karpathy’s blog.

-  `understanding LSTM
   Networks <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>`__

-  `Pattern recognition and machine
   learning <https://www.springer.com/fr/book/9780387310732>`__ by
   Christopher M. Bishop

Natural Language Parsing
------------------------

Parsing refers to building the syntactic structure of a sentence from
the linear sequence of words that compose it. Explore the `various
parsing algorithms <http://www.nltk.org/book/ch08.html>`__\ using the
`Natural Language Toolkit <https://www.nltk.org/>`__.

Neuroimaging
------------

-  Check out `nilearn <http://nilearn.github.io/>`__ and
   `nistats <https://nistats.github.io/>`__ and
   `MNE-python <https://martinos.org/mne/stable/index.html>`__

-  See `data-analysis/Example of a single subject-single run fMRI
   analysis with
   nistats.ipynb <data-analysis/Example%20of%20a%20single%20subject-single%20run%20fMRI%20analysis%20with%20nistats.ipynb>`__




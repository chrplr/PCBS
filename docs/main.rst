

Creating static visual stimuli
==============================

We are going to use `pygame <http://www.pygame.org>`__.

Please read this `quick introduction on drawing with
pygame <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>`__
and run and study the scripts
:download:`square.py <../visual-illusions/square.py>`,
:download:`circle.py <../visual-illusions/circle.py>` and
:download:`triangle.py <../visual-illusions/triangle.py>`.

Kanizsa illusory contours
-------------------------

0. Starting from :download:`square.py <../visual-illusions/square.py>` and   :download:`circle.py <../visual-illusions/circle.py>`, scripts, create a new script to display the following figures:

   .. figure:: images/Kanizsa-square.jpeg
      :alt: Kanizsa square

      Kanizsa square

   .. figure:: images/Kanizsa1.png
      :alt: Kanizsa triangle

      Kanizsa triangle

   Check out my solution:
   :download:`visual-illusions/kanizsa-square.py <../visual-illusions/kanizsa-square.py>`

   To find out more, google ``illusory contours``.

Herman grid
-----------

-  Starting from :download:`square.py <../visual-illusions/square.py>`, write a
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

-  Check out :download:`my solution <../visual-illusions/grid.py>`

- Optional: Read https://stackabuse.com/command-line-arguments-in-python/ and use the ``sys.argv[]`` array from the ``sys`` module (or use the ``argparse`` module) to get from the command lines the number of columns, rows, the size of square and the size of the margins. Play with those parameters to see if you can make the illusion come and go.

Ebbinghaus-Titchener
--------------------

-  Create the static `Ebbinghaus–Titchener
   stimulus <http://www.abc-people.com/illusion/illusion-3.htm#axzz5SqeF15yC>`__.

   .. figure:: images/ebbinghaus-titchener.png
      :alt: Ebbinghaus illusion

      Ebbinghaus illusion

Hint: A bit of `trigonometry <https://en.wikipedia.org/wiki/Unit_circle>`__ can help:
if you want to draw a circle at angle ``alpha`` from the horizontal line
and at distance ``R`` from the origin, the coordinates of its center are
``(R * cos(alpha), R * sin(alpha))``

-  Check out my solution
   :download:`visual-illusions/ebbinghaus.py <../visual-illusions/ebbinghaus.py>`


Honeycomb and Extinction illusions.
-----------------------------------

The extinction illusion is a variant of the Herman grid:

.. figure:: images/extinction.png
   :alt: Extinction illusion

   Extinction illusion

-  Program the stimulus (the lines can be horizontal and vertical rather
   than oblique)

-  Check out :download:`my solution <../visual-illusions/extinction.py>`

Here is the Honeycom illusion:

.. figure:: images/honeycomb.png
   :alt: Honeycomb illusion

   Honeycomb illusion

-  Watch `this video <https://www.youtube.com/watch?v=fDBYSFDXsuE>`__
-  Check out `Bertamini, Herzog, and Bruno (2016). “The Honeycomb
   Illusion: Uniform Textures Not Perceived as
   Such.” <https://doi.org/10.1177/2041669516660727.%20https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5030753/pdf/10.1177_2041669516660727.pdf>`__

-  Optional: Try to program the honeycomb stimulus above. A :download:`solution
   using psychopy <../visual-illusions/Honeycomb.py>` is available on
   `Bertamini’s web
   site <https://www.programmingvisualillusionsforeveryone.online/scripts.html>`__.
   To run it you might need to install “wxpython” (beware: it can be
   troublesome)::

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
   :download:`random_dot_stereogram.py <../random-dot-stereograms/random_dot_stereogram.py>`




Creating dynamic visual stimuli
===============================

Wertheimer line-motion illusion.
--------------------------------

-  Check out `Jancke et al (2004) Imaging cortical correlates of
   illusion in early visual
   cortex <http://www.cnbc.cmu.edu/cns/papers/nature02396.pdf>`__.

-  Program the stimulus.

-  Check out my solution
   :download:`visual-illusions/line-motion.py <../visual-illusions/line-motion.py>`

Flash-lag illusion
------------------

-  Read about the `Flash-lag
   illusion <https://en.wikipedia.org/wiki/Flash_lag_illusion>`__.

-  Program the stimulus.

-  Check out my solution
   :download:`visual-illusions/flash-lag.py <../visual-illusions/flash-lag.py>`

Dynamic version of the Ebbinghaus-Titchener
-------------------------------------------

-  Watch `this video <https://www.youtube.com/watch?v=hRlWqfd5pn8>`__.

-  Program a version where the outer circles (inducers) grow and shrink
   in size.

-  Check out my solution
   :download:`visual-illusions/ebbinghaus-dynamic.py <../visual-illusions/ebbinghaus-dynamic.py>`

--------------

Creating and playing sounds
===========================

-  Install the *simpleaudio* module if it is not already installed on
   your computer (check with ipython: ``import simpleaudio``)::

        pip install simpleaudio

   Run the quick check with ipython::

        import simpleaudio.functionchecks as fc 
        fc.LeftRightCheck.run() 

-  Check out `simpleaudio tutorials <https://simpleaudio.readthedocs.io/en/latest/tutorial.html>`__

-  Study :download:`sound_synth.py <../sound/sound_synth.py>`

-  Write a script that loads the wav file ``cymbal.wav`` and plays it 10
   times, at a rhythm of one per seconds.

   Hint:

   -  use the following functions::

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

Hints: load the sound file into a one dimensional numpy array, make
a copy of the array and shift it, assemble the two arrays in a
bidimensional array (matrix) and save it as a stereo file


Pulsation (Povel & Essen, 1985)
-------------------------------

Create rhythmic stimuli such as the ones described in `Povel and Essen (1985) Perception of Temporal Patterns <http://www.cogsci.ucsd.edu/~creel/COGS160/COGS160_files/PovelEssens85.pdf>`__


Experiments
===========

Simple reaction times
---------------------

1. Write a script that presents a series of trials in which a dot or a
   cross is presented at the center of the screen and the participant
   must click on the mouse as quickly as possible. The reaction times
   must be recorded in a file for further analyses.

2. Here is a :download:`solution using pygame <../reaction-times/simple-detection-visual-pygame.py>`. Run it
   and check `reaction_times.csv`.

3. Here is a :download:`solution using expyriment <../reaction-times/simple-detection-visual-expyriment.py>`.

Run the previous script. Check the results file in the folder ``data``.
Launch ``ipython`` in the ``data`` folder and execute, line by line::

   import pandas as pd
   d = pd.read_csv('simple-detection.xpd',comment='#')
   print(d.RT.mean())
   print(d.RT.std())
   print(d.RT[1:].mean())
   import matplotlib.pyplot as plt
   plt.stem(d.RT)
   plt.show()
   plt.close()
   plt.hist(d.RT)
   plt.show()


4. Read https://docs.expyriment.org/Tutorial.html to understand the basic principles of expyriment. See :download:`/expyriment/expyriment_minimal_template.py <../expyriment/expyriment_minimal_template.py>`

5. Modify :download:`reaction-times/simple-detection-visual-expyriment.py <../reaction-times/simple-detection-visual-expyriment.py>` to play a short sound (`click.wav`) in lieu of displaying a cross. Thus you have created a simple detection audio experiment.

6. Modify the script to have 3 blocks of trials: one in which the target
   is visual, one in which it is audio, and one in which it is randomly
   visual or auditory. Are we slowed down in the latter condition?



Sound-picture matching
----------------------

:download:`../expyriment/sentence_picture_matching/sentence-picture-matching.py <../expyriment/sentence_picture_matching/sentence-picture-matching.py>`
 presents a sound, followed by one picture and waits for the participant to press a button.


Exercice: Modify the prvious script to present two pictures and use expyriment's `TouchScreenButtonBox` to record the subject's response, using the example from
:download:`expyriment/touchscreen_test/touchscreen-test.py  <../expyriment/touchscreen_test/touchscreen-test.py>`



Posner’s attentional cueing task
--------------------------------

Program the  `Posner’s attentional cueing task <https://en.wikipedia.org/wiki/Posner_cueing_task>`__

See solution
in :download:`../Posner-attention/posner_task.py <../Posner-attention/posner_task.py>`


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

-  After trying to program it yourself, you can compare with :download:`my
   solution <../Stroop-effect/create_stroop_cards.py>`

-  Run :download:`stroop_task.py <../Stroop-effect/stroop_task.py>` and check the
   naming times in ``data``. Compute the average reading times as a
   function of the language (you can use R or Python).


Lexical Decision Task
---------------------

In a lexical decision experiment, a string of characters is flashed at
the center of the screen and the participant has to decide if it is real
word or not, indicating his/her decision by pressing a left or right
button. Reaction time is measured from the word onset, providing an
estimate of the speed of word recognition.

-  Visit the web sites http://www.lexique.org and https://chrplr.github.io/openlexicon/
-  To learn to query Lexical databases from R, follow the instructions in
   http://chrplr.github.io/PCBS/lexique/interroger-lexique-avec-R.nb.html
-  Select 20 high frequency nouns, 20 low frequency nouns, 20 high
   frequency verbs and 20 low frequency verbs. They must all have
   a length of 5 to 8 characters.
-  Generate 50 pseudowords using either https://github.com/chrplr/openlexicon/blob/master/scripts/generate-pseudowords1/generate-pseudowords.R or
   `Wuggy <http://crr.ugent.be/programs-data/wuggy>`__
-  Program a lexical decision using the `expyriment` module. 
-  Run it and compute the average decision times using pandas


See a solution at https://github.com/chrplr/PCBS-LexicalDecision

A general audio visual stimulus presentation script
---------------------------------------------------

In some experiments, we know in advance the precise timing of all
stimuli (the program flow does not depends on external events). I wrote
a script that reads the timing of audiovisual stimuli and presents them
at the expected times — Its code is available at https://www.github.com/chrplr/audiovis


More examples using expyriment.org
----------------------------------

-  See http://docs.expyriment.org/old/0.9.0/Examples.html
-  Fork https://github.com/expyriment/expyriment-stash and contribute by
   adding new scripts!


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

-  Read about the principle of `permutation tests <https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests>`__

-  Implement a python script that uses a permutation test to compare two
   samples.

-  Check out the solution I propose:
   :download:`permutation_test/permutation_test.py <../permutation_test/permutation_test.py>`.

Bootstrap
---------

-  Implement the
   `bootstrap <https://en.wikipedia.org/wiki/Bootstrapping_(statistics)>`__
   to obtain confidence intervals on the means of a sample.


Frequency Analysis
------------------

-  See
   :download:`../data-analysis/short-intro-fourier <../data-analysis/short-intro-fourier>`
   and the associated jupyter notebook :download:`../data-analysis/short intro to frequency analysis (Fourier series).ipynb <data-analysis/short%20intro%20to%20frequency%20analysis%20(Fourier%20series).ipynb>`




Lexical Statistics
==================

Zipf law
--------

-  The script :download:`Zipf/word_count.py <../Zipf/word_count.py>` computes the
   distribution of frequencies of occurences in a list of words. Use it
   to compute the distribution of word frequencies in `Alice in
   Wonderland <http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt>`__.

   Note: To remove the punctuation, you can use the following function::

    import string
    def remove_punctuation(text):
       punct = string.punctuation + chr(10)
       return text.translate(str.maketrans(punct, " " \* len(punct)))

-  Zipf law states that the product rank X frequency is roughly
   constant. This ‘law’ was discovered by Estoup and popularized by
   Zipf. See http://en.wikipedia.org/wiki/Zipf%27s_law. Create the Zipf
   plot for the text of `Alice in Wonderland <Zipf/alice.txt>`__
   showing, on the y axis, the log of the frequency and on the x axis
   the word rank (sorting words from the most frequent to the least
   frequent).

-  Display the relationship between word length and word frequencies
   from the data in
   :download:`lexical-decision/lexique382-reduced.txt <../lexical-decision/lexique382-reduced.txt>`

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

A solution: :download:`Benford-law/Benford.py <../Benford-law/Benford.py>`



Simulations
===========

Monte Carlo Estimation
----------------------

-  Read about `Monte Carlo estimation of
   PI <https://academo.org/demos/estimating-pi-monte-carlo/>`__

-  Write a script that estimate pi using this method (then check my
   solution:
   :download:`simulations/estimate_PI_by_MonteCarlo.py <../simulations/estimate_PI_by_MonteCarlo.py>`)

Fractals
--------

`Fractals <https://en.wikipedia.org/wiki/Fractal>`__ are figures that
are self-similar at several scales.

-  Write a script that displays the `Koch
   snowflake <https://en.wikipedia.org/wiki/Koch_snowflake>`__

   Hints:

   -  use the turtle module
   -  use recursion

   My solution: :download:`games/koch.py <../games/koch.py>`


Formal systems
--------------

MU Puzzle
~~~~~~~~~

A famous seminal book in Cognitive Science is *Gödel Escher Bach: An Eternal Golden* by Douglas Hofstadter. Its main topic is recursion and self-reference (see also *I am strange loop* by the same author).


According to Hofstadter, the formal system that underlies all mental activity transcends the system that supports it. If life can grow out of the formal chemical substrate of the cell, if consciousness can emerge out of a formal system of firing neurons, then so too will computers attain human intelligence. Gödel, Escher, Bach is a wonderful exploration of fascinating ideas at the heart of cognitive science: meaning, reduction, recursion, and much more (from https://medium.com/@alibedirhan.d/mu-puzzle-f651ef3957c5)

The book is filled with puzzles, including Hofstadter’s famous **MU puzzle**. The MU puzzle involves a simple formal system called **MIU**.

A starting string, ``MI``, is given. Four rules for changing the string of characters into a new one are provided (see below). A each step, the current string can be transformed into a new string by the application of one of the four rules. Note that rules are one-way!  In case there are several applicable rules, there is nothing that will dictate which rule you should use, it’s up to you! Here are the rules:


1. If you possess a string whose last letter is ``I``, you can add on a ``U`` at the end. For example ``MIUI`` can be rewritten ``MIUII``. This rule can be written ``xI ⟶ xIU`` where ``x`` represents any string
   
2. Suppose you have ``Mx``. Then you may rewrite it ``Mxx``. For example, from ``MIU``, you may get ``MIUIU`` (x = ``IU`` therefore; ``Mxx = MIUIU``; From ``MUM``, you may get ``MUMUM``, From ``MU``, you may get ``MUU``, ...

3. If ``III`` occurs in one of the strings, you may make a new string with ``U`` in place of ``III``. For example, 
    From ``UMIIIMU``, you could make ``UMUMU``; From ``MIIII``, you could make ``MIU`` (also ``MUI``). From ``IIMII``, you can't get anywhere using this rule because the three ``I``'s have to be consecutive.


4. If ``UU`` occurs inside one of your strings, you can drop it. From ``UUU``, you get ``U``. From ``MUUUIII``, get ``MUIII``.


The **Mu Puzzle** asks whether starting from the string ``MI``, there exists a *derivation*, that is a sequence of aplications of the rules, that can yield the string ``MU``.

Exercice: Write a Python script that explores the set of strings generated by this formal system, to try and see if ``MU`` can be generated.

Then you may read :

- https://en.wikipedia.org/wiki/MU_puzzle

- Ernest Nagel and James Newman's book `Gödel's Theorem <http://calculemus.org/cafe-aleph/raclog-arch/nagel-newman.pdf>`__ (translated into French : `Le théorème de Gödel <https://www.eyrolles.com/Sciences/Livre/le-theoreme-de-godel-9782020327787/>`__)


Natural Language Parsing
~~~~~~~~~~~~~~~~~~~~~~~~

Parsing refers to building the syntactic structure of a sentence from
the linear sequence of words that compose it.

* Read Chapter 12 (Constituency Grammars)  and 13 (Constituency Parsing)  of Dan Jurafsky and James H. Martin's `Speech and Language Processing <https://web.stanford.edu/~jurafsky/slp3/>`__
 
* Explore the `various parsing algorithms <http://www.nltk.org/book/ch08.html>`__\ using the
`Natural Language Toolkit <https://www.nltk.org/>`__.


Cellular Automata
~~~~~~~~~~~~~~~~~

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


Neuroimaging
------------

-  Check out `nilearn <http://nilearn.github.io/>`__ and
   `nistats <https://nistats.github.io/>`__ and
   `MNE-python <https://martinos.org/mne/stable/index.html>`__

-  See `data-analysis/Example of a single subject-single run fMRI
   analysis with
   nistats.ipynb <data-analysis/Example%20of%20a%20single%20subject-single%20run%20fMRI%20analysis%20with%20nistats.ipynb>`__




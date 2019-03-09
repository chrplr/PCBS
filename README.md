% Programming for Cognitive and Brain Sciences (notes for the Cogmaster's PCBS
course)

% Time-stamp: <2019-03-09 18:29:45 christophe@pallier.org>

The latest version of this document -- a work in progress -- is at
[https://chrplr.github.io/PCBS](https://chrplr.github.io/PCBS).

Its source as well as the course materials (scripts, etc.) are available at
[http://www.github.com/chrplr/PCBS](http://www.github.com/chrplr/PCBS).

To download them, open a terminal (`git bash` under Windows) and type:

```
    git clone https://github.com/chrplr/PCBS 
        
```

-------------------------------------------------------------------------------

**Companion documents**

* [How to solve problems](how-to-solve-problems.md)
* [Tips for writing clean code](tips.md)
* [Tools for reproducible science](tools-for-reproducible-science.md)
* [Additional exercises](exercices.md). I answer questions on a [slack
  discussion forum](https://cogmaster-pcbs.slack.com) Please [join!](
 https://join.slack.com/t/cogmaster-pcbs/shared_invite/enQtNDUzNDk0NTMyNjk0LTM0YzVhMmI1YjU3ZjRhMjNmZDRjMmVmYzYwYWJiZjA1YTE2MjNkYjE3MzAyNGU3OWI0MTA3NGMyOTFiYmM3NzU)
* Programming projects towards validation:
    - [A few suggestions for projects](ideas-for-projects.md)
    - [Your projects](projects.md)

-------------------------------------------------------------------------------

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Objectives](#objectives)
- [Prerequisites](#prerequisites)
- [Resources](#resources)
    - [Manipulations](#manipulations)
    - [Stimulus/Experiment generation modules](#stimulusexperiment-generation-modules)
    - [Data analyses, Statistics](#data-analyses-statistics)
    - [Simulations](#simulations)
    - [Books relevant to Cognitive and Brain Sciences Programming](#books-relevant-to-cognitive-and-brain-sciences-programming)
    - [Programming skills](#programming-skills)
- [Creating static visual stimuli](#creating-static-visual-stimuli)
    - [Kanizsa illusory contours](#kanizsa-illusory-contours)
    - [Herman grid](#herman-grid)
    - [Ebbinghaus-Titchener](#ebbinghaus-titchener)
    - [Honeycomb and Extinction illusions.](#honeycomb-and-extinction-illusions)
    - [Random-dot stereograms](#random-dot-stereograms)
- [Creating dynamic visual stimuli](#creating-dynamic-visual-stimuli)
    - [Wertheimer line-motion illusion.](#wertheimer-line-motion-illusion)
    - [Flash-lag illusion](#flash-lag-illusion)
    - [Dynamic version of the  Ebbinghaus-Titchener](#dynamic-version-of-the--ebbinghaus-titchener)
- [Creating and playing sounds](#creating-and-playing-sounds)
    - [Sound localisation from binaural dephasing](#sound-localisation-from-binaural-dephasing)
    - [Pulsation (Povel & Essen, 1985)](#pulsation-povel--essen-1985)
- [Experiments](#experiments)
    - [Simple reaction times](#simple-reaction-times)
    - [Posner's attentional cueing task](#posners-attentional-cueing-task)
    - [Stroop Effect](#stroop-effect)
    - [Lexical Decision Task](#lexical-decision-task)
    - [A general audio visual stimulus presentation script](#a-general-audio-visual-stimulus-presentation-script)
    - [More examples using expyriment.org](#more-examples-using-expyrimentorg)
- [Data Analyses](#data-analyses)
    - [Basic Data Analysis with R](#basic-data-analysis-with-r)
    - [Comparing means using Easy ANOVA (Analysis of Variance)](#comparing-means-using-easy-anova-analysis-of-variance)
    - [Permutation tests](#permutation-tests)
    - [Bootstrap](#bootstrap)
- [Lexical Statistics](#lexical-statistics)
    - [Zipf law](#zipf-law)
    - [Benford's law.](#benfords-law)
- [Simulations](#simulations-1)
    - [Fractals](#fractals)
    - [Cellular Automata](#cellular-automata)
    - [Artificial Neural networks](#artificial-neural-networks)
    - [Natural Language Parsing](#natural-language-parsing)
    - [Neuroimaging](#neuroimaging)
- [License](#license)
- [Appendices](#appendices)
    - [Instructions for Software installation](#instructions-for-software-installation)
        - [Warnings](#warnings)
        - [Anaconda Python3](#anaconda-python3)
        - [Expyriment](#expyriment)
        - [Git](#git)
        - [Sublime Text Editor](#sublime-text-editor)
        - [R](#r)
        - [Rstudio Desktop](#rstudio-desktop)
    - [How to open a Terminal](#how-to-open-a-terminal)
        - [Linux](#linux)
        - [Windows](#windows)
    - [Resources to learn the command shell](#resources-to-learn-the-command-shell)
    - [Resources to learn Python](#resources-to-learn-python)
    - [Resources to learn Git](#resources-to-learn-git)

<!-- markdown-toc end -->

-------------------------------------------------------------------------------



# Objectives #

The purpose of these lectures is to allow students to write clean programs in
order to solve the tasks that are typically encountered in cognitive or
neurosciences (data manipulation and analysis, creation of stimuli, programming
of real-time experiments, simulations...).

-------------------------------------------------------------------------------

# Prerequisites #

You should:

* have installed the following software on your computer
  ([Instructions](#instructions-for-software-installation) are provided in the
  appendix):

  * **Python3**. 
  * The Python library **Expyriment** 
  * **Git** from <https://git-scm.com/>
  * **Sublime Text** (text editor) from [Sublime
  Text](https://www.sublimetext.com/) (Unless you are already using a text
  editor that you are happy with)
  * **R** from <https://cran.r-project.org/>
  * **Rstudio Desktop** from <https://www.rstudio.com>


* know [how to open a Terminal](#how-to-open-a-terminal)  and navigate the
  directory structure with `cd`, `pwd` and `ls`.
  
  Try it: Open a Terminal, use `cd` and `pwd` to navigate to the `PCBS` folder
  that you have previously downloaded with `git clone`, and list the files with
  `ls`).

* know how to launch [ipython](http://ipython.org) in a Terminal.
  
  Try it: Open a Terminal, type `ipython`, and enter `2**64`

* know how to download a Python script from the Internet and execute it from the
  command line in a Terminal:
  
  Try it: Download [games/matches.py](games/matches.py) and
  run it in a terminal

* know how to create and/or modify scripts with a text editor such as [Sublime
  Text](https://www.sublimetext.com/) or using an Integrated Development Environment
  like Spyder (included in Anaconda).

* know basic programming concepts expressions, instructions, variables, lists,
  dictionaries, tests (if..then..else), string manipulations, loops (while and
  for), functions (call, definition, local variables), file input/output
  operations ) and their implementation in Python3. For instance, you should be able 
  to understand the scripts in the [games](games/) folder.
  
  Check out [Resources to learn Python in the Appendix](#resources-to-learn-python)

* know the basic usage of [Git](https://www.gitbook.com/), that is the
  commands`git clone, git pull, git init, git add, git status, git commit` 
  
  Check out [Resources to learn Git in the Appendix](#resources-to-learn-git)


-------------------------------------------------------------------------------

# Resources #

## Manipulations ##

_Automate the boring stuff with Python_ by Al Sweigart
(<http://automatetheboringstuff.com/>) is a great book to learn to manipulate
files, extracting information from web pages, etc.

## Stimulus/Experiment generation modules ##

* <http://www.pygame.org>
     - Tutorial "PyGame Drawing Basics":
     <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>
* <http://www.lexique.org>
* <http://www.expyriment.org> (my favorite)
     - Tutorial: <https://docs.expyriment.org/Tutorial.html>
* <http://psychopy.org>
     - Tutorial "Programming with PsychoPy":
     <https://www.socsci.ru.nl/wilberth/nocms/psychopy/print.php>
* <http://psychtoolbox.org/> (Matlab only)

## Data analyses, Statistics ##

* Modules: numpy, scipy, pandas, seaborn, statsmodel, sklearn
   - Data manipulation:
   <http://pandas.pydata.org/pandas-docs/stable/tutorials.html>
   - Plotting:
      - <http://matplotlib.org/users/pyplot_tutorial.html>
      - <https://seaborn.pydata.org/tutorial.html>

* _Scipy Lecture Notes_: <http://www.scipy-lectures.org/>
* _Think Stats_ by Allen B. Downey: <http://greenteapress.com/thinkstats2/>
* _Python Data Science Handbook_ by Jake VanderPlas:
  <https://jakevdp.github.io/PythonDataScienceHandbook>


## Simulations ##

* [_Think Complexity_](http://greenteapress.com/wp/think-complexity-2e/) by
  Allen B. Downey
* The [Brian spiking neural network simulator](http://briansimulator.org/)
* [Deep Learning for Natural Language Processing with
  Pytorch](https://pytorch.org/tutorials/beginner/deep_learning_nlp_tutorial.html)


## Books relevant to Cognitive and Brain Sciences Programming ##

* [_Programming Visual Illusions for
  Everyone_](https://www.programmingvisualillusionsforeveryone.online/) by Marco
  Bertamini:
* _Neural Data Science: A Primer with MATLAB and Python_ by von Erik Lee Nylen
  and Pascal Wallisch
* _Matlab for Brain and Cognitive Scientists_ and _Analyzing neural time series
  data_ by Mike X Cohen
* [_Python in
  Neuroscience_](https://www.frontiersin.org/research-topics/8/python-in-neuroscience)
* _Modeling Psychophysical Data in R_ by Kenneth Knoblauch & Laurence T. Maloney

## Programming skills ##
 
* See my [Tips for writing clean code](tips.md)

* [Software Carpentry](https://software-carpentry.org/lessons/) provides
   lessons on writing software for science.

* [Software Carpentry](https://software-carpentry.org/lessons/) provides
   nice lessons about writing software for science.

-------------------------------------------------------------------------------

# Creating static visual stimuli #

We are going to use [pygame](http://www.pygame.org). You can read a [quick
introduction on drawing with
pygame](https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/).

## Kanizsa illusory contours ##

0. Run and study the scripts [square.py](visual-illusions/square.py),
   [circle.py](visual-illusions/circle.py) and
   [triangle.py](visual-illusions/triangle.py), and create new scripts to
   create the Kanizsa figures:

   ![Kanizsa square](images/Kanizsa-square.jpeg)

   ![Kanizsa triangle](images/Kanizsa1.png)

  You can find more examples by googling 'illusory contours'.

  Check [my solution](visual-illusions/kanizsa-square.py)

## Herman grid ##

* Starting from [square.py](visual-illusions/square.py), write a program to display the [Herman
grid](https://en.wikipedia.org/wiki/Grid_illusion)

   ![Hermann Grid](images/HermannGrid.png)
   
  Hints:
    - use paper and pencil to draw the figure
    - find out the formulas to compute the left top of the square in the ith row and jth column
    - in your python scripts, use nested for loops over rows and columns to display each square one by one  

*  Check [my solution](visual-illusions/grid.py)

* Optional: Read <https://stackabuse.com/command-line-arguments-in-python/> and use the sys.argv[] array from the sys module (or use the argparse module) to get from the command lines the number of columns, rows, the size of square and the size of the margins. Play with those parameters to see if you can make the illusion come and go.


## Ebbinghaus-Titchener ##

Create the static [Ebbinghaus–Titchener
stimulus](http://www.abc-people.com/illusion/illusion-3.htm#axzz5SqeF15yC). 

   ![Ebbinghaus illusion](images/ebbinghaus-titchener.png)


## Honeycomb and Extinction illusions. ##

![Honeycomb illusion](images/honeycomb.png)

- Watch [this video](https://www.youtube.com/watch?v=fDBYSFDXsuE)
- Check out [Bertamini, Herzog, and Bruno (2016). “The Honeycomb Illusion:
  Uniform Textures Not Perceived as
  Such.”](https://doi.org/10.1177/2041669516660727.
 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5030753/pdf/10.1177_2041669516660727.pdf)
- Program the stimulus of the extinction illusion (the lines can be horizontal
  and vertical rather than oblique)
     
![Extinction illusion](images/extinction.png)
 
Check [my solution](visual-illusions/extinction.py)
  
- Try to program the honeycomb stimulus above (optional). A []solution
  psychopy](visual-illusions/Honeycomb.py) from [Bertamini's web
  site](https://www.programmingvisualillusionsforeveryone.online/scripts.html)
    

## Random-dot stereograms

A random-dot stereogram is stereo pair of images of random dots which, when
viewed with the eyes focused on a point in front of or behind the images,
produces a sensation of depth. See
<https://en.wikipedia.org/wiki/Random_dot_stereogram>.

![stereogram](images/stereogram.jpg)

* Write a script that generate random-dot stereograms.

My solution: [random_dot_stereogram.py](random-dot-stereograms/random_dot_stereogram.py)

--------------------------------------------------------------------------------

# Creating dynamic visual stimuli #


## Wertheimer line-motion illusion. ##

Check out [Jancke et al (2004) Imaging cortical correlates of illusion in early
visual cortex](http://www.cnbc.cmu.edu/cns/papers/nature02396.pdf). Program the
stimulus. Compare with
[visual-illusions/line-motion.py](visual-illusions/line-motion.py)

## Flash-lag illusion ##

Read about the [Flash-lag
illusion](https://en.wikipedia.org/wiki/Flash_lag_illusion). Program the
stimulus. Compare with
[visual-illusions/flash-lag.py](visual-illusions/flash-lag.py)

## Dynamic version of the  Ebbinghaus-Titchener ##

Watch [this video](https://www.youtube.com/watch?v=hRlWqfd5pn8).
Program a version where the outer circles (inducers) grow and shrink in size.

--------------------------------------------------------------------------------

# Creating and playing sounds #

* Install the _simpleaudio_ module if it is not already installed on your computer
(check with ipython: `import simpleaudio`), :
     
    pip install simpleaudio

Run the quick check with ipython:

    import simpleaudio.functionchecks as fc 
    fc.LeftRightCheck.run() 

* Check out [simpleaudio tutorials](https://simpleaudio.readthedocs.io/en/latest/tutorial.html)

* Study [sound_synth.py](sound/sound_synth.py).

* Write a script that loads the wav file cymbal.wav and plays it 10 times, at a rhythm of one per seconds.

Hint:
* you can use the following functions:


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


## Sound localisation from binaural dephasing ##

Take a mono sound and create a stereo sound by progressively dephasing the two
channels.

Hints:
* load the sound file into a one dimensional numpy array 
* make a copy of the array and shift it
* assamble the two arrays in a bidimensional array (matrix) and save it as a stereo file 

## Pulsation (Povel & Essen, 1985) ##

3. Create rhythmic stimuli as described in [Povel and Essen (1985) _Perception
   of Temporal
   Patterns_](http://www.cogsci.ucsd.edu/~creel/COGS160/COGS160_files/PovelEssens85.pdf)


# Experiments #

## Simple reaction times ##

1. Write a script that presents a series of trials in which a dot or a cross is
   presented at the center of the screen and the participant must click on the
   mouse as quickly as possible. The reaction times must be recorded in a file
   for further analyses.

    - Here is a [solution using
    pygame](reaction-times/simple-detection-visual-pygame.py). Run it and check
    `reaction_times.csv`.
    - Here is a [solution using
    expyriment](reaction-times/simple-detection-visual-expyriment.py).
    
    Run the previous script. Check the results file in the folder `data`. Launch
    ipython in the `data` folder and type:
    

    import pandas as pd 
    d = pd.read_csv('simple-detection... .xpd',comment='#') 
    d.RT.mean() 
    d.RT.std() 
    d.RT[1:].mean()
    
    import matplotlib.pyplot as plt plt.hist(d.RT) 



3. Read <https://docs.expyriment.org/Tutorial.html> to understand the basic
   pinciples of expyriment. See `PCBS/expyriment_template.py``

4. Modify `simple-detection-visual-expyriment.py` to play a short sound
   (`click.wav`) in lieu of displaying a cross. Thus you have a simple detection
   audio experiment.

5. Modify the script to have 3 blocks of trials: one in which the target is
   visual, one in which it is audio, and one in which it is randomly visual or
   auditory. Are we slowed down in the latter condition?

## Posner's attentional cueing task ##

Program [Posner's attentional cueing
task](https://en.wikipedia.org/wiki/Posner_cueing_task) See solution in
[Posner-attention/posner_task.py](Posner-attention/posner_task.py).


## Stroop Effect ##

The [Stroop Effect](https://en.wikipedia.org/wiki/Stroop_effect) demonstrates
the automaticity of reading. Write a python script to create 4x8 cards for the
task, avoiding repetitions of colors.
 
![Stroop card](images/stroop.png)
 
  You can read a tutorial on [how to display text with
  pygame](https://nerdparadise.com/programming/pygame/part5)
 
   * After trying to program it yourself, you can compare with [my
   solution](Stroop-effect/create_stroop_cards.py)

   * Run [stroop_task.py](Stroop-effect/stroop_task.py) and check the naming
   times in `data`. Compute the average reading times as a function of the
   language (you can use R or Python).
   
## Lexical Decision Task ##

In a lexical decision experiment, a string of characters is flashed at the
center of the screen and the participant has to decide if it is real word or
not, indicating his/her decision by pressing a left or right button. Reaction
time is measured from the word onset, providing an estimate of the speed of word
recognition.

   * Using [lexical-decision/select-words-from-lexique.py] as an example, select
   20 high frequency nouns, 20 low frequency nouns, 20 high frequency verbs and
   20 low frequency verbs, from Lexique382.txt --- from
   <http://www.lexique.org/public/Lexique382.zip>.They must all have a length of
   5 to 8 characters.
   * generate 50 pseudowords using either [Lexique
   tools](http://www.lexique.org/toolbox/toolbox.pub/) or
   [Wuggy](http://crr.ugent.be/programs-data/wuggy)
   * Program a lexical decision using expyriment.
   * Run it and compute the average decision times using pandas

## A general audio visual stimulus presentation script ##

See <https://www.github.com/chrplr/audiovis>

## More examples using expyriment.org ##

* See <http://docs.expyriment.org/old/0.9.0/Examples.html>
* Fork <https://github.com/expyriment/expyriment-stash> and contribute by adding
  new scripts!


# Data Analyses #

## Basic Data Analysis with R

See <http://www.pallier.org/examples-of-basic-data-analyses-with-r.html#examples-of-basic-data-analyses-with-r>

## Comparing means using Easy ANOVA (Analysis of Variance) ##

See <http://www.pallier.org/easy-anova-with-r.html#easy-anova-with-r>

## Permutation tests ##

* Implement the [permutation test](https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests) 
to compare two samples.

My solution: [permutation_test/permutation_test.py](permutation_test/permutation_test.py)

## Bootstrap ##

* Implement the [bootstrap](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) 
to obtain confidence intervals on the means of a sample. 

--------------------------------------------------------------------------------

# Lexical Statistics #

## Zipf law ##

* The script (word-count.py])[Zipf/word-count.py] computes the distribution of
  frequencies of occurences in a list of words. Use it to compute the
  distribution of word frequencies in [_Alice in
  Wonderland_](http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt).

   Note: To remove the punctuation, you can use the following function:


    import string def remove_punctuation(text):
        punct = string.punctuation + chr(10) return
        text.translate(str.maketrans(punct, " " * len(punct)))


* Zipf law states that the product rank X frequency is roughly constant. This
  'law' was discovered by Estoup and popularized by Zipf. See
  <http://en.wikipedia.org/wiki/Zipf%27s_law>. Create the Zipf plot for the text
  of [_Alice in Wonderland_](Zipf/alice.txt) showing, on the y axis, the log of
  the frequency and on the x axis the word rank (sorting words from the most
  frequent to the least frequent).

* Display the relationship between word length and word frequencies from the
  data in
  [lexical-decision/lexique382-reduced.txt](lexical-decision/lexique382-reduced.txt)


* Generate random text (each letter from a-z being equiprobable, and the
  spacecharacter being 8 times more probable) of 1 million characters. Compute
  the frequencies of each 'pseudowords' and plot the rank/frequency diagram.

* To know more about lexical frequencies:

    - Read Harald Baayen (2001) _Word Frequency Distributions_ Kluwer Academic
    Publishers.
    - Read Michel, Jean-Baptiste, Yuan Kui Shen, Aviva P. Aiden, Adrian Veres,
    Matthew K. Gray, The Google Books Team, Joseph P. Pickett, et al. 2010.
    “Quantitative Analysis of Culture Using Millions of Digitized Books.”
    Science, December. <https://doi.org/10.1126/science.1199644.> (use
    scholar.google.com to find a pdf copy). Check out **google ngrams** at
    <https://books.google.com/ngrams>. (Note that at the bottom of the page,
    there is a message "Raw data is available for download here").
    
## Benford's law. ##

Learn about [Benford's law](https://brilliant.org/wiki/benfords-law/). Write a
Python script that displays the distribution of the most significant digit in a
set of numbers. Apply it to the variables in
[Benford-law/countries.xlsx](Benford-law/countries.xlsx).

A solution: [Benford-law/Benford.py](Benford-law/Benford.py)

--------------------------------------------------------------------------------

# Simulations #

## Fractals ##

[Fractals](https://en.wikipedia.org/wiki/Fractal) are figures that are
self-similar at several scales.

* Write a script that displays the [Koch
  snowflake](https://en.wikipedia.org/wiki/Koch_snowflake)

Hints: 
* use the turtle module
* use recursion

My solution: [games/koch.py](games/koch.py)


## Cellular Automata ##

Learn about Conway's [Game of
Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Watch
[this](https://www.youtube.com/watch?v=S-W0NX97DB0) and
[that](https://www.youtube.com/watch?v=C2vgICfQawE) videos.

* Implement an [Elementary cellular
  automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton). The
  aim is to reproduce the graphics shown at the bottom on the previous page. you
  can take inspiration from the excellent [_Think
  Complexity_](http://greenteapress.com/wp/think-complexity-2e/) by Allen B.
  Downey. My solution is at
  [cellular-automata/1d-ca.py](cellular-automata/1d-ca.py).

* Implement the Game of Life in 2D.

* Going futher: If you enjoy Cellular Automata, you can read Stephen Wolfram's
  [_A New Kind of
  Science_](https://en.wikipedia.org/wiki/A_New_Kind_of_Science). A more general
  book about Complexity is Melanie Mitchell's _Complexity: a guided tour_.


## Artificial Neural networks ##
 
To understand the basics of artificial neural networks, I recommend thayt you
watch the four excellent videos at
<https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi> . The
last two of them focus on the backpropagation algorithm that allow to train
network to learn mapping.

Next, you can read and try to understand this
[implementation](https://visualstudiomagazine.com/articles/2017/06/01/back-propagation.aspx)
of the backpropagation algorithm.

Then, see a modern and efficient implementation of neural networks:
<https://pytorch.org/tutorials/beginner/deep_learning_nlp_tutorial.html>

More readings:

* [The Unreasonable Effectiveness of Recurrent Neural
  Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) on Andrej
  Karpathy's blog.

* [understanding LSTM
  Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

* [Pattern recognition and machine
  learning](https://www.springer.com/fr/book/9780387310732) by Christopher M.
  Bishop


## Natural Language Parsing ##

Parsing refers to building the syntactic structure of a sentence from the linear
sequence of words that compose it. Explore the [various parsing
algorithms](http://www.nltk.org/book/ch08.html)using the [Natural Language
Toolkit](https://www.nltk.org/).

## Neuroimaging ##

Check [nilearn](http://nilearn.github.io/) and
[nistats](https://nistats.github.io/) and
[MNE-python](https://martinos.org/mne/stable/index.html)



-------------------------------------------------------------------------------

# License #

All documents in this repository are distributed under the [Creative Commons
Attribution-ShareAlike 4](https://creativecommons.org/licenses/by-sa/4.0/). The
code is distributed under the [GPL v3
LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html).

-------------------------------------------------------------------------------

# Appendices #


## Instructions for Software installation ##

We will install:

  * **Python3**. 
  * The Python library **Expyriment** 
  * **Git** from <https://git-scm.com/>
  * **Sublime Text** (text editor) from [Sublime
  Text](https://www.sublimetext.com/) (Unless you are already using a text
  editor that you are happy with)
  * **R** from <https://cran.r-project.org/>
  * **Rstudio Desktop** from <https://www.rstudio.com>


### Warnings ###

* You will need to download about 1GB of software from the Internet. Therefore,
  make sure to have a decent connection.
* Make sure that you have at least 5GB of free space on your hard drive to
  unpack the softwares.
* You might need to have administrator rights to install some of the softwares.
  If you are using a computer from an Institution, this is not always the case.
  Check with your IT team.
* If you are using Windows 10, make sure your user name doesn't include spaces
  or characters that don't belong to the English alphabet (accents,
  ideograms,...). If you do, better create a new user with a

### Anaconda Python3 ###

We will make use of the [Anaconda distribution](https://www.continuum.io)

1. Download the Anaconda Python3 distribution Python from
   <https://www.continuum.io/download>.
2. Go to your download folder and execute the Anaconda3 file installer.
3. In the Anaconda Setup Wizard, beware, pay attention to the following options
   option:
   - verify that you Install for `Just Me (recommended)`, then click on `Next`
   - Accept the default Destination folder and click on `Next`
   - Check "Add Anaconda to my PATH" and check "Register
   Anaconda as my default Python" and click on `Install`
   - upon completion, click on 'Next', then `Finish`

### Expyriment ###

We will make use of the Python library [Expyriment](http://www.expyriment.org/)

1. Open a Terminal:

* Under Linux, launch `Terminal` from your applications menu or use
  `Ctrl-Alt-T`.
* under MacOS: type `terminal` in the Spotlight search field. Alternatively, you
  can open a `Finder` window and select the `Application` folder, then the
  `Utilities` folder, then double-click on the `Terminal` icon..
* Under Windows, launch `Anaconda Prompt`
 
2. Type:

    pip install expyriment


### Git ###

Git is a version control tool for software development, an indispensable tool for reproducible science. 

* **Ubuntu Linux** : Just execute `sudo apt install git` in a terminal.
* **Windows**: Download `Git for windows` from
  <https://git-scm.com/download/win> and execute it. Accept all the defaults.
* **MacOS***: Download the `Git for Lac` installer from
  <https://git-scm.com/download/mac> and execute it. Accept all the defaults.

To configure git, open a Terminal (or launch *Git Bash* under Windows) and type:

    git config --global user.name "your_first_and_last_names_here" 
    git config --global user.email your_email_here 
    git config --global core.editor nano


### Sublime Text Editor ###

Unless you already master a text editor, we recommend that you download and
install _Sublime Text_ from <https://www.sublime text.com/>. Follow the
instructions specific for your Operating System.


### R ###

R is a programming language specialized for data analyses.

 * **Windows** Download and install the latest version of R from
 <https://cran.rstudio.com/bin/windows/base/>
 * **MacOS**: Download and install the latest version of R from
 <https://cran.rstudio.com/bin/macosx/>
 * **Linux**: Find the version relevant for your distribution at
 <https://cran.rstudio.com/bin/linux/> and follow the instructions in the
 `README.html`  file.


### Rstudio Desktop ###

Rstudio is an Integrated Developpement Environment for R which greatly
simplifies the use of *RMarkdown**

Download and install the latest version of RStudio Desktop from
<https://www.rstudio.com/products/rstudio/download/>

--------------------------------------------------------------------------------

## How to open a Terminal ##

### Linux ###

Launch `Terminal` from your applications or use `Ctrl-Alt-T` (gnome, xfce), or
Win+Enter (i3)).


### MacOS ###

Type `terminal` in the Spotlight search field. 

Alternatively, you can open a `Finder` window and select the `Application`
folder, then the `Utilities` folder, then double-click on the `Terminal` icon..

### Windows ###

Launch `Git Bash` (This assumes that you have installed `Git for windows` from
<https://git-scm.com/download/win ):

 1. Click the Windows or Start icon.
 2. In the Programs list, open the Git folder.
 3. Click the option for Git Bash.

--------------------------------------------------------------------------------

## Resources to learn the command shell ##

Why learn the command shell?

> "What is a command shell? To properly understand the role of a shell, it's
> necessary to visualize what a computer does for you. Basically, a computer is
> a tool; in order to use that tool, you must tell it what to do—or give it
> “commands.” These commands take many forms, such as clicking with a mouse on
> certain parts of the screen. But that is only one form of command input.

> By far the most versatile way to express what you want the computer to do is
> by using an abbreviated language called script. In script, instead of telling
> the computer, “list my files, please”, one writes a standard abbreviated
> command word—‘ls’. Typing ‘ls’ in a command shell is a script way of telling
> the computer to list your files.1

> The real flexibility of this approach is apparent only when you realize that
> there are many, many different ways to list files. Perhaps you want them
> sorted by name, sorted by date, in reverse order, or grouped by type. Most
> graphical browsers have simple ways to express this. But what about showing
> only a few files, or only files that meet a certain criteria? In very complex
> and specific situations, the request becomes too difficult to express using a
> mouse or pointing device. It is just these kinds of requests that are easily
> solved using a command shell.

> For example, what if you want to list every Word file on your hard drive,
> larger than 100 kilobytes in size, and which hasn't been looked at in over six
> months? That is a good candidate list for deletion, when you go to clean up
> your hard drive. But have you ever tried asking your computer for such a list?
> There is no way to do it! At least, not without using a command shell.

> The role of a command shell is to give you more control over what your
> computer does for you. Not everyone needs this amount of control, and it does
> come at a cost: Learning the necessary script commands to express what you
> want done. A complicated query, such as the example above, takes time to
> learn. But if you find yourself using your computer frequently enough, it is
> more than worthwhile in the long run. Any tool you use often deserves the time
> spent learning to master it."

> (Extract from Emacs' eshell documentation)


  - [The Linux Command Line](http://linuxcommand.org/tlcl.php) by Williams
  Shotts.
  - [Openclassrooms
  MOOC](https://openclassrooms.com/courses/reprenez-le-controle-a-l-aide-de-linux)
  
--------------------------------------------------------------------------------  

## Resources to learn Python ##

  - MOOCs:
       * [Udemy's Python programming for absolute
       beginners](https://www.udemy.com/python-programming-for-absolute-beginners/)
       * [Code Academy's _Learn Python_
       module](https://www.codecademy.com/learn/learn-python)
       * [Openclassrooms' Apprendre à programmer en
       Python](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python)
       * [Python 3 : des fondamentaux aux concepts avancés du
       langage](https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/eb326b60bec3461ba2621fd4d6bd95b8/).
   - Books: [_Apprendre à Programmer avec
   Python3_](https://inforef.be/swi/python.htm) , [_Think
   Python_](http://greenteapress.com/thinkpython2/),

--------------------------------------------------------------------------------

## Resources to learn Git ##

  * The [Git Book](https://www.gitbook.com/)
  * Openclassrooms' MOOC
  <https://openclassrooms.com/en/courses/3321726-manage-your-code-with-git-and-github?status=published>
  * <https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners>
  * <https://git-scm.com/book/en/v2/Getting-Started-Git-Basics>
  * my own [git cheat
  page](http://www.pallier.org/version-control-at-your-fingertips-a-quick-start-with-git.html#version-control-at-your-fingertips-a-quick-start-with-git)

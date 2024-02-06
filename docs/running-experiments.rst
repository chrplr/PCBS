Experiments
===========

.. contents::


Simple reaction times
---------------------

Many psychology experiments measure *reaction-times* or *decision-times*.

The script :download:`simple-detection-visual-pygame.py <../experiments/pygame_reaction_times/simple-detection-visual-pygame.py>` is a simple detection experiment programmed with pygame. The task is simple: the participant must press a key as quickly as possible when a cross appears at the center of the screen. 

Download it and run it with::

     python simple-detection-visual-pygame.py

The results are saved in ``reaction_times.csv`` which you can inspect with any text editor.


If you are an R afficionado, you can open it and type::

   data = read.csv('reaction_times.csv')
   summary(data)
   attach(data)
   plot(RT)
   dev.new()
   plot(RT ~ Wait)

Here are my results:

   .. figure:: images/simple_rts.png

      Simple Reaction Times as a function of trial

   .. figure:: images/waittime_rts.png

      Relationship between wait time and reaction time


Browse the code of :download:`simple-detection-visual-pygame.py <../experiments/pygame_reaction_times/simple-detection-visual-pygame.py>`

It is pretty technical! This is because Pygame_ is meant to program simple video games, not psychology experiments.

A more adequate library for this task is Expyriment_ (another one is Psychopy_).

.. _Pygame: http://www.pygame.org
.. _Expyriment: http://www.expyriment.org
.. _Psychopy: http://www.psychopy.org


From here, we are going to use it to generate experiments.

Make sure you have installed Expyriment_::

   $ python
   >>> import expyriment


If an error message ``moduleNotFoundError: No module named 'expyriment'`` appears, check :doc:`software-installation`.

Let us start by downloading :download:`simple-detection-visual-expyriment.py <../experiments/xpy_simple_reaction_times/simple-detection-visual-expyriment.py>` and run it with::

    python simple-detection-visual-expyriment.py

Then, in the subfolder ``data``, locate a file with a name starting with  ``simple-detection...`` and the extension ``.xpd``. This is a text file containing the reactions times. To analyse them, download :download:`analyse_rt.py <../experiments/xpy_simple_reaction_times/analyse_rt.py>` and run::

    python analyse_rt.py data/simple-detection-visual-expyriment_*.xpd 


Compare the codes of ``simple-detection-visual-expyriment.py`` and ``simple-detection-visual-pygame.py``. This should convince you that using expyriment will make your life simpler if you need to program a psychology experiment.

The documentation of expyriment is available at http://docs.expyriment.org/. Have q a quick look at it, especially http://docs.expyriment.org/expyriment.stimuli.html

The basic principles of the ``expyriment`` module are introduced in https://docs.expyriment.org/Tutorial.html. 
I provide a minimal template at :download:`expyriment_minimal_template.py <../experiments/expyriment_minimal_template.py>` that one can use to start writing a expyriment script.

Exercises:

1. Modify ``simple-detection-visual-expyriment.py`` to display a white disk instead of a cross.

2. Modify  ``simple-detection-visual-expyriment.py`` to display a white disk on half of the trials and a gray disk on the other half of the trials (thesis experimental conditions should be shuffled randomly). Then modify it to display disks with four levels of gray. Thus you can assess the effect of luminosity on detection time. (see  :download:`xpy_simple_reaction_times/grey-levels.py <../experiments/xpy_simple_reaction_times/grey-levels.py>` for a solution using Expyriment's ``design.Block`` and ``design.Trial`` objects).

3. Modify  ``simple-detection-visual-expyriment.py`` to play a short sound (:download:`click.wav <../experiments/xpy_simple_reaction_times/click.wav>`) in lieu of displaying a visual stimulus (hint: use ``stimuli.Audio()``). Thus, you have created a simple audio detection experiment.

4. Download and run  :download:`simple-detection-audiovisual.py <../experiments/xpy_simple_reaction_times/simple-detection-audiovisual.py>`::  

        python simple-detection-audiovisual.py

There are three blocks of trials: a first one in which the target is always visual, a second one in which it is always a sound, and a third one in which the stimulus is, randomly, visual or auditory. Are we slowed down in the latter condition? Use :download:`analyse_audiovisual_rt.py <../experiments/xpy_simple_reaction_times/analyse_audiovisual_rt.py>` to analyse the reaction times.

Exercice: add python code to ``simple-detection-audiovisual.py`` to display instructions at the start of the experiment. 


Decision times
--------------

In the previous example, the user just had to react to a stimulus. This involved a very simple type of decision ("is a target present or not?")

Other tasks involves taking a decision about some property of the stimulus.

Exercise:
| - Modify :download:`simple-detection-visual-expyriment.py <../experiments/xpy_simple_reaction_times/simple-detection-visual-expyriment.py>` to display, rather than a cross, a random integer between 0 and 9 (hint: Use ``stimuli.TextLine()``). Now, the task is to decide if the figure is odd or even, by pressing one of two keys.


| Here is a solution: :download:`parity.py <../experiments/xpy_parity_decision/parity.py>`

| Comparing the average decision time to the time to react to a simple cross provides a (rough) estimate of the time to decide about the parity of a number. By the way, one can wonder what happens for multiple digits numbers: are we influenced by the flanking digits? 

| - Add feedback; when the subjects presses the wrong key, play the sound :download:`wrong-answer.ogg <../experiments/xpy_parity_decision/wrong-answer.ogg>`.


  Here is a solution: :download:`parity_feedback.py <../experiments/xpy_parity_decision/parity_feedback.py>`


Numerical distance effect
-------------------------

Exercise: Create a script to present, at each trial, a random number between 1 and 99, and ask the subject to decide wether the presented number is smaller or larger than ``55``. Plot the reactions times as a function of the number. 

Do you replicate the distance effect reported by Dehaene, S., Dupoux, E., & Mehler, J. (1990) in "Is numerical comparison digital? Analogical and symbolic effects in two-digit number comparison." *Journal of
Experimental Psychology: Human Perception and Performance*, 16, 626–641.?


Lexical Decision
----------------

In a lexical decision experiment, a string of characters is flashed at
the center of the screen and the participant has to decide if it is a actual
word or not, indicating his/her decision by pressing a left or right
button. Reaction time is measured from the word onset, providing an
estimate of the speed of word recognition.

Let us program such a task.


Step 1: stimuli listed in constants
+++++++++++++++++++++++++++++++++++

Modify the :download:`parity task script <../experiments/xpy_parity_decision/parity.py>` to display either a word or a pseudoword at each trial (in a random order).

For testing purposes, you can use the following variables::

   words = ['bonjour', 'chien', 'président']
   pseudos = ['lopadol', 'mirance', 'clapour' ]

A solution is proposed in :download:`lexdec_v1.py <../experiments/xpy_lexical_decision/lexdec_v1.py>`

Step 2: read stimuli from a csv file
++++++++++++++++++++++++++++++++++++

Then modify the lexical decision script to read the stimuli from a comma-separated text file (`stimuli.csv`) with two columns. Here is the content of ``stimuli.csv``::

    item,category 
    bonjour,W
    chien,W
    président,W
    lopadol,P
    mirance,P
    clapour,P

(hint: To read a csv file, one can use ``pandas.read_csv()``)

A solution is proposed in :download:`lexdec_v2.py <../experiments/xpy_lexical_decision/lexdec_v2.py>` 

Note: You can use a file comparator, e.g. `meld <https://meldmerge.org/>`__, to compare the two versions::

     meld lexdec_v1.py lexcdec_v2.py


Select words in a lexical dabatase
++++++++++++++++++++++++++++++++++

1. Go to http://www.lexique.org

   Click on “Recherche en Ligne” and play with the interface:

   -  enter ``5...5`` in the ``nbletters`` field
   -  enter ``^b.t$`` in the field ``ortho`` field (see
      http://www.lexique.org/?page_id=101 for more examples of pattern
      that can be used)

2. how many words of grammatical category (``cgram``) ‘NOM’, and of
   length 5 (``nblettres``), of lexical frequency (``freqfilms2``)
   comprised between 10 and 100 per millions are there in this database?
   (answer=367). Save these words (i.e. the content of the field
   ``Words``) into a ``words.csv`` file (you may have to clean manually,
   ie. remove unwanted columns, using Excel or Libroffice Calc).



Automatising database searches with R and Python
++++++++++++++++++++++++++++++++++++++++++++++++

To select words, rather than using the interface at
http://www.lexique.org, one can write scripts in R or Python. This
promotes reproducible science.

1. Open
   https://github.com/chrplr/openlexicon/tree/master/documents/Interroger-Lexique-avec-R
   and follow the instructions in the document
   ``interroger-lexique-avec-R.pdf``

2. Read
   https://github.com/chrplr/openlexicon/tree/master/scripts#selecting-lexical-items-with-python

To select 100 five letters long nouns for our lexical decision, execute::

   import pandas
   lex = pandas.read_csv("http://www.lexique.org/databases/Lexique382/Lexique382.tsv", sep='\t')
   subset = lex.loc[(lex.nblettres == 5) & (lex.cgram == "NOM") & (lex.freqfilms2 > 10) & (lex.nombre == 's')]
   samp = subset.sample(100)
   samp2 = samp.rename(columns = {'ortho':'item'})
   samp2.item.to_csv('words.csv', index=False)

This creates ``words.csv``.


Generate nonwords
+++++++++++++++++

1. Write a function that returns a nonword (a string containing random
   characters)

   ::

       def pseudo(length):
           """ returns a nonword of length `length` """

   Solution at :download:`create_nonwords.py <../experiments/xpy_lexical_decision/create_nonwords.py>`


2. Use this function to create a list of 100 nonwords and save it in a
   file ``"pseudowords.csv"`` (one pseudoword per line) (see
   https://www.pythontutorial.net/python-basics/python-write-text-file/)



Create a stimuli file
+++++++++++++++++++++

Merge ``words.csv`` and ``pseudowords.csv`` into a single
``stimuli2.csv`` file::

       import pandas
       w = pandas.read_csv('words.csv')
       w['category'] = 'W'
       p = pandas.read_csv('pseudowords.csv')
       p['category'] = 'P'
       allstims = pandas.concat([w, p])
       allstims.to_csv('stimuli2.csv', index=False)


Use `sys.argv` to pass the name of the file containing the list of stimuli  
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Modify `lexdec_v2.py` to be able to pass the name of the stimuli file as an argument on the command line::

        python lexdec_v3.py stimuli2.csv

(hint: use `sys.argv[]`; see https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/)

Solution at :download:`lexdec_v3.py <../experiments/xpy_lexical_decision/lexdec_v3.py>` 



Improving the pseudowords
+++++++++++++++++++++++++

1. Check out the pseudoword generator
   `UniPseudo <http://www.lexique.org/?page_id=582>`__

2. Generate a new list of pseudowords and add them to a new
   ``stimuli3.csv`` file


Data analysis
+++++++++++++

After running::

      python lexdec_v3.py stimuli2.csv

the subject's responses are stored in the subfolder ``data/`` contains a file ``lexdec...xpd``

You can download this :download:`xpd file <../experiments/xpy_lexical_decision/data/lexdec_v3_02_202112131227.xpd>` as an example.

1. Use ``pandas.read_csv(..., comment='#')`` to read the responses into a pandas dataframe.

2. Compute the average reaction times for words and for pseudo-words. 

3. Plot the distribution of reactions times using ``seaborn.boxplot()``

4. Use  ``scipy.stats.ttest_ind()`` to perform a Student t-test compairn gthe RTs of Words and Non-Words.

Check a solution :download:`analyze_RT.py <../experiments/xpy_lexical_decision/analyze_RT.py>`

Auditory Lexical Decision
+++++++++++++++++++++++++

Transform ``lexdec_v1.py`` into an auditory lexical decision script using the sound files 
from the   `lexical decision folder <../experiments/xpy_lexical_decision/>`:: 

    bonjour.wav
    chien.wav
    président.wav
    clapour.wav
    lopadol.wav
    mirance.wav


Solution at :download:`lexdec_audio.py <../experiments/xpy_lexical_decision/lexdec_audio.py>`


Finally
+++++++

Check out an example of a “real” lexical decision experiment at
https://chrplr.github.io/PCBS-LexicalDecision


Posner’s attentional cueing task
--------------------------------

Exercise (\*\*): Read about `Posner’s attentional cueing task <https://en.wikipedia.org/wiki/Posner_cueing_task>`__ and program the experiment. 

  See a solution in :download:`Posner-attention/posner_task.py <../experiments/xpy_Posner_attention_networks_task/posner_task.py>`

Stroop Effect
-------------

The Stroop effect (Stroop, John Ridley (1935). "Studies of interference in serial verbal reactions". Journal of Experimental Psychology. 18 (6): 643–662. doi:10.1037/h0054651) may be the most well known psychology experiment. Naming the color of the ink is difficult when there is a confict with the word itself.
This is interpreted as a proof that reading is automatic, i.e. cannot be inhibited.

In the previous chapter, we created Stroop cards with Pygame. 


    .. figure:: images/stroop.png
       :alt: Stroop Card


    Stroop card


  (see  :download:`create_stroop_cards.py <../experiments/xpy_Stroop_task/create_stroop_cards.py>`)

Download :download:`stroop.zip <../experiments/Stroop_task.zip>`. Extract the files and run::

   python stroop_task.py

The times are in the subfolder ``data``. Compute the average reading times as a function of the language (using ``R`` or ``python``).


Exercise: Program a Stroop task with a single colored word displayed at each trial. To record actual naming times, you will need to record (!) the subject's vocal response. A simple solution is to run a audio recording application while the script is running. You script should play a brief sound each time you present a target. Then, with a audio editor  (e.g. `Audacity <https://www.audacityteam.org/>`__), you can locate the times of presentation of stimuli and the onsets of vocal responses. Check out the program "CheckVocal" at https://github.com/0avasns/CheckVocal which does just that!





A general audio visual stimulus presentation script
---------------------------------------------------

In some experiments, we know in advance the precise timing of all
stimuli (the program flow does not depend on external events). A script that reads the timing of audiovisual stimuli in a csv file and presents them
at the expected times is available at https://www.github.com/chrplr/audiovis


Sound-picture matching using a touchscreen
------------------------------------------

The :download:`sentence-picture-matching.py <../experiments/xpy_sentence_picture_matching_test/sentence-picture-matching.py>` script presents a sound, followed by a picture and waits for the participant to press a button.


Exercise: Modify the previous script to present *two* pictures and use expyriment's `TouchScreenButtonBox` to record the subject's response, using the example from :download:`expyriment/touchscreen_test/touchscreen-test.py  <../experiments/xpy_touchscreen_test/touchscreen-test.py>`


More examples using Expyriment
------------------------------

Besides the examples from this course, you can find more expyriment scripts at

   * https://mbroedl.github.io/cognitive-tasks-for-expyriment/
   * https://github.com/expyriment/expyriment-stash


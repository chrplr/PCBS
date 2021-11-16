Experiments
===========

.. contents::


Simple reaction times
---------------------

Many psychology experiments measure *reaction-times* or *decision-times*.

The script :download:`simple-detection-visual-pygame.py <../experiments/reaction-times/simple-detection-visual-pygame.py>` is a simple detection experiment programmed with pygame. The task is simple: the participant must press a key as quickly as possible when a cross appears at the center of the screen. 

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


Browse the code of :download:`simple-detection-visual-pygame.py <../experiments/reaction-times/simple-detection-visual-pygame.py>`

It is pretty technical! This is because Pygame_ is meant to program simple video games, not psychology experiments.

A more adequate library for this task is Expyriment_ (another one is Psychopy_).

.. _Pygame: http://www.pygame.org
.. _Expyriment: http://www.expyriment.org
.. _Psychopy: http://www.psychopy.org


From here, we are going to use it to generate experiments.

Make sure you have installed Expyriment_::


     $ python
     >>> import expyriment


If an error message ``moduleNotFoundError: No module named 'expyriment'`` appears, check :doc:`software_installation.rst`.

Let us start by downloading :download:`simple-detection-visual-expyriment.py <../experiments/expyriment/simple_reaction_times/simple-detection-visual-expyriment.py>` and run it with::

    python simple-detection-visual-expyriment.py

Then, in the subfolder ``data``, locate a file with a name starting with  ``simple-detection...`` and the extension ``.xpd``. This is a text file containing the reactions times. To analyse them, download :download:`analyse_rt.py <../experiments/expyriment/simple_reaction_times/analyse_rt.py>` and run::

    python analyse_rt.py data/simple-detection-visual-expyriment_*.xpd 


Compare the codes of ``simple-detection-visual-expyriment.py`` and ``simple-detection-visual-pygame.py``. This should convince you that using expyriment will make your life simpler if you need to program a psychology experiment.

The documentation of expyriment is available at http://docs.expyriment.org/. Have q a quick look at it, especially http://docs.expyriment.org/expyriment.stimuli.html

The basic principles of the ``expyriment`` module are introduced in https://docs.expyriment.org/Tutorial.html. 
I provide a minimal template at :download:`/expyriment/expyriment_minimal_template.py <../experiments/expyriment/expyriment_minimal_template.py>` that one can use to start writing a expyriment script.

Exercises:

1. Modify ``simple-detection-visual-expyriment.py`` to display a white disk instead of a cross.

2. Modify  ``simple-detection-visual-expyriment.py`` to display a white disk on half of the trials and a gray disk on the other half of the trials (thesis experimental conditions should be shuffled randomly). Then modify it to display disks with four levels of gray. Thus you can assess the effect of luminisity on detection time.   

3. Modify  ``simple-detection-visual-expyriment.py`` to play a short sound (:download:`click.wav <../experiments/expyriment/simple_reaction_times/click.wav>`) in lieu of displaying a visual stimulus (hint: use ``stimuli.Audio()``). Thus, you have created a simple audio detection experiment.

4. Download and run  :download:`simple-detection-audiovisual.py <../experiments/expyriment/simple_reaction_times/simple-detection-audiovisual.py>`::  

        python simple-detection-audiovisual.py

There are three blocks of trials: a first one in which the target is always visual, a second one in which it is always a sound, and a third one in which the stimulus is, randomly, visual or auditory. Are we slowed down in the latter condition? Use :download:`analyse_audiovisual_rt.py <../experiments/expyriment/simple_reaction_times/analyse_audiovisual_rt.py>` to analyse the reaction times.

Exercice: add python code to ``simple-detection-audiovisual.py`` to display instructions at the start of the experiment. 


Decision times
--------------

In the previous example, the user just had to react to a stimulus. This involved a very simple type of decision ("is a target present or not?")

Other tasks involves taking a decision about some property of the stimulus.

Exercise:
| - Modify :download:`simple-detection-visual-expyriment.py <../experiments/expyriment/simple_reaction_times/simple-detection-visual-expyriment.py>` to display, rather than a cross, a random integer between 0 and 9 (hint: Use ``stimuli.TextLine()``). Now, the task is to decide if the figure is odd or even, by pressing one of two keys.


| Here is a solution: :download:`parity.py <../experiments/expyriment/parity_decision/parity.py>`

| Comparing the average decision time to the time to react to a simple cross provides a (rough) estimate of the time to decide about the parity of a number. By the way, one can wonder what happens for multiple digits numbers: are we influenced by the flanking digits? 

| - Add feedback; when the subjects presses the wrong key, play the sound :download:`wrong-answer.ogg <../experiments/expyriment/parity_decision/wrong-answer.ogg>`.


  Here is a solution: :download:`parity_feedback.py <../experiments/expyriment/parity_decision/parity_feedback.py>`


Numerical distance effect
-------------------------

Exercise: Create a script to present, at each trial, a random number between 1 and 99, and ask the subject to decide wether the presented number is smaller or larger than ``55``. Plot the reactions times as a function of the number. 

Do you replicate the distance effect reported by Dehaene, S., Dupoux, E., & Mehler, J. (1990) in "Is numerical comparison digital? Analogical and symbolic effects in two-digit number comparison." *Journal of
Experimental Psychology: Human Perception and Performance*, 16, 626–641.?


Posner’s attentional cueing task
--------------------------------

Exercise (\*\*): Read about `Posner’s attentional cueing task <https://en.wikipedia.org/wiki/Posner_cueing_task>`__ and program the experiment. 

  See a solution in :download:`Posner-attention/posner_task.py <../experiments/Posner-attention/posner_task.py>`

Stroop Effect
-------------

The Stroop effect (Stroop, John Ridley (1935). "Studies of interference in serial verbal reactions". Journal of Experimental Psychology. 18 (6): 643–662. doi:10.1037/h0054651) may be the most well known psychology experiment. Naming the color of the ink is difficult when there is a confict with the word itself.
This is interpreted as a proof that reading is automatic, i.e. cannot be inhibited.

In the previous chapter, we created Stroop cards with Pygame. 


    .. figure:: images/stroop.png
       :alt: Stroop Card


    Stroop card


  (see  :download:`create_stroop_cards.py <../experiments/stroop/create_stroop_cards.py>`)

Download :download:`stroop.zip <../experiments/stroop.zip>`. Extract the files and run::

   python stroop_task.py

The times are in the subfolder ``data``. Compute the average reading times as a function of the language (using ``R`` or ``python``).


Exercise: Program a Stroop task with a single colored word displayed at each trial. To record actual naming times, you will need to record (!) the subject's vocal response. A simple solution is to run a audio recording application while the script is running. You script should play a brief sound each time you present a target. Then, with a audio editor  (e.g. `Audacity <https://www.audacityteam.org/>`__), you can locate the times of presentation of stimuli and the onsets of vocal responses. Check out the program "CheckVocal" at https://github.com/0avasns/CheckVocal which does just that!


Lexical Decision Task
---------------------

In a lexical decision experiment, a string of characters is flashed at
the center of the screen and the participant has to decide if it is real
word or not, indicating his/her decision by pressing a left or right
button. Reaction time is measured from the word onset, providing an
estimate of the speed of word recognition.

-  Visit the web site http://www.lexique.org
-  Learn to query Lexical databases from R, follow the instructions in
   http://chrplr.github.io/PCBS/databases/lexique/interroger-lexique-avec-R.nb.html
-  Select 20 high frequency nouns, 20 low frequency nouns, 20 high
   frequency verbs and 20 low frequency verbs. They must all have
   a length of 5 to 8 characters.
-  Generate 50 pseudowords using either https://github.com/chrplr/openlexicon/blob/master/scripts/generate-pseudowords1/generate-pseudowords.R or `Wuggy <http://crr.ugent.be/programs-data/wuggy>`__
-  Program a lexical decision using the ``expyriment`` module. 
-  Run it and compute the average decision times using pandas


See a solution at https://github.com/chrplr/PCBS-LexicalDecision




A general audio visual stimulus presentation script
---------------------------------------------------

In some experiments, we know in advance the precise timing of all
stimuli (the program flow does not depend on external events). A script that reads the timing of audiovisual stimuli in a csv file and presents them
at the expected times is available at https://www.github.com/chrplr/audiovis


Sound-picture matching using a touchscreen
------------------------------------------

The :download:`sentence-picture-matching.py <../experiments/expyriment/sentence_picture_matching/sentence-picture-matching.py>` script presents a sound, followed by a picture and waits for the participant to press a button.


Exercise: Modify the previous script to present *two* pictures and use expyriment's `TouchScreenButtonBox` to record the subject's response, using the example from :download:`expyriment/touchscreen_test/touchscreen-test.py  <../experiments/expyriment/touchscreen_test/touchscreen-test.py>`


More examples using Expyriment
------------------------------

Besides the examples from this course, you can find more expyriment scripts at

   * https://mbroedl.github.io/cognitive-tasks-for-expyriment/
   * https://github.com/expyriment/expyriment-stash


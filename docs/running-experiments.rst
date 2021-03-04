Experiments
===========

.. contents::


Simple reaction times
---------------------

1. Write a script that presents a series of trials in which a dot or a
   cross is presented at the center of the screen and the participant
   must click on the mouse as quickly as possible. The reaction times
   must be recorded in a file for further analyses.

2. Here is a :download:`solution using pygame <../reaction-times/simple-detection-visual-pygame.py>`. Run it and check `reaction_times.csv`.

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


Exercice: Modify the previous script to present two pictures and use expyriment's `TouchScreenButtonBox` to record the subject's response, using the example from
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
stimuli (the program flow does not depend on external events). A script that reads the timing of audiovisual stimuli in a csv file and presents them
at the expected times is available at https://www.github.com/chrplr/audiovis


More examples using expyriment.org
----------------------------------

-  Check out https://github.com/expyriment/expyriment-stash
- Fork it and contribute by adding new scripts!

Experiments
===========

.. contents::


Simple reaction times
---------------------

Pygame version
~~~~~~~~~~~~~~

Download :download:`simple-detection-visual-pygame.py <reaction-times/simple-detection-visual-pygame.py>`. Run it with::

     python reaction-times/simple-detection-visual-pygame.py

The task is simply to press a key as quickly as possible when a cross appears at the center of the screen. The results are save in ``reaction_times.csv``. Open ``R`` and type::

   data = read.csv('reaction_times.csv')
   with(data, plot(RT))
   with(data, plot(RT ~ Wait))

Here are my results:

   .. figure:: simple_rts.png

      Simple Reaction Times as a function of trial

   .. figure:: waittime_rts.png

      Relationship between wait time and reaction time


Browse the code of :download:`simple-detection-visual-pygame.py <reaction-times/simple-detection-visual-pygame.py>`

Expyriment version
~~~~~~~~~~~~~~~~~~

Download :download:`solution using expyriment <../reaction-times/simple-detection-visual-expyriment.py>` and run it with::

    python simple-detection-visual-expyriment.py

Type::

   cd data
   ls

There should be a file with a name starting with  ``simple-detection...`` and the extension ``.xpd``. This is a text file containing the result. Where are going to quickly examine them using the Pandas_ library.

.. _Pandas: https://pandas.pydata.org/

On the command line, with the ``data`` folder as working directory, launch ``ipython`` and execute::

   %matplotlib
   import matplotlib.pyplot as plt
   import pandas as pd

   # you may have to use a different filename than 'simple-detection.xpd'
   d = pd.read_csv('simple-detection.xpd', comment='#')

   d.head()
   d.RT.mean()
   d.RT.std()
   d.RT[5:].mean()

   plt.stem(d.RT)
   plt.close()
   plt.hist(d.RT)


Read https://docs.expyriment.org/Tutorial.html to understand the basic principles of the ``expyriment`` module.

Check out :download:`/expyriment/expyriment_minimal_template.py <../expyriment/expyriment_minimal_template.py>`

Modify :download:`reaction-times/simple-detection-visual-expyriment.py <../reaction-times/simple-detection-visual-expyriment.py>` to play a short sound (`click.wav`) in lieu of displaying a cross. Thus you have created a simple audio detection experiment.

Modify the script to have 3 blocks of trials: one in which the target is visual, one in which it is audio, and one in which it is randomly
   visual or auditory. Are we slowed down in the latter condition?



Sound-picture matching
----------------------

The :download:`../expyriment/sentence_picture_matching/sentence-picture-matching.py <../expyriment/sentence_picture_matching/sentence-picture-matching.py>` scripts presents a sound, followed by a picture and waits for the participant to press a button.


Exercise: Modify the previous script to present *two* pictures and use expyriment's `TouchScreenButtonBox` to record the subject's response, using the example from :download:`expyriment/touchscreen_test/touchscreen-test.py  <../expyriment/touchscreen_test/touchscreen-test.py>`


Posner’s attentional cueing task
--------------------------------


Execise (\*\*\*): Read about `Posner’s attentional cueing task <https://en.wikipedia.org/wiki/Posner_cueing_task>`__ and program the experiùent. 

See a solution in :download:`../Posner-attention/posner_task.py <../Posner-attention/posner_task.py>`


Stroop Effect
-------------

In the previous chapter, we created Stroop cards with Pygame. 


.. figure:: images/stroop.png
   :alt: Stroop card

   Stroop card


  (see  :download:`create_stroop_cards.py <../stroop/create_stroop_cards.py>`)

Download :download:`stroop.zip <../stroop.zip>`. Extract the files and run::

   python stroop_task.py

The naming times are in the subfolder ``data``. Compute the average reading times as a
   function of the language (using ``R`` or ``python``).


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

- Check out https://github.com/expyriment/expyriment-stash
- Fork it and contribute by adding new scripts!

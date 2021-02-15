Creating stimuli
================

.. contents::


Static visual stimuli
~~~~~~~~~~~~~~~~~~~~~


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



Dynamic visual stimuli
~~~~~~~~~~~~~~~~~~~~~~

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


Creating and playing sounds
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


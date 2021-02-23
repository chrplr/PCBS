****************
Creating stimuli
****************

.. contents::


Static visual stimuli
=====================


We are going to use module `pygame <http://www.pygame.org>`__ to generate visual displays

Here is a python script (:download:`square.py <../visual-illusions/square.py>`) using pygame that opens a window and displays a square. Run it.  

.. code:: python

    """ Display a square.

          See https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
    """

    import pygame

    # Colors are triplets containint RGB values (see <https://www.rapidtables.com/web/color/RGB_Color.html>
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (127, 127, 127)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    W, H = 500, 500  # Size of the graphic window size
    # Note that (0,0) is at the *upper* left hand corner of the screen.

    #  create the window
    pygame.init()
    screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)

    screen.fill(WHITE)  #  fill it with white

    # Draw a rectangle
    width, height = 200, 200
    left, top = (W - width) // 2, (H-height) // 2
    pygame.draw.rect(screen, BLUE, (left, top, width, height))

    pygame.display.flip()  # display the backbuffer

    # save the image into a file
    pygame.image.save(screen, "square-blue.png")
    
    # wait until the window is closed
    done = False
    while not done:
          pygame.time.wait(10)
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                   done = True


The `quick introduction on drawing with pygame <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>`__ provides some help.

Exercise (*): modify the script to
   - change the color of the rectangle to RED
   - change the size of the rectangle to 100 x 300



It is possible to draw other shapes. Check out the two scripts :download:`circle.py <../visual-illusions/circle.py>` and
and :download:`triangle.py <../visual-illusions/triangle.py>`.

Exercice (*): modify the script :download:`circle.py <../visual-illusions/circle.py>` to draw two circles, one red and on blue, side-by-side  (check out the solution :download:`two_circles.py <../visual-illusions/two_circles.py>`)


Kanizsa illusory contours
-------------------------

Exercice (**): Using :download:`square.py <../visual-illusions/square.py>` and   :download:`circle.py <../visual-illusions/circle.py>` create a new script to display the (right) Kanisza square.

   .. figure:: images/Kanizsa-square.jpeg
      :alt: Kanizsa square

      Kanizsa square

   .. figure:: images/Kanizsa1.png
      :alt: Kanizsa triangle

      Kanizsa triangle

   You can then check out :download:`kanizsa-square.py <../visual-illusions/kanizsa-square.py>`

   To find out more about this illusion, do a google search with the keywords `illusory contours`.

Herman grid
-----------

-  Starting from :download:`square.py <../visual-illusions/square.py>`, write a
   program to display the `Herman grid <https://en.wikipedia.org/wiki/Grid_illusion>`__

   .. figure:: images/HermannGrid.png
      :alt: Hermann Grid

      Hermann Grid

   Hints:

   -  use paper and pencil to draw the figure
   -  find out the formulas to compute the left top of the square in the
      ith row and jth column
   -  in your python scripts, use nested for loops over rows and columns
      to display each square one by one

-  Check out :download:`grid.py <../visual-illusions/grid.py>`

- Optional: Read https://stackabuse.com/command-line-arguments-in-python/ and
  use the ``sys.argv[]`` list from the ``sys`` module (or use the ``argparse``
  module) to get from the command lines the number of columns, rows, the size of
  square and the size of the margins. Play with those parameters to see if you
  can make the illusion come and go.

Ebbinghaus-Titchener
--------------------

-  Create the static `Ebbinghaus–Titchener stimulus <http://www.abc-people.com/illusion/illusion-3.htm#axzz5SqeF15yC>`__.

   .. figure:: images/ebbinghaus-titchener.png
      :alt: Ebbinghaus illusion

      Ebbinghaus illusion

Hint: A bit of `trigonometry <https://en.wikipedia.org/wiki/Unit_circle>`__ can help:
if you want to draw a circle at angle ``alpha`` from the horizontal line
and at distance ``R`` from the origin, the coordinates of its center are
``(R * cos(alpha), R * sin(alpha))``

-  Check out my solution
   :download:`ebbinghaus.py <../visual-illusions/ebbinghaus.py>`


Honeycomb and Extinction illusions.
-----------------------------------

The extinction illusion is a variant of the Herman grid:

.. figure:: images/extinction.png
   :alt: Extinction illusion

   Extinction illusion

-  Program the stimulus (the lines can be horizontal and vertical rather
   than oblique)

-  Check out :download:`exctinction.py <../visual-illusions/extinction.py>`

Here is the Honeycom illusion:

.. figure:: images/honeycomb.png
   :alt: Honeycomb illusion

   Honeycomb illusion

-  Watch `this video <https://www.youtube.com/watch?v=fDBYSFDXsuE>`__
-  Check out `Bertamini, Herzog, and Bruno (2016). “The Honeycomb Illusion: Uniform Textures Not Perceived as Such.” <https://doi.org/10.1177/2041669516660727.%20https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5030753/pdf/10.1177_2041669516660727.pdf>`__

-  Optional: Try to run :download:`Honeycomb.py <../visual-illusions/Honeycomb.py>`, available from `Bertamini’s web site <https://www.programmingvisualillusionsforeveryone.online/scripts.html>`__ .  The challenge is to install the mopdule `psychopy` and all its dependencies (notably `wxPython`).



Random-dot stereograms
----------------------

A random-dot stereogram is a pair of images of random dots which,
when viewed with the eyes focused on a point in front of or behind the
images, produces a sensation of depth. See
https://en.wikipedia.org/wiki/Random_dot_stereogram.

.. figure:: images/stereogram.jpg
   :alt: stereogram

   stereogram

-  Write a script that generate random-dot stereograms.

-  Check out :download:`random_dot_stereogram.py <../random-dot-stereograms/random_dot_stereogram.py>`


More illusions
--------------

Check out `Akiyoshi KITAOKA's illusion pages <http://www.ritsumei.ac.jp/~akitaoka/index-e.html>`. Try to program some of his stimuli, e.g. the first one at <http://www.psy.ritsumei.ac.jp/~akitaoka/o1saishe.html>


Dynamic visual stimuli
======================

Illusory line-motion illusion.
--------------------------------

-  Check out `Jancke et al (2004) Imaging cortical correlates of illusion in early visual cortex <http://www.cnbc.cmu.edu/cns/papers/nature02396.pdf>`__.

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
===========================

Install the `simpleaudio` module::

        pip install simpleaudio

Then run the quick check with ipython::

        import simpleaudio.functionchecks as fc 
        fc.LeftRightCheck.run() 

Check out `simpleaudio's tutorials <https://simpleaudio.readthedocs.io/en/latest/tutorial.html>`__

Study :download:`sound_synth.py <../sound/sound_synth.py>`

Exercise (**) Using functions from the sound_synth` module, write a script that loads the wav file ``cymbal.wav`` and plays it 10 times, at a rhythm of one per second. (Warning: a basic knowledge of numpy arrays is necessary).

Then, check :download:`cycle.py <../sound/cycle.py>`


Sound localisation from binaural dephasing
------------------------------------------

Exercise (**) Take a mono sound and create a stereo sound by progressively dephasing
the two channels.

Hints: load the sound file into a one dimensional numpy array, make
a copy of the array and shift it, assemble the two arrays in a
bidimensional array (matrix) and save it as a stereo file


Pulsation (Povel & Essen, 1985)
-------------------------------

Exercise (***) Create rhythmic stimuli such as the ones described in `Povel and Essen (1985) Perception of Temporal Patterns <http://www.cogsci.ucsd.edu/~creel/COGS160/COGS160_files/PovelEssens85.pdf>`__


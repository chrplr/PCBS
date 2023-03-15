Online experiments
++++++++++++++++++

To program online experiments, you need to acquire basic knowledge of:

* HTML (Hyper Text Markup Language). The language that is used to write documents that can be displayed by WEB browsers.
* CSS (Cascading style sheets). The language that describes the style of HTML elements. 
* Javascript. The programming language spoken by the browsers.
  


HTML Basics
===========

Browser display (including with jsPsych) relies on HTML, most often
HTML5. Let us see how it works.

   **To go further** The point of this lecture is to raise your
   understanding of HTML, CSS, JS & JsPsych enough to code your own
   experiments. For those who may want to go further / better understand
   the magic at hand, I will leave notes as the present one in the form
   of quotes. They are not necessary, but may answer questions you may
   have.

HTML document structure overview
--------------------------------

A HTML file contains:

- A declaration that you are using HTML5;

 
   ``<!DOCTYPE html>``

   **What happens if you remove it? - A note on browser compatibility**
   Most browsers will not care and behave similarly. However, you have
   no guarantee that it will do so: in fact, Internet Explorer will just
   treat this as plain text! In the case of an online experiment, this
   means you may lose some participants/data. Even worse, this means
   that you may have flawed data without realising it!

-  A head where most webpage-level elements (e.g. title) are defined,

.. code-block:: html


   <head></head>

..

   **Tags in HTML** Here, we write “head” between chevrons. This is
   known as a *tag* in HTML. Tags tell information to your browser, here
   that this is the head of the document. Notice that we have two tags
   here, one after another. Think of them as brackets: everything that
   we want to define in the head will be enclosed between the tags.
   Accordingly, the first tag is called the *opening tag* and the other
   one the *closing tag*. Closing tags specifically have an additional
   ``/`` slash at the start). Note that a few tags do not enclose
   content and only use a single tag, with the slash ``/`` at the end
   (e.g. line breaks ).

-  A body which will contain the main elements of the page, especially
   what will be displayed to the user.

.. code-block:: html


   <body></body>

Our first document thus look like this, and is read as a blank page.

.. code-block:: html


   <!DOCTYPE html>
   <head></head>
   <body></body>

Setting up a title
------------------

You can use the ``<title>`` tag in the head of the document to set a
title.

.. code-block:: html


   <head>
     <title>My first page!</title>
   </head>

Simple shapes
=============

Square
------

Creating divs
~~~~~~~~~~~~~

Rectangles are very simple shapes to draw in HTML. Although there are a
variety of way, we will start by using colored ‘divs’.

   **Divs** Divs are precisely HTML element with a rectangle shape. They
   are most often used as generic containers, but this won’t interest us
   right now.

You may use the following body for your HTML code.

.. code-block:: html


   <body>
    <div></div>
   </body>

As you may notice, the page is still blank. Press f12 to understand why.

   **Inspector** f12 opens your browser’s inspector, which allows you to
   see the HTML code of the web page you are currently browsing.

Open the body tags and hover over the ``<div>`` element. It should show
you the element on the webpage, and give you its dimensions. Notice the
issue? It is simply of width 0, so of course you won’t see it. TODO
IMAGE

Setting size
~~~~~~~~~~~~

Let’s specify a width for our ``<div>``. To do so, will add
specifications to our tag, so that the browser knows how to deal with
the element it marks. Here, we will use the ``style`` keyword to specify
a style that forces a 200px width and a 200px height.

The result is as follows:

.. code-block:: html


   <body>
    <div style = "width: 200px; height: 200px"></div>
   </body>

Notice that the style specification has a precise syntax:
``keyword: value``, with successive entries being separated by
semicolumns ``;``. The style won’t be applied if you omit semicolumns,
or use equal sign instead of columns ``:``! Similarly, the value part
must have a unit. Here we use pixels (``px``), but there are many
others!

   **Setting size with style in HTML** Here we use style to specify the
   width and height of the element. There are other ways, with specific
   ``width`` and ``height`` tags. However, these specifications may
   behave unexpectedly at times, which is why we will use ``style`` in
   this lecture.

..

   **Size units in HTML** To set the size of an element, we have many
   useful units that can adapt to each screen. Here we used pixels
   (``px``) which are the base unit of computer screens. Since pixel
   size may vary between computers, we could also use centimeters
   (``cm``) to get a constant value. Conversely, we could want to adapt
   our display to the size of the window, and use viewport height
   (``vh``) and width (``vw``). If we want more specifically to adapt to
   a given container, we can use percents (``%``).

Setting background color
~~~~~~~~~~~~~~~~~~~~~~~~

If you update the page, you’ll see that you in fact still don’t see the
div. Check again with f12; it should highlight an actual square this
time. The reason why you don’t see it is that, by default, elements take
the background color of their parent, here ``<body>``. So you are
looking at a white square on a white background, which is a good reason
not to see it!

To specify the color (actually background color of the square), you may
use another specification in the style:

.. code-block:: html


   <body>
    <div style = "...; background-color = "red""></div>
   </body>

..

   **Names with spaces** Names with spaces are always annoying when
   programming, since they should actually be taken as a whole by the
   language. To prevent this, several alternatives exist (such as
   CamelCase or snake_case), with each language having its usually
   prefered alternative. In HTML/CSS, we replace spaces ```` with dashes
   ``-``.

   **Changing background color of the body** Like with any other
   elements, you can change the style of the body. Try setting it to
   ``gray`` with the ``background-color`` specification!

Centering
~~~~~~~~~

At this point, you should finally have a square ! However, it lies sad
and alone in the corner of the screen. We’ll see more on the placing of
elements, but for now we will stick to simple solutions.

First, we can specify the position of the left corner on the square in
the style. This works similar to setting the dimensions of the square.

.. code-block:: html


   <div style = "...; top: 100px; left: 200px"></div>

Although we are moving the square, it is still not centered on the
screen. It is pointless to use trial-and-error here, as it won’t be
centered anymore if you resize your browser window. To get a unit
relative to the size of the window, we will use viewport height (``vh``)
and width (``vw``). ``1vh`` correspond to 1% of the *height* of the
window. ``1vw`` is 1% of the *width* of the window. Do not confuse both!

As such, we can (somewhat) center the square using the following style:

.. code-block:: html


   <div style = "...; top: 50vh; left: 50vw"></div>

Notice that we are still slightly off, since we actually centered the
top left corner of the square. To correct this we will apply a simple
translation, of half the square dimensions.

.. code-block:: html


   <div style = "...;
     top: 50vh; left: 50vw;
     transform: translate(-50%, -50%)"></div>

..

   **Percent unit** The percent unit ``%`` refers to the dimension of
   the parent container. E.g., for our ``div`` within the body, setting
   ``top`` and ``left`` to 50% would put our top left corner to the
   center of the body. Here, with the call to ``translate``, it becomes
   as if self centered, and the translation is thus of 50% of the
   *square* size.

ID
~~

We can specify the id of an element using ``id = "my-id"``.

   IDs are not necessary, but they come in handy for several reasons.
   The main reason for us now is to be able to identify component in the
   inspector view. It also helps identification of the element by other
   elements, which helps for applying a specific style (more later) or
   retrieving the element in JavaScript (more even later , see next
   session).

And voilà, we have a neat centered square! The final code can be found
here: [square.py (PLACEHOLDER)].

Circle
------

As said above, ``<div>``\ s are rectangle elements, but they may also be
slightly modified. As an example, their corners can be rounded, a
property which we will make use of to make circles. For that we will use
a ``border-radius`` specification within our style.

.. code-block:: html


   <div style = "...; border-radius = 50%"></div>

You may try and change the value of this ``border-radius``, to better
understand the behavior we’re making use of. Notice how much we start
definitely resorting to tricks here, which may (and will) be
insufficient at some point. HTML proposes alternatives that are more
suited to drawing shapes, such as *Scalable Vector Graphics* (SVG).

In HTML, SVGs are elements like divs, but which are designed to contain
shapes. Here we will use the ``<circle>`` shape element. We will specify
its properties (radius, center, color) with tags directly linked to the
element.

.. code-block:: html


   <svg>
     <circle cx="100" cy="100" r="100" fill="red"/>
   </svg>

..

   Notice that we are at the same level as style **TODO** Also notice
   that here we space things with spaces and not semicolumns. some
   attributes are specific to ``<circle/>``

What is going wrong here? Well, f12 can enlighten us here again. As you
may see, the circle is cut by the border of the container. In other
words, our 150x300 pixels containers does not have the right shape to
display the whole shape. We thus have to specify the size of the
container, with the usual ``style`` attribute.

.. code-block:: html


   <svg style = "height = 200px; width=200px">
     <circle cx="100" cy="100" r="100" fill="red"/>
   </svg>

Triangle
--------

A good reason to learn about SVGs is that you can’t draw triangles with
divs (or rather, you will have an extremely hard time doing so). With
SVGs, doing so is much easier, as you can draw any polygon using the
``<polygon/>`` tag. ``<polygon/>`` takes a specific attribute named
``points`` which takes a list of integers corresponding to the
coordinates of the polygon’s vertices. Integers in the list will be
paired to create the *x* and *y* coordinates of each point.

You may separate integers with spaces ```` or commas ``,`` alike. In the
code for an isoceles triangle below, I use a mix of both: spaces
separate *x* and *y* coordinates, while commas separates vertices.

.. code-block:: html


   <svg>
       <polygon points="0 200, 200 200, 100 0" fill="red" />
   </svg>

Style usage
-----------

In all the above examples, you probably reused the same value for the
``style`` attribute, over and over. HTML provides a convenient way to
deal with this by providing a style sheet. It may be defined in the head
of the file as per the following code (which defines an empty style).

.. code-block:: html


   <head>
     <style>
       <!-- Put the style here -->
     </style>
   </head>

..

   **Comments in HTML** The ``<!--`` and ``-->`` serve as opening and
   closing markers for comments in HTML. This is made so that you’ll
   (hopefully) never need them for any other purpose, since HTML is
   designed to display all kinds of texts.

We can now define our stylesheet. First, let us make all divs have a red
background by default.

.. code-block:: html


   <style>
     div {
       background-color: red
     }
   </style>

This property can now be removed from the ``style`` of the ``<div>``
elements of the body. Try it!

We now want to deal with the centering elements. Since we don’t want to
center everything, we’ll manually flag elements that should be centered
using the ``class`` attribute. To define a style for a class named
``my-class``, we reuse the same syntax as before, but replace the
element name (``div``) with the class name ``my-class`` preceded by a
dot ``.``. The dot indicates that this style applies to a class.

.. code:: code-block:: html <style>

     .centered {
       position: absolute;
       top: 50vh; left: 50vw;
       transform: translate(-50%, -50%);
     }
   </style>

..

   **Cascading Style Sheets** Style sheets can apply at several levels:
   to all elements of the document, to all elements of a kind
   (e.g. divs), to all elements of a special class (defined with the
   ``class`` attribute), or elements with a given id… These levels apply
   one after another, with most specific style sheets applying over the
   more generic ones; they are, in a sense, cascading. This precisely
   gave this ‘style’ language its name: *Cascading Style Sheets*, or
   *CSS* for short.

To apply this style to our divs, we have to specify that this class
applies such as in the following example.

.. code-block:: html


   <body>
     <div class = "centered">
     </div>
   </body>

..

   **Multiple classes** You may apply several classes to a single
   element, simply by listing them with a space in between different
   classes: e.g. ``class = "centered circle"`` if you also happen to
   have a ``.circle`` style.

Of course, redefining it at the beginning of each sheet can be very
tedious, which is why style sheets are often defined in their own
``.css`` file. Move everything we previously defined within ``<style>``
into a file named ``shapes.css``. You may now load the styl in your HTML
file, using the following code in the ``<head>`` section.

.. code-block:: html


   <head>
     <link rel="stylesheet" href ="./shapes.css">
     </link>
   </head>

Be careful, if you move the file from the current folder you will have
to update the ``href`` attribute with the new path!

Combining shapes
================

You now have the basics to recreate the following illusion from
`previous
lectures <https://pcbs.readthedocs.io/en/latest/stimulus-creation.html#static-visual-stimuli>`__:
- Two circles ([solution (PLACEHOLDER)]) - Troxler ([solution
(PLACEHOLDER)]) - Kanisza square ([solution (PLACEHOLDER)])

A small note for Kanisza
------------------------

If you did Kanisza (or peeked at the solution), you may have notice that
we didn’t actually draw circle slices, but rather hid the undesired
parts of the circle with a square. This is because there is no simple
way to do it with the tools we have now.

   **The issue of the present design** Since the result is visually
   satisfying, one may think it is not a big deal to leave it as such.
   However, remember that the whole point of the Kanisza illusion is to
   trigger a form *that does not exist in the first place*! You do not
   always control what happens on the screen, and as such this may
   introduce some terrible noise in your data. As an example, since HTML
   elements are actually displayed one after another, old computers
   might show the square with a delay that could be a comfounding factor
   to the effect you want to show!

In the next section, we will learn how to draw these slices using
canvas. These are some sort of ‘drawing boards’ that have to be drawn
upon using JavaScript.

Combining shapes with JS
========================

Plugging JavaScript into HTML
-----------------------------

You can plug a JavaScript script in HTML using the ``<script>`` tag.
Note that everything within this tag will be interpreted as JavaScript.

For our first script, we will display a simple text on the console. To
this end, we may use the line code ``console.log(myText)``.

.. code-block:: html


   <body>
     <script>
       // All that is written here is JavaScript!
       console.log("Bonjour le monde !");
     </script>
   </body>

..

   TODO Here we use the method ``log`` from the object ``console``. This
   relationship is embodied by the ``.`` between the two.

Do not expect to see anything on your HTML page! The text is printed in
the console, which you can access alongside the inspector. This can be
very useful for debugging!

Basic syntax of JavaScript
--------------------------

The following code shows you the basics of the JavaScript synta

.. code-block:: javascript

   let x = 0;
   function printNumber(x){
     console.log(x);
     return -1;
   }

   console.log(x);
   printNumber(x);
   x = 1;
   printNumber(x);
   printNumber(0);
   console.log(printNumber(x));

..

   The semicolumn ``;`` is facultative if you use line breaks.

Output:

:: 

   0
   0
   1
   0
   1
   -1

**If you only get one 0** in the console, check that it is not because
the two zeros were wrapped in the same line (a small ``2`` on the
right).

Loops
~~~~~

This code prints integers from 0 to 5.

.. code-block:: javascript 

   for (i = 0; i < 5; i++){
     console.log(i);
   }

Modifying elements with innerHTML
---------------------------------

.. code-block:: javascript 

   document.body.innerHTML +=
     "<div style = "background-color:red; height: 200px; width: 200px"></div>"

..

   **Multiline strings in JS** It is done by adding a backslash ``\``
   continuation at the end of each line.

.. code-block:: javascript 

      "This is \
      a \
      multiline string".

   Be careful not to put any space after the continuation!

   
Modifying elements with pure JS
-------------------------------

Create element with ``document.createElement("div")`` (you may use which
ever type you prefer) Modify element attributes (/ property):
``element.id = "my-id"`` Modify style:
``element.style.height = "200px"``

Drawing on canvas.
------------------

Using JsPsych
=============

JsPsych is a library that allows you to easily create experiments from
premade plugins. First, download the library in version 7.3.0 from the
`following
link <https://www.github.com/jspsych/jspsych/releases/latest/download/jspsych.zip>`__, create a subfolder ``jspsych-7.3.0`` in your code folder and unzip ``jspsych.zip`` there. The library's code should be in ``./jspsych-7.3.0/dist``.

Loading JsPsych
---------------

The library itself consists in the ``jspsych.js`` JavaScript file, which
we will load in our experiment. To load an external script in HTML, one
can simply use the ``src`` attribute of the ``<script>`` tag, with the
path to the script file as a value.

.. code-block::  javascript

   <!DOCTYPE html>
   <head>
     <title>A simple jsPsych experiment</title>
   </head>
   <body>
     <script src="./jspsych-7.3.0/dist/jspsych.js">
     </script>
   </body>

Here, you only loaded all the helper functions of JsPsych. You will now
need to load create an instance of the plugin using ``initJsPsych``, which will
handle all your JsPsych-related instructions.

.. code-block::  javascript

     <script src="./jspsych-7.3.0/dist/plugin-html-keyboard-response.js">
     </script>
		 
   <script>
     const jsPsych = initJsPsych();
   </script>

..

   **Constants** Notice that here we use a ``const`` instead of a
   ``let`` or ``var`` declaration. This means that the value of this
   variable can not be changed. This is convenient to prevent undesired
   bugs from redeclaring a variable.

Timeline and trials
-------------------

As said in the introduction of the JsPsych lecture series, JsPsych
revolves around successive trials forming what is called a *timeline*.
This timeline is implemented as an array containing all the trials.
Arrays in JavaScript are defined using square brackets ``[]``. We will
first start with an empty timeline, which we’ll gradually fill.

.. code-block::  javascript

   let timeline = [];

..

   **Initializing non-empty arrays** Arrays may be implemented with
   items already in them, by simply putting the items within the square
   brackets ``[]`` and separating them with commas ``,``. As an example,
   if you already have two trials ``trial1`` and ``trial2``, you may
   create an array containing both (in this order) with
   ``[trial1, trial2]``.

We now want to create trials to fill our timeline with. You can think of
trials as a parametrized task, with the task being effectively encoded
as a JsPsych plugin.

For now, we will stick to simple decision tasks. Stimuli will be
displayed from simple HTML code similar to what we used previously. The
dedicated plugin is (logically) called ``jsPsychHtmlKeyboardResponse``.

We can thus instantiate a trial with this plugin, using an object
structure. Long story short, an object structure is defined using
brackets ``{}``; it holds properties, defined with ``name: value``, and
separated by commas ``,``. Below is the instantiation of a
``jsPsychHtmlKeyboardResponse`` trial.

.. code-block::  javascript

   let trial = {
     type: jsPsychHtmlKeyboardResponse,
   };

..

   **Trailing commas** You may notice I left a comma ``,`` after the
   ``type`` property, although I did not specify any other property.
   This is not a typo: it is what we call a *trailing comma*. JavaScript
   licenses them as it makes it easy to add new elements.

You may now add the trial to the timeline using the ``push`` method of
arrays, which adds an element at the end of it.

.. code-block::  javascript

   timeline.push(trial);

..

   **In-place modifications** TODO

And we can finally run the experiment with our 1-trial timeline, using
the ``jsPsych`` instance we previously created.

.. code-block::  javascript

   jsPsych.run(timeline);

Your final code should look like this:

.. code-block::  javascript

   // We initialize JsPsych
   const jsPsych = initJsPsych();

   // We create an empty timeline
   let timeline = [];

   // We create a basic decision trial
   let trial = {
     type: jsPsychHtmlKeyboardResponse,
   };

   // We add this trial to the timeline
   // /!\ Do not forget this essential step /!\
   timeline.push(trial);

   // We run the timeline with JsPsych
   jsPsych.run(timeline);

You may now run it by opening your HTML page. Press a key and see what
happens .

If nothing happens (and this should be the case!), just do as you should
always do in this situation: open the console. It should display you the
following error message in red: “You must specify a value for the
stimulus parameter in the html-keyboard-response plugin.”. Such errors
are fatal and prevent the script from proceeding any futher.

The issue here is that, although we did specify the type of our trial,
we did not give it the necessary parameters for it to run properly. As
the message tells us, we actually didn’t specify what stimulus this
decision task was about. In fact, the plugin displays “unspecified” as
the top of the page.

Let us first specify a simple text prompting to press any key as our
stimulus. We can do it as follows.

:: 

   let trial = {
     type: jsPsychHtmlKeyboardResponse,
     stimulus: "Bonjour! Please press any key."
   }

Now, loading the page should prompt you with the text you entered. If
you press any key, it disappears: the experiment is actually finished.

   We could also use ``jsPsychImageKeyboardResponse`` if we want to
   pre-generate our stimuli as images and display them directly. More
   precisions
   `here <https://www.jspsych.org/7.3/tutorials/rt-task/#part-4-displaying-stimuli-and-getting-responses>`__.

Using the console interactively: accessing experiment data
----------------------------------------------------------

Before going any further, let us test that the experiment worked as
intended. If so, the data in our trial should have been registered. You
can access JsPsych’s saved data using ``jsPsych.data.get()``

   If we break down this line, here we access the property ``data`` of
   our ``jsPsych`` instance. But ``data`` actually saves many
   metainfomations which are not of interest to us. Luckily; this
   ``data`` object has a convenient function (or method) ``get()`` that
   allows us to precisely access test data.

Although you could use it in your script to access it at any given time
(and, e.g. print it), you can also use the console to access it whenever
you want. Just type the line into it!

It should print you something of the form
``Object { trials: (1) […] }``, which you can unfold: ``trials``
precisely contain the data about each trial. Right now, it should only
contain one single trial, as an object with ``rt``, ``stimulus``, and
``response`` properties.

Response keys
-------------

In your trial’s data, ``response`` may contain any single key, since all
are allowed by default. However, decision tasks will require them to
press one of two chosen keys. We can specify the valid keys using (yet
another) parameter: ``choices``. As a value, we will pass it an array of
valid keys in the forms of strings, here ‘f’ and ‘j’

:: 

   let trial = {
     type: jsPsychHtmlKeyboardResponse,
     stimulus: "Bonjour! Please press any key."
     choices: ['f', 'j'].
   }

Practice: color-detection task
------------------------------

You should now be able to program a simple experiments. Say we want to
test if shapes interfere with color detection: subjects will have to
flag the color of successive shapes. They will have to press ‘f’ for red
shapes and ‘j’ for blue shapes. The design should be 3 shapes
(rectangle, triangle, circle) by 2 colors (red and blue), with 6 trials
in total. The order will be fixed, and you are in charge of choosing it!

   Beware of priming effects!

You can find a solution
`here <../Examples/jspsych-color-detection-fixed-order>`__.

   **Difference between viewport width (``vw``) and height (``vh``) and
   percents (``%``)** If you used percents, you may notice that the
   figures are slightly off.JsPsych uses a content wrapper, so ``%``
   refers to it size.

Randomizing order
-----------------

Of course, an experiment with trials in a fixed order is not
interesting, because any effect we find may be restricted to this
specific order.

JsPsych provides use with a function to shuffle an array, i.e. order its
element randomly: ``jsPsych.randomization.shuffleNoRepeats``. To
randomize the timeline, use:

.. code-block::  javascript

   timeline = jsPsych.randomization.shuffleNoRepeats(timeline);

Here, we create a random array from the timeline. The ``...NoRepeats``
part specifies that equal elements are not in successive order. Since we
only have a single occurrence of each trial, no item in our timeline is
equal, and it thus does not have any effect here.

However, it allows more to do more than prevent repetition of identical
trials: we can also specifically define what it means to be equal. To do
so, we simply pass an additional argument: a function that returns
whether two trials are equals. Here, we want to define equal trials as
those which have the same shape.

First, let’s add a shape property to our trial object. If you coded
cleanly, creating a trial should be done using parameters (in a ``for``
loop or even better a function) including a ``shape`` variable. Adding
it to the trial should thus be fairly straightforward.

.. code-block::  javascript

   trial = {
     ...
     color: color;
   }

..

   **Additional properties to the trial** In JsPsych, a trial is a
   javascript object that uses some mandatory and/or optional
   properties. It will only ever look up those, but that doesn’t mean
   you can not add other properties.

You may check with the console that properties added this way will not
be added in the data! The next session will develop how to do it.

In the mean time, we can now define our equality function:

.. code-block::  javascript

   timeline = jsPsych.randomization.shuffleNoRepeat(timeline,
     function(trial1, trial2){return trial1.shape == trial2.shape});

..

   **Factorial design** We used here a 3 by 2 factorial design, which
   was simple enough to generate with a ``for`` loop. For more
   complicated factorial design, you may want to look up the
   ```jsPsych.randomization.factorial``
   function <https://www.jspsych.org/7.0/reference/jspsych-randomization/#jspsychrandomizationfactorial>`__.

Adding data to be saved
-----------------------

Although we could theoretically retrieve the color and property from the
HTML string, it would be rather uneasy. We can rather save directly
``color`` and ``shape`` values in our data, using the ``data`` property
of our trial. ``data`` will be an object that contains, as properties,
everything we might want to plug into our data.

:: 

   let trial = {
     ...
     data: {color: "red", shape: "blue"},
   }

As a small exercise: how can we update our equality test function?

Saving answer
-------------

If you go through the trials and try to analyse your data, you may
notice that ``response`` only contains the pressed keys, and not the
color responded by the participant. While you could theoretically
reconstruct it during your data analysis, this approach is error-prone
(in particular when you randomly assign responses keys).

   **Random response keys** It is advised to randomly assign response
   keys to your participants, since there are some known interactions
   between response side and task performance (see, e.g., `the SNARC
   effect <https://psycnet.apa.org/doiLanding?doi=10.1037%2F0096-3445.122.3.371>`__).
   To implement such a random choice, you may want to have a look at the
   ```Math.random``
   function <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random>`__
   from native JavaScript.

However, since the response is not known *a priori*, there is not much
you can do as you create the trial (but you should register response
side for safekeeping!). JsPsych provides us with a neat workaround with
the ``on_finish`` property of trials. ``on_finish`` has to be a function
that takes the trial’s data as an argument; it is not expected to return
anything.

We can thus use on finish to modify the response encoded in our data:

.. code-block::  javascript

   let trial = {
     ...,
     on_finish: function(data){
       // We first save the response key in a more adequate variable
       data.responseKey = data.response;

       // We then save the actual responded color as the response
       if(data.responseKey == "f"){
         data.response = "red";
       } else {
         data.response = "blue";
       }
     }
   };

..

   **Ternary operators** The ``if-else`` construction here is rather
   cumbersome. Most languages (including JavaScript) offer a ternary
   operator ``?:`` that allow to replace it: ``condition ? a : b`` is
   ``a`` when ``condition`` is true, and ``b`` otherwise. Try it!

This design is however **very** error-prone: if the **[F]** key is not
litteraly encoded as the character ``"f"`` (or whichever you use here),
it may assign the wrong color to the response key! You also have to
adapt everything each time you want to change the keys or the color.

We’ll only focus on the first issue of key encoding here, since you
should be able to have a code that is more robust to keys/color changes
on your own. JsPsych provides us with a way to compare the encoding of a
key to a representation such as ``"f"``:
``jsPsych.pluginAPI.compareKeys``.

.. code-block::  javascript

   let trial = {
     ...,
     on_finish: function(data){
       // We first save the response key in a more adequate variable
       data.responseKey = data.response;

       // We then save the actual responded color as the response
       if(jsPsych.pluginAPI.compareKeys(data.responseKey, "f")){
         data.response = "red";
       } else {
         data.response = "blue";
       }
     }
   };

Audio feedback
--------------

Here are two .wav sounds: `correct.wav <../res/sound/correct.wav>`__ and
`incorrect.wav <../res/sound/incorrect.wav>`__.We want to play them at
the end of the trial to give audio feedback to our participants.

To play audio in JavaScript, you first have to create ``Audio`` objects
containing the audio file you want to play.

.. code-block::  javascript

   let audio = new Audio(pathToFile);

You can now play the audio using the ``play`` function of this audio
object:

.. code-block::  javascript

   audio.play()

As small exercise, you should now be able to play a valid auditory
feedback at the end of every trial. Hint below!

.. raw::  html

   <details>

.. raw::  html

   <summary>

Hint

.. raw::  html

   </summary>

:: 

   You should use the `on_finish` property we saw above!

.. raw::  html

   </details>

Saving the data
---------------

The experiment is almost ready! What we want to do now is to save our
data. It can be saved locally (on the machine that took the experiment),
or, more interestingly, on a distant server.

In this course, we will only use local save, which is still useful for
debugging and/or piloting. Our ``data`` object possesses a ``localSave``
method that precisely saves the experiment’s data as a ``.csv`` file:

.. code-block::  javascript

   jsPsych.data.get().localSave('csv', "data.csv");

Where (i.e. when) to should this instruction be executed? At the end of
the experiment! Similarly to trials, our JsPsych instance can be created
with an additional ``on_finish`` method. Note that unlike for trials,
this one does not take a ``data`` argument.

.. code-block::  javascript

   let jsPsych = initJsPsych({
     on_finish: function(){
       jsPsych.data.get().localSave('csv', "data.csv");
     }
   })

..

   You may be surprised that we make a reference to the variable
   ``jsPsych`` within its actual creation. This is possible because
   JavaScript will not evaluate functions before actually calling them.
   In other words, when ``on_finish`` is called at the end of the trial,
   the function will then (and only then) look at whatever variable
   labeled ``jsPsych`` it can find. By then, we will have created the
   variable already and so it will work. I personally dislike this
   design which is error-prone (what if some code changes the value of
   ``jsPsych``?); however, this is what is officially used in `JsPsych’s
   documentation <https://www.jspsych.org/7.0/overview/data/>`__. One
   protection I can propose is to make ``jsPsych`` a constant with the
   ``const`` keyword. In JS like in most languages, constants have a
   name in capital letters and spaces ```` are replaced by underscores
   ``_``: ``JS_PSYCH``.

Of course, youwant to go further than just storing the data on the
participant’s computer. We want to retrieve it on our laboratory server!
Since the code will be very tributary of how said server is set up, you
should see details with your lab’s referent (where can you store the
code, what protections…). You may find some documentation
`here <https://www.jspsych.org/7.0/overview/data/#storing-data-permanently-as-a-file>`__

Random ID
---------

You may notice that we haven’t done anything about participant IDs.
Assigning each participant a *random* ID is of course mandatory in
psychology experiments. JsPsych provides use with a convenient way to
generate random IDs of a given length:
``jsPsych.randomization.randomID``.

We can create a 10-character long ID for our participant with the
following line. We use a constant here because it should never be
modified.

.. code-block::  javascript

   const ID = jsPsych.randomization.randomID(10);

We can now add this ID info to all our trials. To this end, you can
modify each trial individually using the ``data`` property as above.
Another way is to add a common property to the whole data, as describe
in the
`documentation <https://www.jspsych.org/7.0/overview/data/#adding-data-to-all-trials>`__.

As a final note, you will most likely want to use this ID for the data
file you save at the end of the experiment: if all participants’ files
have the same name, they will overwrite one another!

.. code-block::  javascript

   jsPsych.data.get().localSave('csv', "data-"+ID+".csv");

..

   **String formatting** To get a cleaner script, you may use string
   formatting to plugging code output into a string. Formatted string
   use this quote
   \`\`\ ``and have codes marked between brackets``\ ``, the opening bracket being preceded by a dollar sign``\ $\ ``. An exemple:``\ Bonjour!
   My name is ${my_name}!`.

Final code
----------

You can find a solution for the final code
`here <../Examples/jspsych-color-decision-task>`__. Make sure to try out
to code it first! Practice makes perfect.

I did not do it in this example, but you should leave an end message to
your participants, thanking them for their time. You can create a
``jsPsychHtmlKeyboardResponse`` trial with no possible response by
giving the ``choices`` property the ``"NO_KEYS"`` value.

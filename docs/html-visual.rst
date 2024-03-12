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

An HTML file can be as simple as this: open your notepad, copy-paste the
following lines, and save the file as ``test.html`` (or whatever name
you want, but keep the ``.html`` extension).

.. code:: html

   <!DOCTYPE html>
   <html>
     <head></head>
     <body></body>
   </html>

Now try to open this file (if your computer asks, use a web browser).
Congratulations, you just created your first HTML page ! Granted, it’s a
bit bland; we’ll populate this later. Let us quickly go over what we
have here.

Our HTML file contains: - A declaration that we are using HTML5;

``<!DOCTYPE html>``

-  A head where most webpage-level elements (e.g. title) will be
   defined,

``<head></head>``

-  A body which will contain the main elements of the page, especially
   what will be displayed to the user.

``<body></body>``

   **What happens if you remove DOCTYPE? - A note on browser
   compatibility** Most browsers will not care and behave similarly.
   However, you have no guarantee that it will do so: in fact, Internet
   Explorer will just treat your file as plain text! In the case of an
   online experiment, this means you may lose some participants/data.

..

   **Tags in HTML** Here, we write ``head`` and ``body`` between
   chevrons ``<>``. This is known as a *tag* in HTML. Tags tell
   information to your browser, here that this is the head of the
   document.

   Notice that we have two tags here, one after another. Think of them
   as brackets: everything that we want to define in the head will be
   enclosed between the tags. Accordingly, the first tag is called the
   *opening tag* and the other one the *closing tag*. Closing tags
   specifically have an additional ``/`` slash at the start).

   Note that a few tags do not enclose content and only use a single
   tag, with the slash ``/`` at the end (e.g. line breaks ``<br/>``).

Setting up text and title
-------------------------

So far, our document is empty: it does only display a blank page and the
title is basically the files path. Can you change the title to
``My HTML file`` and display the following text in your page?

``Hello, world!``

You can find a solution in the following file:
`hello_world.html <../stimuli/html-and-js/hello_world.html>`__. But before looking
at it…

**Some questions for you!** - Did you end up having
``My HTML file Hello, world!`` written on your page?

This is expected and means that you probably miss a tag: how can your
browser know that you want this to be a title? Placing it inside the
head is not sufficient: you need to use the ``<title></title>`` tag!

-  Did you specify the title within the head, and the text within the
   body?

If so, good, but would it work otherwise? Try, and see that it could
indeed. But we generally prefer to do this kind of stuff this way. More
onto this in the lecture if I have time.

-  What happens if you try to write ``Enchanté, cher monde !`` instead
   of ``Hello world!``?

There is a chance that some of you will have a weird character at the
end of ``Enchanté``, while others will have no issues. This is because
your browser does not necessarily know how to interpret those weird
diacritics that non-English speakers use. To fix this issue, you can
specify to your computer that you want to use utf-8 encoding, inserting
``<meta charset="utf-8">`` in the head of your file.

Simple shapes
=============

Let us now create more interesting pages than text alone! Just like we
did with python, we start with shapes.

Square
------

Creating divs
~~~~~~~~~~~~~

Rectangles are very simple shapes to draw in HTML. Although there are a
variety of way, we will start by using colored ‘divs’. Here is the code
for what we will first try to achieve:
` <../stimuli/html-and-js/SimpleShapes/square-div.html>`__

   **Divs** Divs are precisely HTML element with a rectangle shape. They
   are most often used as generic containers, but this won’t interest us
   right now.

You may use the following body for your HTML code.

.. code:: html

   <body>
    <div></div>
   </body>

As you may notice, the page is still blank. Press f12 to understand why.

   **Inspector** On Windows and Linux, f12 opens your browser’s
   inspector, which allows you to see the HTML code of the web page you
   are currently browsing. It can be a little less straightforward on
   MacOS depending on the distribution; you may find some guidance
   `here <https://developer.apple.com/documentation/safari-developer-tools/inspecting-safari-macos>`__.

Open the body tags and hover over the ``<div>`` element. It should show
you the element on the webpage, and give you its dimensions. Notice the
issue? It is simply of width 0, so of course you won’t see it.

TODO IMAGE

Setting size
~~~~~~~~~~~~

Let’s specify a width for our ``<div>``. To do so, will add
specifications to our tag, so that the browser knows how to deal with
the element it marks. Here, we will use the ``style`` keyword to specify
a style that forces a 200px width and a 200px height.

The result is as follows:

.. code:: html

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

.. code:: html

   <body>
    <div style = "...; background-color: red"></div>
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

.. code:: html

   <div style = "...; top: 100px; left: 200px"></div>

Although we are moving the square, it is still not centered on the
screen. It is pointless to use trial-and-error here, as it won’t be
centered anymore if you resize your browser window. To get a unit
relative to the size of the window, we will use viewport height (``vh``)
and width (``vw``). ``1vh`` correspond to 1% of the *height* of the
window. ``1vw`` is 1% of the *width* of the window. Do not confuse both!

As such, we can (somewhat) center the square using the following style:

.. code:: html

   <div style = "...; top: 50vh; left: 50vw"></div>

Notice that we are still slightly off, since we actually centered the
top left corner of the square. To correct this we will apply a simple
translation, of half the square dimensions.

.. code:: html

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

And voilà, we have a neat centered square!

Circle
------

Rounded divs
~~~~~~~~~~~~

Let’s move on to the next shape: a circle! We will create it in two
ways. The first way will use divs, as we just saw:
` <circle-div.html>`__

As said above, ``<div>``\ s are rectangle elements, but they may also be
slightly modified. As an example, their corners can be rounded, a
property which we will make use of to make circles. For that we will use
a ``border-radius`` specification within our style.

.. code:: html

   <div style = "...; border-radius: 50%"></div>

You may try and change the value of this ``border-radius``, to better
understand the behavior we’re making use of. Notice how much we start
definitely resorting to tricks here, which may (and will) be
insufficient at some point. HTML proposes alternatives that are more
suited to drawing shapes, such as *Scalable Vector Graphics* (SVG). The
adapted code can be found
`here <../stimuli/html-and-js/SimpleShapes/circle-svg.html>`__.

SVGs
----

In HTML, SVGs are elements like divs, but which are designed to contain
shapes. Here we will use the ``<circle>`` shape element. We will specify
its properties (radius, center, color) with tags directly linked to the
element.

.. code:: html

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

.. code:: html

   <svg style = "height: 200px; width: 200px">
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

.. code:: html

   <svg>
       <polygon points="0 200, 200 200, 100 0" fill="red" />
   </svg>

You may separate integers with spaces ```` or commas ``,`` alike. In the
code for an isoceles triangle above (`full
file <../stimuli/html-and-js/SimpleShapes/triangle-svg.html>`__), I use a mixture
of both: spaces separate *x* and *y* coordinates, while commas separates
vertices.

Style usage
-----------

Regardless of whether you used divs or svgs above, you most likely used
the same ``style`` attribute to center the shape, over and over. To
avoid tiresome repetitions, HTML provides a convenient way to deal with
this: providing a stylesheet. A stylesheet essentially defines keywords,
which can be later used to apply the desired style to an element. You
may find an example for our square `here <../stimuli/html-and-js/SimpleShapes/>`__.

Definition in the head
~~~~~~~~~~~~~~~~~~~~~~

The simplest way to define a style is to do so in the ``head`` of your
document. You can also do it in a separate file; more on that later.

.. code:: html

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

.. code:: html

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

.. code:: html

   <style>
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

.. code:: html

   <body>
     <div class = "centered">
     </div>
   </body>

..

   **Multiple classes** You may apply several classes to a single
   element, simply by listing them with a space in between different
   classes: e.g. ``class = "centered circle"`` if you also happen to
   have a ``.circle`` style.

Definition in a separate file.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course, redefining it at the beginning of each sheet can be very
tedious, which is why style sheets are often defined in their own
``.css`` file. Move everything we previously defined within ``<style>``
into a file named ``shapes.css``. You may now load the style in your
HTML file, using the following code in the ``<head>`` section. Here is
how it looks like in `our square
file <../stimuli/html-and-js/SimpleShapes/square-css.html>`__, using a `separate
spreadsheet <../stimuli/html-and-js/SimpleShapes/square.css>`__. Notice how the
code is much simpler to read!

.. code:: html

   <head>
     <link rel="stylesheet" href ="./shapes.css">
     </link>
   </head>

Be careful, if you move the file from the current folder you will have
to update the ``href`` attribute with the new path!

Exercises
=========

It is now your turn.

Recreate the shapes
-------------------

Could you rewrite the code for the circle (a solution
`here <../stimuli/html-and-js/SimpleShapes/circle-style.html>`__) and the triangle
()\ `here <../stimuli/html-and-js/SimpleShapes/triangle-style.html>`__)? Bonus
points if you manage to use a single stylesheet for both!

Illusions
---------

Could you recreate the complex stimuli seen in `this
lecture <https://pcbs.readthedocs.io/en/latest/stimulus-creation.html#displaying-geometric-shapes>`__,
this time in html? 1. The two circles (a solution
`here <../Illusions/two-circles.html>`__) 2. The troxler effect
(`here <../Illusions/troxler.html>`__) 3. Kanisza’s square
(`here <../Illusions/kanisza-square.html>`__)

And anything else your heart may wish for! Remember that programming
makes perfect (in programming, at least).

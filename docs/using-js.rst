Using JavaScript
================

Combining shapes with JS
------------------------

[The previous chapter] should have given you the basics to recreate,
using HTML, the following illusions from `previous lectures on
Python <https://pcbs.readthedocs.io/en/latest/stimulus-creation.html#static-visual-stimuli>`__:
1. The two circles (a solution :download:`here <../stimuli/html-and-js/Illusions/two-circles.html>`)
2. The troxler effect (:download:`here <../stimuli/html-and-js/Illusions/troxler.html>`)
3. Kanisza’s square (:download:`here <../stimuli/html-and-js/Illusions/kanisza-square.html>`)

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

Plugging JavaScript into HTML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can plug a JavaScript script in HTML using the ``<script>`` tag.
Note that everything within this tag will be interpreted as JavaScript.

For our first script, we will display a simple text on the console. To
this end, we may use the line code ``console.log(myText)``.

.. code:: html

   <body>
     <script type="javascript">
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
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following code shows you the basics of the JavaScript syntax. You
may try it in you browser console, which is accessible in the same
window as the inspector.

.. code:: javascript

   // We define a variable x with value 0.
   let a = 0;

   // We define a function that prints a number
   function printNumber(x){
     console.log(x);
   }

   // We define a function that add 1
   function add1(x){
     return x + 1;
   }

   printNumber(a);
   a = 1
   printNumber(a);

..

   The semicolumn ``;`` is facultative if you use line breaks.

Loops
~~~~~

JavaScript uses two kind of loops you may be familiar with: ``for``
loops, and ``while`` loops

For loops
^^^^^^^^^

For loops are used to execute a piece of code a *given* number of times.
As an example, below we want to print 5 integers, from 0 to 4.

.. code:: javascript

   for (let i = 0; i < 5; i++){
     console.log(i);
   }

The way to understand the code is as follows: “starting from i=0, do i++
(increase i by 1) as long as i < 5”.

JavaScript also allows you to loop through collections such as lists.
You can define a list between square brackets ``[]`` using commas ``,``
as separators, like this : ``[1, 2, 3]``.

There are two ways to loop through a list: ``for (let x in l)`` and
``for (let x of l)``. Try this in your browsers. Can you spot the
difference?

.. code:: javascript

   for (let x in [1,2,3]){
     console.log(x);
   }

   console.log("---");

   for (let x of [1, 2, 3]){
     console.log(x);
   }

Modifying elements with innerHTML
---------------------------------

The main interest of javascript is that it can interact with HTML. As an
example, you can directly modify the HTML code of a document using
``document.body.innerHTML``. Here is :download:`an
example <../stimuli/html-and-js/SimpleShapes/square-js-inner-html.html>`.

.. code:: javascript

   document.body.innerHTML +=
     "<div style = 'background-color:red; height: 200px; width: 200px'></div>"

..

   **Multiline strings in JS** It is done by adding a backslash ``\``
   continuation at the end of each line.

   ::

      "This is \
      a \
      multiline string".

   Be careful not putting any space after the continuation!

Modifying elements with pure JS
-------------------------------

Of course, this innerHTML technique will not bring us very far, since we
are basically rewriting the HTML code with an additional JavaScript
layer… Hopefully, we can also create everything directly using
JavaScript. We can create an element using the
``document.createElement`` method. We simply have to specify what kind
of element we want to have, e.g., a div, by passing it as an argument :
``let element = document.createElement("div")``.

Then, we can modify its attributes, among which its style, using the
following code snippets : ``element.id = "my-id"`` or
``element.style.height = "200px"``. You can find
:download:`here <../stimuli/html-and-js/SimpleShapes/square-pure-js.html>` a code for the
red square, with the JavaScript part detailed below.

.. code:: javascript

   let square = document.createElement('div');
   square.id = "my-square";
   square.style.background = "red";
   square.style.position = "absolute";
   square.style.width = "200px";
   square.style.height = "200px";
   square.style.top = "50vh";
   square.style.left = "50vw";
   square.style.transform = "translate(-50%, -50%)";

   // Do not forget to add your element to the document!
   document.body.appendChild(square)

..

   **Chains of properties.** Note the weird ``square.style.X`` syntax.
   This is because JavaScript works with objects: square is an object,
   that is a kind of box that stores several variables and functions.
   One of these variables is the id, which we access with style.id.
   Another is the style, which we access with square.style. The style
   itself is an object, that has many variables like the background, the
   position… all of which are character strings, or strings for short.

Drawing on canvas.
------------------

Back to our problem of Kanisza’s square, we can introduce canvas, which
are exactly that: canvas on which we will paint. We can create the canvas using the same method as above. You can find the resulting file
:download:`here <../stimuli/html-and-js/SimpleShapes/circle-js.html>`.

.. code:: javascript

   let canvas = document.getElementById("tutorial");

To paint on it, we will want to access its ‘context’.

.. code:: javascript

   let ctx = canvas.getContext("2d");

Here is some code to draw a 50x50 rectangle, at the position (10, 10)
–of the canvas!

.. code:: javascript

   // Specify the color
   ctx.fillStyle = "rgb(200, 0, 0)";
   // Fill the rectangle
   ctx.fillRect(10, 10, 50, 50);

Drawing a circle is slightly more complicated, because there is no
proper built-in function. Instead, we will draw the path of our brush.

.. code:: javascript

   ctx.beginPath();
   // Draw a full circle (from 0 to 2pi radians) at position (100, 75) with radius 50px
   ctx.arc(100, 75, 50, 0, 2 * Math.PI);
   // Draw the path
   ctx.stroke();

   // Or we could fill it!
   // ctx.fill();

..

   \*\* TODO a note about style vs height & width

Think that you'll fill based on your starting point! You can move it use `ctx.moveTo(x,y)`.

Back to Kanisza
~~~~~~~~~~~~~~~

You can now recreate a cleaner version of Kanisza's square:
:download:`here <../stimuli/html-and-js/Illusions/kanisza-square-with-js.html>`

Using JsPsych
-------------

JsPsych is a library that allows you to easily create experiments from
premade plugins. First, download the library in version 7.3.0 from the
`following
link <https://www.github.com/jspsych/jspsych/releases/latest/download/jspsych.zip>`__,
and unzip it in your code folder. The following codes assume that the
folder is named ``jspsych-7.3.0``.

We will start by creating a very simple ‘experiment’ that greets the
participant and registers any key they press :
:download:`jspsych-hello-world-example.html <../web-experiments/experiments/jspsych-hello-world-example.html>`.

Loading JsPsych
~~~~~~~~~~~~~~~

The library itself consists in the ``jspsych.js`` JavaScript file, which
we will load in our experiment. To load an external script in HTML, one
can simply use the ``src`` attribute of the ``<script>`` tag, with the
path to the script file as a value.

.. code:: html

   <!DOCTYPE html>
   <head>
     <title>A simple jsPsych experiment</title>
   </head>
   <body>
     <script src="./jspsych-7.3.0/jspsych.js">
     </script>
   </body>

Here, you only loaded all the helper functions of JsPsych. You will now
create an instance of the plugin using ``initJsPsych``, which will
handle all your JsPsych-related instructions.

.. code:: javascript

   const jsPsych = initJsPsych();

..

   **Constants** Notice that here we use a ``const`` instead of a
   ``let`` or ``var`` declaration. This means that the value of this
   variable can not be changed. This is convenient to prevent undesired
   bugs from redeclaring a variable.

Timeline and trials
~~~~~~~~~~~~~~~~~~~

As said in the introduction of the JsPsych lecture series, JsPsych
revolves around successive trials forming what is called a *timeline*.
This timeline is implemented as an array containing all the trials.
Arrays in JavaScript are defined using square brackets ``[]``. We will
first start with an empty timeline, which we’ll gradually fill.

.. code:: javascript

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

.. code:: javascript

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

.. code:: javascript

   timeline.push(trial);

..

   **In-place modifications** TODO

And we can finally run the experiment with our 1-trial timeline, using
the ``jsPsych`` instance we previously created.

.. code:: javascript

   jsPsych.run(timeline);

Your final code should look like this:

.. code:: javascript

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

.. code:: javascript

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~

In your trial’s data, ``response`` may contain any single key, since all
are allowed by default. However, decision tasks will require them to
press one of two chosen keys. We can specify the valid keys using (yet
another) parameter: ``choices``. As a value, we will pass it an array of
valid keys in the forms of strings, here ‘f’ and ‘j’

.. code:: javascript

   let trial = {
     type: jsPsychHtmlKeyboardResponse,
     stimulus: "Bonjour! Please press any key."
     choices: ['f', 'j'].
   }

Practice: color-detection task
------------------------------

You should now be able to program a simple experiment. Say we want to
test if shapes interfere with color detection: subjects will have to
flag the color of successive shapes. They will have to press ‘f’ for red
shapes and ‘j’ for blue shapes. The design should be 3 shapes
(rectangle, triangle, circle) by 2 colors (red and blue), with 6 trials
in total. The order will be fixed, and you are in charge of choosing it!

   Beware of priming effects!

You can find a solution
:download:`here <../web-experiments/experiments/jspsych-color-detection-fixed-order>`.

   **Difference between viewport width (``vw``) and height (``vh``) and
   percents (``%``)** If you used percents, you may notice that the
   figures are slightly off.JsPsych uses a content wrapper, so ``%``
   refers to it size.

Randomizing order
~~~~~~~~~~~~~~~~~

Of course, an experiment with trials in a fixed order is not
interesting, because any effect we find may be restricted to this
specific order.

JsPsych provides use with a function to shuffle an array, i.e. order its
element randomly: ``jsPsych.randomization.shuffleNoRepeats``. To
randomize the timeline, use:

.. code:: javascript

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

.. code:: javascript

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

.. code:: javascript

   timeline = jsPsych.randomization.shuffleNoRepeat(timeline,
     function(trial1, trial2){return trial1.shape == trial2.shape});

..

   **Factorial design** We used here a 3 by 2 factorial design, which
   was simple enough to generate with a ``for`` loop. For more
   complicated factorial design, you may want to look up the
   ```jsPsych.randomization.factorial``
   function <https://www.jspsych.org/7.0/reference/jspsych-randomization/#jspsychrandomizationfactorial>`__.

Adding data to be saved
~~~~~~~~~~~~~~~~~~~~~~~

Although we could theoretically retrieve the color and property from the
HTML string, it would be rather uneasy. We can rather save directly
``color`` and ``shape`` values in our data, using the ``data`` property
of our trial. ``data`` will be an object that contains, as properties,
everything we might want to plug into our data.

.. code:: javascript

   let trial = {
     ...
     data: {color: "red", shape: "blue"},
   }

As a small exercise: how can we update our equality test function?

Saving answer
~~~~~~~~~~~~~

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

.. code:: javascript

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

.. code:: javascript

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
~~~~~~~~~~~~~~

Here are two .wav sounds: :download:`correct.wav <../web-experiments/res/sound/correct.wav>` and
:download:`incorrect.wav <../web-experiments/res/sound/incorrect.wav>`.We want to play them at
the end of the trial to give audio feedback to our participants.

To play audio in JavaScript, you first have to create ``Audio`` objects
containing the audio file you want to play.

.. code:: javascript

   let audio = new Audio(pathToFile);

You can now play the audio using the ``play`` function of this audio
object:

.. code:: javascript

   audio.play()

As small exercise, you should now be able to play a valid auditory
feedback at the end of every trial. Hint below!

.. raw:: html

   <details>

.. raw:: html

   <summary>

Hint

.. raw:: html

   </summary>

::

   You should use the `on_finish` property we saw above!

.. raw:: html

   </details>

Saving the data
~~~~~~~~~~~~~~~

The experiment is almost ready! What we want to do now is to save our
data. It can be saved locally (on the machine that took the experiment),
or, more interestingly, on a distant server.

In this course, we will only use local save, which is still useful for
debugging and/or piloting. Our ``data`` object possesses a ``localSave``
method that precisely saves the experiment’s data as a ``.csv`` file:

.. code:: javascript

   jsPsych.data.get().localSave('csv', "data.csv");

Where (i.e. when) to should this instruction be executed? At the end of
the experiment! Similarly to trials, our JsPsych instance can be created
with an additional ``on_finish`` method. Note that unlike for trials,
this one does not take a ``data`` argument.

.. code:: javascript

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
~~~~~~~~~

You may notice that we haven’t done anything about participant IDs.
Assigning each participant a *random* ID is of course mandatory in
psychology experiments. JsPsych provides use with a convenient way to
generate random IDs of a given length:
``jsPsych.randomization.randomID``.

We can create a 10-character long ID for our participant with the
following line. We use a constant here because it should never be
modified.

.. code:: javascript

   const ID = jsPsych.randomization.randomID(10);

We can now add this ID info to all our trials. To this end, you can
modify each trial individually using the ``data`` property as above.
Another way is to add a common property to the whole data, as describe
in the
`documentation <https://www.jspsych.org/7.0/overview/data/#adding-data-to-all-trials>`__.

As a final note, you will most likely want to use this ID for the data
file you save at the end of the experiment: if all participants’ files
have the same name, they will overwrite one another!

.. code:: javascript

   jsPsych.data.get().localSave('csv', "data-"+ID+".csv");

..

   **String formatting** To get a cleaner script, you may use string
   formatting to plugging code output into a string. Formatted string
   use this quote
   \`\`\ ``and have codes marked between brackets``\ ``, the opening bracket being preceded by a dollar sign``\ $\ ``. An exemple:``\ Bonjour!
   My name is ${my_name}!`.

Final code
~~~~~~~~~~

You can find a solution for the final code
:download:`here <../web-experiments/experiments/jspsych-color-decision-task>`. Make sure to try out
to code it first! Practice makes perfect.

I did not do it in this example, but you should leave an end message to
your participants, thanking them for their time. You can create a
``jsPsychHtmlKeyboardResponse`` trial with no possible response by
giving the ``choices`` property the ``"NO_KEYS"`` value.

Web Scraping
============

(activity developed by `Ewan Dunbar <http://individual.utoronto.ca/ewan_dunbar/>`_)

  .. container::
      :name: TOC

      -  `!!Read this first!! <#read-this-first>`__
      -  `Overview <#overview>`__
      -  `Web scraping <#web-scraping>`__

         -  `General instructions and a partly-worked example
            exercise <#general-instructions-and-a-partly-worked-example-exercise>`__

            -  `Notes on idiomatic
               Python <#notes-on-idiomatic-python>`__
            -  `Notes on Python style
               conventions <#notes-on-python-style-conventions>`__
            -  `Notes on how to do this
               project <#notes-on-how-to-do-this-project>`__
            -  `Notes on opening files <#notes-on-opening-files>`__
            -  `Notes on testing your
               code <#notes-on-testing-your-code>`__
            -  `Hint <#hint>`__
            -  `Unicode <#unicode>`__

         -  `Exercise 1: Command line
            arguments <#exercise-1-command-line-arguments>`__

            -  `Recommended approach <#recommended-approach>`__

         -  `Exercise 2: Processing
            HTML <#exercise-2-processing-html>`__

            -  `Structure <#structure>`__
            -  `Reminder <#reminder>`__
            -  `Documentation strings <#documentation-strings>`__
            -  `Docstrings versus inline
               comments <#docstrings-versus-inline-comments>`__
            -  `What functions should do <#what-functions-should-do>`__
            -  `Note <#note>`__
            -  `Scope <#scope>`__

         -  `Exercise 3: Accessing web
            pages <#exercise-3-accessing-web-pages>`__

            -  `BE CAREFUL <#be-careful>`__
            -  `This is a bigger task <#this-is-a-bigger-task>`__

         -  `Exercise 4: Refactoring your
            code <#exercise-4-refactoring-your-code>`__

            -  `Importing functions <#importing-functions>`__
            -  `Scripts and modules <#scripts-and-modules>`__
            -  `Testing your code <#testing-your-code>`__

         -  `Exercise 5: Crawling
            websites <#exercise-5-crawling-websites>`__
         -  `Exercise 6: Cleaning up
            text <#exercise-6-cleaning-up-text>`__
         -  `Exercise 7: Transition
            probabilities <#exercise-7-transition-probabilities>`__
         -  `Exercise 8: Generating text from a bigram language
            model <#exercise-8-generating-text-from-a-bigram-language-model>`__

      -  `Resources <#resources>`__

   .. container:: section level3
      :name: read-this-first

      .. rubric:: !!Read this first!!
         :name: read-this-first

      This is an optional project aimed at those who have a fair bit of
      experience programming and want to learn quickly how to do some
      useful things in Python, and/or feel like they know how to mess
      around with code but don’t quite feel like “programmers,” or would
      just like to become better programmers. You may not feel like a
      programmer when you are done either, but, if you follow the
      instructions you will certainly feel much **more** like a
      programmer. In that spirit, it is very much a “self-guided tour.”
      You will get instructions on what to do, but you will need to make
      heavy use of online resources to figure out how to do these
      things.

      This project consists of a series of exercises. It is incremental.
      You need to start at the beginning, because each part relies on
      the previous, but you can stop at any point.

      This project will not be marked. But, if you take this project on,
      we would like to:

      -  See you finish it by the end of the course
      -  Check in on you each week
      -  Spend a small amount of time at the end of the course going
         over your project to give qualitative comments

      We will also of course help you by answering any questions you may
      have by email or in person. For this reason, if you are going to
      do this project, we ask that you sign up: send an e-mail to both
      Info 2 instructors (Christophe Pallier and Ewan Dunbar) saying
      that you’re going to do the project (not to the Google Group).
      Keeping in touch will also help us to fix any potential bugs in
      the project instructions as quickly as possible.

      You are encouraged, but not required, to find a partner, and work
      on this project in pairs. If you choose to do this, it is up to
      you to divide the labour. It is recommended that you use the
      opportunity to read each other’s code carefully, check it over,
      and discuss it.

      In either case, again, **if you are going to do this project,** we
      ask that you sign up: please **send an e-mail to us saying that
      you’re going to do the project** (not to the Google Group). If you
      are going to work in pairs, one email (cc’ed to both partners),
      will suffice.

   .. container:: section level3
      :name: overview

      .. rubric:: Overview
         :name: overview

      This project will introduce you to a programming task that will be
      useful if you do projects with language: harvesting textual data
      from the web and cleaning it up. The last exercise will also get
      you thinking about what you can do with textual data.

      On the way, you will be required to learn certain key Python
      skills which are far more generally applicable, including:

      -  Using the Python documentation
      -  Reading from a file
      -  Writing to a file
      -  Downloading web pages
      -  Command line arguments
      -  Common Python idioms
      -  Imports
      -  Basic text processing

      Thus, perhaps the more pertinent goal of this project is to give a
      self-guided tour of Python to those who have programmed before in
      other languages, and/or to give those who have programmed before,
      either in Python or not, a good sense for some basic good
      programming practices, including:

      -  Style and variable naming
      -  Documentation
      -  Use of functions
      -  Organizing your code
      -  Attacking complex problems by sub-dividing them

      The point of the last is to help you build up the skills to create
      working code. The point of the first four is to prevent you from
      creating code that is “write-only”: code which works, but which
      cannot be revisited or modified (or maybe even finished) by you or
      anyone else, because it cannot be read or understood. The larger
      goal of these last four is to remind you that computer **source
      code** is exclusively for human beings, not for computers;
      compiled computer **machine code** (which you may never touch) is
      for computers. Source code is a way for you to sort out a
      human-comprehensible explanation of what the machine code to solve
      your problem should do, save it, share it with other human beings
      who would like to understand it too, and use it again in the
      future for other purposes (it is, incidentally, also the easiest
      way to generate machine code, but it is not the only way). The
      instructions for this project will give you some very general
      guidance on how to do these five things.

      The instructions for this project will **not** give you much
      guidance on how to integrate two other essential programming
      practices into your work, the use of **unit tests** and the use of
      the **interactive debugger,** because the above is already a lot,
      but, if you’d like a bit more practice, you may also find this to
      be a good exercise in developing these practices. You can find
      useful information on unit tests and the interactive debugger
      below under **Resources.**

      By the end of the project, your instructions will become less
      detailed. You will have to make more and more design and style
      decisions for yourself. To guide you, should try and find as many
      examples of good Python code as possible. `This page is a good
      resource. <http://docs.python-guide.org/en/latest/writing/reading/>`__

   .. container:: section level3
      :name: web-scraping

      .. rubric:: Web scraping
         :name: web-scraping

      You may often want to download a large set of web pages, or
      specific content from those web pages, from an entire web site or
      set of web sites. A program which does this is called a **web
      crawler.** A web crawler that looks for very specific information
      and tries to extract it automatically is called a **web scraper.**
      Web scraping is sometimes used by companies to collect up-to-date
      information on prices or other quickly-changing information, and
      may not be well looked upon by the target sites, for various
      reasons, but mainly that any web crawler has the potential to
      create a huge amount of traffic and overload the site. However, if
      done in a respectful way, web crawlers can be very useful, and,
      indeed, are essential to your daily life: Google relies on a
      massive web crawler to find new or updated web pages, so that it
      can then index them so that you can find them when you search.

      Your job is to write Python code that automatically downloads a
      portion of Wikipedia. It is not strictly necessary to crawl
      Wikipedia, because the entire contents are freely available to
      download in large compressed files. If you want to work with
      Wikipedia in the future, it is recommended that you make use of
      thse files instead of crawling. However, Wikipedia permits light
      crawling of articles, and, as Wikipedia is a very useful
      collection of natural language texts, it serves as a useful
      example.

      .. container:: section level4
         :name: general-instructions-and-a-partly-worked-example-exercise

         .. rubric:: General instructions and a partly-worked example
            exercise
            :name: general-instructions-and-a-partly-worked-example-exercise

         This is a warmup exercise that is mostly done for you. This
         section is intended to establish some coding conventions that
         you should use in this project.

         All of your code should run on the command line (rather than
         from inside a Python notebook or iPython). If you’re not
         familiar with how to run Python scripts programs from the
         command line, `read this document
         first <http://pythoncentral.io/execute-python-script-file-shell/>`__
         (if your path is set up correctly on Windows, which it already
         should be, then you should not need to type the full path name
         to the Python interpreter, ``python.exe``, contrary to what is
         suggested in the document).

         You should create a folder just for this project.

         Go in your browser to `the English Wikipedia page for the
         stipple-throated
         antwren. <https://en.wikipedia.org/wiki/Stipple-throated_antwren>`__
         Copy and paste all of the text from this page and save it as a
         text file in your project folder. Let’s start by writing a
         Python program that reads this file and prints it to the
         screen.

         .. container:: section level5
            :name: notes-on-idiomatic-python

            .. rubric:: Notes on idiomatic Python
               :name: notes-on-idiomatic-python

            In each programming language, there are conventions for
            writing programs or for doing certain programming tasks in a
            particular way that are generally adhered to, or at least
            very easily understood, by the community, but may not be
            obvious a priori (programming language “idioms”).
            Programmers in that language adhere to these conventions
            mainly because doing so helps make programs in that language
            easier to read and understand (for you, not just for
            others), and also sometimes because they may be useful ways
            to avoid errors.

            The idiomatic Python way to write a program that runs on the
            command line is to structure your file like this:

            ::

               # Imports, definition of functions, ...

               if __name__ == "__main__":
                   # The code that runs when the program is launched...

            .. with the code that runs when the program is launched
            coming at the **end** of the file. The reason for this
            convention is explained on `this Stack Overflow
            question. <http://stackoverflow.com/questions/419163/what-does-if-name-main-do>`__

            You should adhere to this convention for the rest of this
            project.

            For example, in this exercise - which doesn’t really require
            you to write any new functions, but which might require you
            to import the ``sys`` module, depending on how you solve it
            - you might get a short script that looks something like
            this:

            ::

               import sys

               if __name__ == "__main__":
                   # All your code...

            You can get more tips on writing idiomatic Python `at this
            site. <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`__

         .. container:: section level5
            :name: notes-on-python-style-conventions

            .. rubric:: Notes on Python style conventions
               :name: notes-on-python-style-conventions

            Similar to idioms (but more to do with low-level things like
            formatting) is “style.” This includes naming variables and
            constants, the number of spaces with which you indent, how
            many spaces you put around parentheses, and so on. When
            working on large collaborative projects you will almost
            always be asked to adhere to a set of style guidelines (and
            if you are working in a pair, you should do that here too).
            At the very least, you need to be consistent internally.
            Many text editors have a “Format” function which can apply
            many of your personal style conventions automatically, and
            most will do automatic indentation and allow you to set the
            number of spaces.

            In Python, the standard, and highly recommended, style
            guidelines are called `PEP 8, and are accessible
            here <https://www.python.org/dev/peps/pep-0008/>`__.

            The specification for this exercise asks you to read **one**
            file. The simplest way to do this (and therefore the ideal
            way, following the `Zen of
            Python <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#the-zen-of-python-1>`__)
            is to hard-code the filename as a constant (a variable that
            doesn’t change). In Python, unlike in other languages,
            constants have no special status - they are variables like
            any other, and it is up to you not to change them. The style
            convention for showing that something is a constant (nearly
            universally adhered to in all programming languages) is to
            put them in ALL_CAPS_SEPARATED_BY_UNDERSCORES. Thus, your
            program will look something like this:

            ::

               # Imports if necessary 

               if __name__ == "__main__":
                   INPUT_FILE = "stipple_throated_antwren.txt"
                   # Code to read and print the contents of that file...

         .. container:: section level5
            :name: notes-on-how-to-do-this-project

            .. rubric:: Notes on how to do this project
               :name: notes-on-how-to-do-this-project

            This project is a self-guided tour. That means that the
            `Python documentation <https://docs.python.org/2/>`__ and
            `Stack
            Exchange <http://stackoverflow.com/questions/tagged/python>`__
            are your new best friends - well, right after
            `Google <https://www.google.fr/?q=google+is+your+friend>`__.

            Here, for example, is the `sub-page from the Python tutorial
            on modules and
            imports. <https://docs.python.org/2/tutorial/modules.html>`__

         .. container:: section level5
            :name: notes-on-opening-files

            .. rubric:: Notes on opening files
               :name: notes-on-opening-files

            There are many ways to open a file and you may find various
            pieces of advice, but there is an idiom. The idiom has
            changed over the years, so we point out the idiomatic way to
            do this today, which is using ``with``, `as described
            here. <http://stackoverflow.com/questions/11555468/how-should-i-read-a-file-line-by-line-in-python>`__
            This page will give you almost the whole solution to this
            exercise (but not quite).

         .. container:: section level5
            :name: notes-on-testing-your-code

            .. rubric:: Notes on testing your code
               :name: notes-on-testing-your-code

            You should always verify that your code is correct (i.e.,
            that it gives the right answer on some important cases for
            which you know the right answer).

            In this case, the way to do that is to put the output of
            your program in a new file and then compare that one with
            the original file. You can do this by redirecting the output
            that is printed to the screen into a text file, such as
            ``output.txt`` (see `instructions
            here <http://sc.tamu.edu/help/general/unix/redirection.html>`__
            for Unix-type systems, a subset of which should `also work
            on
            Windows <https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/redirection.mspx?mfr=true>`__).

            On Unix-type systems (such as Linux and OS X), as well as
            Windows 10 (`if you follow these
            instructions <http://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/>`__),
            you can then compare the two files byte-by-byte using the
            ``diff`` program. If you don’t have access to ``diff``,
            there are many tools online for comparing two files.

            The best practice is to have a program that automatically
            runs tests on your code, so that when you change it, you
            know that it’s still doing what it used to do correctly. An
            important tool for doing this is to write **unit tests** for
            each of your functions. As discussed above, developing the
            habit of unit testing is beyond the scope of this project.
            However, it is a good idea, and if you wish to start now,
            you can `start by reading this document about unit testing
            in
            Python. <http://pymbook.readthedocs.io/en/latest/testing.html>`__

         .. container:: section level5
            :name: hint

            .. rubric:: Hint
               :name: hint

            Yes, the output should be exactly the same. If there are
            extra spaces or blank lines in your output, even at the end
            of the file, get it so that your script’s output matches
            exactly before moving on.

         .. container:: section level5
            :name: unicode

            .. rubric:: Unicode
               :name: unicode

            Sooner or later, you will run into error messages that
            mention Unicode, which have to do with special (non-ASCII)
            characters. These errors are awful. Fixing problems with
            Unicode was a major motivation behind Python 3. We, however,
            are using Python 2. As soon as you start getting these
            errors, see the **Unicode** section under **Resources**
            below, and learn how to work them out as quickly as you can.

      .. container:: section level4
         :name: exercise-1-command-line-arguments

         .. rubric:: Exercise 1: Command line arguments
            :name: exercise-1-command-line-arguments

         Finish the example exercise if you haven’t already, and save it
         as ``exercise_warmup.py.`` Make a copy called ``exercise_1.py``
         and modify it so that it reads the input filename as the first
         and only command-line argument rather than storing it as a
         constant, and gives an appropriate error if no arguments are
         given. Continue to save the rest of the exercises as separate
         scripts (for example, with the next exercise in a new file
         called ``exercise_2.py``).

         .. container:: section level5
            :name: recommended-approach

            .. rubric:: Recommended approach
               :name: recommended-approach

            After a bit of Googling, you will be able to work out the
            basics of how command-line arguments work in Python (you’ll
            know you’ve arrived when you start playing around with
            something called ``sys.argv``). You may also discover
            modules called ``getopt`` and ``argparse``, which are more
            general solutions for reading command-line arguments. It is
            very rarely a good idea to use a general solution when there
            is a simple one unless you really need it, but ``argparse``
            is so useful that there is no reason not to use it all the
            time. Learn to use ``argparse``. It will serve you well for
            the rest of the project, and for the rest of your career, to
            keep a template handy for all your new Python scripts that
            might look very roughly like this:

            ::

               import sys
               import argparse

               if __name__ == "__main__":
                   parser = argparse.ArgumentParser()
                   # ... Set up argparse ...
                   args = parser.parse_args(sys.argv[1:])
                   # ... Rest of your program starts here ...

      .. container:: section level4
         :name: exercise-2-processing-html

         .. rubric:: Exercise 2: Processing HTML
            :name: exercise-2-processing-html

         In a web browser, save the raw HTML of the Wikipedia article on
         the stipple-throated antwren (rather than just copying and
         pasting the text). Write a function called
         ``extract_wikipedia_contents`` that takes HTML source and
         returns just the text of the article. Your script should take a
         single command-line argument which is the name of the HTML
         file, call this function on the contents of the HTML file, and
         print the text of the article to the screen (to be more
         precise, to `standard
         output <http://www.diveintopython.net/scripts_and_streams/stdin_stdout_stderr.html>`__).
         It’s up to you to determine what exactly “the text of the
         article” means, except that it shouldn’t contain HTML codes or
         JavaScript, and it should correspond, basically, to the English
         text that a human being would read if they went to read the
         Wikipedia article. It doesn’t need to be the exact text that
         you copied and pasted above (and in fact, it probably
         shouldn’t, because that likely contained Wikipedia navigation
         links which aren’t part of the article text).

         .. container:: section level5
            :name: structure

            .. rubric:: Structure
               :name: structure

            This is where the idiomatic Python script structure starts
            to become non-trivial. Put your function definition(s)
            **above** ``if __name__ == "__main__"``, not inside it. This
            will make your script look something like this:

            ::

               # ... Imports ...

               def extract_wikipedia_contents():
                   # ... Docstring ...
                   # ... 

               if __name__ == "__main__":
                   # ... Get command line arguments, read file ...
                   article_contents = extract_wikipedia_contents(article_html_source)
                   # ... Print article contents ...

         .. container:: section level5
            :name: reminder

            .. rubric:: Reminder
               :name: reminder

            Your function should apply to the contents of the HTML file,
            not to the filename, and it should return the text, not
            print it.

         .. container:: section level5
            :name: documentation-strings

            .. rubric:: Documentation strings
               :name: documentation-strings

            All of your functions must be documented with block comments
            called documentation strings, or simply **docstrings.** The
            purpose of a docstring is to explain what the arguments to
            your function are, what it returns, as well as a very
            concise, one-phrase summary of what it does, with perhaps a
            short paragraph elaborating some relevant details. To get
            you started, here is a partial docstring for the
            ``extract_wikipedia_contents``. (Notice that ``html_source``
            is the name of the argument to the function.)

            ::

                   """Extract the text of a Wikipedia article from HTML

                   Here, it would be useful to describe a bit more about how you've chosen to
                   format the text that you're returning, and what exactly you mean by the
                   "article text."

                   Args:
                       html_source (str): HTML source of a Wikipedia article

                   Returns:
                       str: The text of the Wikipedia article
                   """

            A good practice (one which you have to force yourself to do,
            but which will help you write your programs faster) is to
            write your docstrings **before** you write your functions.
            They force you to state exactly what you intend the function
            to do. If you have that sorted out, writing the function
            becomes much easier. (For example, now it should be
            absolutely clear that the input and output to this function
            are supposed to be **strings,** and not lists or anything
            else.)

            In the **Resources** below, you will find guidelines for
            writing docstrings in Python. Be consistent in your style
            and remember that you’re communicating with the rest of the
            world.

         .. container:: section level5
            :name: docstrings-versus-inline-comments

            .. rubric:: Docstrings versus inline comments
               :name: docstrings-versus-inline-comments

            Docstrings are not the same as inline comments. Inline
            comments (comments interspersed in your code) should be used
            sparingly, and only where necessary, unlike docstrings.
            Inline comments explain the logic of your code, if it isn’t
            obvious. They should not be used to explain what variable or
            function names mean, or to explain enigmatic constants or
            clever ways to do things in only one line. The way to
            clarify unclear variable names or mysterious constants is
            not to use unclear variable names or mysterious constants.
            The way to clarify the clever thing you did is to never do
            clever things. Source code is a human-comprehensible
            explanation of how some machine code works. You have the
            power to make fun puzzles for the reader, but you shouldn’t.

            Here is a good summary of `appropriate uses of inline
            comments <https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/>`__.

         .. container:: section level5
            :name: what-functions-should-do

            .. rubric:: What functions should do
               :name: what-functions-should-do

            Another useful result of writing your docstrings before you
            write your functions is that you will find out whether or
            not your function is trying to do too much. A general rule
            is that if you can’t state precisely in a few words what
            your function does, it’s probably trying to do too much.

         .. container:: section level5
            :name: note

            .. rubric:: Note
               :name: note

            You may, of course, write as many functions as you want for
            this exercise, as long as you write
            ``extract_wikipedia_contents``.

         .. container:: section level5
            :name: scope

            .. rubric:: Scope
               :name: scope

            The goal of this exercise is not to learn to parse HTML.
            That’s a pain. Doing it well demands a whole course of its
            own. Find a Python module that parses the HTML for you, then
            get the text out. Find the simplest one possible.

      .. container:: section level4
         :name: exercise-3-accessing-web-pages

         .. rubric:: Exercise 3: Accessing web pages
            :name: exercise-3-accessing-web-pages

         Write a modified version of your previous script which accesses
         Wikipedia online. It will still take a single, text input file,
         specified on the command line, but that file will now contain a
         list of URLs to Wikipedia articles, each on one line. The
         script will download each of these pages, and then print the
         contents of all of them to standard output, in sequence. No
         clear separation between articles is necessary, nor do they
         need to be in any particular order. You should be able to find
         Python modules that will download the HTML contents of web
         pages for you and return them as a string, so you should be
         able to re-use your ``extract_wikipedia_contents`` function
         (copy and paste it into your new script).

         .. container:: section level5
            :name: be-careful

            .. rubric:: BE CAREFUL
               :name: be-careful

            You are writing a script that accesses web pages. People who
            build websites make web pages for people, not for scripts.
            You should not push your luck, or you may be blocked from
            accessing the website. Wikipedia is fine with you using
            scripts to access it, as long as you respect some rules:

            -  Don’t go too fast. Put a short delay (one second at
               least) between requests for pages.
            -  Make sure that your script reads and respects the
               ``robots.txt`` file. Specifically, that file (which is
               just a text file), specifies what URLs you are allowed to
               access and what files you are not. Don’t access any URLs
               you’re not allowed to.
            -  Respect `Wikipedia’s policy on
               User-Agents <https://meta.wikimedia.org/wiki/User-Agent_policy>`__.

         .. container:: section level5
            :name: this-is-a-bigger-task

            .. rubric:: This is a bigger task
               :name: this-is-a-bigger-task

            This exercise is more complex. It may take some time, and it
            should take more than one function to accomplish. You need
            to read the ``robots.txt`` file, retrieve the contents of
            each of the URLs (being sure to filter appropriately to
            respect ``robots.txt``), and then apply
            ``extract_wikipedia_contents``. You need to make quite a few
            design decisions, and you need to document them in your
            docstrings. (Where do you apply
            ``extract_wikipedia_contents``? Where do you filter the
            URLs? Where do you read the ``robots.txt``? Where do you
            pause between requests?) Furthermore, before you do any of
            that, you need to do some digging to figure out just how to
            do each of those things. (How do you access web pages? Where
            is the ``robots.txt`` file? What happens if there’s a
            problem accessing a web page?)

      .. container:: section level4
         :name: exercise-4-refactoring-your-code

         .. rubric:: Exercise 4: Refactoring your code
            :name: exercise-4-refactoring-your-code

         Your code from Exercise 3 has two logical components,
         corresponding to Exercise 2 (cleaning up Wikipedia page HTML)
         and a new part corresponding to Exercise 3 (accessing
         websites). Up to now, you’ve been told to write separate
         scripts, one for each exercise, and you were told to copy and
         paste your function from Exercise 2 into your Exercise 3
         script. In this exercise, you will learn how to share Python
         code across different files in the same directory, each of
         which collects together a set of useful, related functions.

         Make a copy of your Exercise 2 script called ``wikipedia.py``,
         and a copy of your Exercise 3 script called ``web.py``. In your
         ``exercise_4.py`` script, you will treat those scripts as
         modules, and import the functions that you need from them. Your
         Exercise 4 script should behave exactly like your original
         Exercise 3 script from the outside (that is, this is an
         exercise in `refactoring your
         code <https://en.wikipedia.org/wiki/Code_refactoring>`__).
         However, you should ensure that all the functions in your new
         ``web.py`` script should work for any website, not just
         Wikipedia. You may simplify your interpretation of complex
         ``robots.txt`` files, so long as you err on the side of caution
         (never do anything that you’re not allowed to do).

         .. container:: section level5
            :name: importing-functions

            .. rubric:: Importing functions
               :name: importing-functions

            There are two conventional ways of importing functions (from
            your own code or from other modules) that are recommended.
            One is to import the individual functions you need, as
            follows:

            ::

               from wikipedia import extract_wikipedia_contents

            Another is to import the entire file/module as a separate
            `namespace <https://bytebaker.com/2008/07/30/python-namespaces/>`__.

            ::

               import wikipedia

            This requires that you then make explicit reference to the
            file/module that you imported when calling functions from
            it:

            ::

                   article_contents = wikipedia.extract_wikipedia_contents(article_html_source)

            This can get quite verbose, so there is a way of
            abbreviating the names of the files/modules you import (or,
            rather, of changing the names of the associated namespaces):

            ::

               import wikipedia as wp

               # ...

                   article_contents = wp.extract_wikipedia_contents(article_html_source)

            There is one method that is often cautioned against, because
            it may fill up your namespace unexpectedly with function or
            variable names that you do not need and do not want, and
            that is this:

            ::

               from wikipedia import *

            In this case, it probably won’t do anything different
            (unless you defined additional functions in
            ``wikipedia.py``). But the above alternatives represent more
            predictable and understandable code.

         .. container:: section level5
            :name: scripts-and-modules

            .. rubric:: Scripts and modules
               :name: scripts-and-modules

            You have just learned to import functions not from external
            modules, but from your own code! You may be wondering how
            this is possible. It is possible because a Python module is
            simply any Python script that defines functions, variables,
            or anything else (`see
            here <https://docs.python.org/2/tutorial/modules.html>`__).
            Yet the files you’ve written weren’t originally intended for
            that. They were intended to be used as scripts to be run on
            the command line. This is not a bug - it is a feature.
            There’s no need to work against it by removing the
            ``if __name__ == "__main__":`` section of your newly created
            ``wikipedia.py`` and ``web.py`` files. This section of your
            code now serves as an example of a standard way to use the
            functions you’ve defined.

         .. container:: section level5
            :name: testing-your-code

            .. rubric:: Testing your code
               :name: testing-your-code

            Your Exercise 4 script should behave exactly like your
            original Exercise 3 script, and you should ensure that all
            the functions in your new ``web.py`` script should work for
            any website, not just Wikipedia (including respecting the
            ``robots.txt`` file, under whatever conservative
            interpretation you have decided to take). As always, you
            should test your code and ensure that this is true. Now that
            you know how to import functions, it is all the easier to
            start unit testing, i.e., writing your tests as separate
            functions that you put into a separate testing script.

      .. container:: section level4
         :name: exercise-5-crawling-websites

         .. rubric:: Exercise 5: Crawling websites
            :name: exercise-5-crawling-websites

         Instead of reading a list of URLs from a file, you will now
         crawl Wikipedia, starting from one article (or perhaps a set of
         articles) and following links from those articles to find more
         articles to download. The article or set of articles should be
         specified as titles (not as URLs) and you should also specify
         which language’s Wikipedia contains the target article. You
         should decide whether it makes more sense to start from one
         article or from more than one, and how to pass the article
         titles and the language in to your program. Your crawler will
         download a maximum of 100 articles by following the **first**
         article link contained in each article. (Your job is **not** to
         crawl all of Wikipedia - that will take forever and it may get
         you blocked - and you should not need to build a tree of any
         kind.)

         Instead of writing to standard output, you should now write the
         text of each article to a separate text file. Each text file
         should have a filename that uniquely identifies that article in
         that language (it needn’t be the title and language directly,
         but it could be).

         As in Exercise 4, structure your code using modules and
         imports. You are free to create as many new module files as you
         feel are appropriate, and add new functions to your old
         modules. Modules can import code from other modules if
         necessary, but try and organize them so that they don’t, so
         that they can be used independently of each other, as much as
         possible. Don’t reinvent the wheel. If you can reuse your old
         code, do so. As always, document and test everything.

      .. container:: section level4
         :name: exercise-6-cleaning-up-text

         .. rubric:: Exercise 6: Cleaning up text
            :name: exercise-6-cleaning-up-text

         Exercise 6 will be intended to work on the basis of the output
         of Exercise 5. Your new script will take as command line
         arguments an output directory, and a list of file names
         (corresponding to individual Wikipedia articles). For each file
         name, you will save a new version of that file in the specified
         output directory, which has been cleaned up so as to have:

         -  One sentence per line
         -  The words in each sentence separated from each other by
            exactly one space
         -  Case (upper-case/lower-case) should be removed (normalize to
            either upper or lower case)

         Choose to define “sentence” and “word” in some convenient (not
         necessarily careful) way. Decide how to organize your new code,
         and document and test it.

      .. container:: section level4
         :name: exercise-7-transition-probabilities

         .. rubric:: Exercise 7: Transition probabilities
            :name: exercise-7-transition-probabilities

         Write a script that takes a collection of text formatted as in
         the output of Exercise 6, specified on the command line as a
         set of corpus files and estimates, over the whole corpus (i.e.,
         all the files, taken together), the **transition probability**
         between words. That is, the probability of observing word
         :presentation:`B\ :math:`B``\ :math:`B` right after word
         :presentation:`A\ :math:`A``\ :math:`A` in the corpus. For
         example, in the following three sentences -

         ::

            The fox jumped
            The dog kicked the fox
            A fox jumped

         -  an easy transition probability to estimate is the
            probability of *dog* given *the*. There are three instances
            of *the*, and one of them is followed by *dog*, so a
            reasonable estimate of the transition probability of *dog*
            following *the* would be 1/3. The word here is “estimate”
            because your corpus is only a finite sample, and simply
            counting would lead to some surprising results. For example,
            the transition probability of *dog* following *a* would come
            out as zero. Look up and implement **back-off** and
            **smoothing**, and implement simple versions of these. You
            will also need to calculate the probability of starting or
            finishing a sentence with a particular word.

         A useful resource for understanding these concepts is `Jurafsky
         and Martin’s
         textbook <http://stp.lingfil.uu.se/~santinim/ml/2014/JurafskyMartinSpeechAndLanguageProcessing2ed_draft%202007.pdf>`__,
         and in particular Chapter 4 on n-grams.

         **Do not rely on NLTK or any external module for this.**

         Print the transition probabilities to a text file, in a format
         of your choosing. Decide how to organize your new code, and
         document and test it.

      .. container:: section level4
         :name: exercise-8-generating-text-from-a-bigram-language-model

         .. rubric:: Exercise 8: Generating text from a bigram language
            model
            :name: exercise-8-generating-text-from-a-bigram-language-model

         Write a script that takes the output of Exercise 7 and
         generates random text that follows the transition
         probabilities.

   .. container:: section level3
      :name: resources

    .. rubric:: Resources
         :name: resources

      **Idioms and style**

      -  `On the ``if __name__ == "__main__":``
         convention <http://stackoverflow.com/questions/419163/what-does-if-name-main-do>`__
      -  `On writing idiomatic
         Python <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`__
      -  `PEP 8 style
         guidelines <https://www.python.org/dev/peps/pep-0008/>`__.
      -  `The ``with`` idiom for opening
         files <http://stackoverflow.com/questions/11555468/how-should-i-read-a-file-line-by-line-in-python>`__

      **Docstrings and comments** - `Wikipedia on Python
      docstrings <https://en.wikipedia.org/wiki/Docstring#Python>`__ -
      `Google Python docstring
      style <http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`__
      - `PEP 257 docstring
      guidelines <https://www.python.org/dev/peps/pep-0257/>`__ - `What
      inline comments are
      for <https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/>`__

      **Command line arguments** -
      ```argparse`` <https://docs.python.org/3/library/argparse.html>`__

      **Useful facts** - `Standard input, output, and
      error <http://www.diveintopython.net/scripts_and_streams/stdin_stdout_stderr.html>`__
      -
      `Namespaces <https://bytebaker.com/2008/07/30/python-namespaces/>`__
      - `Python
      modules <https://docs.python.org/2/tutorial/modules.html>`__

      **Examples** `Example Python
      code <http://docs.python-guide.org/en/latest/writing/reading/>`__

      **Unicode** - `Stack Overflow explanation of Unicode print
      problems <http://stackoverflow.com/questions/4545661/unicodedecodeerror-when-redirecting-to-file>`__
      - `More on Unicode print
      problems <https://wiki.python.org/moin/PrintFails>`__ - `A more
      technical list of Unicode frustrations in
      Python <https://pythonhosted.org/kitchen/unicode-frustrations.html>`__
      - `Reading Unicode <http://www.evanjones.ca/python-utf8.html>`__ -
      `Python Unicode
      HOWTO <https://docs.python.org/2/howto/unicode.html>`__

      **Unit testing** - `Unit testing and the ``unittest``
      module <http://pymbook.readthedocs.io/en/latest/testing.html>`__

      **Python debugger** -
      `pdb <https://docs.python.org/2/library/pdb.html>`__

      **NLP textbook** - `Jurafsky and Martin
      draft <http://stp.lingfil.uu.se/~santinim/ml/2014/JurafskyMartinSpeechAndLanguageProcessing2ed_draft%202007.pdf>`__


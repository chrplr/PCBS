Projects
========

The aim is that you spend a few dozens hours programming a project
related to cognitive or neurocognitive sciences (experimental tasks,
simulations of models, data analyses, …), in order for you to learn new
things and improve your coding skills.

-  All documents (scripts, documentation, data files when not too large)
   related to the project should be on a github.com repository. I should
   be able to read the README.md file and understand what the project is
   about, how to run it, etc.

-  Readability of the code and adherence to good practices: Do not be
   overambitious: I prefer a readable code that does a simple thing
   rather than an unreadble code that does complicated things.

-  Work in binomes to read, check and criticize each other code
   regularily

-  use the slack to ask questions

Some ideas
----------

-  How much time does it take for information to cross the two
   hemispheres? Write a simple detection experiment where a visual
   target can appear in the left or right hemifield and the response can
   be given with the left or right hand. Can you detect a difference
   between the reaction times when the hand and the target are on the
   same side or not? (See Poffenberger, A. T. (1912). Reaction Time to
   Retinal Stimulation. (R. S. Woodworth, Ed.). New York: The Science
   Press and Marzi, Carlo A., P. Bisiacchi, and R. Nicoletti. 1991. “Is
   Interhemispheric Transfer of Visuomotor Information Asymmetric?
   Evidence from a Meta-Analysis.” Neuropsychologia 29 (12): 1163–1177.)

-  The vertical midline splits the visual fields into two halves that
   are represented in contralateral hemispheres. While space is
   retinotopically encoded across most visual areas within each
   hemisphere, the vertical division between hemifields necessarily
   disrupts this topological organization. What are the functional
   consequences of the vertical split. P. Mamassian investigated how
   crossing the vertical midline impairs motion sensitivity (Mamassian,
   P. (2010). Locating the functional vertical midline with a motion
   probe [Abstract]. Journal of Vision, 10(7):1379, 1379a,
   http://www.journalofvision.org/content/10/7/1379,
   doi:10.1167/10.7.1379.). Implement his experiment in Python.

-  What happens when a visual object that is physically present but that
   disappears temporarily from consciousness really disappears? Create a
   motion-induced blindness display, have the subject press and hold a
   button when one of the targets disappears from consciousness, and
   then, after a few seconds, have it really disappear from the screen.
   What do you see? Does the target disappear ‘quietly’, or does
   something else happen? What does this tell you about visual
   consciousness? See Mitroff & Scholl (2005), Forming and updating
   object representations without awareness: evidence from
   motion-induced blindness. (project suggested by Mark Wexler)

-  When asked to generate random sequences of digits, people usually
   perform poorly (i.e., non-random; Wagenaar, 1972). A paradigm to
   measure deviations from randomness is the Random Number Generation
   (RNG; e.g., Ginsburg & Karpiuk, 1994) task. In this task,
   participants are asked to produce sequences of digits (e.g., 1–10) in
   a random fashion. Program the task (It is not trivial as you must use
   automatic speech recognition to recognize the digits), and
   investigate the various vatiables that have been proposed to account
   for subjects’ behavior. See Peters et al. (2007). The random number
   generation task: Psychometric properties and normative data of an
   executive function task in a mixed sample. *Journal of the
   International Neuropsychological Society* (Project suggested by
   Jerome Sackur)

-  Artificial Neural networks. You can program a simulation from scratch
   of one of those simple neural networks:

   -  Hopfield network
   -  Kohonen network
   -  a simple auto-encoder with one middle layer

-  Create a pseudoword generator, that is a program that generates
   strings of characters that look like possible words but do not exist
   in the lexicon of a given language. There are many strategies to
   generate pseudowords (e.g., random, following a probabilistic model,
   using neural networks…). You can implement one or several of them.
   The language can be French or English, or your generator could work
   with any language for which you have a corpus.

-  Build an automatic classifier that tries to identify the language
   (e.g. English vs French) of a text from letter statistics; Test it on
   words, sentences, full documents. You must use cross validation (the
   test and training sets must be different). Plot the identifciation
   performance as a function of the lenght of the text (in characters).

-  `Mix and
   Match <http://www.mrc-cbu.cam.ac.uk/people/maarten-van-casteren/mixandmatch/>`__
   are tools to support experimental research. Mix will allow
   experimental stimuli to be pseudo-randomised, according to
   constraints supplied by the user in a simple script. Match can match
   the conditions of factorial experiments. Write similar tools in
   Python.

-  Do you know the *Countdown game* (“Le compte est bon” en français)?
   An interesting question is how do humans solve it. About this, read
   Daniel Defays (2015) Numbo: A study in cognition and recognition. In
   Douglas Hofstadter (editor), *Fluid concepts and creative analogies:
   computer models of the fundamental mechanisms of thought*). Implement
   one or several algorithms to solve this type of puzzles (after trying
   to invent your own algorithm(s), you can learn about the ones
   proposed by Jean-Marc Alliot (2015). “The (Final) Countdown.”
   ArXiv:1502.05450 [Cs], February. http://arxiv.org/abs/1502.05450.)

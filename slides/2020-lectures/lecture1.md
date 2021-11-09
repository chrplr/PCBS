# Programming for Cognitive and Brain Sciences


![](images/chris.jpg)

* Christophe Pallier, researcher (neurolinguist) @ Neurospin

![](images/cedric.png)

* Cédric Foucault, PhD student in Computational Neuroscience @ Neurospin


---

# Why PCBS?

Cognitive Scientists need to:

- generate stimuli and run experiments
- analyze experimental data (and do reproducible science)
- analyze corpora
- simulate cognitive processes (e.g. with neural nets)

---

# Also need to 

- automate boring tasks ("either you are the slave of your computer or the computer is your slave")

Highly recommended book for beginners (and others too):

![](images/automate_boring.png)

https://automatetheboringstuff.com/

---

# And finally

- need to **understand how computers works** and why they are considered a model of the mind (*Computational Theory of Mind, David Marr's levels of description*, ...).

![](images/marr_3_sm.png)


---

![](images/marr_levels_sm.png)


Recommended reading: 
- Daniel Dennett. The Seven Secrets of Computer Power Revealed. in *Intuition Pumps and Other Tools for Thinking*

---

=> *Basic Programming skills are a necessity* (not convinced? tell us)


---

# Our Aims

1. Taking into account the vast differences in prior knowledge among students

    - to help those with limited (or no) programming experience bootstrap their own education in programming (our past experiences have shown that this is entirely feasible).
    - to give those who already know how to code, some opportunities to acquire new skills (e.g. mastering real-time programming, literate programming, ...) 


---

# Our Aims

Try to distill in everyone the importance of **writing clean code**

   *Writing programs "that work"" is far from sufficient!**


![](images/clean_sm.jpg)

On the importance of distinguishing two conceptual tasks:

    1. inventing an algorithm (recipies)
    2. coding in a particular language 

---

# The programming language choice

![](images/python-logo.png)

**Python** is a good compromise.

1. It is general purpose
2. It is quite readable
3. It is popular and there is a lot of help on the web
4. Free
   
Note: We will use Python 3 (>3.7?)

---

# How

Rather than a series of formal lectures, PCBS is essentially a **hands-on course** ("Atelier")

It involves a *great deal of personal involvement* (39+X hours for 2 ECTS !) because learning to program and learning a programming language requires many hours (just as learning how to play an instrument or a second language).

- The first 6 slots: will mostly consist of **exercises**, preceded by **short presentations**, as well as **debriefings** (Comments, Question & Answers). 

- The last 7 slots will be devoted to sessions where you work on a **self-selected project** (related to cognitive (neuro)sciences). 

In a real classroom, we would come to help you individually and check on your progress while you are working on the exercises and the project. In the pure online course, we will support you through **Zoom  backrooms** and a **Slack discussion forum**.

---

# Menu of the day

1. *Christophe* 

    How to use Python (essentially, how to work with a text editor and the command line to create/run a python script.)

2. *Cédric* 
    - how to work on the exercises 
    - "Primer on lists and dictionaries in Python"  (in Room 1)

3. *Christophe* 

    Support students who may need assistance in software installation (Room 2).

4. **Debriefing** 

---

# Basic skills to work with Python


- Download python scripts from internet, e.g. <https://github.com/chrplr/PCBS/raw/master/games.zip> (unzip it)

- Open a Terminal (see <https://pcbs.readthedocs.io/en/latest/first-things-first.html#learn-how-to-open-a-terminal>)


        $ cd Downloads  # or whatever folder where you downloaded games.zip
        $ cd games
        $ ls
        computer-guess-a-number.py  hammurabi.py  human-guess-a-number.py  koch.py  matches.py
        $ python koch.py
        $ python matches.py


---

# Using Python interactively

```
$ ipython
```

    2**64
    import random
    ?random

---

# Open a programming editor



E.g. Sublime Text (but could be any text editor or python IDE)

```
$ subl hello.py
```

Enter the line 

```
print("Hello PCBS")
```

Save the file, and run

```
$ python hello.py
```


See <https://pcbs.readthedocs.io/en/latest/running-python.html>

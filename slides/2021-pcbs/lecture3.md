Day 3
=====

## Parity task

Follow instructions at <https://pcbs.readthedocs.io/en/latest/running-experiments.html#decision-times>

   - Program the parity task: at each trial, a random integer between 0 and 9 is presented and the participant must press `f` if it is odd, `j` if it i even. (hint: start from `simple-detection-visual-expyriment.py`, and use `stimuli.TextLine()`)

   - Add feedback (play a buzzer sound when the answer is wrong)


Check out <https://github.com/chrplr/PCBS/tree/master/experiments/expyriment/parity_decision> for solutions.

---

## Lexical decision task

In a lexical decision task,  a stimuli is presented at each trial and the subject must decide if it is a word or not (and indicate his response by pressing one of two keys). You are going to program such a task.

First of all, modify the parity task to display either a word or a pseudoword at each trial (in a random order).

For testing purposes, you can use the following variables:

    words = ['bonjour', 'chien', 'president']
    pseudos = ['lopadol', 'mirance', 'clapour' ]

---

Then modify your program to input the stimuli from a text file (.csv) with two columns: 

    stimulus,category 
    bonjour,W
    chien,W
    president,W
    lopadol,P
    mirance,P
    clapour,P

(hint: to read a csv file, you can use `pandas.read_csv`)

---

# Using a lexical dabatase

3. Go to http://www.lexique.org

   Click on "Recherche en Ligne" and play with the interface: 

   - enter `4...5` in the the field `nbletters`
   - enter `^ba` in the field 'ortho'
   - see http://www.lexique.org/?page_id=101 for more examples of pattern that can be used.

- how many words of grammatical category (`cgram`) 'NOM', and of length 5 (`nblettres`), of lexical frequency (`freqfilms2`) comprised between 10 and 100 per millions are there in this database? (answer=367). Save these words (i.e. the content of the field `ortho`) into a csv file.
---

# Creation of pseudowords. 

You could write a function to create non-words (random string of characters), but this would not generate "nice" pseudowords (sublexcical statistics would be off).

Rather, use the pseudoword generator <http://crr.ugent.be/programs-data/wuggy> to generate french pseudowords of length between 5 and 6.

Then, with the word and pseudoword stimuli obtained previously, create a full csv fule to drive your lexical decision script. 

**Bravo! You have created a full-fledged experiment.**

Note: (PROJ course's example of a Lexical decision experiment web site: <https://chrplr.github.io/PCBS-LexicalDecision/>)

---

# Automatising a database search

1. Execute the code in the section 'Example 2: sélection d'items avec Python' of <https://github.com/chrplr/openlexicon/tree/master/scripts>

2. Open <https://github.com/chrplr/openlexicon/tree/master/documents/Interroger-Lexique-avec-R> and follow the instructions in the document `interroger-lexique-avec-R.pdf` 

---

# Anagrams

Given the list of french words, write a program that prints all anagrams (words sharing the same letters in different order).

(For a solution, see <https://github.com/chrplr/openlexicon/tree/master/scripts/anagrams>)

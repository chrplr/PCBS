Lexical Decision Experiment
===========================


The aim of this project was to create a psycholinguistics experiment implementing a lexical decision task in the visual modality. 

The experiment consists in a succession of trials in which a written stimulus is displayed on the screen and the participant must indicate, by pressing one of two response buttons, if this stimulus is a word or not. The response time is recorded. 

The word stimuli are nouns and verbs of varying lexical frequencies (frequencies of occurrence in the language) to allow us to assess the influences of these two factors (Category: noun vs. verb; Frequency: high vs. low) on the speed of word recognition.


<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Lexical Decision Experiment](#lexical-decision-experiment)
    - [Preparation of the stimuli](#preparation-of-the-stimuli)
        - [Words](#words)
    - [b.to_csv('lexique382-reduced.txt', sep='\t', index=False)](#btocsvlexique382-reducedtxt-sept-indexfalse)
    - [verbs_hi.sample(N).ortho.to_csv('verlo.txt', index=False)](#verbshisamplenorthotocsvverlotxt-indexfalse)
    - [Pseudowords](#pseudowords)
    - [Experiment](#experiment)

<!-- markdown-toc end -->


## Preparation of the stimuli

### Words

We obtained a list of French words from <http://lexique.org>, downloading <http://www.lexique.org/public/Lexique382.zip> and unzipping it. Our first step was to reduce the number of columns to make it easier to handle the database. 
To this end, we wrote the script `reduce-lexique.py`:

---
# reduce-lexique.py
""" Extracts some columns from Lexique382.txt """

import pandas as pd

a = pd.read_csv('Lexique382.txt', sep='\t')

b = a[['1_ortho', '4_cgram', '15_nblettres', '9_freqfilms2']].rename(columns={
    '1_ortho': 'ortho',
    '4_cgram': 'categ',
    '15_nblettres': 'length',
    '9_freqfilms2':'freq'})

b.to_csv('lexique382-reduced.txt', sep='\t', index=False)
---

Then, we selected 4 subsets of nouns and verbs, of length comprosed between 5 and 8, with the following script (`select-word-from-lexique.py`):

---
import pandas as pd

lex = pd.read_csv("lexique382-reduced.txt", sep='\t')

subset = lex.loc[(lex.length >= 5) & (lex.length <=8)]

noms = subset.loc[subset.categ == 'NOM']
verbs = subset.loc[subset.categ == 'VER']

noms_hi = noms.loc[noms.freq > 50.0]
noms_low = noms.loc[(noms.freq < 10.0) & (noms.freq > 1.0)]

verbs_hi = verbs.loc[verbs.freq > 50.0]
verbs_low = verbs.loc[(verbs.freq < 10.0) & (verbs.freq > 1.0)]

N = 20

noms_hi.sample(N).ortho.to_csv('nomhi.txt', index=False)
noms_low.sample(N).ortho.to_csv('nomlo.txt', index=False)
verbs_hi.sample(N).ortho.to_csv('verhi.txt', index=False)
verbs_hi.sample(N).ortho.to_csv('verlo.txt', index=False)
---

This yielded 4 lists in four files:

    nomhi.txt  nomlo.txt  verhi.txt  verlo.txt



## Pseudowords

Then, to create 80 pseudowords, we used the lexique toolbox pseudoword generator (<http://www.lexique.org/toolbox/toolbox.pub/index.php?page=non_mot>), feeding it with the words generated at the previous step.

We obtained 80 pseudowords, listed in the file `pseudomots.txt`

## Experimental listed

Importing the files `nomhi.txt  nomlo.txt  verhi.txt  verlo.txt and pseudomots.txt` into Openoffice Calc, we created a csv file `stimuli.csv`, with 3 columns:

---
$ head stimuli.csv
Category,Frequency,Item
NOUN,HIFREQ,ordres
NOUN,HIFREQ,reste
NOUN,HIFREQ,couteau
NOUN,HIFREQ,poisson
NOUN,HIFREQ,courant
NOUN,HIFREQ,boulot
NOUN,HIFREQ,position
NOUN,HIFREQ,reine
NOUN,HIFREQ,choix
...
---


## Experiment

the script to run the experiment uses the module expyriment.

---
""" Implementation of a lexical decision experiment. """ 

import random
import csv
import expyriment


STIM_FILE = 'stimuli.csv'
WORD_RESP = expyriment.misc.constants.K_j
NONWORD_RESP = expyriment.misc.constants.K_f
MAX_RESP_TIME = 2500
ITI = 1500

exp = expyriment.design.Experiment(name="Lexical Decision Task") 

expyriment.control.initialize(exp)

trials = []

## Load the stimuli
with open(STIM_FILE, encoding="utf-8") as f:
    r = csv.reader(f)
    next(r)  # skip header line
    for row in r:
        cat, freq, item = row[0], row[1], row[2]
        trial = expyriment.design.Trial()
        trial.add_stimulus(expyriment.stimuli.TextLine(item))
        trial.set_factor("Category", cat)
        trial.set_factor("Frequency", freq)
        trial.set_factor("Item", item)
        trials.append(trial)

random.shuffle(trials)

exp.add_data_variable_names(['key', 'rt'])

## Run the experiment
expyriment.control.start()

expyriment.stimuli.TextScreen("Instructions", """You will see a series of written stimuli displayed at the center of the screen.

After each stimulus, your task is to press the right key ('J') if you think it is an existing word, the left key ('F') otherwise. Place now your index fingers on the keys 'F' and 'J'.

Press the spacebar when you are ready to start.""").present()

exp.keyboard.wait_char(' ')
exp.screen.clear()
exp.screen.update()

for t in trials:
    exp.clock.wait(ITI - t.stimuli[0].preload())
    t.stimuli[0].present()
    button, rt = exp.keyboard.wait([WORD_RESP, NONWORD_RESP],
                                   duration=MAX_RESP_TIME)
    exp.screen.clear()
    exp.screen.update()
    cat, freq = t.get_factor("Category"), t.get_factor("Frequency")
    ok = ((button == WORD_RESP) and (cat != 'PSEUDO')) or ((button == NONWORD_RESP) and (cat == 'PSEUDO'))
    exp.data.add([cat, freq, t.get_factor("Item"), button, ok, rt])

expyriment.control.end()
---


## CONCLUSION

It was a lot of work and we did not have time to implement all the thing we wanted to, notably:

* we wanted to write a script to analyse the data files and create a statistical report
* to include a training phase with feedback before the actual experiment



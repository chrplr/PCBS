#! /usr/bin/env python
# Time-stamp: <2021-04-05 19:00:05 christophe@pallier.org>

import glob
import expyriment

INSTRUCTIONS1 = """
Vous allez voir des mots écrits avec des couleurs de caractères différentes.
Votre tâche sera de dire, à haute voix, la couleur dans laquelle est écrite chacun de mots.

Les mots seront affichés dans une grile rectangulaire:


 mot1  mot2  mot3  mot4
 mot5  mot6  mot7  mot8
 ...


Commencez par le premier mot, en haut à gauche, puis parcourez chacune
des lignes de gauche à droite, comme en lecture normale.

Appuyez sur la barre espace pour continuer... """

INSTRUCTIONS2 = """
Rappellez qu'il faut dire la couleur de "l'encre" à haute voix, et non
pas le mot lui-même.

Votre but doit être allez le plus rapidement possible (votre temps est
chronométré), tout en évitant de faire des erreurs.

Il arrivera toutefois probablement que vous fassiez des erreurs, en en
disant la mauvaise couleur ou en lisant le mot. Quand cela arrive,
re-dite la bonne couleur avant de passez au mot suivant.

Au début de chaque essai apparait une croix. 
Il faut appuyer sur la barre espace pour démarrer l'essai.
Dès que vous avez terminé de nommer les couleurs de tous les mots
affichés à l'écran, appuyez sur la barre espace pour arrêter le chronomêtre
et effacer l'écran.

La durée précise de l'expérience dépend de la vitesse à laquelle vous nommez
les couleurs, mais typiquement, elle dure une dizaine de minutes.

Appuyez sur la barre espace pour continuer.
"""

exp = expyriment.design.Experiment(name="Stroop Experiment")
expyriment.control.initialize(exp)
kb = expyriment.io.Keyboard()

# Load the cards
block = expyriment.design.Block()

for pngfile in glob.glob('Stroop_French*.png'):
    trial = expyriment.design.Trial()
    trial.add_stimulus(expyriment.stimuli.Picture(pngfile))
    trial.set_factor('lang', 'French')
    block.add_trial(trial)

for pngfile in glob.glob('Stroop_English*.png'):
    trial = expyriment.design.Trial()
    trial.add_stimulus(expyriment.stimuli.Picture(pngfile))
    trial.set_factor('lang', 'English')
    block.add_trial(trial)

for pngfile in glob.glob('Stroop_Basque*.png'):
    trial = expyriment.design.Trial()
    trial.add_stimulus(expyriment.stimuli.Picture(pngfile))
    trial.set_factor('lang', 'Basque')
    block.add_trial(trial)

block.shuffle_trials()

bs = expyriment.stimuli.BlankScreen(colour=(0, 0, 0))
fs = expyriment.stimuli.FixCross(size=(25, 25), line_width=3, colour=(127, 127, 127))


# present instructions

instructions1 = expyriment.stimuli.TextScreen("Instructions",
                                              heading_size=60,
                                              text=INSTRUCTIONS1
                                              )

instructions2 = expyriment.stimuli.TextScreen("Instructions",
                                              heading_size=60,
                                              text=INSTRUCTIONS2
                                             )

instructions1.preload()
instructions1.present()
instructions2.preload()
kb.wait_char(' ')

instructions2.present()
kb.wait_char(' ')

expyriment.control.start()

for trial in block.trials:
    bs.present()  # clear screen
    exp.clock.wait(1000)
    fs.present(update=True)
    kb.wait_char(' ')  # wait for a press on the spacebar
    trial.stimuli[0].present(update=True, clear=True)  # display the current card
    key, rt = kb.wait_char(' ')  # wait for a press on the spacebar
    exp.data.add([trial.get_factor('lang'), rt])

expyriment.control.end()

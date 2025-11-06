# ############################################################################
# Word Superiority Effect Experiment
#
# Author: Gemini
# Date: 09 October 2025
#
# Description:
# This script implements the classic Word Superiority Effect experiment using
# the Expyriment library.
#
# In each trial, a four-letter stimulus (either a word or a non-word) is
# briefly presented on the screen, followed by a visual mask.
# Immediately after, two letters are shown, one above and one below the
# position of one of the letters in the stimulus. The participant's task is
# to decide which of the two letters was present in the stimulus.
#
# The primary hypothesis is that participants will be more accurate in
# identifying the letter when it is presented within a real word compared to
# a non-word string, demonstrating the Word Superiority Effect.
#
# How to run:
# 1. Make sure you have Python and the Expyriment library installed.
#    (e.g., `pip install expyriment`)
# 2. Run the script from your terminal: `python word_superiority_effect.py`
#
# Data output:
# Expyriment will automatically create a 'data' folder where it will save
# the results of the experiment in a .xpd file (which can be opened as a
# standard CSV file). The columns will include trial number, stimulus type,
# the presented stimulus, the correct response, the key pressed by the user,
# the reaction time, and whether the response was correct.
# ############################################################################

import random
from expyriment import design, control, stimuli, io, misc

# ############################################################################
# Experiment Configuration
# ############################################################################

# Timings (in milliseconds)
FIXATION_CROSS_DURATION = 500
STIMULUS_DURATION = 100  # Brief presentation of the word/non-word
MASK_DURATION = 500
RESPONSE_TIMEOUT = None # No timeout for participant response

# Stimulus settings
TEXT_SIZE = 60
TEXT_FONT = 'monospace' # Monospaced font for equal character width
STIMULUS_Y_POSITION = 0
LINE_LENGTH = 250
LINE_WIDTH = 5
LINE_DISTANCE_FROM_WORD = 60 # Vertical distance of flanking lines from word center

# Define Stimuli
# Each item is a tuple: (word, non-word, critical_letter_position, correct_letter, alternative_letter)
# The non-word is created by changing the critical letter of the word.
# The alternative letter is chosen such that it would also form a word if placed in the critical position.
STIMULI_LIST = [
    ("WORK", "WORD", 3, "K", "D"),
    ("COLD", "GOLD", 0, "C", "G"),
    ("BEAR", "BEAD", 3, "R", "D"),
    ("LANE", "LAME", 2, "N", "M"),
    ("GAME", "SAME", 0, "G", "S"),
    ("HEAD", "READ", 0, "H", "R"),
    ("TIME", "LIME", 0, "T", "L"),
    ("FOUR", "SOUR", 0, "F", "S"),
    ("ROPE", "ROBE", 3, "P", "B"),
    ("DECK", "DOCK", 2, "E", "O"),
]

N_TRIALS_PER_STIMULUS = 4 # How many times to repeat each word/non-word trial

# ############################################################################
# Initialize Experiment
# ############################################################################

control.defaults.window_mode = True # Set to False for fullscreen
exp = design.Experiment(name="Word Superiority Effect")
control.initialize(exp)

# Define keyboard keys for responses
KEY_TOP = misc.constants.K_UP
KEY_BOTTOM = misc.constants.K_DOWN
exp.data_variable_names = ["trial_id", "stimulus_type", "stimulus_string",
                           "crit_letter_pos", "correct_letter", "alt_letter",
                           "response_key", "RT", "is_correct"]

# ############################################################################
# Create Reusable Stimuli
# ############################################################################

# Fixation cross
fixation_cross = stimuli.FixCross(size=(50, 50), line_width=4)
fixation_cross.preload()

# Mask stimulus (e.g., "####")
mask_stim = stimuli.TextLine("####", text_size=TEXT_SIZE, text_font=TEXT_FONT)
mask_stim.preload()

# Horizontal lines to display above and below the word
top_line = stimuli.Line((-LINE_LENGTH/2, LINE_DISTANCE_FROM_WORD), (LINE_LENGTH/2, LINE_DISTANCE_FROM_WORD), LINE_WIDTH)
top_line.preload()
bottom_line = stimuli.Line((-LINE_LENGTH/2, -LINE_DISTANCE_FROM_WORD), (LINE_LENGTH/2, -LINE_DISTANCE_FROM_WORD), LINE_WIDTH)
bottom_line.preload()

# Instructions screen
instructions = stimuli.TextScreen(
    "Instructions",
    f"""Welcome to the experiment!

In each trial, you will see a string of letters flashed very briefly.
Your task is to identify one of the letters in that string.

After the letters disappear, two choices will appear.
Press the UP arrow key if the correct letter is on TOP.
Press the DOWN arrow key if the correct letter is on BOTTOM.

Please try to be as accurate as possible.

Press any key to start the experiment."""
)

# Thank you screen
thank_you_screen = stimuli.TextScreen("End of Experiment", "Thank you for your participation!")


# ############################################################################
# Create Experimental Trials
# ############################################################################

exp_block = design.Block(name="experiment_block")

for _ in range(N_TRIALS_PER_STIMULUS):
    for s in STIMULI_LIST:
        word, nonword, pos, correct_letter, alt_letter = s

        # Create trial for the WORD condition
        trial_word = design.Trial()
        trial_word.set_factor("stimulus_type", "word")
        trial_word.set_factor("stimulus_string", word)
        trial_word.set_factor("crit_letter_pos", pos)
        trial_word.set_factor("correct_letter", correct_letter)
        trial_word.set_factor("alt_letter", alt_letter)
        exp_block.add_trial(trial_word)

        # Create trial for the NON-WORD condition
        trial_nonword = design.Trial()
        trial_nonword.set_factor("stimulus_type", "nonword")
        # In the non-word condition, the "correct" letter is the one that was in the original word.
        # This is a standard way to design this task.
        trial_nonword.set_factor("stimulus_string", nonword.replace(alt_letter, correct_letter))
        trial_nonword.set_factor("crit_letter_pos", pos)
        trial_nonword.set_factor("correct_letter", correct_letter)
        trial_nonword.set_factor("alt_letter", alt_letter)
        exp_block.add_trial(trial_nonword)


exp_block.shuffle_trials()
exp.add_block(exp_block)


# ############################################################################
# Run Experiment
# ############################################################################

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for trial in exp.blocks[0].trials:
    # Get trial factors
    stim_type = trial.get_factor("stimulus_type")
    stim_string = trial.get_factor("stimulus_string")
    crit_letter_pos = trial.get_factor("crit_letter_pos")
    correct_letter = trial.get_factor("correct_letter")
    alt_letter = trial.get_factor("alt_letter")

    # 1. Fixation Cross
    fixation_cross.present()
    exp.clock.wait(FIXATION_CROSS_DURATION)

    # 2. Present Stimulus (Word or Non-word) with flanking lines
    word_stim = stimuli.TextLine(stim_string, text_size=TEXT_SIZE, text_font=TEXT_FONT)
    word_stim.preload()
    # Create a canvas to draw multiple stimuli at once
    canvas = stimuli.Canvas(size=exp.screen.size)
    word_stim.plot(canvas)
    top_line.plot(canvas)
    bottom_line.plot(canvas)
    canvas.present()
    exp.clock.wait(STIMULUS_DURATION)

    # 3. Present Mask
    mask_stim.present()
    exp.clock.wait(MASK_DURATION)
    exp.screen.clear() # Clear screen before presenting choices

    # 4. Present Two-Alternative Forced Choice
    # Randomly assign correct letter to top or bottom
    if random.choice([True, False]):
        top_letter = correct_letter
        bottom_letter = alt_letter
        correct_key = KEY_TOP
    else:
        top_letter = alt_letter
        bottom_letter = correct_letter
        correct_key = KEY_BOTTOM

    # Calculate x position for the choice letters based on critical letter position
    # This places the choices directly above/below the original letter's location
    char_width_approx = TEXT_SIZE * 0.6 # Approximation for monospaced font
    total_width = len(stim_string) * char_width_approx
    start_x = -total_width / 2
    letter_x_pos = start_x + (crit_letter_pos * char_width_approx) + (char_width_approx / 2)


    top_letter_stim = stimuli.TextLine(top_letter, (letter_x_pos, LINE_DISTANCE_FROM_WORD),
                                       text_size=TEXT_SIZE, text_font=TEXT_FONT)
    bottom_letter_stim = stimuli.TextLine(bottom_letter, (letter_x_pos, -LINE_DISTANCE_FROM_WORD),
                                          text_size=TEXT_SIZE, text_font=TEXT_FONT)

    choice_canvas = stimuli.Canvas(size=exp.screen.size)
    top_letter_stim.plot(choice_canvas)
    bottom_letter_stim.plot(choice_canvas)
    choice_canvas.present()

    # 5. Get Response
    key, rt = exp.keyboard.wait([KEY_TOP, KEY_BOTTOM], duration=RESPONSE_TIMEOUT)

    # 6. Log Data
    is_correct = 1 if key == correct_key else 0
    exp.data.add([trial.id, stim_type, stim_string, crit_letter_pos,
                  correct_letter, alt_letter, key, rt, is_correct])


# ############################################################################
# End Experiment
# ############################################################################
control.end(goodbye_text="Saving data...", goodbye_delay=1000)

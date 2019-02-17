#! /usr/bin/env python3
# Time-stamp: <2019-02-09 13:39:26 christophe@pallier.org>

""" Digit Span task.
In a series of trials, sequences of random digits are displayed and the user must try to recall them.
"""


import random
import argparse
import time
import curses  # See doc at https://docs.python.org/2/library/curses.html


# constants (can be modified by optional command line arguments)
N_TRIALS = 10  # total number of trials
SEQ_LENGTH = 5  #  length of the sequences to recall
FEEDBACK = True  # Give Feedback or no?
DISPLAY_TIME = 0.5  # time of display of an element in the sequence

def generate_random_digits(seq_length):
    return [str(random.randint(1, 9)) for _ in range(seq_length)]


def display_sequence(seq, xpos, ypos, disp_time):
    for char in seq:
        stdscr.addstr(ypos, xpos, char)
        stdscr.refresh()
        time.sleep(disp_time)
        stdscr.addstr(ypos, xpos, ' ')
        stdscr.refresh()
        time.sleep(disp_time)


def display_text(text, xpos, ypos):
    stdscr.clear()
    curses.curs_set(0)  # Hide the cursor
    stdscr.addstr(ypos, xpos - len(text) // 2, text)
    stdscr.refresh()


def main(win):
    global stdscr
    stdscr = win
    height, width = stdscr.getmaxyx()
    cy = (height - 1) // 2
    cx = width // 2

    stdscr.clear()     # Clear screen
    curses.curs_set(0)  # Hide the cursor

    answers = open('memory_span_test_responses.txt', 'w+')
    answers.write('###\n')

    for it in range(1, N_TRIALS + 1):

        display_text(f'{it}/{N_TRIALS}', cx, cy)
        time.sleep(1)
        stdscr.clear()     # Clear screen
        stdscr.refresh()     # Clear screen
        time.sleep(1)

        digits = generate_random_digits(SEQ_LENGTH)

        display_sequence(digits, cx, cy, DISPLAY_TIME)

        # prompts and records the response
        stdscr.addstr(cy, cx - SEQ_LENGTH // 2 - 2, '?')
        curses.curs_set(1)  # shows the cursor
        curses.echo()
        resp = stdscr.getstr(cy, cx - SEQ_LENGTH // 2, SEQ_LENGTH)
        resps = resp.decode('utf-8')

        # compare it to the right one
        sequence = "".join(digits)
        ok = resps == sequence
        answers.write(sequence + '\t' + resps + '\t' + str(ok) + '\n')

        curses.curs_set(0)  # erase the cursor
        stdscr.clear()
        stdscr.refresh()

        if FEEDBACK:
            if ok:
                display_text('Correct!', cx, cy)
            else:
                display_text('Wrong', cx, cy)

            stdscr.refresh()
            time.sleep(1)
            curses.noecho()
            time.sleep(1)

    answers.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

#     parser.add_argument("--splash", help="displays a picture (e.g. containing instructions) before starting the experiment")

#     parser.add_argument('csv_files',
#                     nargs='+',
#                     action="append",
#                     default=[])
#     parser.add_argument('--total-duration',
#                     type=int,
#                     default=-1,
#                     help="time to wait for after the end of the stimuli stream")
#     parser.add_argument("--rsvp-display-time",
#                     type=int,
#                     default=WORD_DURATION,
# :

    curses.wrapper(main)

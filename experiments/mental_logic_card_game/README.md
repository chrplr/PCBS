# Mental logic card guessing game #


## Description ##

The experiment consists of trials where three cards are presented on a row.

First their backs are presented, then one second later, one of the three cards is unmasked, 

Three cards are used throughout the experiement:

   * Queen of Hearts   (red back)
   * Black Spade Ace   (blue back)
   * Red Diamond Ace   (blue back)

Note that only the queen card has a red back while the two ace cards have blue backs!

The task is to identify the *middle* card as quickly as possible, when possible.

The participant must indicates his guess by pressing a key:

   * Queen -> Press 'Q'
   * Black Spade Ace -> Press 'S'
   * Red Diamond Ace -> Press 'D'
   * Dont know -> Press 'N'

Note that the answer will sometimes be obvious (e.g. when the card to guess has a blue back,
because only the Queen has a blue back; or when the middle card is be displayed).

Yet at other times, it will not be possible to decide (in that case, press 'N')



## Isntallation ##

1. If you do not have it yet, install python3, e.g. from <https://www.anaconda.com/products/individual>

2. install the python module `expyriment**, following the instructions at <http://docs.expyriment.org/Installation.html>

## Running ##

        cd mental_logic_card_game
        python mental_logic_card_game.py 


## Data analysis ##

**TBD**

Data are saved in csv files (one per participant) in the folder  `data/` 

---

Christophe Pallier <christophe@pallier.org>



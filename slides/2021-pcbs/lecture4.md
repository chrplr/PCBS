Day 4
=====

## Lexical decision task

In a lexical decision task,  a stimuli is presented at each trial and the subject must decide if it is a word or not (and indicate his response by pressing one of two keys).

In our implementation, the stimuli are listed in table with two columns saved in a csv file: 

    stimulus,category 
    bonjour,W
    chien,W
    president,W
    lopadol,P
    mirance,P
    clapour,P

which can be read with `pandas.read_csv`

See  <https://github.com/chrplr/PCBS/tree/master/experiments/expyriment/lexical_decision> for the full solution.

---

# Using a lexical dabatase

3. Go to http://www.lexique.org

   Click on "Recherche en Ligne" and play with the interface: 

   - enter `4...5` in the the field `nbletters`
   - enter `^ba` in the field 'ortho'
   - see <http://www.lexique.org/?page_id=101> for more examples of patterns that can be used (and, later, <https://pcbs.readthedocs.io/en/latest/regular_expressions.html> to learn more about regular expressions and ho to use them in Python)

- how many words of grammatical category (`cgram`) 'NOM', and of length 5 (`nblettres`), of lexical frequency (`freqfilms2`) comprised between 10 and 100 per millions are there in this database? (answer=367). Save these words (i.e. the content of the field `ortho`) into a csv file `"words.csv"` (on word per line).

---
# Creation of pseudowords. 

1. Write a function that returns a nonword (a string containing random characters)

        def pseudo(length):
            """ returns a nonword of length `length` """


2. Use this function to create a list of 100 nonwords and save it in a file `"pseudowords.csv"` (one pseudoword per line) (see <https://www.pythontutorial.net/python-basics/python-write-text-file/>)

3. Merge `words.csv` and `pseudowords.csv` into a single `stimuli2.csv` file.

4. Modify `lexdec1.py` to be able to pass the name of the stimuli file as an argument on the command line:

        python lexdec1.py stimuli.csv

(hint: use `sys.argv[]`; see <https://www.tutorialspoint.com/python3/python_command_line_arguments.htm>)

---

# Improving the nonwords (=>pseudowords)

1. Check out the pseudoword generator [UniPseudo](http://www.lexique.org/?page_id=582)

2. Generate a new list of pseudowords and add them to a new `stimuli3.csv` file

Note: See PROJ example of a Lexical decision experiment: <https://chrplr.github.io/PCBS-LexicalDecision/>)

---

# Automatising database searches with R and Python

1. Open <https://github.com/chrplr/openlexicon/tree/master/documents/Interroger-Lexique-avec-R> and follow the instructions in the document `interroger-lexique-avec-R.pdf` 

2. Read and execute <https://github.com/chrplr/openlexicon/tree/master/scripts#selecting-lexical-items-with-python>

---

# Distribution of lexical frequencies


1. Write a function that, given a list of words, returns the number of occurences of each word, in the form a python dictionary associating a word to its number of occurences.

2. Use this function to compute frequencies of words in [Alice in Wonderland](http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt). Print the list of words sorted by decreasing frequencies.

Remark: To remove the punctuation, you can use the following function:

    import string
    def remove_punctuation(text):
       punct = string.punctuation + chr(10)
       return text.translate(str.maketrans(punct, " " \* len(punct)))

3. Zipf law states that the product rank X frequency is roughly
   constant. Check out http://en.wikipedia.org/wiki/Zipf%27s_law. 
   
   Create the Zipf plot for the text of `Alice in Wonderland <../stats-and-data-analyses/Zipf/alice.txt>`__
   showing, on the y axis, the log of the frequency and on the x axis
   the word rank (sorting words from the most frequent to the least
   frequent).
   
(see solutions at <https://github.com/chrplr/PCBS/tree/master/stats-and-data-analyses/Zipf>) 

---

# More on lexical frequency and word length

-  Display the relationship between word length and word frequencies
   from the data in
   :download:`lexical-decision/lexique382-reduced.txt <../experiments/lexical-decision/lexique382-reduced.txt>`

-  Generate random text (each letter from a-z being equiprobable, and
   the spacecharacter being 8 times more probable) of 1 million
   characters. Compute the frequencies of each ‘pseudowords’ and plot
   the rank/frequency diagram.

-  To know more about lexical frequencies see  Harald Baayen (2001) *Word Frequency Distributions* Kluwer
      Academic Publishers. and 
   -  Read Michel e al. 2010. “Quantitative Analysis of Culture Using Millions of
      Digitized Books.” _Science_, https://doi.org/10.1126/science.1199644. (use scholar.google.com
      to find a pdf copy). 
      
   - Check out **google ngrams** at
      https://books.google.com/ngrams. (Note that at the bottom of the
      page, there is a message “Raw data is available for download
      here”).

---

# Anagrams

Given a list of words (e.g. the `ortho` field from Lexique383), write a program that prints all anagrams (words sharing the same letters in different order).

(For a solution, see <https://github.com/chrplr/openlexicon/tree/master/scripts/anagrams>)

---

## Rhyme dictionary

Using the field `syll` of the Lexique383.csv, create a dictionary organisez by rhymes, that is the lase, syllable



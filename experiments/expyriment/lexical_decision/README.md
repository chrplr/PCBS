# Programming a Lexical decision task

In a _lexical decision task_, a stimulus is presented at each trial and the subject must decide if it is a word or not (and indicate his response by pressing one of two keys). Let's program such a task.

---

# Step 1: stimuli in constants
First of all, modify the [parity task script](../parity_decision/parity.py) to display either a word or a pseudoword at each trial (in a random order).

For testing purposes, you can use the following variables:

    words = ['bonjour', 'chien', 'président']
    pseudos = ['lopadol', 'mirance', 'clapour' ]

Solution at [lexdec_v1.py](lexdec_v1.py)

---
# Stage 2: read stimuli from a csv file

Then modify the lexical decision script to read the stimuli from a comma-separated text file (`stimuli.csv`) with two columns. Here is the content of `stimuli.csv`:

    item,category 
    bonjour,W
    chien,W
    président,W
    lopadol,P
    mirance,P
    clapour,P

(hint: To read a csv file, one can use `pandas.read_csv`)

Solution at [lexdec_v2.py](lexdec_v2.py) 

--- 

# Select words in a lexical dabatase

1. Go to http://www.lexique.org

   Click on "Recherche en Ligne" and play with the interface: 

   - enter `5...5` in the `nbletters` field
   - enter `^b.t$` in the field `ortho` field (see http://www.lexique.org/?page_id=101 for more examples of pattern that can be used)

2. how many words of grammatical category (`cgram`) 'NOM', and of length 5 (`nblettres`), of lexical frequency (`freqfilms2`) comprised between 10 and 100 per millions are there in this database? (answer=367). Save these words (i.e. the content of the field `Words`) into a `words.csv` file (you may have to clean manually, ie. remove unwanted columns, using Excel or Libroffice Calc).

---

# Create nonwords. 

1. Write a function that returns a nonword (a string containing random characters)

        def pseudo(length):
            """ returns a nonword of length `length` """

   Solution at [create_nonwords.py](create_nonwords.py)

2. Use this function to create a list of 100 nonwords and save it in a file `"pseudowords.csv"` (one pseudoword per line) (see <https://www.pythontutorial.net/python-basics/python-write-text-file/>)

---

# Create a stimuli file

Merge `words.csv` and `pseudowords.csv` into a single `stimuli2.csv` file:

        import pandas
        w = pandas.read_csv('words.csv')
        w['category'] = 'W'
        p = pandas.read_csv('pseudowords.csv')
        p['category'] = 'P'
        allstims = pandas.concat([w, p])
        allstims.to_csv('stimuli2.csv')

---
# Use `sys.argv` to pass the name of the file containing the list of stimuli.  


Modify `lexdec_v2.py` to be able to pass the name of the stimuli file as an argument on the command line:

        python lexdec_v3.py stimuli2.csv

(hint: use `sys.argv[]`; see <https://www.tutorialspoint.com/python3/python_command_line_arguments.htm>)

Solution at [lexdec_v3.py](lexdec_v3.py) 

--- 
# Improving the pseudowords

1. Check out the pseudoword generator [UniPseudo](http://www.lexique.org/?page_id=582)

2. Generate a new list of pseudowords and add them to a new `stimuli3.csv` file


---

# Automatising database searches with R and Python

To select words, rather than using the interface at <http://www.lexique.org>, one can write scripts in R or Python. This promotes reproducible science.

1. Open <https://github.com/chrplr/openlexicon/tree/master/documents/Interroger-Lexique-avec-R> and follow the instructions in the document `interroger-lexique-avec-R.pdf` 

2. Read and execute <https://github.com/chrplr/openlexicon/tree/master/scripts#selecting-lexical-items-with-python>

---

# Finally

Check out the example of a Lexical decision experiment at <https://chrplr.github.io/PCBS-LexicalDecision/>)

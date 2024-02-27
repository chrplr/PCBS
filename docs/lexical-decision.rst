Programming a Lexical decision task
===================================


In a lexical decision experiment, a string of characters is flashed at
the center of the screen and the participant has to decide if it is a actual
word or not, indicating his/her decision by pressing a left or right
button. Reaction time is measured from the word onset, providing an
estimate of the speed of word recognition.

Let us program such a task.


Step 1: stimuli in constants
----------------------------

Modify the :download:`parity task script <../experiments/xpy_parity_decision/parity.py>` to display either a word or a pseudoword at each trial (in a random order). the task of the subject is to press 'F' when the displayed stimulus is a word, 'J' if it is a pseudowords.

For testing purposes, let us assume that::

   words = ['bonjour', 'chien', 'président']
   pseudos = ['lopadol', 'mirance', 'clapour' ]

Run the script and check the results in ``/data``.
   
Compare your script with the solution proposed  :download:`lexdec_v1.py <../experiments/xpy_lexical_decision/lexdec_v1.py>`


Step 2: read stimuli from a csv file
------------------------------------

Modify the lexical decision script so that it reads the stimuli from a comma-separated text file (`stimuli.csv`) with two columns. Here is the content of ``stimuli.csv``::

    item,category 
    bonjour,W
    chien,W
    président,W
    lopadol,P
    mirance,P
    clapour,P

(hint: To read a csv file, you can use ``pandas.read_csv()``)

A solution is proposed in :download:`lexdec_v2.py <../experiments/xpy_lexical_decision/lexdec_v2.py>` 

Note: You can use a file comparator, e.g. `meld <https://meldmerge.org/>`__, to compare the two versions::

     meld lexdec_v1.py lexcdec_v2.py


Optional; 

Select words in a lexical dabatase
----------------------------------

1. Go to http://www.lexique.org

   Click on “Recherche en Ligne” and play with the interface:

   -  enter ``5...5`` in the ``nbletters`` field
   -  enter ``^b.t$`` in the field ``Word`` field (see
      http://www.lexique.org/?page_id=101 for more examples of patterns
      that can be used)

2. how many words of grammatical category (``cgram``) ‘NOM’, and of
   length 5 (``nblettres``), of lexical frequency (``freqfilms2``)
   comprised between 10 and 100 per millions are there in this database?
   (answer=367). Save these words (i.e. the content of the field
   ``Words``) into a ``words.csv`` file (you may have to clean manually,
   ie. remove unwanted columns, using Excel or Libroffice Calc).



Automatising database searches with R and Python
------------------------------------------------

To select words, rather than using the interface at
http://www.lexique.org, one can write scripts in R or Python. This
promotes reproducible science.

1. Open
   https://github.com/chrplr/openlexicon/tree/master/documents/Interroger-Lexique-avec-R
   and follow the instructions in the document
   ``interroger-lexique-avec-R.pdf``

2. Read
   https://github.com/chrplr/openlexicon/tree/master/scripts

To select 100 five letters long nouns for our lexical decision, execute::

   import pandas
   lex = pandas.read_csv("http://www.lexique.org/databases/Lexique382/Lexique382.tsv", sep='\t')
   subset = lex.loc[(lex.nblettres == 5) & (lex.cgram == "NOM") & (lex.freqfilms2 > 10) & (lex.nombre == 's')]
   samp = subset.sample(100)
   samp2 = samp.rename(columns = {'ortho':'item'})
   samp2.item.to_csv('words.csv', index=False)

This creates ``words.csv``.


Generate nonwords
-----------------

1. Write a function that returns a nonword (a string containing random
   characters)

   ::

       def pseudo(length):
           """ returns a nonword of length `length` """

   Solution at :download:`create_nonwords.py <../experiments/xpy_lexical_decision/create_nonwords.py>`


2. Use this function to create a list of 100 nonwords and save it in a
   file ``"pseudowords.csv"`` (one pseudoword per line) (see
   https://www.pythontutorial.net/python-basics/python-write-text-file/)



Create a stimuli file
---------------------

Merge ``words.csv`` and ``pseudowords.csv`` into a single
``stimuli2.csv`` file::

       import pandas
       w = pandas.read_csv('words.csv')
       w['category'] = 'W'
       p = pandas.read_csv('pseudowords.csv')
       p['category'] = 'P'
       allstims = pandas.concat([w, p])
       allstims.to_csv('stimuli2.csv', index=False)


Use `sys.argv` to pass the name of the file containing the list of stimuli  
--------------------------------------------------------------------------

Modify ``lexdec_v2.py`` to be able to pass the name of the stimuli file as an argument on the command line::

        python lexdec_v3.py stimuli2.csv

(hint: use `sys.argv[]`; see https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/)

Solution at :download:`lexdec_v3.py <../experiments/xpy_lexical_decision/lexdec_v3.py>` 



Improving the pseudowords
-------------------------

1. Check out the `Unipseudo <http://www.lexique.org/shiny/unipseudo/>`__ pseudoword generator.
 

2. Generate a new list of pseudowords and add them to a new
   ``stimuli3.csv`` file


Data analysis
-------------

After running::

      python lexdec_v3.py stimuli2.csv

the subject's responses are stored in the subfolder ``data/`` contains a file ``lexdec...xpd``

You can download this :download:`xpd file <../experiments/xpy_lexical_decision/data/lexdec_v3_02_202112131227.xpd>` as an example.

1. Use ``pandas.read_csv(..., comment='#')`` to read the responses into a pandas dataframe.

2. Compute the average reaction times for words and for pseudo-words. 

3. Plot the distribution of reactions times using ``seaborn.boxplot()``

4. Use  ``scipy.stats.ttest_ind()`` to perform a Student t-test compairn gthe RTs of Words and Non-Words.

Check a solution :download:`analyze_RT.py <../experiments/xpy_lexical_decision/analyze_RT.py>`



Auditory Lexical Decision
-------------------------

Transform ``lexdec_v1.py`` into an auditory lexical decision script using the sound files 
from the   `lexical decision folder <../experiments/xpy_lexical_decision/>`:: 

    bonjour.wav
    chien.wav
    président.wav
    clapour.wav
    lopadol.wav
    mirance.wav


Solution at :download:`lexdec_audio.py <../experiments/xpy_lexical_decision/lexdec_audio.py>`



Finally
-------

Check out the example of a 'real' lexical decision experiment at
https://chrplr.github.io/PCBS-LexicalDecision/)

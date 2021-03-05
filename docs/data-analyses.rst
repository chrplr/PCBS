Data Analyses
=============

.. contents::


Basic Data Analysis with R
--------------------------

See
http://www.pallier.org/examples-of-basic-data-analyses-with-r.html#examples-of-basic-data-analyses-with-r


Comparing means using Easy ANOVA (Analysis of Variance)
-------------------------------------------------------

See http://www.pallier.org/easy-anova-with-r.html#easy-anova-with-r


Permutation tests
-----------------

-  Read about the principle of `permutation tests <https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests>`__

-  Implement a python script that uses a permutation test to compare two
   samples.

-  Check out the solution I propose:
   :download:`permutation_test/permutation_test.py <../stats-and-data-analyses/permutation_test/permutation_test.py>`.

Bootstrap
---------

-  Implement the
   `bootstrap <https://en.wikipedia.org/wiki/Bootstrapping_(statistics)>`__
   to obtain confidence intervals on the means of a sample.


Frequency Analysis
------------------

-  See
   :download:`short-intro-fourier <../stats-and-data-analyses/short+intro+to+frequency+analysis+%28Fourier+series%29.pdf>`




Lexical Statistics
==================

Zipf law
--------

-  The script :download:`Zipf/word_count.py <../stats-and-data-analyses/Zipf/word_count.py>` computes the
   distribution of frequencies of occurences in a list of words. Use it
   to compute the distribution of word frequencies in `Alice in
   Wonderland <http://www.umich.edu/~umfandsf/other/ebooks/alice30.txt>`__.

   Note: To remove the punctuation, you can use the following function::

    import string
    def remove_punctuation(text):
       punct = string.punctuation + chr(10)
       return text.translate(str.maketrans(punct, " " \* len(punct)))

-  Zipf law states that the product rank X frequency is roughly
   constant. This ‘law’ was discovered by Estoup and popularized by
   Zipf. See http://en.wikipedia.org/wiki/Zipf%27s_law. Create the Zipf
   plot for the text of `Alice in Wonderland <../stats-and-data-analyses/Zipf/alice.txt>`__
   showing, on the y axis, the log of the frequency and on the x axis
   the word rank (sorting words from the most frequent to the least
   frequent).

-  Display the relationship between word length and word frequencies
   from the data in
   :download:`lexical-decision/lexique382-reduced.txt <../experiments/lexical-decision/lexique382-reduced.txt>`

-  Generate random text (each letter from a-z being equiprobable, and
   the spacecharacter being 8 times more probable) of 1 million
   characters. Compute the frequencies of each ‘pseudowords’ and plot
   the rank/frequency diagram.

-  To know more about lexical frequencies:

   -  Read Harald Baayen (2001) *Word Frequency Distributions* Kluwer
      Academic Publishers.
   -  Read Michel, Jean-Baptiste, Yuan Kui Shen, Aviva P. Aiden, Adrian
      Veres, Matthew K. Gray, The Google Books Team, Joseph P. Pickett,
      et al. 2010. “Quantitative Analysis of Culture Using Millions of
      Digitized Books.” Science, December.
      https://doi.org/10.1126/science.1199644. (use scholar.google.com
      to find a pdf copy). Check out **google ngrams** at
      https://books.google.com/ngrams. (Note that at the bottom of the
      page, there is a message “Raw data is available for download
      here”).


Benford’s law
-------------

Learn about `Benford’s law <https://brilliant.org/wiki/benfords-law/>`__. Write a Python script that displays the distribution of the most significant digit in a set of
numbers. Apply it to the variables in `Benford-law/countries.xlsx <../stats-and-datra-analyses/Benford-law/countries.xlsx>`__.

A solution: :download:`Benford-law/Benford.py <../stats-and-data-analyses/Benford-law/Benford.py>`


Neuroimaging
------------

-  Check out `nilearn <http://nilearn.github.io/>`__ and `nistats <https://nistats.github.io/>`__ and `MNE-python <https://martinos.org/mne/stable/index.html>`__

-  See `stats-and-data-analyses/Example of a single subject-single run fMRI analysis with nistats.ipynb <../stats-and-data-analyses/Example%20of%20a%20single%20subject-single%20run%20fMRI%20analysis%20with%20nistats.ipynb>`__

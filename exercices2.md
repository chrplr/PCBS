Exercices 2:

1. Given a list of numbers, print the largest one.

2. Given a list of numbers, print them separated by a space (e.g. `[1, 2, 4]` -> `1 2 3`).

3. Given a list of words, print how many different
words are in that list (hint: use a dictionary or a set)

4. Given a list of words, count the number of times each word appears in the list. Eg. `[Jim, Alan, Jim, Joe]` -> `Jim:2, Alan:1, Joe:1`  (hint: use dictionary)


5. Write a script that prints the first 10 lines of a file (or the whole file is it is less than 10 lines long).

6. Write a script that prints the last 10 lines of a file  (or the whole file is it is less than 10 lines long).

7. Two taxi companies propose differents pricing schemes: "A charges 
rge 4.80€ plus 1.15€ by km travelled; B 3.20€ plus  
1.20€ by km travelled. Write a script that finds which company is the cheapest
as a function of the distance to travel.

8. Computing descriptive statistics from a detection experiment

In a signal detection experiment, a faint stimulus (e.g. a faint sound or a
faint visual target) is presented or not at each trial and the participant
must indicate whether he has perceived it or not. There are four possible outcomes for each trial:

   1. A _hit_ is when the participant correctly detects the target.
   2. A _miss_ is when the target was there but the participant did not detect it.
   3. A _false alarm_ is when the participant reports the presence of the target when it was not actually there.
   4. A _correct rejection_ is when the participant correctly reports that the
  target was not present.

One defines;

 *  The _hit rate_ , equal to #hits / (#hits + #misses)
 *  The _False alarm rate_, equal to #false alarms / (#false alarms + # correct rejections)

Let us first suppose that the data from a participant is represented as a string. This string represents a series of trials, each trial being
represented by two characters indicating the trial type (1=target present,
0=target absent) and the participant's response (Y=target perceived, N=No target
perceived). For example:

    ---
    data = "0Y,0N,1Y,1Y,0N,0N,0Y,1Y,1Y"
    ---
 
Write a function that, given such a string, returns the Hit rate and the  False rate (hint: use the function `split()`)

Now, the results from different participants are stored in different files `subj*.dat` (download the files from https://github.com/chrplr/PCBS/tree/master/exercices2/subjdat.zip`)

Write a script that computes the hit rates and false alarms for each subject, andisplays the group averages and standard deviations. 


Use `matplotlib.pyplot.plot` to display each participant as a dot on a graphics with False alarm rate on the X-axis and Hit Rate on the Y-axis. 

Read the section on reading comma separated value (`.csv``) files from http://automatetheboringstuff.com/chapter14/


9. (optional) Write a reverse Polish arithmetic expression evaluator (https://en.wikipedia.org/wiki/Reverse_Polish_notation). E.g. `3 4 * 5 -` evaluate to `7`.





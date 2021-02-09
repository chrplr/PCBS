# Menu of the day

1. Short Quizz about Python on Schoology 

2. Depending on the outcome:

    -  Python_fundamentals: objects, control flow (tests, loops), functions
 
    OR

    - Self-training on *Regular expressions* (a very useful tool)
    
    (+ extra on register machines)

3. At noon, debriefing (Q & A session)

Remark: You can always use http://cogmaster-pcbs.slack.com/ to ask questions. 


---

# Self-training *Regular Expressions*

It is common to have to search for strings of characters that conform to certain patterns.

For example, in a french dictionary, all nouns that end in 'er'.

If you are interested in the phonotactics of a language, all possible consonant clusters.

Regular expressions are the tools of choice for this type of task.

See <https://pcbs.readthedocs.io/en/latest/regular_expressions.html>

---

# Bonus on Register Machines (advanced students)

A register machine is a universal computational model (as a Turing machine). 

Skim through [The seven secrets of computer power revealed](../documents/Dan_Dennett-The_seven_secrets_of_computers_revealed.pdf)

- try the simulator at <http://proto.atech.tufts.edu/RodRego/>

- (if you dare) Implement a Rodrego interpreter in Python, that is, a script that will take as input a Rodrego source code, 10 integer values representing the initial state of registers, and will execute the program step by step, following the logic of the langage.

- Compare with my solution at <https://raw.githubusercontent.com/chrplr/PCBS/master/solutions-to-exercices/rodrego.py>

---

# Python fundamentals

---

# Skill 1: Edit/Run Python scripts

Using a text editor (e.g., SublimeText) and a Terminal (e.g., Git Bash) side by side.

(Check out <https://www.youtube.com/watch?v=2yhcWvBt7ZE&feature=youtu.be>)

If you have issues, today you can use an on-line python interpreter <https://repl.it/languages/python3>

---

Question: what happens when one types:

    python mycode.py 
    
    
on a command line in a Terminal?

---

Answer:

`mycodes.py`` containes a "recipies"

A program (python) is started that read its lines ("instructions") and executes them one by one, from top to bottom.

```python
print(3)
print(3.1415)
print("hello")
var = input("your name?")
print(var)
```

remarks: 
- comments, starting with `#`
- possibility of skipping some lines depending on conditions, or repeating some lines (looping)
- definition of functions (code to be executed later)


#  Python basic objects

```python
# integer
-6
2**64

# float
3.1415
float('inf')

# strings

s1 = 'hello'
s2 = "hello"
s3 = """hello.
Did you sleep well?"""

print(s1 + s2)
print(s3.split())


# tuples

red = (255, 0 , 0)
print(red[0])

# lists

simple = [5, 7, 8, 0]
complex = ['abc', 5, (4, 5), ['hello', 6]]
print(complex[3][1])

# dictionaries
d= {'alpha':1, 'beta':2}
print(d['alpha'])

```

---
# Control flow: loops


# repeating

```python
for _ in range(5):
    print("boring!")

```


```python
for _ in range(20):
    print("boring!")

```

Note the indentation !!!

```python
for _ in range(10):
    print('a', end='')
    print('b', end='')
    
print('c')
```

Notion of **block of instructions**

# Doing something with the loop index

```python
for i in range(10):
    print(2 * i)
```

```python
for name in ['Jim', 'John', 'Donald']:
    print('Hello ' + name)
```

Nested loops

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i, "*", j, "=", i * j)
```


---

# conditional (branching)

```python
if condition:
   code1
else:
   code2
```


```python
a = 4
if a % 2 == 0:
    print(a, " is even")
else:
    print(a, " is odd")
```

---

# Breaking a loop

```python
N = 72239
for i in range(2, 300):
    if N % i == 0:
        print(i)
```

Suppose I only need the smallest divisor:

```python
N = 72239
for i in range(2, 300):
    if N % i == 0:
        print(i)
        break
```

---

# Case study: "Guess the number"

Visualize the following code at http://pythontutor.com/visualize.html#mode=display

```python
import random

guessesTaken = 0
 
print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range(6):
     print('Take a guess.') # Four spaces in front of "print"
     guess = input()
     guess = int(guess)

     if guess < number:
         print('Your guess is too low.') # Eight spaces in front of "print"

     if guess > number:
         print('Your guess is too high.')

     if guess == number:
         break

if guess == number:
     guessesTaken = str(guessesTaken + 1)
     print('Good job, ' + myName + '! You guessed my number in ' +
          guessesTaken + ' guesses!')

if guess != number:
     number = str(number)
     print('Nope. The number I was thinking of was ' + number + '.')
```


(taken from https://inventwithpython.com/invent4thed/chapter3.html)


---

# functions


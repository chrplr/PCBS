# Quiz Draft


## Template

*Purpose of below questions: Check whether the student understands: What is X?*

<!-- ![](question_code.png) -->

**Sample Question?** 

```
1. instruction_1
2. instruction_2
```

- [ ] Option a
- [ ] Option b
- [ ] Option c
- [ ] Option d


## Values, Expressions, Variables


*Purpose of below questions: Check whether the student understands: The notion of "value" and "expression"*

**What does the following code print?** 

```
print(3)
```

- [ ] It does not print anything.
- [ ] Three
- [ ] 3
- [ ] 0

**What does the following code print?** 

```
print(3 + 2)
```

- [ ] It does not print anything.
- [ ] 5
- [ ] 32
- [ ] 3 + 2

**What does the following code print?** 

```
print("3 + 2")
```

- [ ] It does not print anything.
- [ ] None
- [ ] 3 + 2
- [ ] 5

*Purpose of below questions: Check whether the student understands: What is a variable, what does it evaluate to in an expression?*

**What does the following code print?** 

```
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] x

**What does the following code print?** 

```
x = 5
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] 5
- [ ] x

**What does the following code print?**

```
x = 5
print(x - 3)
```

- [ ] It does not print anything. An error occurs.
- [ ] x - 3
- [ ] 2
- [ ] 5 - 3


*Purpose of below questions: Check whether the student understands: Assignment, how reassignment works,
the order of execution of instructions*


**What does the following code print?**

```
x = 0
x = 1
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] x
- [ ] 0
- [ ] 1

**What does the following code print?**

```
x = 0
print(x)
x = 1
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] x <br/>
      x
- [ ] 0 <br/>
      0
- [ ] 0 <br/>
      1
- [ ] 1 <br/>
      1
- [ ] 1 <br/>
      0
- [ ] It depends. Two executions can lead to different outcomes.

**What does the following code print?**

```
x = 5
y = 7
x = y
print(x, y)
```

- [ ] It does not print anything. An error occurs.
- [ ] 5 7
- [ ] 7 5
- [ ] 7 7
- [ ] 5 5
- [ ] x y

**What does the following code print?**

```
x = 2
x = x - 1
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] 2
- [ ] x
- [ ] 1
- [ ] -1


## Control Flow: Conditions, Branching, Code blocks

*Purpose of below questions: Check whether the student understands: Boolean values,
difference between equality boolean operator and assignment*

**What does the following code print?**

```
print(1 == 2)
```

- [ ] It does not print anything. An error occurs.
- [ ] 1 == 2
- [ ] False
- [ ] 2

**What does the following code print?**

```
x = 3 == 3
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] 3
- [ ] True
- [ ] x

*Purpose of below questions: Check whether the student understands:
the if statement, the else statement*


**What does the following code print?**

```
if 0 == 1:
    print("a")
print("b")
```

- [ ] It does not print anything. An error occurs.
- [ ] It does not print anything. But no error.
- [ ] a <br/>
      b
- [ ] a
- [ ] b

**What does the following code print?**

```
if 0 == 1:
    print("a")
else:
    print("b")
```

- [ ] It does not print anything. An error occurs.
- [ ] It does not print anything. But no error.
- [ ] a <br/>
      b
- [ ] a
- [ ] b

*Purpose of below questions: Check whether the student understands: code blocks*

**What does the following code print?**

```
if 0 == 1:
    print("a")
    print("b")
```

- [ ] It does not print anything. An error occurs.
- [ ] It does not print anything. But no error.
- [ ] a <br/>
      b
- [ ] a
- [ ] b

**What does the following code print?**

```
if 0 == 1:
    print("a")
    print("b")
else:
    print("c")
    print("d")
print("e")
```

- [ ] It does not print anything. An error occurs.
- [ ] a
- [ ] c
- [ ] e
- [ ] a <br/>
      b
- [ ] a <br/>
      b <br/>
      e
- [ ] c <br/>
      d
- [ ] c <br/>
      d <br/>
      e

**What does the following code print?**

```
if 0 == 1:
    print("a")
    print("b")
print("e")
else:
    print("c")
    print("d")
```

- [ ] It does not print anything. An error occurs.
- [ ] a
- [ ] c
- [ ] e
- [ ] a <br/>
      b
- [ ] a <br/>
      b <br/>
      e
- [ ] c <br/>
      d
- [ ] e <br/>
      c <br/>
      d

*Purpose of below questions: Check whether the student understands: nested ifs*


**What does the following code print?**

```
if 0 == 1:
    print("a")
else:
    if 1 == 1:
        print("b")
    else:
        print("c")
    print("d")
```

- [ ] It does not print anything. An error occurs.
- [ ] It does not print anything. But no error.
- [ ] a
- [ ] b
- [ ] c
- [ ] d
- [ ] b <br/>
      d
- [ ] c <br/>
      d
- [ ] b <br/>
      c <br/>
      d

## Control Flow: Loops


*Purpose of below questions: Check whether the student understands: while statement*

**How many lines does the following code print?**

```
n = 0
while n > 1:
    print("ok")
```

- [ ] 0
- [ ] 1
- [ ] Theoretically, infinitely many

**How many lines does the following code print?**

```
n = 3
while n > 1:
    print("ok")
```

- [ ] 0
- [ ] 1
- [ ] Theoretically, an infinite amount of times

**How many lines does the following code print?**

```
n = 3
while n > 1:
    n = n - 1
    print("ok")
```

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] Theoretically, infinitely many


**What does the following code print?**

```
x = 1
y = -1
while x < 5:
    y = y - 1
    x = x * 2
print(x, y)
```

- [ ] x, y
- [ ] 4 -4
- [ ] 4 -3
- [ ] 5 -5
- [ ] 5 -4
- [ ] 8 -4
- [ ] 8 -8

**What does the following code print?**

```
n = 0
while n < 3:
    if n < 2:
        print("less")
    else:
        print("more")
    n = n + 1
```
- [ ] It does not print anything.
- [ ] less
- [ ] more
- [ ] less <br/>
      more
- [ ] less <br/>
      less <br/>
      more
- [ ] less <br/>
      more <br/>
      more
- [ ] less <br/>
      less <br/>
      more <br/>
      more


*Purpose of below questions: Check whether the student understands: for-in statement and nested loops*

**What does the following code print?**

```
for x in [3, 1]:
    for y in [2, 4]:
        print(x, y)
```

- [ ] 1 2 <br/>
      3 4
- [ ] 3 2 <br/>
      1 4
- [ ] 3 2 <br/>
      1 2 <br/>
      3 4 <br/>
      1 4
- [ ] 3 2 <br/>
      3 4 <br/>
      1 2 <br/>
      1 4


## Functions

*Purpose of below questions: Check whether the student understands:
The notions and distinctions between function definition, function call, function parameters, body of the function.
Which instructions are executed and in what order when defining and calling one function.*

**What does the following code print?**

```
def print_one():
    print(1)
```

- [ ] It does not print anything.
- [ ] 1

**What does the following code print?**

```
def print_one():
    print(1)
print_one()
```

- [ ] It does not print anything.
- [ ] 1
- [ ] 1<br/>
      1

**What does the following code print?**

```
def print_one():
    print(1)
print(2)
print_one()
```

- [ ] It does not print anything.
- [ ] 1<br/>
      2
- [ ] 2<br/>
      1
- [ ] 1<br/>
      2<br/>
      1


**Consider the following code:**

```
def print_sum(x, y):
    print(x + y)
```

**What is the name of the above-defined function?**

- [ ] def print_sum(x, y)
- [ ] print_sum(x, y)
- [ ] print_sum

**What are the parameters (or arguments) of the above-defined function?**

- [ ] x, y
- [ ] x + y
- [ ] There are none

**Which line(s) correspond(s) to the body of the above-defined function?**

- [ ] The first line
- [ ] The second line
- [ ] The first and the second lines
- [ ] There is no function body

**Which line(s) contain(s) a function call in the above code?**

- [ ] The first line
- [ ] The second line
- [ ] The first and the second lines
- [ ] There are no function calls

*Purpose of below questions: Check whether the student understands: how to pass values to a function*

**What does the following code print?**

```
def print_sum(x, y):
    print(x + y)

x = 1
y = 2
print_sum(3, 4)
```

- [ ] It does not print anything. No error.
- [ ] It does not print anything. An error occurs.
- [ ] 3
- [ ] 7
- [ ] 3<br/>
      7


*Purpose of below questions: Check whether the student understands: the return value*

**What does the following code print?**

```
def sum(x, y):
    print(x)
    return x + y

a = 1
b = sum(a, -1)
print(b)
```

- [ ] It does not print anything. An error occurs.
- [ ] 1
- [ ] 0
- [ ] 1<br/>
      0

*Purpose of below questions: Check whether the student understands:
Which instructions are executed and in what order when
using several functions, possibly calling each other.*

**What does the following code print?**

```
def fun_a(x):
    print(x - 1)
    return x + 1

def fun_b(y):
    print(y)
    z = fun_a(x)
    print(z)
    return z * 2

y = 1
z = fun_b(y)
print(z)
```
- [ ] It does not print anything. An error occurs.
- [ ] 0<br/>
      1<br/>
      2<br/>
      4
- [ ] 1<br/>
      0<br/>
      2<br/>
      4
- [ ] 4<br/>
      1<br/>
      0<br/>
      2
- [ ] 4<br/>
      1<br/>
      0<br/>
      2

## Types

*Purpose of below questions: Check if students know primitive types in Python.*

**What is the type of the below expression?**
```
"three"
```

- [ ] int (integer)
- [ ] float
- [ ] bool (boolean)
- [ ] var (variable)
- [ ] function
- [ ] string


**What is the type of the below expression?**
```
3.1
```

- [ ] int (integer)
- [ ] float
- [ ] bool (boolean)
- [ ] var (variable)
- [ ] function
- [ ] string

**What is the type of the below expression?**
```
3 > 4
```

- [ ] int (integer)
- [ ] float
- [ ] bool (boolean)
- [ ] var (variable)
- [ ] function
- [ ] string

**What is the type of the below expression?**
```
3 + 4
```

- [ ] int (integer)
- [ ] float
- [ ] bool (boolean)
- [ ] var (variable)
- [ ] function
- [ ] string

*Purpose of below questions: Check if students know the behavior of + and * operators with strings.*

**What does the following code print?**

```
print("3" + "4")
```

- [ ] It does not print anything. An error occurs.
- [ ] 7
- [ ] 34


**What does the following code print?**

```
print("3" + 4)
```

- [ ] It does not print anything. An error occurs.
- [ ] 7
- [ ] 34

**What does the following code print?**

```
print("4" * 2)
```

- [ ] It does not print anything. An error occurs.
- [ ] 8
- [ ] 44

**What does the following code print?**

```
print("4" * "2")
```

- [ ] It does not print anything. An error occurs.
- [ ] 8
- [ ] 44


## General notions

**What is a program?**

- [ ] Something you follow along at a play or concert
- [ ] A computation, even a symbolic computation
- [ ] A sequence of instructions that specifies how to perform a computation
- [ ] An algorithm (program and algorithm are synonymous)

**What is the source code of a program?**

- [ ] The language that you are programming in (e.g. Python)
- [ ] The environment in which the program is executed
- [ ] The instructions in a program, stored in one or several files
- [ ] The sequence of binary numbers that the program takes as input


**What of the following is a syntax error?**

- [ ] Attempting to divide by 0
- [ ] Forgetting to divide by 100 when calculating a percentage
- [ ] Forgetting a colon at the end of a statement where one is required

**What of the following is a runtime error?**

- [ ] Attempting to divide by 0
- [ ] Forgetting to divide by 100 when calculating a percentage
- [ ] Forgetting a colon at the end of a statement where one is required

**What of the following is a semantic error?**

- [ ] Attempting to divide by 0
- [ ] Forgetting to divide by 100 when calculating a percentage
- [ ] Forgetting a colon at the end of a statement where one is required


**What is a function in Python?**

- [ ] A mathematical expression that calculates a value
- [ ] A statement of the form x = 5 + 4
- [ ] A named sequence of statements
- [ ] Any sequence of statements

**What is one main purpose of a function?**

- [ ] To improve the speed of execution
- [ ] To calculate values
- [ ] To help the programmer organize programs into chunks that match
      how they think about the solution to the problem

**What is a module in Python?**

- [ ] One line of code in a program
- [ ] A separate block of code
- [ ] A file that contains definitions and statements intended for use in other Python programs
- [ ] A file that contains documentation about functions in Python

**What determines the name of the module, which you must put after the `import` statement to use the module?**

- [ ] A line in the module that starts with special characters
- [ ] The first variable name in the module
- [ ] The comment at the top of the module
- [ ] The filename of the module


## Python idioms, syntactic sugar, idiosyncrasies

<!-- *Purpose of below questions: Check whether the student understands: elif statement*

**What does the following code print?**

```
if 0 == 1:
    print("a")
elif 2 == 1:
    print("b")
```

- [ ] It does not print anything. An error occurs.
- [ ] It does not print anything. But no error.
- [ ] a
- [ ] b

```
if 0 == 1:
    print("a")
elif 1 == 1:
    print("b")
else:
    print("c")
```

- [ ] It does not print anything. An error occurs.
- [ ] It does not print anything. But no error.
- [ ] a
- [ ] b
- [ ] c
- [ ] b <br/>
      c
 -->




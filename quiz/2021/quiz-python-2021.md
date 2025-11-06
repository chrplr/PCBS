# PROG Python Quizz 

These are all multiple choice questions with only one correct answer.


## Values, Expressions, Variables


Q1. **What does the following code print?** 

```
print(3)
```

- [ ] It does not print anything.
- [ ] Three
- [ ] 3
- [ ] 0

Q2. **What does the following code print?** 

```
print(3 + 2)
```

- [ ] It does not print anything.
- [ ] 5
- [ ] 32
- [ ] 3 + 2

Q3. **What does the following code print?** 

```
print("3 + 2")
```

- [ ] It does not print anything.
- [ ] None
- [ ] 3 + 2
- [ ] 5

*Purpose of below questions: Check whether the student understands: What is a variable, what does it evaluate to in an expression?*

Q4. **What does the following code print?** 

```
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] x

Q5.**What does the following code print?** 

```
x = 5
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] 5
- [ ] x

Q6. **What does the following code print?**

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


Q7. **What does the following code print?**

```
x = 0
x = 1
print(x)
```

- [ ] It does not print anything. An error occurs.
- [ ] x
- [ ] 0
- [ ] 1

Q8. **What does the following code print?**

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

Q9. **What does the following code print?**

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

Q10. **What does the following code print?**

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

## Control Flow: Conditionals


*Purpose of below questions: Check whether the student understands: Boolean values,
difference between equality boolean operator and assignment*

Q11. **What does the following code print?**

```
print(1 == 2)
```

- [ ] It does not print anything. An error occurs.
- [ ] 1 == 2
- [ ] False
- [ ] 2

Q12. **What does the following code print?**

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


Q13. **What does the following code print?**

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

Q14. **What does the following code print?**

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

Q15. **What does the following code print?**

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

Q16. **What does the following code print?**

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

Q17. **What does the following code print?**

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


Q18. **What does the following code print?**

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

Q19. **How many lines does the following code print?**

```
n = 0
while n > 1:
    print("ok")
```

- [ ] 0
- [ ] 1
- [ ] Theoretically, infinitely many

Q20. **How many lines does the following code print?**

```
n = 3
while n > 1:
    print("ok")
```

- [ ] 0
- [ ] 1
- [ ] Theoretically, an infinite amount of times

Q21. **How many lines does the following code print?**

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


Q22. **What does the following code print?**

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

Q23. **What does the following code print?**

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

Q24. **What does the following code print?**

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

Q25. **What does the following code print?**

```
def print_one():
    print(1)
```

- [ ] It does not print anything.
- [ ] 1

Q26. **What does the following code print?**

```
def print_one():
    print(1)
print_one()
```

- [ ] It does not print anything.
- [ ] 1
- [ ] 1<br/>
      1

Q27. **What does the following code print?**

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

Q28. **What is the name of the above-defined function?**

- [ ] def print_sum(x, y)
- [ ] print_sum(x, y)
- [ ] print_sum

Q29. **What are the parameters (or arguments) of the above-defined function?**

- [ ] x, y
- [ ] x + y
- [ ] There are none

Q30. **Which line(s) correspond(s) to the body of the above-defined function?**

- [ ] The first line
- [ ] The second line
- [ ] The first and the second lines
- [ ] There is no function body

Q31. **Which line(s) contain(s) a function call in the above code?**

- [ ] The first line
- [ ] The second line
- [ ] The first and the second lines
- [ ] There are no function calls

*Purpose of below questions: Check whether the student understands: how to pass values to a function*

Q32. **What does the following code print?**

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

Q33. **What does the following code print?**

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

Q34. **What does the following code print?**

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
      

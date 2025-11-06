## Functions

**Note: There is only one correct answer per question.**

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
  
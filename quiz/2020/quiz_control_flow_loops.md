## Control Flow: Loops

**Note: There is only one correct answer per question.**

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

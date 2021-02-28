

# Clean Code


---

# The goal of "clean code" is to make your code **easy to understand** and **easy to change**.

---


<!-- The goal of "clean code" is to make your code
**easy to understand** and **easy to change**. -->

Analogy between writing code and writing a schedule:

* using [iclr2020.ics as a text file](images/iclr2020_ics_screenshot.png)

    * hard to understand

    * hard to change


* using [ICLR2020 as a google calendar](images/iclr2020_calendar_google_screenshot.png)

    * easy to understand
    (the "things" we care about are immediately visible; unimportant details are abstracted away; easy to see the interactions between different parts;
    easy to navigate between different levels of abstraction)

    * easy to change


<!-- ![](images/iclr2020_ics_screenshot_small.png) -->

<!-- ![](images/iclr2020_calendar_google_screenshot_small.png) -->

---

*Let's illustrate the principles of clean code [CC] by example.*

---

```
w = x2 - x1
```

---

```
w = x2 - x1
```


* What are `w`, `x1` and `x2`?
    * What do they represent?
    * What are they used for?
    <!-- * what type of data do they hold (e.g. scalar, vector…)? -->
* Does "w" stand for "weight", "window", "word", or is it just a symbol for a generic computation?

---

```
w = x2 - x1
```

* What are `w`, `x1` and `x2`?
    * what do they represent?
    * what are they used for?
    <!-- * what type of data do they hold (e.g. scalar, vector…)? -->

* Does "w" stand for "weight", "window", "word", or is it just a symbol for a generic computation?


```
width = x_right - x_left
```


* This answers all of the previous questions!

---

# **CC1. Use meaningful names**

---

```
width = x_right - x_left
```

- **[CC1]** Give names that **reveal the purpose** of things.

---

Next:

```
width = x_right - x_left + 10
```


---

```
width = x_right - x_left + 10
```

- Where does '10' come from?
- What does it represent?
- Can I change it?

---

```
width = x_right - x_left + 10
```

- Where does '10' come from?
- What does it represent?
- Can I change it?

```
width = x_right - x_left + 2 * padding_x
```

- **[CC1]** Replace **magic numbers** with **named constants** or **named parameters**

---

    !python
    width = (21 - 2 * 1.5) * 0.3937007874

- **[CC1]** Replace **magic numbers** with named constants or named parameters

---

    !python
    INCHES_PER_CENTIMETER = 0.3937007874
    # ...
    width = (21 - 2 * 1.5) * INCHES_PER_CENTIMETER

- **[CC1]** Replace magic numbers with **named constants** or named parameters

---

    !python
    INCHES_PER_CENTIMETER = 0.3937007874
    # ...
    def get_content_width(page_width_cm=21.0, page_margin_cm=1.5):
        content_width_cm = (page_width_cm - 2 * page_margin_cm)
        content_width_inches = content_width_cm * INCHES_PER_CENTIMETER
        return content_width_inches

- **[CC1]** replace magic numbers with named constants or **named parameters**

---

```
    check_divisible(a, b)
```

- What do you expect this will do?


---

```
    check_divisible(a, b)
```

- What do you expect this will do?

- **[CC1] Function names should say what they do**


---

The implementation:

    !python
    def check_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

**Misleading name**: I don't expect "something that checks" to print anything


---

A more accurate name:

    !python
    def print_if_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

- **[CC1] Function names should say what they do**

- **[CC1] Function names should describe side-effects** (such as printing to the console)

---

    !python
    remove(l, i)

---

    !python
    remove(l, i)

**Ambiguous name**:

* Are we removing the element in `l` whose value is equal to `i`?
* Or are we removing the element at index `i`?

---

An unambiguous name:

    !python
    remove_list_element_at_index(l, i)

---

An unambiguous name:

    !python
    remove_list_element_at_index(l, i)

* **[CC1] Choose unambiguous names**
* **Clarity at the point of use** is more important than brevity
* Include all the words needed to avoid ambiguity from the perspective of someone calling the function
* A general naming template: **`verb_keywords`** (the verb indicates what the function does, the keywords what parameters are expected)

---

    !python
    add_number(a , b)
    add_list(c, d)

- What do you expect these will do?

---

The implementation:

    !python
    def add_number(a , b):
        return a + b

    def add_list(l, e):
        l.append(e)

---

The implementation:

    !python
    def add_number(a , b):
        return a + b

    def add_list(l, e):
        l.append(e)

**Confusing** to use the same word "add" for the two functions:

* in the first case, `add` calculates the addition
* in the second case, `add` inserts an element
* in the first case, `add` has no side effects, in the second, it does!

---

A way to remove the confusion:

    !python
    def add_numbers(a , b):
        return a + b

    def append_element_to_list(e, l):
        l.append(e)

---

A way to remove the confusion:

    !python
    def add_numbers(a , b):
        return a + b

    def append_element_to_list(e, l):
        l.append(e)

- **[CC1] Use different words for different concepts**

---

    !python
    distance(couple_1, couple_2)

- What is this?

---

    !python
    distance(couple_1, couple_2)

- What is this? **Unclear**:

    * What kind of distance? Distance in what space?

    * What do `couple_1` and `couple_2` represent?

    * A "couple" could stand for many things: a point in 2D geometry, an interval, a rational number, a complex number...

---

    !python
    distance(couple_1, couple_2)

* **Problem:** we are **mixing two levels of abstraction**
    * Level 1: the distance between some abstract objects
    * Level 2: the low-level implementation of these objects as couples


---

A solution:

    !python
    distance(point_1, point_2)

- **[CC1] Use the appropriate level of abstraction**

---

A solution:

    !python
    distance_between_points(point_1, point_2)
    distance_between_intervals(interval_1, interval_2)

- **[CC1] Use the appropriate level of abstraction**
- If several kinds of distance can be used in your program, you need to disambiguate which kind of distance is computed in the function name.

---

Let's revisit an earlier example:

    !python
    def print_if_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

* This function does two things:

    1. Calculating whether an integer is divisible by another

    2. Printing conditionally on the result

---

    !python
    def print_if_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

* This function does two things:

    1. Calculating whether an integer is divisible by another

    2. Printing conditionally on the result

* These are **two conceptually distinct operations**. There is no good reason for them to be done in the same function.

---

A solution:

    !python
    def is_divisible(n, divisor):
        return (n % divisor == 0)

- **Functions should do one thing**

---

# **CC2. Create functions that do one thing**

---

[Example code from a past student](images/functions_do_one_thing_shortened_bad.png)

- What does `display_dots_sparsity_cong` do?
- Do you find it easy to understand?
- How would you make it easier to understand?

<!-- ![](images/functions_do_one_thing_shortened_bad_sm.png) -->

---

[Potential rewrite](images/functions_do_one_thing_shortened_good.png)

- Do you find it easier to understand?

![](images/functions_do_one_thing_shortened_good_sm.png)

---

**CC2. Create functions that do one thing**

- A lot of programming is about **building abstractions**
- Abstractions help you reason about your program and control its intellectual complexity
- Top-down approach: Break the function down into simpler ones
- Bottom-up approach: Chunk a combination of operations in one function (which you manipulate as one conceptual unit)

---

# **3.** [Wait for it]

---

[Example code from a past student](images/DRY_example_student_bad.png)

- What's wrong?

![](images/DRY_example_student_bad_sm.png)

<!-- https://commie.io/#PXwfzTcW -->

---

![](images/DRY_example_student_bad_annotated_sm.png)

---

- What's wrong? **Code duplication**.

- Why is it wrong? It makes code **hard to change**.

---

# **CC3. DRY: Don't Repeat Yourself**

---

- How would you solve this?

![](images/DRY_example_student_bad_annotated_sm.png)

---

- A solution:

![](images/DRY_example_student_good_annotated_sm.png)

---

Last principle of clean code…

---

# **CC4. Explain yourself in code, not comments**

---

Example from a past student:

    !python
    if shuffledtarg_dist[i][1] == 1: ### IF TARGET ###
        # [some code ...]
    elif shuffledtarg_dist[i][1] == 0: ### IF DISTRACTOR ###
        # [some other code ...]

---

Example from a past student:

    !python
    if shuffledtarg_dist[i][1] == 1: ### IF TARGET ###
        # [some code ...]
    elif shuffledtarg_dist[i][1] == 0: ### IF DISTRACTOR ###
        # [some other code ...]

- Why do we need such comments next to `if` and `elif`?
- Good intentions, but bad approach
- **[CC4] Comments do not make up for bad code**

---

A first solution:

    !python
    if stimulus_type == STIMULUS_TYPE_TARGET:
        # [some code ...]
    elif stimulus_type == STIMULUS_TYPE_DISTRACTOR:
        # [some other code ...]

- **[CC4] Clear and expressive code** with few comments is superior to
obscure code with lots of comments
- Can we do even better?

---

An even better solution:

    !python
    if is_target(stimulus):
        # [some code ...]
    elif is_distractor(stimulus):
        # [some other code ...]

- **[CC4] Clear and expressive code** with few comments is superior to
obscure code with lots of comments
- Does this need any comments?

---

Example from a past student:

    !python
    def distance_points(couple1,couple2):
        """Fonction controllant la distance entre nos points
        pour notre ensemble de points aléatoires"""
        return math.sqrt((couple1[0]-couple2[0])**2+(couple1[1]-couple2[1])**2)

---

Example from a past student:

    !python
    def distance_points(couple1,couple2):
        """Fonction controllant la distance entre nos points
        pour notre ensemble de points aléatoires"""
        return math.sqrt((couple1[0]-couple2[0])**2+(couple1[1]-couple2[1])**2)

- **Misleading comment**. It does not accurately describe what the function does.

---

An alternative:

    !python
    def distance_between_points(point_1, point_2)

- Does this need any comments?

---

Example from a past student:

    !python
    exp = design.Experiment("Task") #create and name new exp object

---

Example from a past student:

    !python
    exp = design.Experiment("Task") #create and name new exp object

- Redundant comment. This is just noise. Remove it.

---

# Recap: Clean Code Principles

The goal is to make code **easy to understand** and **easy to change**.

* **CC1 Use meaningful names**.
Reveal purpose. Replace magic numbers.
Say what functions do. Describe side-effects. Remove ambiguity.
Use different words for different concepts.
Use the appropriate level of abstraction

* **CC2 Create functions that do one thing**. Build abstractions.

* **CC3 DRY: Don't Repeat Yourself**. Avoid code duplication.

* **CC4 Explain yourself in code, not comments**. Comments do not make up for bad code.


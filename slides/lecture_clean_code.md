
# The goal of *clean code* is to make your code **easy to understand** and **easy to change**.

---

<!-- 


# The goal of *clean code* is to make your code **easy to understand** and **easy to change**.

Analogy:
iclr2020.ics as text file
ICLR2020 in google calendar


![](images/iclr2020_ics_screenshot_small.png)

* hard to understand
* hard to change

![](images/iclr2020_calendar_google_screenshot_small.png)

* easy to understand. (interactions, what affects what)
* easy to change  

-->

---

    !python
    w = x2 - x1

---

    !python
    w = x2 - x1


* what are 'w' and 'x'?
    * what do they represent?
    * what are they used for?
* does 'w' stand for 'weight', 'window', 'word', or is it just an arbitrary name for a generic computation?
* what type of data do they hold (e.g. scalar, vector…)?

---


    !python
    width = x_right - x_left

---

# **1. Use meaningful names**

---

    !python
    width = x_right - x_left

- **[CC1]** give names that **reveal the purpose** of things

---

    !python
    width = x_right - x_left + 10


---

    !python
    width = x_right - x_left + 10

- where does '10' come from?
- what does it represent?
- can I change it?

---

    !python
    width = x_right - x_left + 2 * padding_x

- **[CC1]** replace **magic numbers** with **named constants** or **named parameters**

---

    !python
    width = (21 - 2 * 1.5) * 0.3937007874

- **[CC1]** replace **magic numbers** with named constants or named parameters

---

    !python
    INCHES_PER_CENTIMETER = 0.3937007874
    # ...
    width = (21 - 2 * 1.5) * INCHES_PER_CENTIMETER

- **[CC1]** replace magic numbers with **named constants** or named parameters

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

    !python
    check_divisible(a, b)

What do you expect this will do?


---

    !python
    check_divisible(a, b)

What do you expect this will do?

- **[CC1] function names should say what they do**


---

    !python
    def check_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

**misleading**: I don't expect "something that checks" to print anything


---

a more accurate name:

    !python
    def print_if_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

**[CC1] function names should describe side-effects** (such as printing to the console)

---

    !python
    remove(list, i)

---

    !python
    remove(list, i)

**ambiguous**:

* are we removing the element(s) in `list` whose value is equal to `i`?
* or are we removing the element at index `i`?

---

    !python
    remove_list_element_at_index(list, i)

- **[CC1] choose unambiguous names**

---

    !python
    remove_list_element_at_index(list, i)

* **[CC1] choose unambiguous names**
* **clarity at the point of use** is more important than brevity
* include all the words needed to avoid ambiguity from the perspective of the one calling the function
* a general naming template: **`verb_keywords`** (the verb indicates what the function does, the keywords what parameters are expected)

---

    !python
    add_number(a , b)
    add_list(c, d)

What do you expect these will do?

---

    !python
    def add_number(a , b):
        return a + b

    def add_list(l, e):
        l.append(e)

**confusing**:

* in the first case, `add` calculates the addition
* in the second case, `add` inserts an element
* in the first case, `add` has no side effects, in the second, it does!

---

    !python
    def add_numbers(a , b):
        return a + b

    def append_element_to_list(e, l):
        l.append(e)

- **[CC1] use different words for different concepts**

---

    !python
    distance(couple_1, couple_2)

---

    !python
    distance(couple_1, couple_2)

**unclear**:

* what kind of distance is this? distance in what space?
* what do the couples represent?
* a couple could stand for many things: a 2D point, an interval, a rational number, a complex number...

---

    !python
    distance(couple_1, couple_2)

* **problem:** we are **mixing two levels of abstraction**
    * level 1: the space of objects in which a distance can be measured
    * level 2: the implementation of these objects as couples


---

    !python
    distance(point_1, point_2)

- **[CC1] use the appropriate level of abstraction**

---

    !python
    distance_between_points(point_1, point_2)
    distance_between_intervals(interval_1, interval_2)

- **[CC1] use the appropriate level of abstraction**
- if several kinds of distance can be used, it is necessary to disambiguate in the function name which kind of distance is computed.

---

    !python
    def print_if_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

---

    !python
    def print_if_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

* this function does two things:
    * calculating whether an integer is divisible by another
    * printing conditionally on the result

---

    !python
    def print_if_divisible(n, divisor):
        if (n % divisor == 0):
            print(n, ' is divisible by ', divisor)

* this function does two things:
    * calculating whether an integer is divisible by another
    * printing conditionally on the result
* these are two conceptually distinct things. there is no good reason for them to be in the same function.

---

    !python
    def is_divisible(n, divisor):
        return (n % divisor == 0)

- **functions should do one thing**

---

# **2. Create functions that do one thing**

---

Example from a past student

---

![](images/functions_do_one_thing_shortened_bad_sm.png)

---

- what does `display_dots_sparsity_cong` do?
- do you find it easy to understand?
- how would you make it easier to understand?

---

![](images/functions_do_one_thing_shortened_good_sm.png)

---

- do you find it easier to understand?

---

- a lot of programming is about **building abstractions**
- abstractions help you reason about your program and control its intellectual complexity
- top-down: break the function down into simpler ones
- bottom-up: chunk a combination of operations in one function (which you manipulate as one conceptual unit)

---

# **3.** [Wait for it]

---

Example from a past student

---

![](images/DRY_example_student_bad_sm.png)

<!-- https://commie.io/#PXwfzTcW -->

---

What's wrong?

---

![](images/DRY_example_student_bad_annotated_sm.png)

---

What's wrong?

**Code duplication**

Why is it wrong?

**Hard to change**

---

# **3. DRY: Don't Repeat Yourself**

---

![](images/DRY_example_student_bad_annotated_sm.png)

---

How would you solve this?

---

![](images/DRY_example_student_good_annotated_sm.png)

---


---

# **4. Explain yourself in code, not comments**

---

Example from a past student

---

    !python
    if shuffledtarg_dist[i][1] == 1: ### IF TARGET ###
        # [some code ...]
    elif shuffledtarg_dist[i][1] == 0: ### IF DISTRACTOR ###
        # [some other code ...]

---

    !python
    if shuffledtarg_dist[i][1] == 1: ### IF TARGET ###
        # [some code ...]
    elif shuffledtarg_dist[i][1] == 0: ### IF DISTRACTOR ###
        # [some other code ...]

- why do we need such comments next to `if` and `elif`?
- good intentions, but bad approach
- **[CC4] comments do not make up for bad code**

---

    !python
    if stimulus_type == STIMULUS_TYPE_TARGET:
        # [some code ...]
    elif stimulus_type == STIMULUS_TYPE_DISTRACTOR:
        # [some other code ...]

- **clear and expressive code** with few comments is superior to
obscure code with lots of comments
- can we do even better?

---


    !python
    if is_target(stimulus):
        # [some code ...]
    elif is_distractor(stimulus):
        # [some other code ...]

- **clear and expressive code** with few comments is superior to
obscure code with lots of comments
- does this need any comments?

---

Example from a past student

---

    !python
    def distance_points(couple1,couple2):
        """Fonction controllant la distance entre nos points
        pour notre ensemble de points aléatoires"""
        return math.sqrt((couple1[0]-couple2[0])**2+(couple1[1]-couple2[1])**2)

---

    !python
    def distance_points(couple1,couple2):
        """Fonction controllant la distance entre nos points
        pour notre ensemble de points aléatoires"""
        return math.sqrt((couple1[0]-couple2[0])**2+(couple1[1]-couple2[1])**2)

- **Misleading comment**. It does not accurately describe what the function does.

---

    !python
    def distance_between_points(point_1, point_2)

- Does this need any comments?

---

Example from a past student

---

    !python
    exp = design.Experiment("Task") #create and name new exp object

- Redundant comment. This is just noise.

---

# Recap: Clean Code Principles

The goal is to make code **easy to understand** and **easy to change**.

**CC1 Use meaningful names**.
Reveal purpose. Replace magic numbers.
Say what functions do. Describe side-effects. Remove ambiguity.
Use different words for different concepts.
Use the appropriate level of abstraction

**CC2 Create functions that do one thing**. Build abstractions.

**CC3 DRY: Don't Repeat Yourself**. Avoid code duplication.

**CC4 Explain yourself in code, not comments**. Comments do not make up for bad code.


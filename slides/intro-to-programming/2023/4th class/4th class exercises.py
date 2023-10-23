##################
### Exercice 1 ###
##################

# - Define a function with two arguments:
#  + a string msg and a number nrepetitions 
#  + that prints msg, nrepetition times.

def print_n_times(msg, n):
    for x in range(n):
        print(msg)

print_n_times("test0", 0)
print_n_times("test1", 1)
print_n_times("test4", 4)


##################
### Exercice 2 ###
##################

# Read https://en.wikipedia.org/wiki/Fahrenheit and write a function that converts from Fahrenheit to Celsius, and another one that converts from Celsius to Fahrenheit

def Fahrenheit_to_Celsius(f):
    return (f - 32) * 5.0/9.0

def Celsius_to_Fahrenheit(c):
    return (c * 9.0/5.0) + 32
  
Fahrenheit_to_Celsius(15)
Celsius_to_Fahrenheit(15)
Fahrenheit_to_Celsius(-40)
Celsius_to_Fahrenheit(-40)


##################
### Exercice 3 ###
##################

# Define a function is_prime(x) which returns True if x is a prime number, else False. Use it to list all prime numbers below 1000.

def is_prime(n):
    if n < 3:
        return True
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

print([x for x in range(1, 1000) if is_prime(x)])





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



##################
### Exercice 4 ###
##################

# Two taxi companies propose differents pricing schemes: Company A charges 4.80€ plus 1.15€ by km travelled. Company B charges 3.20€ plus 1.20€ by km travelled. Write a first function which, given a distance, returns the costs of both companies, and a second function that returns 'company A' and 'company B', the cheapest company for a given distance.

def costs(distance):
    price_A = 4.8 + 1.15 * distance
    price_B = 3.2 + 1.20 * distance
    return (price_A, price_B)

def cheapest_company(distance):
    a, b = costs(distance)
    if a < b:
        return 'Company A'
    else:
        return 'Company B'

for d in range(1, 50):
    print(f"{d} km -> " + cheapest_company(d))



##################
### Exercice 5 ###
##################

# - Write a function are_anagrams(word1, word2) that tests if two words are anagrams, that is contain the same letters in different orders.

def are_anagrams(w1, w2):
    return sorted(w1) == sorted(w2)

print(are_anagrams('listen', 'silent'))
print(are_anagrams('listen', 'speak'))
##################
### Exercice 1 ###
##################

print("\n# Lottery pick")
# Lottery pick. Generate 100 random lottery tickets 
# (one ticket is a sequence of 5 digits) and pick one 
# winner out of it. 
from random import *

lottery_list=[]
for i in range(100):
    lottery_list.append(randrange(10000,99999))
print(lottery_list)
winner = sample(lottery_list,1)
print("Winner ticket: ", winner)


##################
### Exercice 2 ###
##################

print("\n# Generating random password")
# Note here that we could create set of character to define upper case, lower case, digit and punctuation
# As we want to make it shorter we will use the list of character available in the string module
import string
#from random import * 
import random

# write a program that genereate a random 10 character long password including 6 letters with 2 of them uppercase, 1 digit and one special symbol.
random_lower_letter = random.sample(string.ascii_lowercase,4)
print(random_lower_letter)
random_upper_letter = random.sample(string.ascii_uppercase,2)
print(random_upper_letter)
random_digit = random.sample(string.digits,1)
print(random_digit)
random_punctuation = random.sample(string.punctuation,1)
print(random_punctuation)


random_password = random_lower_letter + random_upper_letter + random_digit + random_punctuation
print(random_password)
print(random.shuffle(random_password))
print(type(random_password))
# Here we have a list and we need to concatenate it using an empty character "" and the join() function
random_password = ' '.join(random_password)
print(random_password)



##################
### Exercice 3 ###
##################

print("\n# Monte Carlo estimation of Pi")
# Monte Carlo estimation of Pi: one way to estimate the value of the π is to generate a large number of random points in 
# the unit square and see how many fall within the unit circle; their proportion is an estimate of the area of the circle. 
# See https://academo.org/demos/estimating-pi-monte-carlo. Implement the proposed algorithm to estimate the value of π.
import random

draws = 1000000

hits = 0
for _ in range(draws):
    x = random.random()  # returns a random number (float) between 0 and 1
    y = random.random()
    if x**2 + y**2 < 1:
        hits += 1

estimate1 = 4 * hits / draws

print("Estimate =", estimate1)

print(random.random())

##################
### Exercice 6 ###
##################
print("\n# N rows of Pascal's triangle")
# Write a program that prints the first N rows of Pascal’s triangle (see https://www.youtube.com/watch?v=XMriWTvPXHI).
N = 10  # number of lines to print

row = [0] * N
row[0] = 1

for _ in range(N):
    for i in row:
        print(i if i != 0 else '', end=' ')
    print()

    old_row = row

    row = [0] * N
    row[0] = 1
    for i in range(1, N):
        row[i] = old_row[i - 1] + old_row[i]
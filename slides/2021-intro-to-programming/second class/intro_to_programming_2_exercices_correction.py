#Exercices



##################
### Exercice 1 ###
##################
# Lists: 
#     - Given a list of numbers, print their sum 
#     - Given a list of numbers, print their product 
#     - Given a list of numbers, print the sum of their squares 
#     - Given a list of numbers, print the largest one 
#     - Given a list of numbers, print the second largest

list1 = [1,2,3,4,1]

print("\n# sum1:")
# sum
y=0
for x in list1:
    y += x
    print(y)


print("\n# sum2")
print(sum(list1))


print("\n# product")
# product
y=1
for x in list1:
    y *= x
    print(y)


print("\n# sum of their squares 1")
# sum of their squares 
y=0
for x in list1:
    y += x*x
#   y = y + x*x 
    print(y)


# largest one
print("\n# largest one1")
print(max(list1))

print("\n# largest one2")
y=0
for x in list1:
    if x>=y:
        y=x
print(y)


# second largest
print("\n# second largest 1")
list1.sort()
print(list1[len(list1)-2])


print("\n# second largest 2")
list1.remove(max(list1))
print(max(list1))

print("\n# second largest 3")
y = 0
z = 0
for x in list1:
    if x>=y:
        y=x
    if y>=z:
        z=y

print(z,y)


# NB :If you want to multiply all the items of the list you could do like
list1 = [1,2,3,4,1]
print("\nSquare of all items in a list 1")
for i in range(1,len(list1)):
    list1[i] *= list1[i]
    print(list1)

print("\nSquare of all items in a list 2")
[i**2 for i in list1]
print(list1)

##################
### Exercice 2 ###
##################

print("\n# List of word")
# Given a list of words, count the number of times each word 
# appears in the list (using dictionary)
list2 = [ "one", "two", "three","one"]

dictio ={}
for x in list2:
    if x in dictio:
        print("Already in the list")
        dictio[x]+=1
        # dictio[x] = dictio[x] +1
    else:
        dictio[x]=1
print(dictio)
    


##################
### Exercice 3 ###
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
### Exercice 4 ###
##################

print("\n# Generating random password")
# Note here that we could create set of character to define upper case, lower case, digit and punctuation
# As we want to make it shorter we will use the list of character available in the string module
import string
from random import * 

# write a program that genereate a random 10 character long password including 6 letters with 2 of them uppercase, 1 digit and one special symbol.
random_lower_letter = sample(string.ascii_lowercase,4)
print(random_lower_letter)
random_upper_letter = sample(string.ascii_uppercase,2)
print(random_upper_letter)
random_digit = sample(string.digits,1)
print(random_digit)
random_punctuation = sample(string.punctuation,1)
print(random_punctuation)

random_password = random_lower_letter + random_upper_letter + random_digit + random_punctuation
print(random_password)
shuffle(random_password)
# Here we have a list and we need to concatenate it using an empty character "" and the join() function
random_password = ' '.join(random_password)
print(random_password)



##################
### Exercice 5 ###
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

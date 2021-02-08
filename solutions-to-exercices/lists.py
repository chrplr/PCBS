## lists ##

# * Read about:
#    - [Python Lists](https://www.w3schools.com/python/python_lists.asp)
#    - [List comprehensions](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
#    - if you have time, read <https://automatetheboringstuff.com/chapter4/>


################################################################################
# Given a list of numbers, print their sum

liste = [1, 4, -6, 7, 2, 3, 9, 11, 6]

somme = 0
for x in liste:
    somme = somme + x
print(f'Sum of {liste} = {somme}')

# solution 2
print(f'Sum of {liste} = {sum(liste)}')

################################################################################
# Given a list of numbers, print their product

liste = [1, 4, -6, 7, 2, 3, 9, 11, 6]

prod = 1
for x in liste:
    prod = prod * x
print(f'product of {liste} = {prod}')

#or
import numpy as np
print(f'product of {liste} = {np.prod(liste)}')


################################################################################
# Given a list of numbers, print the sum of their square
somme_des_carres = 0
for x in liste:
    somme_des_carres = somme_des_carres + x * x
print(f'Sum of squares of {liste} = {somme_des_carres}')

################################################################################
# Given a list of numbers, print the largest one.

maximum = float("-inf")
for x in liste:
    if x > maximum:
        maximum = x
print(f'max of {liste} = {maximum}')

################################################################################
# Given a list of numbers, print the second largest one.

print(f'Second max of {liste} = {sorted(liste, reverse=True)[1]}')

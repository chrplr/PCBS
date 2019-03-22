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
print(somme)

# solution 2
print(sum(liste))

################################################################################
# Given a list of numbers, print the sum of their square
somme_des_carres = 0
for x in liste:
    somme_des_carres = somme_des_carres + x * x
print(somme_des_carres)

################################################################################
# Given a list of numbers, print the largest one.

maximum = float("-inf")
for x in liste:
    if x > maximum:
        maximum = x
print(maximum)

################################################################################
# Given a list of numbers, print the second largest one.

print(sorted(liste, reverse=True)[1])

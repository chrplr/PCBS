"""
Two taxi companies propose differents pricing schemes: "A charges 4.80€ plus 1.15€ by km travelled; B 3.20€ plus 1.20€ by km travelled. Write a script that finds which company is the cheapest as a function of the distance to travel.
"""

def selectAorB(distance):
    priceA = 4.8 + 1.15 * distance
    priceB = 3.2 + 1.20 * distance
    if priceA < priceB:
        return 'Take A!'
    else:
        return 'Take B!'

for d in range(1, 50):
    print(f"{d} km -> " + selectAorB(d))

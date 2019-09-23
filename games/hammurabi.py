#! /usr/bin/env python3
# Time-stamp: <2019-03-09 13:12:26 christophe@pallier.org>

"""Game of Hammurabi (from a BASIC listing in *The Acorn Atom Magick Book*, Timedata, 1981).

In this game, you are King Hammurabi and each year you determine how to
allocate your scarce bushels of grain: buying and selling acres of land,
feeding your population, and planting seeds for next year's crops.

Each person needs 15 bushels of grain each year to live and can seed at most 25 grain per year.

It is useless to seed more than 2 grain per acre.

"""


import random

population = 100  # humans
grain = 3000
land = 1000

year = 0

while population > 0:
    print('')
    print("O Hammurabi, king of Sumaria,")
    print(f"Your subjects now number {population}.")
    print(f"Your kingdom covers {land} acres.")
    print(f"You have {grain} bushels of grain.")

    land_price = random.randint(20, 25)
    print(f"Land is {land_price} bushels per acre")
    print('')

    acres = input(f"How many acres do you buy (price={land_price} bushels per acre; max={grain // land_price}) (negative number if you want to sell)? ")
    acres = int(acres)
    assert acres * land_price <= grain

    land = land + acres
    grain = grain - (land_price * acres)
    print(f"{grain} bushels remaining.")
    food = input(f"How many bushels for food (Max={15 * population})? ")
    food = int(food)
    assert(food <= grain )

    grain = grain - food
    print(f"{grain} bushels remaining.")

    seed = input("How many bushels for seed? ")
    seed = int(seed)
    assert (seed <= grain)

    grain = grain - seed
    print(f"{grain} bushels remaining.")

    if seed > 2 * land:  # max production because of land size
        seed = 2 * land

    if seed > 25 * population:  # max production is limited by human forces
        seed = 25 * population

    rats = random.randint(0, 1 + grain // 2)  # rats
    harvest = seed // 4 + random.randint(0, seed * 4)
    grain = grain + harvest - rats

    # update population
    deaths = population - food // 15
    if deaths < 1:
        deaths = 0
    population -= deaths

    newborns = population // 20 + random.randint(0, population // 20) # newborn
    population +=  newborns

    pleague  = 0  # deaths by pleague
    if random.randint(1, 4) == 1:
        pleague = population // 3 + random.randint(0, population // 4)
    population = population - pleague

    year = year + 1
    print("O King, I beg to report that")
    print(f"in Year {year} of your reign,")
    print(f"you harvested {harvest} bushels")
    if rats > 0:
        print(f"But rats ate {rats} bushels.")
    print(f"{deaths} People starved, {newborns} were born.")
    if pleague > 0:
        print(f"{pleague} died of pleague")

print("As you have no subjects left,")
print("This is the end of your reign.")

import itertools
import time

# List of all character that will be tested
character_tested = ("abcdefghijklmnopqrstuvwxyz")

# Ask user the password
password = input("What is your password?\n")

# checking starting time
tstart = time.time()

# How many combinations were tested
combination_counter = 1

# Number of character in the password (starting by 1)
passwordLength = 1

# Tryng all length from 0 to 15
for passwordLength in range(1,15):
#    print("For ", passwordLength, "character long, there are ", len(list(password_combinations)), " possible combination")

    print("\n")
    #This finds all of the possible combinations of characters that are of the correct length.
    password_combinations = (itertools.product(character_tested, repeat = passwordLength))

    #These print information for the user on the progress of the crack.
    print("currently working on passwords with ", passwordLength, " chars")
    print("We are currently at ", (combination_counter / (time.time() - tstart)), "attempts per seconds")
    print("It has been ", time.time() - tstart, " seconds!")
    print("We have tried ", combination_counter, " possible passwords!")

    #This is the way to print the products of generators.
    for i in password_combinations:

        #As the itertools.products() returns a tuple, it has to be converted into a sting.
        i = str(i)

        #The parts that were added as a result of conversion from tuple have to be removed.
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")

        #This checks if the password created by the user was correct.
        if i == password:

            #This takes the time at which the program finished.
            tend = time.time()

            #This works out the time it took to find the password.
            timetaken = tend - tstart

            #This tells the user how long it took to find the password as well as how many attempts it took.
            print("Found it in ", timetaken, " seconds and ", combination_counter, "attempts")

            #This tells the user how many attempst were made per second.
            print("That is ", combination_counter / timetaken, " attempts per second!")

            #This prints the password to confirm for the user that the program was sucessful.
            print(i)

            #This stops the program from exiting until the user presses enter.
            input("Press enter when you have finished")

            #This exits the program
            exit()

        #This increases the number of combinations tried by one to show that one more has been tried.
        combination_counter += 1

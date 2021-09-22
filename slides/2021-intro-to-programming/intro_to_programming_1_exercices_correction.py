# Exercice 1: Write code that prints the string “All work no play makes Jack a dull boy” 50 times

# Exercice 2: Write code that prints the squares of all integers between 1 and 100 using range

# Exercice 3: Write code that browses the integer from 0 to 100 but only prints the number 1, 50 and 100

# Exercice 4: Write code that prints only odd numbers between 0 and 100

# Exercice 5: Write code that computes the factorial of aninteger (no function, no recursion, just a loop)



##################
### Exercice 1 ###
##################

print("Exercice 1")
# solution 1
sentence = "All work no play makes Jack a dull boy"

for i in range(50):
	print(sentence)

# Solution 2
print(sentence*50)


##################
### Exercice 2 ###
##################

print("Exercice 2")
for i in range(1,101):
	print(i*i)


##################
### Exercice 3 ###
################## 

print("Exercice 3")
# solution 1
for i in range(101):
	if i == 1: 
		print(i)
	elif i == 50:
		print(i)
	elif i == 100:
		print(i)

# solution 2
for i in range(101):
	if i == 1 or i == 50 or i ==100:
		print(i)

# solution 3
for i in range(101):
	if i in [1, 50, 100]:
		print(i)


##################
### Exercice 4 ###
##################

print("Exercice 4")
# solution 1
for i in range(101):
	if i%2 != 0:
		print(i)

# solution 2
for i in range(101):
	if i%2:
		print(i)

# solution 3
for i in range(1,101,2):  # in that solution the range fonction increment 2 by 2 so i would always be odd.
	print(i)



##################
### Exercice 5 ###
##################

print("Exercice 5")
# solution 1
j = 1
for i in range(1,15):
	j= i * j
	print(i,j)

	


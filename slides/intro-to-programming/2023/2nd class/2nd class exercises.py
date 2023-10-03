##################
### Exercice 1 ###
##################

list1=[1,2,3,4,1]

# for loop
	# sum
	# product
	# sum of squares

sum1 = 0
product1 = 1
square1 =0

for idx in list1:
	# sum
	sum1 = sum1 +idx
	# product
	product1 = product1 * idx
	# sum of squares
	square1 = square1 + idx * idx


print(sum1,product1, square1)


# while loop
	# sum
	# product
	# sum of square
sum2 = 0
product2 = 1
square2 =0

i=0
while i < len(list1):
	print(i)
	# sum
	sum2 += list1[i]
	# product
	product2 *= list1[i]
	# sum of square
	square2 += list1[i]*list1[i]
	i+=1
print(sum2, product2, square2)
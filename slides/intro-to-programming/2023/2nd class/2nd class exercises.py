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



# largest number

##solution1
list1=[1,2,3,4,1]
maximum=list1[0]
for idx in list1:
	if idx>maximum:
		maximum = idx
print('largest number = ')
print(maximum)


##solution 2
maximum = max(list1)
print(maximum)


# while
list1=[1,2,3,4,1]
i = 0
hv = list1[0]
while i < len(list1):
	print(i,hv)
	if hv < list1[i]:
		hv = list1[i]
	i += 1
print(hv)



# second largest
##solution 1
list1=[1,2,3,4,1]
maximum=list1[0]
second_max =0
for idx in list1:
    if idx>maximum:
        second_max = maximum
        maximum = idx
        
    elif idx > second_max and idx < maximum:
        second_max = idx
print('second largest number = ')
print(second_max)


##solution 2
list1=[1,2,3,4,1]
list1.remove(max(list1))
print(max(list1))


# while
list1=[1,5,3,4,1]
i = 0
large = list1[0]
large2 = 0
while i < len(list1):
	print(i,large)
	if large < list1[i]:
		large2 = large
		large = list1[i]
	elif list1[i] > large2 and list1[i] < large:
		large2 = list1[i]
	i += 1
print(large,large2)

##################
### Exercice 2 ###
##################

l=[1, 2, 3, 6, 7, 4, 5]

# from list to tuple
t = tuple(l)
print(type(t))

# min and max of each tuple

tuple1 = [(1,3,2), (6,4,5), (8,7,9)]

# solution 1
minimum = 0
maximum = 0
for t in tuple1:
	for idx in t:
		if idx == t[0]:
			minimum = maximum =idx
		else:
			if idx > maximum:
				maximum = idx
			elif idx < minimum:
				minimum = idx
	print(minimum, maximum)

# solution 2
for t in tuple1:
	print(min(t))
	print(max(t))


## Return the tuples with only positive elements
test_tuples = [(1,2,3), (4,5,6), (7,8,9), (-1,2,3)]
for t in test_tuples:
	for idx in t:
		if idx<0:
			test_tuples.remove(t)

print(test_tuples)


##################
### Exercice 3 ###
##################	

## Order l and transform it into a set
l.sort()
print(l)
s=set(l)
print(type(s))

## Remove the 4th items
set1 = { 1,2,3,3,4,5,6,7}
list2 = list(set1)
list2.remove(list2[3])
set2 = set(list2)
print(set2)

## Print if Sets have items in common
a = {"apple", "pineapple", "peach", "pears", "lemon", "lychee"} 
b = {"banana", "mango" , "lychee", "kiwi", "apple", "orange"}

l_a = list(a)
l_b = list(b)

# solution 1
for itema in l_a:
	for itemb in l_b:
		if itema == itemb:
			print(itema)

# solution 2
print(a.intersection(b))


##################
### Exercice 4 ###
##################	

animaList=["dog", "horse", "cat", "fish", "cat", "fox", "tiger", "tiger", "flamingo", "cat"]

dict1=dict()

for item in animaList:
	if item in dict1:
		dict1[item] +=1
	else :
		dict1[item]=1
print(dict1)

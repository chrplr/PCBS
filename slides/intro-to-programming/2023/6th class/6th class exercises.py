##################
### Exercice 1 ###
##################

print("Exercise 1")

# - 1 Write a script that prints the first 10 lines of a file

MyTestFile = open('Survival rules for programming.txt', 'r')
lines = MyTestFile.readlines()
print(lines[0:9])
MyTestFile.close()

print("solution 2")

with open('Survival rules for programming.txt', 'r') as MyTestFile:
  lines = MyTestFile.readlines()
  for idx,line in enumerate(lines):
    if idx <10:
      print(line)


##################
### Exercice 2 ###
##################

print("Exercise 2")

# - 2 Write a script that prints the last 10 lines of a file (or the whole file is it is less than 10 lines long)

MyTestFile = open('Survival rules for programming.txt', 'r')
lines = MyTestFile.readlines()

nbline = len(lines)
nbline_toprint = 10

if nbline_toprint >= nbline:
  index = nbline
else:
  index = nbline_toprint


for i in range(1,index):
  print(lines[-i])

MyTestFile.close()


print("solution 2")

with open('Survival rules for programming.txt', 'r') as MyTestFile:
  lines = MyTestFile.readlines()
  print(len(lines))
  for idx in range(len(lines)-index,len(lines)):
    print(lines[idx])


##################
### Exercice 3 ###
##################

print("Exercise 3")

#- 3 Write a script that opens and read a text file, and print all the lines that contain a given target word

def print_line_with_specific_word(text,word):
  for l in range(1,len(text)):
    if word in text[l]:
      print(text[l])
    else :
      print("FALSE")
  

with open('Survival rules for programming.txt', 'r') as MyTestFile:
  text = MyTestFile.readlines()
  
  print_line_with_specific_word(text,"manual")



##################
### Exercice 4 ###
##################

print("Exercise 4")

# - 4 compute the number of words (removing punctuation) in a text file (Hint: use split() functions)

import string

def count_words(text):
  c = 0
  for l in text: # 
    print(l.split()) # split the line
    for w in l.split(): # for loop through all word of strip and split line
      print(list(w))
      print(type(w))
      for char in list(w):
        #print(c)
          if char in string.punctuation: # If character in the string punctuation collection
            w =w.replace(char,'') # You replace a punctuation by empty space
      if w != '': # check that you don't have an empty word
        c +=1
      print(w)
          
  return c

MyTestFile = open('Survival rules for programming.txt', 'r')
text = MyTestFile.readlines()

print(count_words(text))

MyTestFile.close()

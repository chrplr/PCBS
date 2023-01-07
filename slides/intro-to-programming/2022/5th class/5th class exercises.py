##################
### Exercice 1 ###
##################

# 1 - Write a recursive function to reverse a list

def rev(l):
  if len(l) == 0: # ending condition
    return []
  return [l[-1]] + rev(l[:-1]) # return the last element l[-1] and call the next iteration of the function rev(l[:-1]) with the new list (without the last element)
  
print(rev(["a", "b", "c", "d"]))


##################
### Exercice 2 ###
##################

# 2 - Write a recursive function to generate all permutations of a string of character

def perms(s):
  if(len(s)==1): # ending condition
    return [s]
  result=[]
  for i,v in enumerate(s): # run through a list with the position and the value at the same time
    result += [v+p for p in perms(s[:i]+s[i+1:])]  # return 
  return result

print(perms('abc'))

# Other way to write the function by just decomposing the second for loop
def perms2(s):
    if(len(s)==1): # ending condition
      return [s] 
    result=[]
    for i,v in enumerate(s): # run through a list with the position and the value at the same time
      for p in perms2(s[:i]+s[i+1:]):  # for loop running through the rest of the list
        result += [v+p]   # return the remaining list
    return result

print(perms2('abc'))

##################
### Exercice 3 ###
##################

#3 - Write a script that returns the pathnames of all the files contained inside a directory (at any depth of the hierarchy). You will need to use os.listdir() and os.path.isdir().


import os # os is the package to access and manipulate operation system functionnality https://docs.python.org/3/library/os.html
 
def listdirs(rootdir):
  for file in os.listdir(rootdir): # running through all file in a directory
    print(file)  # print all files
    d = os.path.join(rootdir, file)  # appending the name of the file to the actual path 
    if os.path.isdir(d): # if the new path is a directory and not a file
      print(d)  # print the new file
      listdirs(d)  # call the new iteration of the function that goes into a deeper directory
 
rootdir = '/home/dbhenri/Documents/Cours python/PCBS/slides/intro-to-programming/2022/'  # give the starting directory (it depends of your own architecture and operation system)
listdirs(rootdir)


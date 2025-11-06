

print "Think about a number between 1 and 100 and I will try to guess it"
max = 100
min = 1
myguess = (max + min)/2
answer = raw_input('Is it ' + str(myguess) + "? (y/+/-)")

while answer != 'y':
    if answer == '+':
        min = myguess
    else:
        max = myguess
    myguess = (max + min)/2
    answer = raw_input('Is it ' + str(myguess) + '? (y/+/-)')

print 'I am so good!!!'

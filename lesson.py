import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))

for arg in sys.argv[1:]:
  print(arg)
n = input("Enter a number: ")
# n = 100
try:
    int(n)
except TypeError:
    #Handle the exception
    print 'Please enter an integer'

i = 0

while i <= n :
    if i % 5 == 0 and i % 3 == 0:
        print "fizzbuzz"
    elif i % 3 == 0: 
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i 
    i = i + 1

#n - 1

# Have a hard-coded upper line, n.
# Print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
# Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
# Print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen).
# Each number should be printed on a new line.
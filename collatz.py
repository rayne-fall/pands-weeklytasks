# collatz
# Author: Sylvia Chapman Kent
# asks users to input any positive integer, divides the current value by two (if even) or multiplies it by three and adds one (if odd), and ends once the value reaches 1

number = int(input("Enter any positive integer: "))

if (number%2) == 0: 
    result = (number/2) # if value is even, value is divided by 2
elif number == 1:
    print ("Program end: value = 1") # ends program if value reaches 1
else:
    result = ((number*3)+1) # if value is odd, value is multplied by 3 and 1 is added

while (result%2) == 0:
    print(result)
    result /= 2
    if result == 1.0:
        print ("Program end: value = 1")
while (result%2) != 0:
    print (result)
    result *= 3+1

# Incomplete: fails with higher numbers and doesn't display answeres in a single line


# References
# Article showing how to check if a number is even or odd in python https://www.programiz.com/python-programming/examples/odd-even
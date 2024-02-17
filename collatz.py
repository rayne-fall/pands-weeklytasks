# collatz
# Author: Sylvia Chapman Kent
# demonstrates the Collatz conjecture and prints the results on a single line

def collatz_conjecture(number): # defines the function we're going to use on the user's input
    while (number!=1): # breaks the loop and ends the program when number reaches 1
       if (number%2==0):
          number = (number//2) # divides by 2 if number is even
          print (number, end=" ")
       else:
          number = (3*number)+1 # multiplies by 3 and adds 1 if number is odd
          print (number, end=" ")

user_input= int(input("Enter number: "))
collatz_conjecture(user_input) 

# References
# Article showing how to check if a number is even or odd in python https://www.programiz.com/python-programming/examples/odd-even
# W3 schools article showing how to define a function https://www.w3schools.com/python/python_functions.asp 
# Comments showing how to display outputs in a single line with spacing between https://stackoverflow.com/questions/58655551/how-to-print-output-in-single-line
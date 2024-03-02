# squareroot
# Author: Sylvia Chapman Kent
# reads in a positive number and outputs the approximate square root

# using Newton's method lets us start with a broad guess at the answer and continually narrow it down until it gets close enough to the actual answer for us to accept it

def squrt(number, attempt, tolerance):
    next_attempt = (attempt+number/attempt)/2 # simplified version of the formula for Newton's method
    if abs(attempt-next_attempt) <= tolerance:
        return (next_attempt) #stops the function when the result comes within the accepted tolerance
    
    else:
        return squrt(number, next_attempt, tolerance) #keeps calling the function until the result is within the accepted tolerance

number = float(input("Enter a positive number: "))
tolerance = 0.0001 # we'll accept the result once it gets close enough to the actual value
attempt = number/2 # gives the function a place to start guessing the answer from
square_root = squrt(number, attempt, tolerance)

print(f"The square root of {number} is approx. {square_root}")

# References:
# Section 4.9 of Calculus Volume 1 by Strang and Herman describing how to calculate roots using Newton's method https://openstax.org/books/calculus-volume-1/pages/4-9-newtons-method
# W3Schools page on functions in Python https://www.w3schools.com/python/python_functions.asp
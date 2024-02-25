# weekday
# Author: Sylvia Chapman Kent
# tells us if today is a weekday or not

from datetime import datetime

today = datetime.today() # determines which day of the week it is

if today.weekday() == 6: # prints the weekend message if today is Sunday
    print ("It's the weekend! Time to relax :)") 

elif today.weekday() == 5: # prints the weekend message if today is Saturday
    print ("It's the weekend! Time to relax :)")

else: # prints the weekday mesage on an day that isn't Saturday or Sunday
    print ("It's a weekday. Back to the grind :(") 

# References:
# Shows how to import the datetime module https://pynative.com/python-current-date-time/
# Shows how to use the datetime module to determine which day of the week it is https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
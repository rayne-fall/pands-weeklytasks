# accounts
# author: Sylvia Chapman Kent
# reads in a ten digit number and returns a redacted version with only the final four digits visible

account_number = input("Enter your 10 digit account number ")

print(f"The account number is XXXXXX{account_number[6:]}")

# References:
# W3 Schools page on slicing strings https://www.w3schools.com/python/python_strings_slicing.asp
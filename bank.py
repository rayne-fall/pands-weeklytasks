# bank
# author: Sylvia Chapman Kent
# prompt the user to enter two money amounts in cent and output the sum of these two figures in euros and cents

amount_1 = int(input("Enter amount 1 in cent "))
amount_2 = int(input("Enter amount 2 in cent "))
total = int((amount_1+amount_2))

# need to show total to two decimal places as this is the usual convention for writing money figures

result_as_decimal = int(float(f'{total:.2f}'))

# need to divide result_as_decimal by 100 to convert from cents to euros

answer_in_euro = result_as_decimal/100.00

print (f"The total is €{answer_in_euro}")

# References
# Comment by The_Outsider showing that "answer" needs to be entered as a string when printing result https://stackoverflow.com/questions/45744364/python-how-do-i-add-variables-with-integer-values-together
# Comment by Ehsan Fathi about using f strings to show result with two decimal places https://stackoverflow.com/questions/2075128/python-print-all-floats-to-2-decimal-places-in-output
# Comment by FdoBad and user3064538 about converting strings to floats to avoid "invalid literal for int() with base 10 error" when converting result to euros and cents https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10


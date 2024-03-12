# weekly task 7 
# author: Sylvia Chapman Kent
# reads in a .txt file and outputs the number of "e"s in the file

import sys

filename = sys.argv[1] # takes the filename entered in the command line

with open (filename, "r") as f: # opens the text file in read mode
   number_of_e = sum(line.count ("e") for line in f) # calculates the number of times the letter e appears in each line and assigns the total to the variable number_of_e

print (number_of_e) # prints how many time e appears in the file


# References

# wordpress post showing how to take filename from command line arguments https://tech.sadaalomma.com/python/how-to-take-file-name-as-input-in-python/
# StackOverflow post with comments showing how to use sum and generator expressions to get the total number of instances https://stackoverflow.com/questions/69319005/count-a-string-in-a-text-file-with-python
# .txt file: Transcript of The Magnus Archives Episode 1 written by Jonathan Sims and directed by Alexander J Newell https://rustyquillcom.sharepoint.com/:w:/r/_layouts/15/Doc.aspx?sourcedoc=%7B57E26BB9-7523-4CBF-BB88-5336E917A98F%7D&file=MAG%20001%20-%20Anglerfish%20-%20Transcript%20Re-formatted.docx&action=default&mobileredirect=true
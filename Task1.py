"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def getAllNumbers():
    all_numbers = []
    for text in texts:
        all_numbers.append(text[0])
        all_numbers.append(text[1])
    for call in calls:
        all_numbers.append(call[0])
        all_numbers.append(call[1])
    return all_numbers
    
def getUniqueNumbers():
    all_numbers = getAllNumbers()
    unique_numbers = []
    for number in all_numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

print("There are " + str(len(getUniqueNumbers())) + " different telephone numbers in the records.")

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

"""PART A SOLUTION"""
def getNumbersCalledByBangalore():
  receiving_numbers = []
  for call in calls:
    if call[0].startswith('(080)'):
      receiving_numbers.append(call[1])
  return receiving_numbers

def getAllAreaCodes():
  receiving_numbers = getNumbersCalledByBangalore()
  all_area_codes = []
  for number in receiving_numbers:
    if number.startswith('140'):
      all_area_codes.append('140')
    elif number.startswith('('):
      end_index = number.find(')')
      all_area_codes.append(number[0:end_index+1])
    elif number.startswith('7') or number.startswith('8') or number.startswith('9'):
      all_area_codes.append(number[0:4])
  return all_area_codes

def getUniqueAreaCodes():
  all_area_codes = getAllAreaCodes()
  unique_area_codes = list(set(all_area_codes))
  unique_area_codes.sort()
  return unique_area_codes
  
def printUniqueAreaCodes():
  unique_area_codes = getUniqueAreaCodes()
  print("The numbers called by people in Bangalore have codes:")
  for area_code in unique_area_codes:
    print(area_code)

printUniqueAreaCodes()

"""PART B SOLUTION"""
def getPercentage():
  all_area_codes = getAllAreaCodes()
  total_calls = len(all_area_codes)
  bangalore_receiving_calls = all_area_codes.count('(080)')
  return round(bangalore_receiving_calls / total_calls * 100, 2)

print(str(getPercentage()) + 
      " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
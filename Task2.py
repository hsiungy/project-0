"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def getCallDurations():
    call_durations = {}
    for call in calls:
        calling_number = call[0]
        receiving_number = call[1]
        call_duration = int(call[3])
        if calling_number not in call_durations:
            call_durations[calling_number] = call_duration
        else:
            call_durations[calling_number] += call_duration
        if receiving_number not in call_durations:
            call_durations[receiving_number] = call_duration
        else:
            call_durations[receiving_number] += call_duration
    return call_durations

def getLongestCaller():
    call_durations = getCallDurations()
    return max(call_durations, key=call_durations.get)

def getLongestCallTime():
    call_durations = getCallDurations()
    return max(getCallDurations().values())

print(getLongestCaller() + " spent the longest time, " +
        str(getLongestCallTime()) + " seconds, on the phone during September 2016.")
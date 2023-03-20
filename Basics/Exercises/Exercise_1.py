"""
Ask for the number of seconds 
and pass it to hours, minutes and seconds
"""

sec = int (input("Enter the number of seconds >> "))

hour = sec // 3600
temp = sec % 3600
minutes = temp // 60
seconds = temp % 60

print("Hours >>", hour)
print("Minutes >>", minutes)
print("Seconds >>", seconds)
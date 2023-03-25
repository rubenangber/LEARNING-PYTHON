"""
   P  O  L  L  I  T  O
   0  1  2  3  4  5  6  --> Index
  -7 -6 -5 -4 -3 -2 -1  --> Negative index
"""

letter = "POLLITO"[4]
print(letter)

array = "POLLITO"
letter = array[-2]
print(letter)

# [start : end]
subArray = array[:] # All
print(subArray)

subArray = array[2:]
print(subArray)

subArray = array[:3]
print(subArray)

subArray = array[-6:-1]
print(subArray)

# Slicing with jumps
subArray = array[::2]
print(subArray)

subArray = array[::-1] # Reverse
print(subArray)
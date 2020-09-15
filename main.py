# Author: Woosung Lim wml5207@psu.edu
# Collaborator: Alex Delargy add5529@psu.edu
# Collaborator: John Sheilds jts5975@psu.edu
# Collaborator: Varun Patel vkp5116@psu.edu
# Section: 2
# Breakout: 6

def sum_n(n):
  if n <= 0:
    return 0
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if n <= 1:
    print(s)
  else:
    print(s) 
    print_n(s,n-1)
  
num=int(input("Enter an int: "))
print(f"sum is {sum_n(num)}.")
print_n(input("Enter a string: "), num)
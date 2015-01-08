import sys

n = 0

if len(sys.argv) == 1: # handle when no user input at command line
  while True:
    try:
      n = int(raw_input("Please enter a number! ")) 
    except ValueError: 
      print("oops, not a number")
      continue
    else:
      break
else: # handle user input at command line
    try:
        n = int(sys.argv[1])
    except ValueError:
      print("Oops, not a number")
      while True:
        try:
          n = int(raw_input("Please enter a number! "))
        except ValueError:
          print("Oops, not a number")
          continue
        else:
          break
      
print("Fizz buzz counting up to " + str(n)) # print the number entered at command line

for num in range(1,n+1): # looping thru range of numbers and printing Fizz and Buzz
  if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)
        

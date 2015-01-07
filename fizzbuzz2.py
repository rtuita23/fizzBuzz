import sys

if len(sys.argv) >= 2: # user supplied input at command line
  try:
    n = int(sys.argv[1])
    if n is int
      print("Fizz buzz counting up to " + str(n))

    for num in range(1,n+1):
      if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
      elif num % 3 == 0:
        print("Fizz")
      elif num % 5 == 0:
        print("Buzz")
      else:
        print(num)
  except ValueError:
    print("This is not a number!")
    n = int(raw_input("Please enter a number: "))
    
    print("Fizz buzz counting up to " + str(n))

    for num in range(1,n+1):
      if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
      elif num % 3 == 0:
        print("Fizz")
      elif num % 5 == 0:
        print("Buzz")
      else:
        print(num)
    
else:
  try:
    n = int(raw_input("Please enter a number! "))
    print("Fizz buzz counting up to " + str(n))

    for num in range(1,n+1):
      if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
      elif num % 3 == 0:
        print("Fizz")
      elif num % 5 == 0:
        print("Buzz")
      else:
        print(num)
  except ValueError:
    print("This is not a number!")
    n = int(raw_input("Please enter a number: "))
    
    print("Fizz buzz counting up to " + str(n))

    for num in range(1,n+1):
      if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
      elif num % 3 == 0:
        print("Fizz")
      elif num % 5 == 0:
        print("Buzz")
      else:
        print(num)

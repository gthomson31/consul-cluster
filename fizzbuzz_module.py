import sys

# Pulling in the Var from Bash to use in Python
n = int(sys.argv[1])

# Defining the FizzBuzz Function
def fizzBuzz(n):
   if n% 3 == 0 and n%5 == 0:
      print("FizzBuzz")
   elif n %3 == 0:
      print("Fizz")
   elif n% 5 == 0:
      print("Buzz")
   else:
      print(str(n))

# Kicking off the function
fizzBuzz(n)




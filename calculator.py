import sys
class functions:
#Add your function below using the template
  # def funcName(input):
      # whatever you are doing
      # print(variable)

   def index(a,b):
      print(a ** b)


def add(a, b):
	return a + b
def square(n):
  return n**2


def squareroot(x):
    return x ** (1.0 / 2)

def modulus(n, m):
    return n % m

   def div(n,m):
      print(n / m)


   def add(a,b):
      print(a + b)

   def fact(x):
      total = 1

      while x != 0:
         total = total * x
         if x > 0:
            x = x - 1
         elif x < 0:
            x = x + 1
      return total


   def multi(n,m):
       print(n * m)
     
   def square(n):
      print(n ** 2)


   def abs(x):
      if x < 0:
         print(x = -x)
      else:
         print(x)
   
   def percent(x):
      print(x / 100.0)
      
    
if __name__ == "__main__":
# So this main func takes in a function name and variable(s) and assigns them to variables. 
   fnc = input("What function do you want to use? ")
   n = input("What is you input?(Seperate values with a space! ")
   if len(n) > 1:
#we split just so that the input is in lst for if # of ints is greater than one
      n = [int(n) for n in n.split()]
      getattr(functions, fnc)(int(n[0]), int(n[1]))
   else:
      getattr(functions, fnc)(int(n))
#the getattr function can take input = n, and a variable = fnc and will go to the function with the same name as fnc and pass in n

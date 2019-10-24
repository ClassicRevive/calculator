import sys
class functions:
#Add your function below using the template
  # def funcName(input):
      # whatever you are doing
      # print(variable)

   def index(a,b):
      print(a ** b)

   def div(n,m):
      print(n / m)

   def add(a,b):
      print(a + b)

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

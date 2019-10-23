
def div(n, m):
   return n / m

def add(a, b):
	return a + b

def multi(n, m):
    return n * m
  
def square(n):
	print n ** 2

def main():
	x = square(15)
	print(x)

def fact(x):
   total = 1

   while x != 0:
      total = total * x
      if x > 0:
         x = x - 1
      elif x < 0:
         x = x + 1
   return total



if __name__ == "__main__":
  print("test")

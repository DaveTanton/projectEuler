fibcount = 50
num1, num2 = 0, 1
count = 0
total = 0
max = 4000000

while count < fibcount:
  fib = num1 + num2
  num1 = num2
  num2 = fib
  if num2%2 == 0:
      total+=num2
      if (total>max):
        print("total:",fib)
        break
count += 1

#needs work

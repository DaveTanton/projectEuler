def factors (n):
  r=[]
  for x in range(1,n+1):
    y = n % x
    if y==0:
      r.append(x)
  return r

def isPrime(n):
  f = factors(n)
  if len(f)==2:
    return True
  else:
    return False

def primeFactors(n):
  r=[]
  f = factors(n)
  # TODO find the prime factors
  for x in f:
    if isPrime(x):
      r.append(x)
  return r

def maxFactor(n):
  r=primeFactors(n)
  # only returns max prirme
  max=r[len(r)-1]
  return max

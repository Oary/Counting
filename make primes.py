out=open("primes.txt", "w")
UPPERLIMIT = 500
import math
def primeQ(num):
  primeq = null
  if math.sqrt(num) < 2:
    primeq = True
  for j in range(2, math.sqrt(num):
    if num % j == 0:
      primeq = False
      break
    elif num % i != 0:
      primeq = True
  return primeq
for i in range(2, UPPRLIMIT):
	if primeQ(i)==True:
    out.write(i)

out=open("primesBinary.txt","w")
import math
intes=open("primes.txt")
ints=intes.read().split("\n")
for i in ints:
  out.write(str(bin(int(i)))[2:]+"\n")

#!/usr/bin/python

import math

# sha256 key values

primes = [2,3,5,7,11,13,17,19]

# for first 8 primes, take square root, take fractional part, multiply by 2**32, truncate to integer

for i in primes:
  a = math.pow(i, 1.0/2.0)
  b = math.fmod(a,1.0)
  c = b * 2**32
  d = math.trunc(c)
  e = "0x%0.8X" % d
  print e

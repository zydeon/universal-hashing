#!/usr/bin/env python3

from math import ceil, log2
from primesieve import nth_prime
from random import randint

class UniversalHashing:
  """ N = #bins
      p = prime number st: p >= N """
  def __init__(self, N, p = None):
    self.N = N
    if p is None:
      p = nth_prime(1, 1 << max(32, ceil(log2(N))))
    assert p >= N, 'Prime number p should be at least N!'
    self.p = p

  def draw(self):
    a = randint(1, self.p - 1)
    b = randint(0, self.p - 1)
    return lambda x: ((a * x + b) % self.p) % self.N

if __name__ == '__main__':
  N = 50       #bins
  n = 100000   #elements
  H = UniversalHashing(N)
  h = H.draw()

  T = [0] * N
  for _ in range(n):
    x = randint(0, n * 10)
    T[h(x)] += 1

  for i in range(len(T)):
    print(T[i] / n)    # This should be approximately equal

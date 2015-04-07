# -*- coding: utf-8 -*-

import numpy as np
import random

def binary_matrix_generator(r, c):
  a = np.random.random_integers(0, 1, (r, c))
  print "%d %d" % (c, r) 
  for r in a:
    print " ".join(map(str, r.tolist()))
  return a

if __name__ == "__main__":
  print binary_matrix_generator(4, 5)


import math as mt
from itertools import permutations
import numpy as np
from array import *
import itertools
from re import search
import sys,os
from models.materials import Material

def Populate(superstrate,substrate,min_layer_thickness,max_layer_thickness,step,max_layer_number,materials):
  out = []
  mat_len = len(materials)
  for i in range(1, max_layer_number+1):
    n_layers = i
    product_list = list(itertools.product([i for i in range(min_layer_thickness, max_layer_thickness+1, step)], repeat = n_layers))
    mat = [item for item in list(itertools.product(materials, repeat=n_layers)) if Search_substr(''.join(item),[str(i)+str(i) for i in materials])==0]
    for k in range(len(mat)):
        for l in range(len(product_list)):
          dict = {
          'm_list' : list(itertools.chain([Material(superstrate), *[Material(x) for x in mat[k]], Material(substrate)])),
          'd_list' : list(itertools.chain([mt.inf, *product_list[l], mt.inf]))
          }
          out.append(dict)    
  return(out)

def Search_substr(string, substrings):
  res = 0
  for i in range(len(substrings)):
    if search(substrings[i], string):
      res = res+1
    else:
      continue
  return res

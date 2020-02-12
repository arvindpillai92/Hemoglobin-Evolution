import math
import pylab
import numpy as np
from PIL import Image
import random

def tetramer_pop(G1,G2,G3,G4,G5):
    G = 0
    structure = [["a","b","b","a"],["b","b","b","b"],["a","b","b","b"],["b","a","b","b"],["b","b","a","b"],["b","b","b","a"],["a","a","b","b"],["b","b","a","a"],["b","a","a","b"],["b","a","b","a"],["a","b","a","b"]]


    G_list = []
    Gsum =0
    for elt in structure:
      G = 0.0
      if elt[0] == "a" and elt[1] == "b":
         G += G1
      if elt[0] == "b" and elt[1] == "a":
         G += G1
      if elt[2] == "a" and elt[3] == "b":
         G += G1

      
      if elt[0] == "b" and elt[1] == "b":
         G += G2
      if elt[2] == "b" and elt[3] == "a":
         G+= G1
      if elt[2] == "b" and elt[3] == "b": 
        G+=G2
      if elt[2] == "b" and elt[3] == "b": 
        G+=G2
      if elt[2] == "b" and elt[3] == "b": 
        G+=G2
      if elt[2] == "a" and elt[3] == "a": 
        G+=G5
      if elt[0] == "a" and elt[1] == "a": 
        G+=G5
      if elt[1] == "a" and elt[3] == "b": 
        G+=G3
      if elt[0] == "b" and elt[2] == "a": 
        G+=G3
      if elt[1] == "b" and elt[3] == "a": 
        G+=G3
      if elt[0] == "a" and elt[2] == "b": 
        G+=G3
      if elt[1] == "b" and elt[3] == "b": 
        G+=G4
      if elt[0] == "b" and elt[2] == "b": 
        G+=G4
    #  print (G,str(elt))
      G_list.append(G)
      Gsum += G
    fraction = []
    k = 8.31
    t = 293
    esum = 0
    for elt in G_list:
    #    print elt
        esum+=math.exp(-elt/(k*t))
  #  print esum

    for i in range(len(G_list)):
   #   print (i,structure[i],(math.exp((-G_list[i]/(k*t))))/esum)
      fraction.append(math.exp((-G_list[i]/(k*t)))/esum)

 #   return fraction[1],fraction[2]+fraction[3]+fraction[4]+fraction[5]

    print ("Fractions populated")
    if G1>G2:
      print ("A2B2=",(fraction[0]+fraction[8]),"B4=",(fraction[1]),"A1B3=",(fraction[2]+fraction[3]+fraction[4]+fraction[5]),"A2B2_other=",(fraction[9]+fraction[6]+fraction[7]+fraction[10]))
         #    return (fraction[0]+fraction[8])
#    print ("total sum:")
#    print (np.sum(fraction))


im = Image.open("heatmap.png") # Can be many different formats.
pix = im.load()

G1 = 0.0 # ab1
G2 = 0.0 #bb1
G3 = 0.0 #ab2
G4 = 0.0 #bb2
G5 = 0.0 #aa1
G = 0.0

for i in range(0,100):
  tetramer_pop(random.uniform(0,10000),random.uniform(0,10000),random.uniform(0,10000),random.uniform(0,10000),random.uniform(0,10000))
  
  
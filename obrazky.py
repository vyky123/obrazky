#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:49:26 2018

@author: vyk35227
"""

from pylab import imshow, show

data = []

for i in range(64):
    barva = 1
    radek = []
    for j in range(64):
        
            if j % 2 == 0:
                radek.append(1)
                
            else:
                radek.append(0)
                
    data.append(radek)
    
    
imshow(data, interpolation = "none", cmap = "binary")

show()



"""
            ind = radek.index(p)
            radek.remove(radek[ind])
            radek.insert(ind, barva)
            if barva == 1:
                barva = 0
            else:
                barva = 1
            p = p + 1
            
          
"""
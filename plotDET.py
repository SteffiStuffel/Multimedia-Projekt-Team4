# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import matplotlib.backends.backend_tkagg
import sys


fig, ax = plt.subplots()

ytickvalues = [0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.5]
	
plt.xlabel('FPPW')
plt.title('DET')
plt.ylabel('miss rate')
#plt.axis([0.000001, 0.1, 0.01, 0.5])
plt.axis([0.000001, 1, 0.01, 0.75])

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_yticks(ytickvalues)
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

#plt.axis([0, 0.1, 0, 0.5])
#plt.show()
plt.savefig('myfig.png')


#Draw DET of First-SVM
with open("DETdata_first.txt", "r") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

x = 0
while x < len(content):
   print(content[x+1] + " " + content[x+2])
   plt.plot(content[x+2], content[x+1], 'ro')
   x += 3

f.close

#Draw DET of retrained-SVM
with open("DETdata_retrained.txt", "r") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

x = 0
while x < len(content):
    #print(content[x+1] + " " + content[x+2])
    plt.plot(content[x+1], content[x+2], 'bs')
    x += 3



f.close

# evenly sampled time at 200ms intervals
#t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
#plt.plot(t, t, 'r--')
#plt.plot(t, t**2, 'bs')
#plt.plot(t, t**3, 'g^')

#plt.show()

#plt.savefig('myfig.png')
import math
import os
import random
import re
import sys

from pip._vendor.distlib.compat import raw_input

n = int(raw_input().strip())
print(n)
nv = ""
for i in range(6, 20):
    nv  = nv + str(i)+ ", "
print(nv)
value = n % 2 !=0
print(value)
if value:  # Odd
    print("Weird")
else:  # Even
    if n in range(2,5):
        print("Not Weird 1")
    elif n in range(6,21):
        print("Weird 3")
    else:
        print("Not Weird 2")
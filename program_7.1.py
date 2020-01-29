# =============================================================================
# ABE 651 
# 1/29/2020
# Logan Heusinger
# EX 7.1
# Parts all
# create table that checks function with math.sqrt and calculates dif
# a   mysqrt(a)           math.sqrt         diff
#__   _________           _________         ____
#1    1.0000000000      1.0000000000     -0.0000000000 
#2    1.4142135624      1.4142135624     -0.0000000000 
#3    1.7320508100      1.7320508076     -0.0000000024 
#4    2.0000000000      2.0000000000     0.0000000000 
#5    2.2360679779      2.2360679775     -0.0000000004 
#6    2.4494897428      2.4494897428     -0.0000000000 
#7    2.6457513111      2.6457513111     -0.0000000000 
#8    2.8284271247      2.8284271247     -0.0000000000 
#9    3.0000000000      3.0000000000     -0.0000000000 
# ============================================================================
import math

def mysqrt(a):#calculate a square root
    x = a/2
    while True:
        y = ( x + a / x ) / 2
        if abs(y-x) < .0001: #stop once error becomes smaller than this
            x = y
            return y
            break
        x = y
        
def differ(a): #calculate difference between math.sqrt and mysqrt
    d = math.sqrt(a) - mysqrt(a)
    return d 


print(" a   mysqrt(a)           math.sqrt         diff")#table headers
print("__   _________           _________         ____")

while a<10: #values for A in the table
    print("{:.0f}    {:.10f}      {:.10f}     {:.10f} " .format(a,mysqrt(a), math.sqrt(a), differ(a)))
    a = a +1   
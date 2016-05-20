import cmath
import math
from matplotlib.pylab import *
import  matplotlib.pylab as plt

tau = 2 * math.pi

'''
1. vector addition
2. average of vectors
3. logarithmic conversion from complex plane to (real) degrees
'''

def my_average(readings):
  # base = e ** (1j) # one radian turn around the unit circle
  # base = e ** (1j * tau) # one turn around the unit circle
  base = cmath.exp(1j * tau/360) # one degree turn around the unit circle
  total = 0
  for r in readings:
    v = r[1] * base ** r[0] # scaling number in complex plane by the 'speed'
    total += v
    arrow(0,0,v.real, v.imag, head_width=0.05, head_length=0.05, fc='r', ec='r')
  result = total / len(readings)
  arrow(0,0, result.real, result.imag, head_width=0.05, head_length=0.05, fc='b', ec='b')
  xlim([-1.5, 1.5])
  ylim([-1.5, 1.5])
  xlabel('Real')
  ylabel('Imaginary')
  return ( cmath.log(result, base).real, abs(result) ) # tuple, inverse operation of exp

a = [(12,1), (15,1), (13,1), (9,1), (16,1)]
b = [(358,2), (1,2), (359,10), (355,2), (2,2)]
c = [(210,2), (290,2), (10,2), (90,2), (170,2)]

a_avg = my_average(a)
print "List a" + str(a) + " AVG:" + str(a_avg)
plt.show()

b_avg = my_average(b)
print "List b" + str(b) + " AVG:" + str(b_avg)
plt.show()

c_avg = my_average(c)
print "List c" + str(c) + " AVG:" + str(c_avg)
plt.show()

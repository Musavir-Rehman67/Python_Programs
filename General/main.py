# import add
# print(add.addition(2,3))
# from math import add
# print(add.addition)
import sys
sys.path.append('E:/Python/')
from math_mod.sub import Substract
from math_mod.add import Addition
b = Addition(2,3,4)
print(b.addition())
a = Substract(1,2,3)
print(a.substract())
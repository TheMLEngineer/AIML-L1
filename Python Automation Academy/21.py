'''

Math and Random Modules

'''
import random
import math

# a
number = 0.756
print(round(number))

# b
print(math.sqrt(23))




# c 
print(random.uniform(0,1))

# d
print(random.randint(10 , 500))

# e

# Math Module 

print('Math Module : ')
x = 4
y = 5.324

print(math.sqrt(x))
print(math.ceil(x))
print(math.copysign(x, y))
print(math.fabs(x))
print(math.factorial(5))
print(math.floor(x))
print(math.fmod(x, y))
print(math.frexp(x))
print(math.fsum([1,2,3,4,5]))
print(math.isfinite(x))
print(math.isinf(x))
print(math.isnan(x))
print(math.modf(x))
print(math.trunc(x))
print(math.exp(x))
print(math.expm1(x))
print(math.log1p(x))
print(math.log2(x))
print(math.log10(x))
print(math.pow(x, y))
print (math.acos(0.55))
print(math.asin(0.55))
print(math.atan(0.55))
print(math.atan2(0.55, 0.55))
print(math.cos(x))
print(math.hypot(x, y))
print(math.sin(x))
print(math.tan(x))
print(math.degrees(x))
print(math.radians(x))
print(math.acosh(x))
print(math.asinh(x))
print (math.atan(0.39))
print(math.cosh(x))
print(math.sinh(x))
print(math.tanh(x))
print(math.erf(x))
print(math.erfc(x))
print(math.gamma(x))
print(math.lgamma(x))
print(math.pi)
print(math.e)

# Random module

print(random.seed(3))
print(random.getstate())
state = random.getstate()
print(random.setstate(state))
print(random.getrandbits(43))
print(random.randrange(5))
print(random.randrange(3,7))
print(random.randint(3,5))
print(random.choice(list(range(10))))
print(random.shuffle(list(range(10))))
print(random.sample(range(10000000), k=60))
print(random.uniform(3,76))
print(random.triangular(1,3,6))
print(random.betavariate(0.3 , 0.7))
print(random.expovariate(1.5))
print(random.gammavariate(1.5 , 4.5))
print(random.gauss(34, 5))
print(random.lognormvariate(34, 5))
print(random.normalvariate(34,5))
print(random.vonmisesvariate(34,5))
print(random.paretovariate(34))
print(random.weibullvariate(34,5))


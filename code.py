#Daniel Volinsky 313193716
#Arial Ganazya 313532798

import math
# give python eqn of the formula using python math syntax
def f(x):
    return (math.pow(x, 4) + 3 * math.pow(x, 3) - 3 * math.pow(x, 2))


def bisect(func, low, high, tol, N):
    if (f(high) * f(low) > 0): return ("Error, fa and fb fail IVT, no fx at interval")
    count=0
    lastFuncVal = func(low)
    for i in range(0, N):
        mid = (high + low) / 2.0
        if func(mid) == 0 or (high - low) / 2.0 < tol:
            return mid
        # same sigh
        if func(mid) * func(low) > 0:
            low = mid
        # diff sign
        else:
            high = mid
        lastFuncVal = func(mid)

        count+=1
        print(count, " & ", low, " & ", high, " & ", f(low), " & ", f(high))
    return "Method failed after {} iterations".format(N)

def bisectOptimaize(func, low, high, range):
    error =(-1)*((math.log((0.0001) / (high - low), 10)) / (math.log(2, 10)))  #-1*ln(Error/b-a)/ln2


    print("Error founded:" , error)
    temp = low
    while temp <= high:
        if func(temp) * func(temp + range) < 0:
            bisect(func, temp, temp + range, 0.0001, int(error + 1))
        temp = temp + range


# globals
eps = 10 ** -10
A = -1
B = 6
N = 100
# Number of iteration  (K+1)


print("Bisection method soln: x = ", bisect(f, A, B, eps, N))
bisectOptimaize(f,-2,2,0.1)

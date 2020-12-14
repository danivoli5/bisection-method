import math
#Daniel Volinsky 313193716
#Arial Ganazya 313532798


# give python eqn of the formula using python math syntax
def f(x):
    return (math.pow(x, 4) + 3*math.pow(x,3) - 3*math.pow(x,2))



def bisect(func, low, high, tol, N):

    if (fa * fb > 0): return ("Error, fa and fb fail IVT, no fx at interval")

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
        
        print(count, " & ", low, " & ", high, " & ", f(low), " & ", f(high))
    return "Method failed after {} iterations".format(N)


# globals
eps = 10**-10
A = -2
B = 2
N=100
#Number of iteration  (K+1)




print("Bisection method soln: x = ", bisect(f, A, B, eps, N))

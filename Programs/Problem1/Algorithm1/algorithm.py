from math import gcd
from sympy import perfect_power

def solve_equation(n):
    solutions = [(1, 1, 1, 1)]

    for m in range(2, n-1):
        if m % (n-m) == 0:
            power = m//(n-m)
            solutions.append((m, power, m, power+1))

        else:
            hcf = gcd(m, n-m)
            y = (n-m)//hcf
            ret = perfect_power(m, [y])

            if ret:
                power = m//hcf
                solutions.append((ret[0], power, ret[0], power+y))

    if n != 2:
        solutions.append((n-1, n-1, n-1, n))
    
    return solutions

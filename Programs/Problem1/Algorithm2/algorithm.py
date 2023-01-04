from sympy import perfect_power, divisors as get_divisors
from math import log2, gcd

def solve_equation(n):
    solutions = [(1, 1, 1, 1)]

    divisors = get_divisors(n)
    divisors.pop()

    for d in divisors:
        otherd = n//d

        solutions.append((n-d, otherd-1, n-d, otherd))

        for k in range(2, min(int(log2(n)) + 1, otherd)):
            if gcd(otherd, k) == 1:
                power = n - k*d
                ret = perfect_power(power, [k])

                if ret:
                    solutions.append((ret[0], otherd - k, ret[0], otherd))
    
    return solutions

from math import gcd
from sympy import perfect_power

def print_solutions(solutions):
    for a_base, a_exp, b_base, b_exp in solutions:
        print(f"a = {a_base}^{a_exp}, b = {b_base}^{b_exp}")

def solve_equation(n):
    solutions = [(1, 1, 1, 1)]

    for m in range(2, n-1):
        if m % (n-m) == 0:
            x = m//(n-m)
            solutions.append((m, x, m, x+1))

        else:
            hcf = gcd(m, n-m)
            y = (n-m)//hcf
            ret = perfect_power(m, [y])

            if ret:
                x = m//hcf
                z = ret[0]
                solutions.append((z, x, z, x+y))

    if n != 2:
        solutions.append((n-1, n-1, n-1, n))
    
    return solutions


if __name__ == "__main__":
    
    n = int(input())
    solutions = solve_equation(n)
    print_solutions(solutions)

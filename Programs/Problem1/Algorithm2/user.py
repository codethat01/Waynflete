from sympy import perfect_power, divisors as get_divisors
from math import log2, gcd


def print_solutions(solutions):
    for a_base, a_exp, b_base, b_exp in solutions:
        print(f"a = {a_base}^{a_exp}, b = {b_base}^{b_exp}")

        
def solve_equation(n):
    solutions = [(1, 1, 1, 1)]

    if n == 2:
        return solutions

    divisors = get_divisors(n)
    divisors.pop()

    for d in divisors:
        x = n//d

        solutions.append((n-d, x-1, n-d, x))

        for y in range(2, min(int(log2(n)) + 1, x)):
            if gcd(x, y) == 1:
                ret = perfect_power(n - y*d, [y])

                if ret:
                    z = ret[0]
                    solutions.append((z, x - y, z, x))
    
    return solutions



if __name__ == "__main__":
    
    n = int(input())
    solutions = solve_equation(n)
    print_solutions(solutions)

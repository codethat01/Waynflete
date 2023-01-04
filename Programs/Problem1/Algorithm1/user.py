from math import gcd

def print_solutions(solutions):
    for a_base, a_exp, b_base, b_exp in solutions:
        print(f"a = {a_base}^{a_exp}, b = {b_base}^{b_exp}")

def solve_equation(n):
    solutions = [(1, 1, 1, 1)]

    for m in range(2, n-1):
        if m % (n-m) == 0:
            power = m//(n-m)
            solutions.append((m, power, m, power+1))

        else:
            hcf = gcd(m, n-m)
            y = (n-m)//hcf
            base = round(m**(1/y))

            if base**y == m:
                power = m//hcf
                solutions.append((base, power, base, power+y))

    if n != 2:
        solutions.append((n-1, n-1, n-1, n))
    
    return solutions


if __name__ == "__main__":
    
    n = int(input())
    
    solutions = solve_equation(n)
    print_solutions(solutions)

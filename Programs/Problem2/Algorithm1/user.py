from math import comb as binomial_coefficient


def format_term(power, coefficient):
    string = ""
    
    if coefficient != 1 or power == 0:
        string += str(coefficient)

    if power > 0:
        string += 'x'
    if power > 1:
        string += '^' + str(power)

    return string

  
def print_polynomial(polynomial):
    terms = []

    for power, coefficient in enumerate(polynomial):
        if coefficient != 0:
            term = format_term(power, coefficient)
            terms.append(term)

    formatted_string = ' + '.join(terms[::-1])

    print(f"A_{n}(x) = {formatted_string}")

    
def calculate_coefficient(n, k, coefficients):
    total = binomial_coefficient(n, k) * ((-1) ** k)

    for m in range(n):
        intermediate_sum = 0

        for r in range(min(k, m+1)):
            intermediate_sum += coefficients[m][r] * binomial_coefficient(n-m-1, k-r-1) * ((-1) ** (k-r-1))

        total += binomial_coefficient(n, m) * intermediate_sum
    
    return total

  
def generate_coefficients(max_n):
    coefficients = [[1]+[0]*length for length in range(max_n+1)]

    for n in range(1, max_n+1):
        for k in range(1, n):
            coefficients[n][k] = calculate_coefficient(n, k, coefficients)
    
    return coefficients



if __name__ == "__main__":
    
    n = int(input())
    coefficients = generate_coefficients(n)
    print_polynomial(coefficients[n])

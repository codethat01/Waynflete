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

    
def update_coefficient(n, k, coefficients):
    coefficients[k] *= k+1
    coefficients[k] += (n-k) * coefficients[k-1] 
  
  
def generate_coefficients(max_n):
    coefficients = [1]

    for n in range(1, max_n+1):
        coefficients.append(0)
        for k in range(n-1, 0, -1):
            update_coefficient(n, k, coefficients)
    
    return coefficients



if __name__ == "__main__":
    
    n = int(input())
    coefficients = generate_coefficients(n)
    print_polynomial(coefficients)

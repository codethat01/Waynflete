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

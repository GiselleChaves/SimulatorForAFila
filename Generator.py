def linearCongruentGenerator(a,c,m,seed):
    numbers = []
    result = seed
    num_iterations = 1000  
    
    for i in range(num_iterations):
        
        xn = result
        result = ((a * xn + c) % m )
        numbers.append(result)
        
    return numbers


def uniformity(numbers, m):
    standardized_values = []
    
    for i in numbers:
        standardized_values.append(i/m)
    
    return standardized_values



        
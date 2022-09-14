#builds the Pascal's Triangle of given size and returns it's last row
from math import factorial

def binomial_coefficient(n, k): 
    return int((factorial(n)) / ((factorial(k)) * factorial(n - k)))

def pascals_triangle(rows):
    triangle = [] 
    
    for count in range(rows): 
        row = [] 
        for element in range(count + 1): 
            row.append(binomial_coefficient(count, element))
        triangle.append(row)
    return triangle

n = int(input())
print(pascals_triangle(n+1)[n])

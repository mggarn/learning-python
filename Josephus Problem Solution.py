#A little description of the problem is here 
#https://www.geogebra.org/m/ExvvrBbR

#function that translates number in decimal numerical system to binary
def decimal_to_binary(n):
    binary = ''
    while n > 0:
        if n%2 == 0:
            binary += '0'
        else:
            binary += '1'
        n //= 2
    return(int(binary[::-1]))

#function that translates number in binary numerical system to decimal
def binary_to_decimal(n):
    decimal = 0
    binary_str = str(n)
    len_binary_str = len(binary_str)
    
    for i in range(len_binary_str):
        if binary_str[i] == '1':
            decimal += 2**(len_binary_str-i-1)
        
    return decimal

#finds out the solution for josephus problem for k = 2 using translation to binary system
def josephus_winner(n):
    winner = str(decimal_to_binary(n))
    winner = int(winner[1:]+winner[0])
    
    return binary_to_decimal(winner)
    
#finds out the general solution for josephus problem for any given k
n, k = int(input()), int(input())
if k == 2:
    print(josephus_winner(n))
else:
    l = list(range(1,n+1))
    i = k-1
    while len(l) > 1:
        del l[(i)%len(l)]
        i = (i+k-1)%len(l)
        
    print(*l)

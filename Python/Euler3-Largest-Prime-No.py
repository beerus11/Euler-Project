# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

for j in range(0,t):
    n=input()
    print largest_prime_factor(n)
    

from fractions import gcd

def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers)

t=input()
for i in range(0,t):
	print lcm(range(1,input()+1))

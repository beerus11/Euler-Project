# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
def check_prime(no):
    i=2
    while i*i <=no:
        if no%i==0:
            return False
        i=i+1
    return True
primes=[]
i=2
while True:
    if len(primes)==10001:
        break;
    if check_prime(i)==True:
        primes.append(i)
    i=i+1
for i in xrange(0,t):
    print primes[int(raw_input().strip())-1]

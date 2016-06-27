# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
for i in xrange(t):
    no=input()
    print abs((sum(range(no+1))**2)-sum([i**2 for i in range(no+1)]))

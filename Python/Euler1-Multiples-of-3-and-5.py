# Enter your code here. Read input from STDIN. Print output to STDOUT
t= input()
for i in range(0,t):
    no=input()
    n=(no-1)/3
    sum_3=(n*(2*3+3*(n-1))/2)
    n=(no-1)/5
    sum_5=(n*(2*5+5*(n-1))/2)
    n=(no-1)/15
    sum_15=(n*(2*15+15*(n-1))/2)
    print sum_3+sum_5-sum_15

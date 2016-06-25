def fib(max):
    f1, f2 = 0, 1
    while f1 < max:
        yield f1
        f1, f2 = f2, f1 + f2

t=input()
for i in range(0,t):
    print(sum(filter(lambda n: n % 2 == 0, fib(input()))))

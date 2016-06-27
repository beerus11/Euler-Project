# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
left=[]
right=[]
for i in range(0,t):
    string=raw_input()
    left.append(int(string[0:25]))
    right.append(int(string[26:]))
print str(sum(left)+int(str(sum(right))[0]))[0:10]

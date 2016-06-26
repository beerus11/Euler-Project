t=input()
for i in range(0,t):
    no=input()
    for k in range(no-1,101100,-1):
        if str(k)==str(k)[::-1]:
            lst = [k for e in range(100,999) if k%e==0 and len(str(k/e))==3]
            if lst :
                print max(lst)
                break

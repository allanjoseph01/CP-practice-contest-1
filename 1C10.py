n,m=map(int,input().split())
def nextprime(x):
    while True:
        count=0
        L=[]
        for i in range(2,x):
            if(x%i==0):
                count+=1
                break
        if count==0:
            return x
        x+=1
b=nextprime(n+1)
if b==m:
    print("YES")
else:
    print("NO")

n=int(input())
count=0
def AlmostPrime(x):
    countp=0
    for j in range(2,x):
        if(x%j==0):
            b=IsPrime(j)
            if(b=="True"):
                countp+=1
    return countp
def IsPrime(y):
    countq=0
    for k in range(2,y):
        if(y%k==0):
            countq+=1
    if(countq==0):
        return "True"
    else:
        return "False"
for i in range(2,n+1):
    a=AlmostPrime(i)
    if(a==2):
        count+=1
print(count)          

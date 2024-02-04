n=int(input())
x=n+1
while True:
    L= [int(y) for y in str(x)]
    if(L[0]!=L[1] and L[0]!=L[2] and L[0]!=L[3] and L[1]!=L[2] and L[1]!=L[3] and L[2]!=L[3]):
        print(x)
        break
    else:
        x+=1


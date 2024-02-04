n=int(input())
for i in range(1,n+1):
    i1,i2,i3=map(int, input().split()) 
sum1=0
sum2=0
sum3=0
for i in range(1,n+1):
    sum1+=i1
    sum2+=i2
    sum3+=i3
if(sum1==0 and sum2==0 and sum3==0):
    print("Yes")
else:
    print("No")
print(sum1)

n=int(input())
def func(n):
    while n%2==0:
        n//=2
    return n>1
for i in range(n):
    x=int(input())
    if func(x):
        print("YES")
    else:
        print("NO")
        

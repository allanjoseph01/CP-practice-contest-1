n=int(input())
for i in range(n):
    count=0
    x=int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    for j in range(0,x):
        for k in range(0,x):
            if (lst[j] * lst[k] == (j+1) + (k+1)) and i<j:
                count+=1
    print(count)

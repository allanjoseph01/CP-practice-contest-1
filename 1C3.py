n,t=map(int,input().split())
q=input()
l= [x for x in q]
if(n==1):
    print(q)
else:
    for i in range(0,t):
        j=0
        str=""
        while(j<n-1):
            if(l[j]=='B' and l[j+1]=='G'):
                str+=l[j+1]
                str+=l[j]
                j+=2
            else:
                str+=l[j]
                j+=1
        if(len(q)!= len(str)):
            if((l[-2]=='G' or l[-2]=='B') and (l[-1]=='G' or l[-1]=='B')):
                str+=l[-1]
        l= [x for x in str]  
    print(str)      

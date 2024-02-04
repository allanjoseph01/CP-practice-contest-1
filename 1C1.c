#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int sum1=0,sum2=0,sum3=0;
    for(int i=1;i<=n;i++){
    	int i1,i2,i3;
        scanf("%d %d %d",&i1,&i2,&i3);
        sum1+=i1;
        sum2+=i2;
        sum3+=i3;
    }
    if(sum1==0 && sum2==0 && sum3==0){
        printf("Yes");
    }else{
        printf("No");
    }
    return 0;
}
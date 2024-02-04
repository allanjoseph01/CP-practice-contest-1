#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int x=n+1;
    while(1){
        int i=4;
        int a1,a2,a3,a4;
        int temp=x;
        for(int j = 0; j < 4; j++){
            int ai=temp%10;
            temp/=10;
            i--;
        }
        if(a1!=a2 && a1!=a3 && a1!=a4 && a2!=a3 && a2!=a4 && a3!=a4){
            printf("%d",x);
            break;
        }
        else{
            x++;
        }
    }
    return 0;
}
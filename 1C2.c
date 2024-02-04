#include<stdio.h>
#include<string.h>
int main(){
	int i=0;
    char a[200],b[200]={'\0'};
    gets(a);
    while(a[i]!='\0'){
    	if(a[i]=='.'){
    		char s1[2]={'0','\0'};
    		strcat(b,s1);
    		i++;
		}
		else if(a[i+1]=='.'){
			char s2[2]={'1','\0'};
			strcat(b,s2);
			i=i+2;
		}
		else{
			char s3[2]={'2','\0'};
			strcat(b,s3);
			i=i+2;
		}
	}
    puts(b);
    return 0;
}
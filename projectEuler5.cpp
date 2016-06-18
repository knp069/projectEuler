#include<iostream>
#include<stdio.h>
using namespace std;
int lcm(int n1,int n2);
int main(){

	int testcases,number,k,lc;
	cin>>testcases;
	while(testcases--){
		cin>>number;
		lc = 1;
		k=2;
		while(k<=number){
			lc=lcm(k,lc);
			k++;
		}
		cout<<lc<<endl;
	}
	return 0;
}

int lcm(int n1,int n2){
	int temp1=n1;
    int temp2=n2;
    while(temp1!=temp2)
    {
        if(temp1>temp2)
            temp1-=temp2;
        else
            temp2-=temp1;
    }
    return (n1*n2)/temp1;
}

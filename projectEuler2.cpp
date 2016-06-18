#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define _size 10000

long long int fibonacci(int n,unsigned long int a,unsigned long int b );

long long int fibonacci(int n,unsigned long int a,unsigned long int b ){
    if(n==0) return a;
    else if (n==1) return b;
    else return fibonacci(n-1,b,a+b);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int testcases;
    unsigned long int N;
    unsigned long int fibbonaci[_size];
    unsigned long int result=0;
    cin>>testcases;
    while(testcases--){
        result=0;
        cin>>N;
        int n=0;
        unsigned long int k;
        while((k = fibonacci(n,1,2))<N){
            fibbonaci[n]= k;
            n++;
        }
        for(int i=0;i<n;i++){
            if(fibbonaci[i]%2==0)
                result=result+fibbonaci[i];
        }

        cout<<result<<endl;
    }
    return 0;
}

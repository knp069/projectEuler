#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int testcases=0;
    int N=0;
    cin>>testcases;
    while(testcases--){
        cin>>N;
        unsigned long int n1=(N-1)/3;
        unsigned long int n2=(N-1)/5;
        unsigned long int n3=(N-1)/15;
        unsigned long int s1=(n1)*(6+(n1-1)*3)/2;
        unsigned long int s2=(n2)*(10+(n2-1)*5)/2;
        unsigned long int s3=(n3)*(30+(n3-1)*15)/2;
        cout<<s1+s2-s3<<endl;
    }
    return 0;
}
__author__ = 'knp069'
import math

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def isPrime(n):
    if prime.__contains__(n):
        return True
    elif n>97:
        divisorindex = 0
        while divisorindex<=len(prime) and prime[divisorindex]<=n**0.5 :
            if n%prime[divisorindex] == 0 :
                return False
            divisorindex=divisorindex+1
        prime.append(n)
        return True


def max(x,y):
    if x>y:
        return x
    return y

testcase = int(input())
i = 0
while i<testcase:
    maxprimediv=1
    n = int(input())
    k = prime[len(prime)-1]+2
    while k<=n:
        isPrime(k);
        k=k+2
    if isPrime(n):
        print(n)
    else:
        div=0
        while div<len(prime) and prime[div]<= n**0.5 :
            if(n%prime[div]==0):
                complimentdiv = int(n/prime[div])
                if(isPrime(complimentdiv)):
                    maxprimediv = complimentdiv
                    break
                else:
                    maxprimediv = prime[div]
            div=div+1
        print(maxprimediv)
    i=i+1
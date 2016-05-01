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

testcase = int(input());
i = 0;
while i<testcase:
    n = int(input())
    if n<=len(prime):
        print(prime[n-1])
    else:
        k = prime[len(prime)-1]+2
        ind = 0;
        while ind<n:
            isPrime(k);
            k=k+2
            ind = len(prime)
        print (prime[n-1])
    i=i+1
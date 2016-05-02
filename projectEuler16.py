def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

testcases = int(input())

i=0

while i<testcases:
    n = int(input())
    k = 2**n
    print(sum_digits(k))
    i=i+1
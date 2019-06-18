def isSpecialNumber(n, p):
    if noofPrimeFactors(n) == p:
        return True
    return False
# Function to check if number is Prime
def isprime(n):
    flag = 1
    if n == 2:
        return True
    for i in range(2,n//2+1):
        if n % i ==0:
            flag = 0
            return False
    if flag == 1:
        return True
#isprime(14)
# function to determine number of prime factors for a given number
def noofPrimeFactors(n):
    if isprime(n):
        return 1
    count = 0
    for i in range(2,n // 2 + 1):
        if isprime(i) and n % i == 0:
            count += 1
    return count
#noofPrimeFactors(30)
#isSpecialNumber(30, 2)
def solution2():
    p =int(input())
    t =int(input())
    for i in range(0,t):
        if isSpecialNumber(n,p):
            print("YES")
        else:
            print("NO")
isSpecialNumber(10, 2)
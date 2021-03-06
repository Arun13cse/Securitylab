import random
import math

def expo(a,k,n):
    b=1
    A=a
    if(k==0):
        return b
    if(k & 1):
        b=a
    for i in range(1,int(math.log(k,2)+1)):
        A = (A*A)%n
        if(k & (2**i)):
            b = (A*b)%n
    return b

def miller_rabin(n,t):
    temp = n-1
    s=0
    if(temp%2==0):
        temp = temp/2
        s+=1
    r = temp
    for i in range(0,t):
        a = random.randint(2,n-2)
        y = expo(a,r,n)
        if (y!=1 and y!=n-1):
            j = 1
            while(j<=s-1 and y == n-1):
                y = (y**2)%n
                if(y==1):
                    return 0
                j+=1

            if(y!=n-1):
                return 0
    return 1

if __name__=="__main__":
    n_min = int(input("Enter the minimum:"))
    n_max = int(input("Enter the maximum:"))
    t =3
    count =0
    print "prime numbers between ",n_min," and ",n_max," are:"
    for n in range(n_min,n_max):
        if(n%2!=0):
            if(miller_rabin(n,t)):
                count+=1
                print n
    print "Total Primes:",count

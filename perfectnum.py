def perfect(sum1,n):
    if (sum1 == n):
        print(n," it is perfect number")
        
for n in range(1,1000):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
            perfect(sum1,n)



quantity=int(input("enter the quantity"))

cost=quantity*100

if cost >1000:
    print("total cost=",cost)
    a=cost * 90/100
    print("you get 10 % discount total cost=",a)

else:
    print("total cost=",cost)

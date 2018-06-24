a=int(input("enter your points"))

if a>0 and a<=50:
    print("sorry! No prize this time")
elif a>50 and a<=150:
    print("congratulations, You won wooden dog")
elif a>150 and a<=180:
    print("congratulations, you won book")

elif a>180 and a<=200:
    print("congratulations, you won chocolates")
else:
    print("enter valid points")

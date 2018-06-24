a=int(input("enter the age of 1st person"))
b=int(input("enter the age of 2nd person"))
c=int(input("enter the age of 3rd person"))

if a>b:
    if a>c:
        print("1st person is oldest")

    else:
        print("3rd person is oldest")

elif b>c:
    print("2 person is oldest")
else:
    print("3 person is oldest")

if a<b:
    if a<c:
        print("1st person is young")

    else:
        print("3rd person is young")

elif b<c:
    print("2 person is young")
else:
    print("3 person is young")

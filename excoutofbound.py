try:
    a=[1,2,3]
    print(a[3])
except LookupError:
    print("index out of range")
else:
    print("success")

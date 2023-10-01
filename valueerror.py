try:
    a=10
    b=int(input())
    c=a/b
    print(c)
except ValueError as e:
    print("error occurred",e)
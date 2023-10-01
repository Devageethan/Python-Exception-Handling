try:
    a=10
    b="hi"
    print(a+b)
except TypeError as e:
    print("type error occured",e)
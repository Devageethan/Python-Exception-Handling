try:
    a=11
    b="hi"
    c=a+b
    print(c)
except ValueError:
    print("literal not be operated")
except Exception:
    print("exception occured by type error")
finally:
    print("finished")
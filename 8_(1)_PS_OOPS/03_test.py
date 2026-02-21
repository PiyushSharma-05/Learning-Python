class demo():
    a=4

o=demo()
print(o.a)    # prints class attr becuase instance attr is not present
o.a=0         # instance attr is set
print(o.a)    # prints instance attr becuase instance attr is  present
print(demo.a) # prints class attr
a=set()  #for a empty set

b={2,5,6,9,"Hello",9,9,"Piyush"}
t=type(b)
print(t)
print(b)
print(len(b))

b.add(566)
print(b)
print(len(b))
b.remove(6)
print(b)

p={2,4,6,8,10}
q={1,2,4,6,3,5,7,9}

print(p)
print(q)
print(p.union(q))
print(p.intersection(q))
print(p.union({10,12}))
print(q.union({10,12}))
print(p.intersection({10,11}))
print(q.intersection({3,11}))
print(q.difference(p))
print(q.pop())
print(q)

print(({2,4}).issubset(p))
print(q.issuperset({0,5}))

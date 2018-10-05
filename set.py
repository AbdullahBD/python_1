tpl = (1, 2, 3, 4, 5)
a = set(tpl)
print(a)

li1= (2, 4, 6, 8,10)
b  =set(li1)
print(b)

k = a & b
l = a | b
m = a ^ b
print(k, l, m)

print( 7 in a)
print( 10 in b)

c = set('abcd')
print(c)

li = [1,1,2,2,4,4,5,5,2,3,7,8,9]
print(set(li))

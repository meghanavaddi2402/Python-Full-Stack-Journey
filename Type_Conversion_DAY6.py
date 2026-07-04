'''
=> TYPE CONVERSION
- This is process of converting one data type to other
- Int -> string, float
    num = 24
    num1 = float(num)
    print(num1)
    print(type(num))
    n = 987606
    n1 = str(n)
    print(n1)
    print(type(n1))
- Float -> string, integer
     num = 24.09
    num1 = float(num)
    print(num1)
    print(type(num))
    n = 987606
    n1 = str(n)
    print(n1)
    print(type(n1))
- String -> Integer, Tuple, Dictionary
    a = "3225064"
    b = int(a)
    print(type(a))
    print(type(b))
    print(b+10)
    c = "90.24"
    d = float(c)
    print(type(c))
    print(type(d))
    print(d+2)
    e = "567809"
    f = list(e)
    print(f)
    print(type(e))
    print(type(f))
- Buit-In Functions
1.str()
2.float()
3.int()
4.list()
5.dict()
'''
a = "3225064"
b = int(a)
print(type(a))
print(type(b))
print(b+10)
c = "90.24"
d = float(c)
print(type(c))
print(type(d))
print(d+2)
e = "567809"
f = list(e)
print(f)

print(type(e))
print(type(f))
g = {'p', 'y', 't', 'h', 'o', 'n'}
i = tuple(g)
print(i)
j  = [('a',1), ('b',2)]
k = dict(j)
print(k)
l = (1, 2 ,3 ,4)
m = list(l)
print(m)

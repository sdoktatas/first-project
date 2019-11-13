def sqr(c):
    return  c ** 2

def plus(a=1, b=2):#default paraméterek
    result = a + b
    #print(result)
    #return  result
    return a + sqr(b)

plus(2,3)
plus(7,3)
plus()#default pareméterrel


print(plus(3,2))
r = plus(1,3)
print("Eredmény " + str(r))


##There are 7 basic operators

# 1.arithmatic operators
#2.comparision(Relational)operators
#3.Assignment operator
#4.Logical Operator
#5.Bitwise operators
#6.Membership Operators
#7.Identity Operators

#Arithmatic operator example

#a=4
#b=2
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a//b)
#print(a%b)
#print(a**b)

#comparision operator example
#a=3
#b=5
#if a==b:
    #print("Both are equal")
#if a!=b:
    #print("Both are not equal")
#if a>b:
    #print("A is bigger number")
#else:
    #print("B is bigger number")
#if a<b:
    #print("A is small number")

#Assignment Operators Exampl
#a=2
#b=10
#c=2
#print('a value is',a)
#print('b value is',b)
#print('c value is',c)
#c+=a
#print('add and value of c is',c)
#c-=a
#print('subtract and value of c is',c)
#c*=a
#print('multiply and value of c is',c)
#c/=a
#print('divide and value of c is',c)
#c**=a
#print('exponents and value of c is',c)

'''logical operators example
x=True
y=True
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)'''

"""Membership Operators example
x="Hello World"
y={1:"a",2:"b"}
print('H'in x)
print("globe" not in x)
print(1 in y)
print("a"in y)"""

"""Identity operators example
x1=5
y1=5
print(x1,type(x1),id(x1))
print(y1,type(y1),id(y1))
print(x1 is not y1)"""



a=15
b=10
print(bin(a))
print(bin(b))
print(bin(a|b))
print(bin(a<<b))

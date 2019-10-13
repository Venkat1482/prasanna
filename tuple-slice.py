tup1=('python','linux',1997,2000,2004,70.25)
tup2=(1,2,3,4,5,6,7,8,)
tup3=tup1+tup2
print(tup3)
print(tuple(enumerate(tup1)))
print('tup1[-3]: ',tup1[-3])
print(tuple(enumerate(tup2)))
print('tup2[1:5]: ',tup2[1:5])
print(tup3[-9])
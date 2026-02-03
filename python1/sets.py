"""
un-order collection  
mutable  
i am mutablea and but not add duplicate eliment
cant's contain mutrable data types  
"""
a = {1,2,3,(1,2)}

s = set()
print(s)
print(type(s))
s = {1,2,3,4}
s = {1,2,3,4 ,True ,"hello"}
print(s)
# duplicate dala to cut jayega
# mutable data to error ayega
s = {1,1,12,3}
print(s)


s = {1,2,3}
s1 = {3,1,2}
print(s == s1)
print(id(s))
print(id(s1))

t = (1,2,3)
t1 = (1,2,3)
print(id(t) ,id(t1))

# canot  indexing and slicing beacuse this is unorders
# not add elomet like  this  t[o] = 112 but niche dekho  
# singal item add  
t = {1,2,3}
t.add(11)
# t.add(1111)
# t.add(111)
print(t)
# multipal add elimengt

t.update([1,2,3,4])
print(t)


# deliet eliment 
del t

# del t[0] # not allow

t = {1,2,3}
t.discard(11) # not through error

t.remove(2) # show error not element aviu 

t = {1,2,3,4,7,8,9}
t.pop() # random item del 
print(t)

t.clear()  # clear all set 
print(t)






tupall = tuple()
print(type(tupall))

s = set()
print(type(s))
l = list()
print(type(l))
d= dict()
print(type(d))


d = ("mahesh" ,"harry")
print(type(d))







s = {1,2,3}
s1 = {4,5,6,1}
print(s|s1) # combine
print(s,s1 .union()) #combine gropu
print(s&s1)  # intersection

print(s-s1) #s ke item s1 mai nahi hai 
print(s ^ s1) # all diffrent elements
print(1 in s) 

for  i in s :
    print(i)
"""
min 
max
len
sorted # always list
"""    
# union/update

print(s.union(s1)) # same as s|s1

s.update(s1)
print(s)
print(s1)

# diffrence and diffrense_update



# symetric dirence and  symetric_diffrense_uodate


#id disjoint/issubset/issuperset


# copy 

# frozen set 

""" immutabel """
fs =frozenset([1,2,3])
print(fs)
# set comperhension 

# tup and list sam but tup is imutable and list mutable
''' order ,unchange , allow duplicate  '''

t = ()
t = (1)
print(type(t)) # show int singal item is int ij n tuple

t = (2,)  # abb int nahi aayega  

t = (1,2,3,(4,5,6))
print(t)

# l = list("mahesh")
# print(l)

t = tuple("mahesh")
print(t)

# homoginius and htrogenius also appliocabile in  tup 

t = (1,2,3,(4,5))
print(t[1])
print(t[0:-1])
print(t[::-1])

# accessing but not change it 
 
# t = list(t)
# print(type(t))
del t # work this 
# del t[-1] # not work error show  


t = (1,2,3)
t2 = (2,2,2)
print(t+t2)
print(t*23)
print(1 in t)

for i in t :
    print(i)
    
# function in tup  

print(len(t))    
print(min(t))    
print(sorted(t))    
print(max(t))    


print(t.count(1))
print(t.index(1))  # means  pasing valuse this val  which location avi  


"""
tupal  imutable list  mutable  
tupala  are fast and list are slow  
memory usee less tup  and  more memory in list 
"""
import sys 
l = list(range(1000))
t = tuple(range(1000))
print(sys.getsizeof(l))
print(sys.getsizeof(t))

a,b,c = (1,2,3)
print(type(a))
print(b)
print(c)


a,b ,*others = (1,2,3)
print(a)
print(b)
print(type(others))


a = (1,2,3)
b = (2,22,2)

z = tuple(zip(a,b)) # mathe opration ka nahi hotay  

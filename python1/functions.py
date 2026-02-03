# tyep of argument 
"""
default argumets 
positonal argumets
keyword arguments """


# *args  and **kwargs

def mahesh(*args) :
    """hello """
    p = 1
    for i in args :
       p = p * i
    return p   
x = mahesh(1,2,3,4,5)        
print(x)

print(mahesh.__doc__)







def data(**kwarg) :
    """hello"""
    for (key ,value) in kwarg.items() :
        print(key ,":", value)
data(name ="mahesh" , age = 21)      
print(data.__doc__)  # documentaion 

import sys

print(data.__sizeof__()) # size of this fuc




# global and local variable  



# nested  function  






# def f() :
#     def g() :
#         print("hello mahesh")
#         f()
#     g()    
#     print("hello bhai")
# f()    
    

def sq(a) : 
    return a*a 
x = sq(3)
print(x)      





def f() :
    def g(a,b) :
        return a+b 
    return g
val = f()(1,2)
print(val)




def a() :
    print("hello")
def b(x) :
    print("inside") 
    return x()
print(b(a))

'''
code modularity
code reusability
code reusability
'''       


# lambda function  

a = lambda x ,y : x+y  
print(a(1,2))

'''
return 1 line  
1 time use  '''




# higher order function 


def sq(x) :
    return x**2

def  trans(f ,l) :
    out = []
    for i in l :
        out.append(f(i))
    
    print(out)
l = [1,2,3,4]
trans(sq , l) 
       
"""
map
filter
reduce
""" 



# map 
l = [1,2,3]

x =list(map(lambda x:x**2 ,l))
print(x)     



class hel:
    def n () : 
        print("hello")
a = hel 
a.n()       
print(type(l))
print(type(a))




class show: 
    def __init__(self,name):
        self.name = name

p = show("mahesh")        
p1 = show("harry")        
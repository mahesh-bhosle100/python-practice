# can contain  any kind of objecgt in python 
n = 1
print(id(n))
l1 = [1,2,3]

print(id(l1))
print(id(l1[0]) ,id(n))
print(id(l1[1]))
# list are slow compare to array 
# list are dynamic and mutable and order 
# list are dynamic means  onging add list and remove
# lsit lexibal  
# list are hetroginiou means  multipal data type store 
# list are more memory use compare to array

# list are order [1,2,3] [3,2,1] means 1 and 2 item same but order not same that l1 = l2 not same and not oredre samjne ki koshish karov  
# item can duplicate item in list 
# list are nested  
#  item can acces and changable  

l2 = list()
print(l2)
print([])
# 1 d list 
l3 = [1,2,3]
#  2d list 
l4 = [[1,2,3],[4,5,6]]
print(l4)

# 3d list 
l5 = [[[1,2],[3,4]],[[5,6]]]
print(l5)

# 
l6 = [1,"10" ,True ]
l7 = list("mahes")
print(l7)

#  indexing in python and slicing   
n= [1,2,3,4,5]
n2 = [1,2,3,[4,5,6,7]]

print(n2[3][1])
print(n[:])



# method in list  


a = [1,2,3,4]
a.append(00)
a.append([ 100,11111,2222,3333]) # sath mai add hota hai 
a.extend([12,12,12]) # tod todke addd hota hai
a.insert(0 , 888888) # index and values
a[0] = 9
a[0:2] = [12,2,3] # also 12,2,3 but not pass singal item like 1 or 2 or  3 slicing then pass 3  that set
print(a)


# delet list  ilhe [del a]

del a[-1]
del a[1:3]
print(a)

# remove  value ke hisab se delit

a.remove(12)
print(a)
a.pop()
print(a)


# clear

a.clear()
print(a)



# oprator 

a = [1,2,3]
b = [4,5,6]
print(a+b)
print(a*4)
print(a,"-",b)



# membarship  oprator  

print( 1 not in a)




l = [1,2,3,[1,1] ,"mahesh"]
for i in l :
    print(i ,end="")
print()  
l2 = [1,2,3,[3,4,5]]
for i in  l2 :
    print(i)

# function list  

# this is not permenant
l1  = [ 0 ,1,2,34 ,0 ,0]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1 ,)) #reverse=True
print(l1.count(0))
print(l1.index(0))


# this is permanant  

print(l1.reverse())
print(l1)
l1.sort()
print(l1)

l2 = l1.copy()
l2.append("heyyyyyyyyy")
print(l1)
print(l2)
print(id(l1))
print(id(l2))

# list comperhension 

n = [i for i in range(10)]
print(n)


v  =[1,2,3]
x = 4
x1 = []
for i in v :
    x1.append(i*x)
print(x1)    
z = []
for i in v :
    z.append(i*i)  
print(z)      
    
    
z1 = [i*i for i in v]    
z2 = [i**2 for i in v]    
print(z1)
print(z2)
lang = ["python" ,"sql" ,"java" , "php"]

la = [i for i in lang if i.startswith("p")]
print(la)
basket = ["mago" ,"banana" , "orange"]
my_fruit = ["mango" ,"banana" ,"pineapple"]

l3 = [frt for frt in my_fruit if frt in basket  if frt.startswith("b") ]
print(l3)

x = [[i*j for i in range(1,4)] for j in range(1,4)]
print(x)


l1 = [1,2,3,4]
l2 = [6,7,8,9]


for i in l1 :
    print(i ,end="")
    
    
print()
for i in l1 :
    for j in l2 :
        print(i* j ,end="")
    print()    
    
   
   

x = [[i*j  for i in l2] for j in l1 ]
print(x)

# traverse list 
# item wise 

for i in l1 :
    print(i) # print item
# index wise 
l1 = [1,2,3,0,4]
for i in range(0,len(l1)) :
    print(i) # print index
    

print(list(zip(l1,l2)))    


l1 = [1,2,3,4]
l2 = [6,7,8,9]

x = [i+j for i,j in zip(l1,l2)]
print(x)
# disavantae python  / slow /risky / more memory

a = [1,2,3]
b= a 
b.append(111)
print(a)
print(b) # chnage both a and b  thats why risky


c = a.copy()
c.append(1000000)
print(c)
print(a)
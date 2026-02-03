d = {}
print(d)

d = {
    "name": "mahesh" ,
    "age" :23 ,
    "marks" : [12,34,67]
    
}

d1 = {
    "name": "mahesh" ,
    "collage" : "zp" ,
    "sub" : {
        "python" :23 ,
        "sql" : {
            "a" :1,
            "b" :2
        }
    }
}
print(d1)

d1 =dict([(1,1) ,(2,2)])
print(d1)

d2 = {"name" : "mahesh" , "name" :12}
print(d2)

# mutable   and unorder 
# key not allow mutable data type  


print(d2["name"])
print(d2.get("name"))
d2["gender"] = "male"

d2["name"] = "hello"
print(d2)
# d2.pop(0)
print(d2)
d2.popitem()
print(d2)



name = {
    "name" :"mahesh" ,
    "age" : 23
}

del name["name"]
print(name)


name.clear()
print(name)


s = {
    "name" :"mahesh" ,
    "sunject" : {"sql" :1 ,
                 "p":2}
}
print(s["sunject"]["p"])
s["sunject"]["p"] = 2111111
print(s)



# delate key 

del s["sunject"]["p"]
print(s)


# oprator  membarship and iteraion 
# khojna 


d ={
    "nmae" : "mahesh" ,
    "age" :23 ,
    "gender" : "male"
}


for  i  in d :
    print(i ,d[i])
    
    
for i ,v in d.items() :
    print(i ,v)    
    
print(len(d))
print(sorted(d))
 
"""
kesys ,
items() ,
values
update
"""



# dictionary 


x = {i : i**2 for i in range(1,11)}
print(x)

days = ["sunday" ,"monday" ,"tuesday"]
temp = [1,2,3]

x = {i:j for (i,j) in zip(days ,temp)}
print(x)


pr = {"phone" :10 , "laptop":9}

x = {key:value for (key ,value) in pr.items() if value > 9}
print(x)
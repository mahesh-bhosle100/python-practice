name = "mahesh"
name = """mahesh"""
name = 'mahesh'
# sring are immutable
# python not allow to manupulate originale string but allow copy it strig and manupulate it not chage original str


#  indexing strin  accesing string elememnt [not change original str]

l1 = "python"
print(l1[1])
print(l1[-1])
print(l1[5])

# indexing accesing ellimnet start 1 st is zero  



# slicing  

""" including 1 sta num but  exicidesd last num [start :  stop : step]"""
l1 = 'java'

print(l1[:])
print(l1[0:-1])


print(l1[::-1])

# allow -ve indexing  


# del string   refrance(samja jana bhai class object )


del  l1


# opration in string   / concatination 

print("mahesh"+" "+"bhosle")
print("mahesh","bhosle")
print("mahesh" * 5)

hello = "z" >  "b"
print(hello)   #  start  

# lexiograpy compare   a is chota and z is bada   and also A is chota and a  is bada    


print("mahesh" and "bhosle")
# "any contail"  is trues  that why afirst checck mahesh  this trues but bhosle is trues also  true thats whys 2 nd iis true   \


print("mahesh"or "bhosle")
# becasue or is any 1 is trues then exicute it   



for  i in "mahesh" :
    print(i)
name = "mahesh"

print("m" not in name)    
print("m" in name)    

# function  in str 


name = "maheshzZ" 
print(len(name))

print(max(name))
print(min(name))
print(sorted(name)) # capital letter is samml and smalla letter is big 


print(name.capitalize())
print(name)
print(name.title())
print(name.swapcase()) #  lower ko capital and capital  ko lower 


n = "pythooonn"
print(n.count("o"))

print(n.find("a")) # nahi mila to -1 and
print(n.index("p")) # nahi mila to  error dega  


# startwith and endwith 

one = "hellomahesh"

print(one.startswith("h"))
print(one.endswith("h"))



name = "mahesh"
age = 23

print("my name  is  {} and my age is {}".format(name ,age)) # also pas  index  in bracket 


# isalnum / isalpha /isdigit / isidentifier





name = "mahesh bhosle"
print(name.split( ))
hey = "hello"
print("-".join(hey))


print(hey.replace("h" ,"k"))



l1 = "mahesh "
print(len(l1))
l2 = l1.strip()
print(len(l2))
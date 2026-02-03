

# while loop  

i = 1 
while i <= 10 :
    print(i)
    i +=  1
    
    
i = 1 
while i < 10 :
    if i == 2 :
        break
    print(i)  
    i += 1  


i = 1 
while i < 10 :
    if i == 2 :
        i+= 1
        continue
    print(i) 
    i += 1    
    
    
    
    
    
    
# for loops  

for i in range(1,11)  :
    print(i)   
    
for  i in range (1,10) :
    if i == 4 :
        break
    print(i)    
for i in range(11) :
    if i  ==  4 :
        continue
    print(i)    

for i in range(10) :
    pass



# nested loops  

for i in range (5) :
    for j in range(5) :
        print(i *j ,end= "")
    print()




    
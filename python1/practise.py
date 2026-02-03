s = "mahesh     "

count = 0
for i in s :
    print(i)
    count += 1
print(count)  


name = "hello@mahesh"

name1 = name.index("@")
print(name[:name1])




hello = "mimah@esh@@@@@@@@@@@@@@@@@@@"
term = "@"
count = 0
for i in hello :
    if i == term :
        count += 1
        
print(count)        


hello = "mimah@esh@@@@@@@@@@@@@@@@@@@"
rm = "@"
s = ""
for i in hello :
    if i != rm :
        s+= i
print(s)        





name = "absassaaasvsvfdsba"

flag = True

for i in range(0 ,len(name)//2) :
    if name[i] != name[len(name) - i - 1] :
        flag =False
        print("not palindrome")
        break
if flag :
    print("pallindrome")    
    

name = "hello mahesh" 
temp = ""
l = []
for i in name    :
    
    if i != " " :
        temp += i
    else :
           l.append(temp) 
           temp = ""
l.append(temp)           
print(l)           

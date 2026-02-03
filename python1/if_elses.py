# use compaison oprator

age = int(input("enter a age"))
if age  >= 18 :
    print("can vote")
else :
    print("can  not  vote")

# 3 this is connditon statements that set          



# makse i program   

email = input("enter a gmail")
password = input("enter a passwors")

if email == "mahesh@gmail.com" and password == "1234" :
    print("login")
elif email == "mahesh@gmail.com" and password != "1234" :
    print("password is wrong")
    password = input ("enter a apssword")
    if password ==   "1234" :
        print("login")
    else :
        print("agin wrong paasword")
elif email != "mahesh@gmail.com" and password == "1234" :
    print("emial wrong")
    email = input ("enter a email") 
    if email == "mahesh@gmail.com"  :
        print("login")
    else :
        print("agin email wrong")
else : 
    print("wrong credintial")                     







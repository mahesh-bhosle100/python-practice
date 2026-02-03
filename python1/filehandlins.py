


# f =  open("sampal.txt" ,"w") 
# f.write("hello mahesh")
# f.close() # close ke badd work nahi  karta  



# f = open("sampal.txt" ,"w") 
# f.write("mahesh")
# f.write("\nhello")
# f.close()

# # exiting file pw write kiya to pehla data  delete hoke naya data aata hai  

# f = open("sampal.txt" , "a")
# f.write("\nsalman bhai")
# f.close()
# # "a" se data last me jake appned hota hai  

# # dure path pe file save karna uska path and  and konsi file mai likhna ye dena  
# f = open(r"C:\Users\Admin\Desktop\python1\temp\sampal.txt" ,"a") 
# f.writelines(["hello bhai&\n" ,"sajcakjvbashca\n" ,"asacfacas\n"])
# f.close() 




# f = open("sampal.txt" ,"r")
# s = f.read()
# print(s)
# f.close()



# f = open("mahesh.txt" ,"r")
# s = f.readline()  # readline by line 
# print(s ,end="")


# f = open("mahesh.txt" ,"r")

# while True :
#     data = f.readline()
    
#     if data == "":
#         break
#     else :
#         print(data ,end="")

# """
# read read  all
# readline read line  by  line
# """

# # with  file  




# # with se file close nahi karna padta auto close hota hai  
# with open("samla.txt" ,"w") as f :
#     f.write("sallu bhai")


# with open("samla.txt" ,"r") as f :
#     print(f.read())
    
    
    
# with open("samla.txt" ,"r") as f :
#     print(f.read(10))    
#     print(f.read(10))    
    
    
    

# l = ["hello" for  i in range(10)]
# with open("yes.txt" ,"w") as f :
#     f.writelines(l)
    
# with open("yes.txt" ,"r") as f:
    
#     chunk = 10
    
#     while len(f.read(chunk)) > 0 :
#         print(f.read(chunk) , end= "***")  
#         # f.read(chunk)  

# with open ("mahesh.txt" , "r") as f :
#             print(f.read(10))
#             print(f.tell()) # abb kaha khade ho ye bolta hai  
#             f.seek(0) # kisi bhi charater pe jana  ye seek se 
#             print(f.read(9))
#             print(f.tell())




with open("mahesh.txt" , "w")as f:
    f.write("hello")
    f.seek(0) # o pe jake replace karna  
    
    f.write("ooooo")
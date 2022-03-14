import json
user=input("singup or login:")
name=input("enter yuor name:")
if user=="singup":
    password=input("enter the password:")
    re_password=input("enter the password:")
    dob=input("enter dob:")
    gender=input("your gender:f/m")
    if gender=="f":
        print("female")
    elif gender=="m":
        print("male")    
    else:
        print("not found")    
    print("your ac has been created:")
    data={"user":user, "name":name,"password":password,"re_password":re_password,"dob":dob,"gender":gender}
    with open (name+".json","w")as f:
        b=json.dump(data,f,indent=2)
else:
    print("login") 
    a=open(name+".json","r")  
    b=a.read()
    c=json.loads(b)
    if name==c["name"]:
        password=input("enter your password:")
        if password==c["password"]:
            print("login successfull:")
        else:
            print("password is wrong:")
    else:
        print("your name is wrong:")  





 

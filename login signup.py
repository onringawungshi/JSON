import json
user=input("enter A for login or B for signup:")
if user=="A":
    n=input("enter username:")
    u1=input("enter password:")
    u2=input("confirm password:")
    if u1==u2:
        l, u, p, d = 0, 0, 0, 0
        if (len(u1) >= 8): 
            for i in u1:  
                if (i.islower()): 
                    l+=1 
                if (i.isupper()): 
                    u+=1			 
                if (i.isdigit()): 
                    d+=1		
                if(i=="@"or i=="$" or i=="_" or i=="#" or i=="%" or i=="^" or i=="&" or i=="*"): 
                    p+=1		
        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(u1)): 
            # print("Valid Password")
            pass
        else: 
            print("Invalid Password")
        d,e,s={},{},[]
        d["user"]={}
        s.append(d["user"])
        d["user"]["Username"]=n
        d["user"]["Password"]=u1
        print("please enter your details")
        user1=input("Enter your Bio=") 
        user2=input("Enter Gender=")
        user3=input("Enter your date of birth=") 
        d["user"]["Profile"]={}
        d["user"]["Profile"]["Bio"]=user1
        d["user"]["Profile"]["Gender"]=user2
        d["user"]["Profile"]["DOB"]=user3
        e["user"]=s
        with open("login signup.json","a") as f:
            my=json.dump(e,f,indent=1)
            print(my)
            print("Congrats!",n,"You have sign up successfully!")
    else:
        print("password are not same")
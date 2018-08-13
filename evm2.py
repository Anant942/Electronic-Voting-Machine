def viewvoterlist():
        b=int(input("candidate number                       political party\n1)                          BJP\n2)                         BSP\n3)                         Congress\n4)                         other"))
        if(b==1):
            f=open("bjp","r")
            data=f.read()
            f.close()
            print("---------------------------------------Voter list of BJP-------------------------------------")
            print(data)
        elif(b==2):
            f=open("bsp","r")
            data=f.read()
            f.close()
            print("---------------------------------------Voter list of BSP-------------------------------------")
            print(data)
        elif(b==3):
            f=open("congres","r")
            data=f.read()
            f.close()
            print("---------------------------------------Voter list of CONGRESS------------------------------")
            print(data)
        elif(b==4):
            f=open("other party","r")
            data=f.read()
            f.close()
            print("---------------------------------------Voter list of OTHER PARTY-----------------------------")
            print(data)      
def addparty():
    print(" \n\n                                Welcome to portal of ADD PARTY                                            \n\n  ")
    
    l1= ["BJP","BSP","CONGRESS","OTHER"]

    l1.insert(4,input("enter name"))
    
    print("final list of party is :",l1)
          
def admin():
    ad=int(input("\n1)View Voter List\n2)Add party\n3)Go back\n4)exit\n5)Change password\n"))
    if(ad==1):
        viewvoterlist()
    elif(ad==2):
        addparty()
    elif(ad==3):
        voter()
    elif(ad==4):
        exit()
    else:
        resetpass()
def congress():
    co=open("congres","a")
    co.write(" \n")
    co.write(input( "   Enter your name    \n"))
    co.close()
def other():
    ot=open("other party","a")
    ot.write(" \n")
    ot.write(input( "   Enter your name    \n"))
    ot.close()
def baspa():
    bs=open("bsp","a")
    bs.write(" \n")
    bs.write(input( "   Enter your name    \n"))
    bs.close()
def bhajpa():
    bj=open("bjp","a")
    bj.write(" \n")
    bj.write(input( "   Enter your name    \n"))
    bj.close()
def voter():
    print("|                                                            WELCOME HERE                                             |")
    g=int(input("\n\n1)Vote now\n2)Don't have voter id, generate now!\n3)Admin\n4)About us\n5)exit\n\n                 select any one"))
    if (g==1):
            voting()
    elif (g==2):
            reg()
    elif(g==3):
            adminpass()
    elif(g==4):
            aboutus()
    else:
           quit()
def resetpass():
    print("|                                                   RESET PASSWORD                                                |")
    p=open("password","w")
    p.write(input("Enter your new password"))
    p.close()
    print("Password change successfully")
    first()
def adminpass():
    print("|                                           |WELCOME ADMIN                                                    |")
    p=open("password","r")
    buffer=p.read()
    if (input("Enter Password")) == buffer:
        p.close()
        print("--------------------------Successful------------------------------")
        admin()
    else:
        e=int(input("\n\n################WRONG PASSWORD#####################\n\n1)Exit\n2)Voter \n3)Forgot password\n4)Try again             !!!!!!select any one!!!!!!"))
        if (e==1):
            quit()
        elif (e==2):
            voting()
        elif(e==3):
            resetpass()
        else:
            adminpass()
def reg():
    from random import randint
    rand=str(randint(1000,5000))
    print("|                                            |Register Now|                                 |")
    name=input("enter your name")
    print("Thank u for Registering: ",name)
    print(" Note down your id : =",rand)
    f=open("evm","a")
    f.write (rand+"\n")
    f.close()
    v=int(input("you are done\n                          To move further click 0"))
    if v==0:
        voter()
def lis():
    l1=["bjp","bsp","conngress","others"]
    for i in range(len(l1)):
        print (l1[i])
def vote():
    print("                                              VOTE YOUR BEST CANDIDATE                                       \n\n ")
    
    b=int(input("candidate number           political party\n1)                          BJP\n2)                         BSP\n3)          Congress\n4)                 others"))
    5
    if(b==1):
        bhajpa()
    elif(b==2):
        baspa()
    elif(b==3):
        congress()
    else:
        other()
    zz=int(input("voted successfully\n                  1)exit\n                      2)Next vote"))
    if(zz==1):
         exit()
    else:
         voter()
def voting():
       f=open("evm","r")
       buffer = f.read()
       if (input("enter your voter id number")) in buffer:
           print("\n\nYes you are a true Voter\n***************VOTE NOW***************")
           f.close()
           
           vote()
         
       else:
           print ("\n\nCannot vote:(\n \n1)You are not registered\n2)You are under 18\n3)You already voted")
           z=int(input("                                                   Try Again !!!!!!!! - press 0 \n\nfor exit press1\n\npress 2 for registration"))
           if(z==0):
                voting()
           elif(z==1):
                exit()
           else:
                reg()
          
         
        
print("\n\n +++++++++___________Electronic  Voting Machine_______________+++++++++++\n\n")

def first():
    d=int(input("1)Admin\n2)Voter"))
    if d==1:
        adminpass()
    elif(d==2):
        voter()


first()




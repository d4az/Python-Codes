print("\t\t\t####################")
print("\t\t\t#  log in system   #")
print("\t\t\t####################\n\n")

logins = 0

def changeuseer(name):
    print("\n\n\t WELCOME "+name+'\n\n')
    print("\tThanks For Using Our system!\n\n")




x = 0
y ='test'
print("\tEnter login to log in to out system")
print("\tEnter signup to create a new account")
y = input()
y = y.lower()
            
if y == 'login':
    print("\n")
    success = False
    if(not success):
          supplied_username = str(input("Enter Your User Name : "))
          supplied_password = str(input("Enter Your Password  : "))
          print("\n")
          success = False
          file = open('user.txt','r')
          for i in file:
              a,b = i.split(',')
              b = b.strip()
              if (a == supplied_username and b == supplied_password):
                  changeuseer(a)
                  success = True
                  break
                  file.close()
              else:
                  print("Loading...")
    else:
        print("Wrong Password")
                  
else:
    newname = str(input("Enter Your Name : "))
    npsw = str(input("Enter Your Password :"))
    cpsw = str(input("Confarm Your password again : "))

    if npsw != cpsw :
        print("\n\t [!] The Passwords are not equal try again!\n")
    else:
        print("passwords are equal")
    
    file = open('user.txt','a')
    file.write("\n"+newname+","+npsw)
    file.close()



    
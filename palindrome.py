import pickle
import pyfiglet
import os
from time import sleep
create=open('Studata.dat','ab') #  In case file not exist , while opening for 1st time
create.close()

print('==========================')
print("STUDENT MANAGEMENT SYSTEM ")
print('==========================')
print(pyfiglet.figlet_format("S M S"))
def helpuser():
    print('====================================================================================')
    print('   HELPING GUIDE                       + [AUTHOR]+ :(WhiteDevil) +')
    print('====================================================================================')
    print()
    print('[*] To see all records,type: [-all]')
    print("[*] To insert records, type: [-i] ")
    print("[*] To update records, type: [-u] ")    #Help definition 
    print("[*] To delete a record,type: [-d]")
    print("[*] To exit this application ,type: [-e] or [-q] ")
    print('[*] To see the help arguements type [-h] or [--help]')
    print()
    print('====================================================================================')
def insertrecord():
    rec_no=int(input("Enter number of records you want to insert : "))
    studet={}
    for i in range(rec_no):
        studet['Name']=input("Enter name of student here : ").strip() # record insert funcn
        studet["Rno"]=int(input("Enter roll no :"))
        studet['Admn_no']=int(input("Enter admission number :"))
        studet['Class']=input("Enter class :").strip() # To remove trailing and leading spaces
        studet['Section']=input("Enter section :").upper()
        studet['Age']=int(input("Enter age :"))
        studet["Email_id"]=input("Enter Email id of student :").strip()
        studet['Phone_Number']=int(input("Enter phone number :"))
        with open('studata.dat','ab') as fin:
            pickle.dump(studet,fin)
        print("[*] Record added successfully !!")


def delrec():
    delno=int(input("Enter Admission Number of student :")) #ADMN NO 
    temp=[]
    try:
        fi=open("Studata.dat",'rb+')
        while True:
            a=pickle.load(fi)
                
            if a['Admn_no']==delno:
                    print("Admission number found \n Deleting the record ...")
                    
                    
                
            else:
                    temp.append(a) # Appending all records in a list
    
       
    except:
        fi.close()
        fo=open('Studata.dat','wb')
        for i in temp:
           pickle.dump(i,fo)  #Dumping all the records except deleted one 
        print(f"Deleted successfully record with Admission no {delno}")    
        
    
 
def seeall():# Function that prints all the records
    file_size=os.path.getsize("Studata.dat")
    if file_size==0 :
        print("No records added yet ! ")
    else:
          ct=1 # Counter variable for record no
          try:
              fi=open('studata.dat','rb') 
              while True:     #printing all records
                  print('================================')
                  a=pickle.load(fi)
                  print("Record no :",ct)
                  print("Name :",a['Name'])
                  print("Admn no:",a['Admn_no'])
                  print("Class :",a['Class'])
                  print("Section :",a['Section'])
                  print("Age :",a['Age'])
                  print("Email Id :",a['Email_id'])
                  print("Phone Number :",a['Phone_Number'])
                  ct+=1
                  print('================================')

                  print()   
          except EOFError:
                fi.close()

def update():
    admnno=int(input("Enter Admission no : "))
    fo=open('studata.dat','rb+')
    try:
        while True:
            p=pickle.load(fo)
            if p['Admn_no']==admnno:
                print("[!] Enter the new updated information [!]")
                print()
                print('[1] Name')
                print('[2] Admn no')
                print('[3] Class ')
                print('[4] Section')
                print('[5] Age')
                print('[6] Email')
                print('[7] Phone Number')
                print('[8] Update all fields..')
                print()

                print("Enter the choice number")
                print()
                choice=int(input("What you want to update : "))

                if choice==1:
                    Name=input("Enter the updated name :").strip()
                    p['Name']=Name

                elif choice==2:
                    Admnno=int(input("Enter the updated Admission no : "))
                    p['Admn_no']=Admnno

                elif choice==3:
                    Class=input("Enter the updated class :").upper()
                    Class=Class.strip() 
                    p['Class']=Class          #Class is string type

                elif choice==4:
                    Section=input("Enter the updated section :").upper()
                    p['Section']=Section

                elif choice==5:
                    Age=int(input("Enter the updated age :"))
                    p['Age']=Age

                elif choice==6:
                    Email_id=input("Enter the updated Email id :").strip()
                    p["Email_id"]=Email_id
                elif choice==7:
                    Phone_Number=int(input("Enter the updated phone number :"))
                    p['Phone_Number']=Phone_Number

                else:
                     Name=input("Enter the updated name :").strip()
                     Admnno=int(input("Enter the updated Admission no : "))
                     Class=input("Enter the updated class :").upper()
                     Class=Class.strip()
                     Section=input("Enter the updated section :").upper()
                     Section=Section.strip()
                     Age=int(input("Enter the updated age :"))
                     Email_id=input("Enter the updated Email id :").strip()
                     Phone_Number=int(input("Enter the updated phone number :"))


                     p['Name']=Name
                     p['Admn_no']=Admnno
                     p['Class']=Class
                     p['Phone_Number']=Phone_Number
                     p['Section']=Section
                     p['Age']=Age
                     p["Email_id"]=Email_id

                     
            with open("Studata.dat",'rb+') as fin:
                       pickle.dump(p,fin)
            
            print(" [*] Record Modified successfully !!")
            print()
            
    except EOFError: 
                fo.close()


        
# Helping guide for user

helpuser()  #helpuser function call to display the help commands. 

while True:
        operation=input("Enter operation to be performed : ") #Which operation to be done update , delete,insert or see all records
        print()

        if operation=="-i": 
            insertrecord()


        elif operation=="-all":
            seeall()   #function call to print all data

        elif operation=="-d":
            delrec()


        elif operation=='-u':
            update()


        elif operation=='-h' or '--help':
            helpuser()
            
        else:
            print("You are about to exit")
            print("Exiting ....")
            
            sleep(5)
            exit()
##        ans=input("Press [y] if you want to use again use this system again, otherwise [n] : ").lower()

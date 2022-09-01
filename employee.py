import os
def write():
    f=open("data.txt","a")
    print("empl_id,employee_name,designation,salary(in thousands)")
    s=input("enter comma seperated data:")
    f.write(s+"\n")
    f.close()
def delete():
    f=open("data.txt","r+")
    t=open("temp.txt","a")
    if os.stat("data.txt").st_size == 0:
        print("deletion cannot be performed on empty file...")
    else:
        id=input("enter employee_id to dalete :")
        for line in f.readlines():
            if id not in line:
                t.write(line)    
    f.close()
    t.close()
    os.replace("temp.txt","data.txt")
    display()
def search():
    f=open("data.txt","r")
    if os.stat("data.txt").st_size == 0:
        print("search cannot be performed on empty file...")
    else:
        id=input("enter employee_id to search:")
        for l in f.readlines():
           if id in l:
               print("employee details found...")
               print(l)
               break
        else:
            print("employee details not found...")
    f.close()
def update():
    f=open("data.txt","r+")
    x=open("temp1.txt","r+")
    if os.stat("data.txt").st_size == 0:
        print("update cannot be performed on empty file...")
    else:
        r=input("enter employee_id to update:")
        for line in f.readlines():
            l=line.split(",")
            if l[0]==r:
                n=int(input("enter the parameter to update\n1.name/2.designation/3.salary : "))
                if(n==1):
                    name=input("enter name to update :")
                    l[1]=name
                elif(n==2):
                    desi=input("enter designation to upadte:")
                    l[2]=desi
                elif(n==3):
                    salary=input("Enter salary to update: ")
                    l[3]=salary
                s=','.join(l)
                x.write(s)
            else:
                x.write(line)
        
    x.close()
    f.close()
    os.remove("data.txt")
    os.rename("temp1.txt","data.txt")
    display()
    
def display():
    f=open("data.txt","r")
    if os.stat("data.txt").st_size == 0:
        print("file is empty...")
    else:
        print("1.displaying all employees details:")
        print("2.displaying particular employee details")
        c=int(input())
        if(c==1): 
            for line in f.readlines():
                print(line)
        else:
            id=input("enter employee_id of the employee:")
            for line in f.readlines():
                if id in line:
                    print(line)
    f.close()
print("operations on data.txt file")
print("1.write\n2.delete\n3.search\n4.update\n5.display")
while True:
    op=int(input("enter operation to be performed :"))
    if(op==1):
        write()
    if(op==2):
        delete()
    if(op==3):
        search()
    if(op==4):
        update()
    if(op==5):
        display()
    ch=input("do you want do more operations (y/n) : ")
    if ch in "Nn":
        break
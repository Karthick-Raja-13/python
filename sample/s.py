'''


Java Script Object Notation
import json
data = [{
    "Name":"Luffy",
    "Role":"Captain",
    "Bounty":120000
},{
"Name":"Sanji",
    "Role":"Cook",
    "Bounty":100000
}
]
#json.dump(data,open("data.json","w"))
li = json.load(open("data.json","r"))
print(li)
import math
print(math.log(2))
print(math.sin(30))
print(math.cos(90))
print(math.pow(5,5))
li = [1,2,3,4,5,6]
print(math.prod(li))
import random as r
import random as r
li = ["Stone","Paper","Scissor"]
print(r.choice(li))

print(li)
r.shuffle(li)
print(li)

print(r.randint(1,10))



r.shuffle(li)
print(li)
import datetime as dt
print(dt.datetime.now())
date = dt.datetime.today()
print(date.strftime("%d/%m/%Y"))


import json as j



j.dump(data,open("sample2.json","w"))
li = j.load(open("C:\\Users\\Admin\\PycharmProjects\\Python\\sample\\sample.json","r"))

print(type(li))
import sys
print("Runned")
arg = sys.argv
print(arg)

print(sys.version)
print(sys.path)
import re

str = "Zenjade Automation Technology Private Limited is a key player in the software sector, specializing in innovative automation solutions that streamline business processes and enhance operational efficiency."

if re.match("Zenje",str):
    print("Pattern Found")
else:
    print("Not Found")

print(re.search("Zenjade",str))

print(re.sub("Zenjade","Nanganallur",str))
thread1 = threading.Thread(target=print_numbers, args=())


thread1.start()


thread1.join()
from time import *
def Hello():
    for i in range(5):
        print(f"Hello {i}")
        sleep(1)


def hii():
    for i in range(5):
        print("Hii" + str(i))
        sleep(1)

from threading import *

t1 = Thread(target=Hello)
t2= Thread(target=hii)


t1.start()
t2.start()
t2.join()
t2.join()


'''
class studentdatabase:
    def _init_(self):
        self.students={}
    def create(self,id,department,rollno,name):
        if id in self.students:
            print("student id already exits")
        else:
            self.students[id]={'name':name,'department':department,'roll number':rollno}
            print("student id created successfully👍")
    def delete(self,id):
        if id in self.students:
            del self.students[id]
            print("student id deleted successfully")
        else:
            print("id cannot be  found")
    def update(self,id,name='None',department='None',rollno='None'):
        if id in self.students:
            if name:
                self.students[id]['name']=name
            if department:
                self.students[id]['department']=department
            if rollno:
                self.students[id]['rollno']=rollno
            print("updated successfully")
        else:
            print("student id not found")
    def veiwbyname(self,name):
        g= False
        for id,details in self.students.items():
           if details['name']==name:
               print(f"ID: {id}, Name: {details['name']}, Department: {details['department']}")
               g=True
        if not g:
            print("invalid name")
    def veiwbydept(self,department):
        f=False
        for id, details in self.students.items():
            if details['department'] == department:
                print(f"ID: {id}, Name: {details['name']}, Department: {details['department']}")
                f=True
        if not f:
            print("invalid entry")
def main():
    a=studentdatabase()
    while True:
        print("\nStudent Database Management System")
        print("1. Create Student Record")
        print("2. Delete Student Record")
        print("3. Update Student Record")
        print("4. View by Name")
        print("5. View by Department")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            rollno=input("Enter roll number")
            a.create(id,department,rollno,name)
        elif choice == '2':
            id = input("Enter Student ID to delete: ")
            a.delete(id)
        elif choice == '3':
            id = input("Enter Student ID to update: ")
            name = input("Enter new Name (leave blank to keep unchanged): ")
            department = input("Enter new Department (leave blank to keep unchanged): ")
            rollno = input("Enter roll number")
            a.update(id, name if name else None, department if department else None,rollno if rollno else None )
        elif choice == '4':
            name = input("Enter Name to search: ")
            a.veiwbyname(name)
        elif choice == '5':
            department = input("Enter Department to search: ")
            a.veiwbydept(department)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
c=main()



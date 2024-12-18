'''
try:
    print(2/0)
except:
    print("An Error Occured")

print (" Code beneath Error ")

try:
    #print("Try Block")
    #print(4/2)
    file = open("","")
except:
    print("Unknown Error")
finally:
    print("Runs Always")
    #file.close()

s = input("Enter your calculation")

print(eval(s))
# Used to store multiple values in a single variable
# It can be of any datatype
# it is changable
#Allows Duplicates
#index starts with 0
# Surrounded with square brackets

li = [1,"string",False,3.67,1,1,1]

print(li)
print(li[2])

li[0] = 12
print(li)
li.append(256)
print(li)

li.insert(5,25)
print(li)

li.remove(False)
print(li)

for i in li:
    print(i)

t = (2,54,67,34)
print(t)
print(t[0])

t = list(t)

t[0] = 15

t = tuple(t)
print(t)
s = {1,2,3,4,4,4}

s.add(5)
s.remove(2)
print(s)
data = {
    "name":"Zenjade",
    "li":[1,2,3,4],
    "training":{
        "core":["ACAD,ECAD"],
        "software":["java",'python']
    }
}

print(data)
print(data["training"]["software"][0])

data["name"] = "Zenjade Automation"
del data["li"]
print(data)

data["New"] = "New Value"
print(data)
a ="Zenjade124"
li = []
num = []
for i in a:
    try:
        num.append(int(i))
    except:
        li.append(i)
s = "The cook of the sea is also a gifted fighter"
print(s[0:3])
print(len(s))
print("cooked" in s)
print("cook" not in s)
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("a","an"))

print(s.split(" "))
print(s.startswith("f"))


st = "The cook2 of the sea3 is also a gifted4 fighter5"

print(st[4]) #Indexing

print(st[16:19]) # Slicing or Sub String
print(len(st))
print(st.split(" "))
print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.replace("gifted","not-gifted"))
print(st.strip())
print(st.startswith("The"))
#for i in st:
 #   print(i.isdigit())
class a():
    def __init__(self):
        print("A Objected Created")
    def add(self,a,b):
        print(a+b)
class b(a):
    def __init__(self):
        print("B Objected Created")

    def sub(self, a, b):
        print(a - b)



class c(b):
    def __init__(self):
        print("B Objected Created")

    def mul(self, a, b):
        print(a * b)


obj = c()
obj.sub(4,5)
obj.add(2,3)
obj.mul(5,2)
s = "345f"
for i in s:
    print(i.isdigit())

#Zenjade --> edajnez
word = input("enter a text")
print(word[::-1])
reversed_word=""
for i in range(len(word)-1,-1,-1): # 5,4,3,2,1,0
    reversed_word+=word[i]
print(reversed_word)


li = [1,2,3,4,5,6,7,8]

def odd(a):
    if a%2==0:
        return True
    else:
        return False


print(max(li))

filtered_obj = filter(odd,li)

print(list(filtered_obj))




li = [1,2,3]

li2 = ["a","b","c"]

zipped_obj = zip(li,li2)

print(list(zipped_obj))
class Mobile:
    #Constructor
    def __init__(self,name):
        self.name = name
        print("From Constructor")
    def hii(self):
        print("Mobile Class "+ self.name)

    def __del__(self):
        print("deleted "+ self.name)

print("Before Object Creation")
s = Mobile("S Obj")

s.hii()

b = Mobile("B Obj")

b.hii()

A -> 1
B -> 5

b --> 1,5class greet:
    def __init__(self,name):
        self.name = name
    def hii(self):
        print("Hii "+ self.name)






s = sample("Zen",50)
s.hii()
s.func()
s.hello()
a = 10

a = 15

print(a)

def add (a ,b):

def add(a,b):
    print(a-b)

add(5,2)


class sample1:
    def hii(self):
        print("Hii from Sample 1")

class sample2(sample1):
    def hii(self):
        print("Hii from Sample 2")


s = sample2()
class sample(greet,welcome):
    def __init__(self,name,val):
        #super().__init__(name,val)
        greet.__init__(self,name)
        welcome.__init__(self,val)
    def func(self):
        print("Third Class")
s.hii()

class welcome():
    def __init__(self,val):
        print(val)
    def hello(self):
        print("Hello Welcome")


total_seats = 30

boarding_points = ["Chennai","ChengalPat"]
dropping_points = ["ChengalPat","Kanchipuram"]

class bus:
    def home(self):
        print("Welcome \nSelect Boarding Point")
        j = 0
        for i in boarding_points:
            j+=1
            print(str(j)+ " "+i)
        choice = int(input("Enter Boarding point"))
        self.choice = choice
    def dest(self):
        j = 0
        for i in dropping_points:
            j += 1
            print(str(j) + " " + i)
        choice2 = int(input("Enter dropping point"))
        self.choice2 = choice2

    def ticket(self):
        tks=int(input("Passengers"))
        total = tks*100
        print(f"Total : {total} ")
import json as j

'''

num = [1,2,3,4,5,6,7,8]
even =[]
odd = []
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
'''
even = [i for i in num if i%2 ==0 ]
odd =[i for i in num if i%2 !=0 ]

print(even)
print(odd)
'''
print(even)
print(odd)


#New
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
''' Java Script Object Notation
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


'''


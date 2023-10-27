#parameter less:
def add():
    a=10
    b=20
    print(a + b)
add()
def sub():
    a=10
    b=20
    print(a - b)
sub()

#parameterized function:
def add(literal1: int, literal2: int):
    print(literal1 + literal2)
add(10, 20)

def sub(literal1: int, literal2: int):
    print(literal1 - literal2)
add(10, 20)
a = 10
b = 20
sub(literal1=a, literal2=b)
sub(literal2=b, literal1=a)

#String Transform Functions-capitalize
#Syntax:variable.capitalize()
def capitalize():
    a="jyothi"
    print(a.capitalize())
capitalize()

#Title
#syntax:variable.title()
def title():
    a="jyothi"
    print(a.title())
title()

#upper
#syntax:variable.upper()
def upper():
    a="jyothi"
    print(a.upper())
upper()

#lower
#syntax:variable.lower()
def lower():
    a="JYOTHI"
    print(a.lower())
lower()

#casefold
#syntax:variable.casefold()
def casefold():
    a="JYOTHI"
    print(a.casefold())
casefold()

#swapcase
#syn tax:variable.swapcase()
def swapcase():
    a="Jyothi"
    print(a.swapcase())
swapcase()

#String Check Functions
#isnumeric
#syntax:variable.isnumeric()
def isnumeric():
    a="124"
    print(a.isnumeric())
isnumeric()

#isalphanumeric
#syntax:variable.ialnum()
def isalnum():
    a="jyothi123454666"
    print(a.isalnum())
isalnum()

#isdecimal
#syntax:variable.isdecimal()
def isdecimal():
    a="12123123"
    print(a.isdecimal())
isdecimal()

#isdigit
#syntax:variable.isdigit()
def isdigit():
    a="67468746"
    print(a.isdigit())
isdigit()

#isascii
#syntax:variable.isascii()
def isascii():
    a="jyothi"
    print(a.isascii())
isascii()

#isupper
#syntax:variable.isupper()
def isupper():
    a="jyothi"
    print(a.isupper())
isupper()

#islower
#syntax:variable.islower()
def islower():
    a="JYOTHI"
    print(a.islower())
islower()

#isspace
#syntax:variable.isspace()
def isspace():
    a=" "
    print(a.isspace())
isspace()

#isidentifier
#syntax:variable.isidentifier()
def isidentifier():
    a="jyothi12132"
    print(a.isidentifier())
isidentifier()

#isprintable
#syntax:variable.isprintable()
def isprintable():
    a="jyothi"
    print(a.isprintable())
isprintable()

#istitle
#syntax:variable.istitle()
def istitle():
    a="jyothi korrapati"
    print(a.istitle())
istitle()

#String Search Functions
#index
#syntax:variableName.index(string/char)
def index():
    email="sagar@gmail.com"
    print(email.index("@"))
index()

#rindex
#syntax:variableName.rindex(string/char)
def rindex():
    email="sagar@gmail@.com"
    print(email.rindex("@"))
rindex()

#rfind
#syntax:variableName.rfind(string/char)
def rfind():
    email="sagar@gmail@.com"
    print(email.rindex("@"))
rfind()

#startswith
#syntax:variableName.startswith(string/char)
def startswidth():
    email="sagar@gmail.com"
    print(email.startswith("sagar"))
startswidth()

#endswith
#syntax:variableName.endswith(string/char)
def endswith():
    email="sagar@gmail.com"
    print(email.endswith("sumathi"))
endswith()

#list methods
#Append
#syntax:lst.append()
def append():
    lst=[]
    print(lst.append("venky"))
    print(lst)
append()

#insert
#syntax:lst.insert(index,item)
def insert():
    lst=["sagar","venky"]
    print(lst.insert(1,"sumathi"))
    print(lst)
insert()

#Extend
#syntax:lst.extend(lst1)
def extend():
    name=["sagar","sumathi","venky"]
    name1=["jyothi","vasu"]
    name.extend(name1)
    print(name)
extend()

#count
#syntax:lst.count(item)
def count():
    name=["sagar","sagar","sumathi","jyothi"]
    print(name.count("sagar"))
count()

#pop with index
#syntax:lst.pop(index)
def pop():
    name=["hepsi","vasu","jyo"]
    name.pop(1)
    print(name)
pop()

#pop without index
#syntax:lst.pop()
def pop():
    attendees=["vasu","jyo","hepsi"]
    attendees.pop()
    print(attendees)
pop()

#remove
#syntax:lst.remove()
def remove():
    a=["anu","bavya","chitti"]
    print(a.remove("bavya"))
    print(a)
remove()

#clear
#syntax:lst.clear()
def clear():
    a=["anu","bavya","chitii"]
    print(a.clear())
    print(a)
clear()

#sort
#syntax:lst.sort()
def sort():
    a=[1,2,5,6,3]
    a.sort()
    print(a)
sort()

#reverse
#syntax:lst.reverse()
def reverse():
    a=[1,2,5,6,3]
    a.reverse()
    print(a)
reverse()

#Tuple Methods
#count
#syntax:tpl.count(item)
def count():
    tpl=tuple((1,2,2,2,2,3,5,4))
    print(tpl.count(2))
count()

#index
#syntax:tpl.index(item)
def index():
    tpl=tuple((1,2,3,4,5,6))
    print(tpl.index(3))
index()

#set methods
#add
#syntax:variable.add()
def add():
    a={'a','b','c'}
    a.add('d')
    print(a)
add()

#update
#syntax:variable.update(setvariable)
def update():
    a={'a','b','c'}
    b={'b','c','d'}
    a.update(b)
    print(a)
update()

#remove
#syntax:variableName.remove(item)
def remove():
    a={'a','b','c'}
    a.remove('b')
    print(a)
remove()

#discard
#syntax:variableName.discard(item)
def discard():
    a={'a','b','c'}
    a.discard('c')
    print(a)
discard()

def discard():
    a={'a','b','c'}
    a.discard('d')
    print(a)
discard()

#pop
#syntax:variableName.pop()
def pop():
    a={'a','b','c'}
    a.pop()
    print(a)
pop()

#other methods of sets
#union
#syntax:variableName.union(variable)
def union():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.union(b))
union()

#intersection
#syntax:variableName.intersection(variable)
def intersection():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.intersection(b))
intersection()

#intersection update
#syntax:set1.intersection_update(set2)
def intersection_update():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.intersection_update(b))
    print(a)
    print(b)
intersection_update()

#isdisjoint
#syntax:set1.isdisjoint(set2)
def isdisjoint():
    a={'a'}
    b={'b'}
    print(a.isdisjoint(b))
isdisjoint()

#difference
#syntax:set1.difference(set2)
def difference():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.difference(b))
difference()

#symmetric difference
#syntax:set1.symmetric difference(set2)
def symmetric_difference():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.symmetric_difference(b))
symmetric_difference()

#symmetric difference update
#syntax:set1.symmetric difference update(set2)
def symmetric_difference_update():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.symmetric_difference_update(b))
    print(a)
    print(b)
symmetric_difference_update()

#issubset
#syntax:set1.issubset(set2)
def issubset():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.issubset(b))
issubset()

#issuperset
#syntax:set1.issuperset(set2)
def issuperset():
    a={'a','b','c'}
    b={'b','c','d'}
    print(a.issuperset(b))
issuperset()

#frozenset-union
#syntax:variableName.union(variable)
def union():
    a=frozenset(["venky","sumathi","sagar"])
    b=frozenset(["sumathi","vasu","soni"])
    print(a.union(b))
union()

#intersection
#syntax:variableName.intersection(variable)
def intersection():
    a = frozenset(["venky", "sumathi", "sagar"])
    b = frozenset(["sumathi", "vasu", "soni"])
    print(a.intersection(b))
intersection()

#isdisjoint
#syntax:set1.isdisjoint(set2)
def isdisjoint():
    a = frozenset(["venky", "sumathi", "sagar"])
    b = frozenset(["sumathi", "vasu", "soni"])
    print(a.isdisjoint(b))
isdisjoint()

def isdisjoint():
    a=frozenset(["sagar"])
    b=frozenset(["sumathi"])
    print(a.isdisjoint(b))
isdisjoint()

#issubset
#syntax:set1.issubset(set2)
def issubset():
    a = frozenset(["venky", "sumathi", "sagar"])
    b = frozenset(["sumathi", "vasu", "soni"])
    print(a.issubset(b))
issubset()

def issubset():
    a=frozenset(["sumathi"])
    b=frozenset(["sumathi","sagar","venky"])
    print(a.issubset(b))
issubset()

#issuperset
#syntax:set1.issuperset(set2)
def issuperset():
    a = frozenset(["venky", "sumathi", "sagar"])
    b = frozenset(["sumathi", "vasu", "soni"])
    print(a.issuperset(b))
issuperset()

def issuperset():
    a=frozenset(["sagar","sumathi","venky"])
    b=frozenset(["sumathi"])
    print(a.issuperset(b))
issuperset()

#diffrence
#syntax:set1.difference(set2)
def difference():
    a = frozenset(["venky", "sumathi", "sagar"])
    b = frozenset(["sumathi", "vasu", "soni"])
    print(a.difference(b))
    print(b.difference(a))
difference()

#symmetric_difference
#syntax:set1.symmetric difference(set2)

def symmetric_difference():
    a = frozenset(["venky", "sumathi", "sagar"])
    b = frozenset(["sumathi", "vasu", "soni"])
    print(a.symmetric_difference(b))
symmetric_difference()

#copy
def copy():
    a = frozenset(["venky", "sumathi", "sagar"])
    b = frozenset(["sumathi", "vasu", "soni"])
    c1=a.copy()
    c2=b.copy()
    print(c1)
    print(c2)
copy()

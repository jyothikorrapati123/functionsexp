#function with optional params
#syntax: def functionName(param1,param2,param3=0)
                  #logic

def add(literal1:int,literal2:int,literal3:int=0):
    print(literal1+literal2+literal3)
add(10,20)
add(10,20,5)

#function with arbitary params
#syntax: def functionName(*arb)
              #logic
         #functionName(data1,data2,...)

def add_arb(*literals):
    res:int=0
    for item in literals:
        res+=item
    print(res)
add_arb(1,2,3,4,5,6,7)


#function with arbitary key params
#syntax: def functionName(**arbs)
              #logic
        #functionName(key=value,key=value,...)

def userDetails(**literals):
    name=literals.get("name")
    email=literals.get("email")
    gender=literals.get("gender")
    place=literals.get("place")
    print(name,email,gender,place)
userDetails(name="Jyothi",email="jyothi@gmail.com",gender="Female",place="guntur")
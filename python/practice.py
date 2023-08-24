
class Quote():
    qoutes=[]
    def update(self,quote,index):
        self.qoutes[index]=quote
        
    def add(self,qoutes):
        self.qoutes.append(qoutes)
        
    
class Fame():
    def change(self,ref,occ):
        ref.occ=occ

    def resign(self,ref,occ):
        ref.occ=None
        

class Person(Quote,Fame):
    name=None
    qoute=None
    occ=None
    def __init__(self,name,qoute,occ):
        self.name=name
        self.qoute=qoute
        self.occ=occ
    def getinfo(self):
        return {"name":self.name,"qoute":self.qoute,"occ":self.occ}
   

junaid=Person("junaid","win","ds")
fame=Fame()
print(junaid.getinfo())
junaid.add("live batter life")
junaid.add("day gone")
junaid.update("day after tomarrow", 1)
print(junaid.qoutes)
fame.change(junaid,"singrr")
print(junaid.occ)
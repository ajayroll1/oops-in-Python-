# methods are functions that belong to objects  


# class k andar 2 chiz store hoti hia 1.method 2.attributes

#1.method---------->yeh functions hai jo btata hia ki properies ya featurs kaam kaise karegi .yeh functions hai jo class k andar likhe jate hia isiliye isko meethods kehte hia 

#2.attributes(data)--->properties means features

#Methods isiliye banate hain taaki unke through hum object ko use kar sake aur batayein ki wo behave kaise karega

class Student:
  college="ABC"

  def __init__(self,name,marks):
    self.name=name
    self.marks=marks


  def helloe(self): #yeh method hia means funcrion inside a class
    print("welcome student ",self.name)  


  def getmarks(self):
    print("this is your marks",s1.marks)  


s1=Student("ajay",100)
print(s1.name,s1.marks)
s1.helloe()
s1.getmarks()


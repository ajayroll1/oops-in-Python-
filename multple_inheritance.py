# multiple inheritance mai derived class means child class multiple base classs means parents class se properties leta hi apne mai or i caan say child class agar 1 se zada parent class se data leta hia to mulitple class hogaya 


class Parent1():
  def __init__(self,weight):
    self.weight=weight


class Parent2():
   def __init__(self,age):
    self.age=age


class child(Parent1,Parent2):
  def __init__(self,weight,age):
    Parent1.__init__(self,weight)
    Parent2.__init__(self,age)
    print("child constructor called now ")
       

child1=child(50,20)
print("This is age:", child1.age, "and this is weight:", child1.weight)

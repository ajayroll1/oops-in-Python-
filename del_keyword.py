# yeh keyword use karte hi to  object ka properties ya fir object ko kar saktehia delete 
class Student:
  def __init__(self,name):
    self.name=name



s1=Student("ajay")
print (s1.name)
del s1.name


print (s1.name)




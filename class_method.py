class Person:
  name="ananymous"

  # def changeName(self,name):
    # Person.name=name yeh direct class ka data ko call krkhia 
    # self.__class__.name="ajay" #1st method
  @classmethod  #2nd method
  def changeName(cls,name):
    cls.name=name


p1=Person()
p1.changeName("ajay kumar ")
print(p1.name)
print(Person.name)

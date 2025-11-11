class Car:
  
  @staticmethod # yeh static mehtod hia ismai koi object call nhi hota hia ismai ibuilt likh det hia jo call hoga and 


  # yeh mothods jo class k andar rhte hi awo 3 types k hote hia Method Type	Keyword	Kya Access Kar Sakta Hai	Kaha Use Hota Hai
# Instance Method	(normal method)	Object ka data (self)	Jab method object ke variables (like name, age, etc.) par kaam kare
# Class Method	@classmethod	Class ka data (cls)	Jab method class-level variable ko change ya access kare
# Static Method	@staticmethod	Na object na class	Jab sirf ek helper function chahiye ho jo class se logically related ho
  def start():
    print("car started")

  @staticmethod   # yeh object create nhi karta hia yeh static hia just static site data yahi pass kiya jata hia 
  def stop():
    print("car stop ")  
  


class ToyotaCar(Car):
   def __init__(self,brand):
      self.brand=brand


class Fortuner(ToyotaCar,Car):
  def __init__(self,type):
    self.type=type

car1=Fortuner("diesel")
car1.start()

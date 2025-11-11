# jab ek class apna features means data or mehtod share karta hia dusre class k satrh to isko inheritance kehte hia ya fir dusre class ise use karte hia  called inheritance 


class Car:
  color="black"
  @staticmethod
  def start():
    print("car started")

  @staticmethod
  def stop():
    print("car stop ")  
  


class ToyotaCar(Car):
   def __init__(self,name):
      self.name=name


car1=ToyotaCar("fortuner")
car2=ToyotaCar("car2") 
print(car1.name)   
print(car2.color) 
print(car1.start()) 

      


      # 3 types ka hotahia inheritance ----> single ,multi level and multiple inheritance 

      # 1.single level  inhertiance 
      # ismai ek base class hotahi aand dervied class means ek parent class se  properties child class  jayega .upar diya hiiu a example isi ka hia 


      # 2 multi level inheritance 
      # ismai ek base class hotahi aand dervied class means ek parent class se  properties child class  jayega and child or dervied class se fir jayega ek dusra child class mai isko bole hia multi level inheritance  ismai  1st and second class ka properties 3rc  class mai use ho thi ahi



# super method ek special  mehtod hota hia classes mai jo use hta hia method ko access karne liye jo methods parent claass mai rhte hia 

class Car:
    def __init__(self, type):
        self.type = type
  
    @staticmethod # yeh static mehtod hia ismai koi object call nhi hota hia ismai ibuilt likh det hia jo call hoga and 

    # yeh mothods jo class k andar rhte hi awo 3 types k hote hia Method Type Keyword Kya Access Kar Sakta Hai Kaha Use Hota Hai
    # Instance Method (normal method) Object ka data (self) Jab method object ke variables (like name, age, etc.) par kaam kare
    # Class Method @classmethod Class ka data (cls) Jab method class-level variable ko change ya access kare
    # Static Method @staticmethod Na object na class Jab sirf ek helper function chahiye ho jo class se logically related ho
    def start():
        print("car started")

    @staticmethod   # yeh object create nhi karta hia yeh static hia just static site data yahi pass kiya jata hia 
    def stop():
        print("car stop ")  


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        #super().__init__(type)  #super() ka main use hi ye hai ki child class parent class ka constructor ya parent methods ko easily access kar sake.


car1 = ToyotaCar("prius", "electric")
print(car1.type)

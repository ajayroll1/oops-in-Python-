# abstarction kya karta hai implemenation details ko hide karta ha  class ka and show karta hia essenstial features to the users means hard or complex chiz ko chupaoaw and and needy chiz ko dikahow 
#

#Encapsulation ka matlab: --->  # Jab ek class ke andar attributes (data) aur methods (functions) dono hote hain,
# aur wo methods us data pe kaam karte hain,
# tab use Encapsulation kehte hain.
class Car:
  def __init__(self):# this is constructor 
    self.acc=False
    self.brk=False
    self.clutch=False

  def start(self):#this is mehtod 
      self.clutch=True
      self.acc=True
      print("car started")


car1=Car() # yeh object hia and 
car1.start() # yeh method run ho hri iha
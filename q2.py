class Order:
  def __init__(self,item,price):
    self.item=item
    self.price=price

  def __gt__(self,oder2):
    return self.price > oder2.price




oder1=Order("2chips",30) 
oder2=Order("chips",20)  

print(oder1 >oder2)
    
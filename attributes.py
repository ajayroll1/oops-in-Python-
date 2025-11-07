# attribuetes means koi bhi data ya variable 

# 2 types ----->class.attr ---> ismai hmlok common data ko likjhte hia jaise students ka college name same hai 
#        ----->obj.attr


class Student:
  college="abc college"  # yeh class attribute hia 

  def __init__(self,name,marks):
    self.name=name #yeh object attribute hia 
    self.marks=marks

s1=Student("ajay",99)
print(s1.name,s1.marks,Student.college)    
       
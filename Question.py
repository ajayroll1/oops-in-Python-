# create student class that takes name and marks of 3 subjects as arguments in constructor then creates mehtod to print the average 


class Student :
  def __init__(self,names,marks):
        self.names=names
        self.marks=marks

  def this_is_method(self):#yeh method hia jo ki class k andar likhe jati hia 
    #  return sum(self.marks)/len(self.marks)    
    sum = 0
    for val in self.marks:
     sum += val
    print("hi this ",self.names,"my average maeks is", sum/3)
    



S1=Student("ajay",[200,10,20])
S1.this_is_method() 
S2=Student("sanjay",[200,12,14])

S2.this_is_method()

     


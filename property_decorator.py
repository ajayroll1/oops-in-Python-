# Jaha bhi @property decorator laga hoga, wo method ek normal data/variable ki tarah behave karega.
# Matlab:
# Method hoga, but use attribute ki tarah hoga.

# () parenthesis kabhi nahi use karne padenge.

# Internally function hi call hota hai, par bahar se variable jaisa lagta hai.

class Student:
  def __init__(self,phy,chem,maths):
    self.phy=phy
    self.chem=chem
    self.maths=maths
    # self.percentage=str((self.phy + self.chem+self.maths)/3) + "%"

  # def calculate_percentage(self):
  #   self.percentage=str((self.phy + self.chem+self.maths)/3) + "%"

  @property
  def percentage(self):
    return str((self.phy + self.chem+self.maths)/3) + "%"


Student1=Student(12,25,50)
print(Student1.percentage)



Student1.phy=83

print(Student1.percentage)



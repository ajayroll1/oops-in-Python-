# in python constructor is just __init__() function
#all classes have a function called __init__() whiich is always executed when the class is being initiated

class Student:
  name="karan"

def __init__(self): #ismai ek he parameter hia  this  is called DEFAULT CONSTRUCTORS
  print("this is con")


  def __init__(self,fullname,marks,rollno): # this is called PARAMTERIZED CONSTRUCTOR #yaha multi paramter hai  $ #yaha self parameter hai jo ki reference de rhai jo bhi naya object ban rhai hi and uske variable ko acesss karne k liye jo belong karti hia same class ko 
     self.name=fullname
     self.marks=marks
     self.rollno=rollno
     print("added")
  



# Object create hone ka matlab hai ek khaali dabba (memory space) ban gaya class ka,
# aur constructor (__init__) automatically us dabbe ke andar variables daal deta hai.”



# ✅ Object creation → empty box (via __new__())
# ✅ Initialization → box ke andar data fill (via __init__())

s1 =Student("karan",100,1)
print(s1.name,s1.marks,s1.rollno)

# print(s1.name)
s2 =Student("arjun",200,2)
print(s2.name,s2.marks,s2.rollno)
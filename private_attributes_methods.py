# private attributes and methods  ko use kiya jata hia class k andar sirf and yeh sab class k bahar se accesible nhi hote hia 


# class Account:
#   def __init__(self,account_no,password):
#     self.account_no=account_no
#     self.__password = password   # ✅ double underscore = private


#   def reset_pass(self):
#     print(self.__password)





# acc1=Account(123345,"wedw655wefd")
# print(acc1.account_no)
# print(acc1.reset_pass())    



class Person:
    __name = "anonymous"  # private attribute

    def __hello(self):     # private method
        print("hello")

    def welcome(self):
        self.__hello()     # ✅ accessible inside class


p1 = Person()
# print(p1.__name)      # ❌ Error
print(p1.welcome())   

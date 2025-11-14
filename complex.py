class Complex:
    def __init__(self, real, img):
        # yeh constructor hia jo real aur imaginary part ko set karta hia
        self.real = real
        self.img = img

    def showNumber(self):
        # yeh method complex number ko print karega
        print(self.real, "i  +", self.img, "j")

    # __add__ dunder method hia jo + operator ko override karta hia
    def __add__(self, num2):
        newReal = self.real + num2.real   # dono real parts ka addition
        newImg = self.img + num2.img     # dono imaginary parts ka addition
        return Complex(newReal, newImg)  # naye object ko return karo

    # __sub__ dunder method hia jo - operator ko override karta hia
    def __sub__(self, num2):
        newReal = self.real - num2.real   # real parts ka subtraction
        newImg = self.img - num2.img      # imaginary parts ka subtraction
        return Complex(newReal, newImg)


# yaha se objects bana rhe hia
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(15, 32)
num2.showNumber()

# yaha + operator call karne par __add__ method chalega
# num3 = num1 + num2
# num3.showNumber()

# subtraction ka example
num4 = num2 - num1
num4.showNumber()


# Correct explanation:
# __add__ → + operator
# __sub__ → - operator
# __mul__ → * operator
# __truediv__ → / operator
# __mod__ → % operator
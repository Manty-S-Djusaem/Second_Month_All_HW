def long_function_name(x, y):
    if x == 0:
        return y
    else:
        return long_function_name(y % x, x)


class Fraction:
    def __init__(self, numerator, denominator):
        num_1 = long_function_name(numerator, denominator)
        self.numerator = numerator // num_1
        self.denominator = denominator // num_1

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)

        elif self.numerator > self.denominator:
            return str(self.numerator // self.denominator) + " " + \
                   str(Fraction(self.numerator % self.denominator, self.denominator))

        else:
            return str(self.numerator) + "/" + str(self.denominator)

    """
    
        Dunder Method     
        
    """

    def __mul__(self, another):
        numerator_new = self.numerator * another.numerator
        denominator_new = self.denominator * another.numerator
        return Fraction(numerator_new, denominator_new)

    def __add__(self, another):
        numerator_new = self.numerator * another.denominator + another.numerator * self.denominator
        denominator_new = self.denominator * another.denominator
        return Fraction(numerator_new, denominator_new)

    def __floordiv__(self, another):
        numerator_new = self.numerator // another.denominator
        denominator_new = self.denominator // another.denominator
        return Fraction(numerator_new, denominator_new)

    def __sub__(self, another):
        numerator_new = self.numerator * another.denominator - another.numerator * self.denominator
        denominator_new = self.denominator * another.denominator
        return Fraction(numerator_new, denominator_new)


x = Fraction(5, 5)
y = Fraction(5, 5)
print(x * y)
print(x + y)
print(x // y)
print(x - y)












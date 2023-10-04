import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        new_real = self.real + no.real
        new_imag = self.imaginary + no.imaginary
        return Complex(new_real, new_imag)
    def __sub__(self, no):
        new_real = self.real - no.real
        new_imag = self.imaginary - no.imaginary
        return Complex(new_real, new_imag)
    def __mul__(self, no):
        first = self.real * no.real
        outer = self.real * no.imaginary
        inner = self.imaginary * no.real
        last = self.imaginary * no.imaginary
        new_real = first - last
        new_imag = inner + outer
        return Complex(new_real, new_imag)
    def __truediv__(self, no):
        conjugate = -1 * no.imaginary
        denominator = Complex(no.real, conjugate)
        numerator = self * denominator
        new_denominator = no * denominator
        new_real = numerator.real / new_denominator.real
        new_imag = numerator.imaginary / new_denominator.real
        return Complex(new_real, new_imag)
    def mod(self):
        distance = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(distance, 0)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
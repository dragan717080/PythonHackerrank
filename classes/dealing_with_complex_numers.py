import math

class Complex(object):
    def __init__(self, real, imaginary):
        # Corner case
        if imaginary == -0.0:
            imaginary = 0.0
        prefix = "+" if imaginary >= 0 else ""
        self.real = real
        self.imaginary = imaginary
        self.z = complex(f"{real}{prefix}{imaginary}j")

    def get_res(self, z):
        return Complex(z.real, z.imag)

    def __add__(self, no):
        return self.get_res(self.z + Complex(no.real, no.imaginary).z)

    def __sub__(self, no):
        return self.get_res(self.z - Complex(no.real, no.imaginary).z)

    def __mul__(self, no):
        return self.get_res(self.z * Complex(no.real, no.imaginary).z)

    def __truediv__(self, no):
        return self.get_res(self.z / Complex(no.real, no.imaginary).z)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)

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

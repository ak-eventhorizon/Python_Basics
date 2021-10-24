import math


class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __add__(self, other):
        return Complex(
            (self.real + other.real),
            (self.img + other.img)
        )

    def __sub__(self, other):
        return Complex(
            (self.real - other.real),
            (self.img - other.img)
        )

    def __mul__(self, other):
        return Complex(
            (self.real * other.real - self.img * other.img),
            (self.real * other.img + self.img * other.real)
        )

    def __truediv__(self, other):
        return Complex(
            ((self.real*other.real + self.img*other.img) / (other.real**2 + other.img**2)),
            ((other.real*self.img - self.real*other.img) / (other.real**2 + other.img**2))
        )

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.img ** 2), 0)

    def __str__(self):
        if self.img == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.img >= 0:
                result = "0.00+%.2fi" % self.img
            else:
                result = "0.00-%.2fi" % (abs(self.img))
        elif self.img > 0:
            result = "%.2f+%.2fi" % (self.real, self.img)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.img))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    # x = Complex(2.0, 1.0)
    # y = Complex(5.0, 6.0)

    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

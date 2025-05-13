class MyComplex:
    def __init__(self, real_1, imaginary_1, real_2, imaginary_2):
        self.real_1 = real_1
        self.imaginary_1 = imaginary_1
        self.real_2 = real_2
        self.imaginary_2 = imaginary_2

    def multiply(self):
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        a, b = self.real_1, self.imaginary_1
        c, d = self.real_2, self.imaginary_2

        real_result = a * c - b * d
        imaginary_result = a * d + b * c

        if imaginary_result >= 0:
            print(f"곱셈 결과: {real_result} + {imaginary_result}i")
        else:
            print(f"곱셈 결과: {real_result} - {abs(imaginary_result)}i")


# 테스트용 복소수: a = 3 - 4i, b = -5 + 2i
complex_op = MyComplex(3, -4, -5, 2)
complex_op.multiply()

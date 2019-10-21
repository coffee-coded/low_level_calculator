class operation:

    def __init__(self, category, num1, num2):
        self.category = category
        self.num1 = num1
        self.num2 = num2
        if category == 'd' or category == 'D':
            self.decimal_add()
            self.decimal_sub()
            self.decimal_mul()
            self.decimal_div()
            self.decimal_rem()

        if category == 'b' or category == 'B':
            self.binary_add()
            self.binary_sub()
            self.binary_mul()
            self.binary_div()
            self.binary_rem()

        if category == 'o' or category == 'O':
            self.octal_add()
            self.octal_sub()
            self.octal_mul()
            self.octal_div()
            self.octal_rem()

        if category == 'h' or category == 'H':
            self.hexadecimal_add()
            self.hexadecimal_sub()
            self.hexadecimal_mul()
            self.hexadecimal_div()
            self.hexadecimal_rem()

    def decimal_add(self):
        n1 = int(self.num1)
        n2 = int(self.num2)
        print(n1, "+", n2, "=", n1 + n2)

    def decimal_sub(self):
        n1 = int(self.num1)
        n2 = int(self.num2)
        print(n1, "-", n2, "=", int(n1) - int(n2))

    def decimal_mul(self):
        n1 = int(self.num1)
        n2 = int(self.num2)
        print(n1, "*", n2, "=", int(n1) * int(n2))

    def decimal_div(self):
        n1 = int(self.num1)
        n2 = int(self.num2)
        print(n1, "/", n2, "=", int(n1) / int(n2))

    def decimal_rem(self):
        n1 = int(self.num1)
        n2 = int(self.num2)
        print(n1, "%", n2, "=", int(n1) % int(n2))

    def binary_add(self):
        n1 = int(self.num1, 2)
        n2 = int(self.num2, 2)
        print(n1, "+", n2, "=", int(n1) + int(n2))

    def binary_sub(self):
        n1 = int(self.num1, 2)
        n2 = int(self.num2, 2)
        print(n1, "-", n2, "=", int(n1) - int(n2))

    def binary_mul(self):
        n1 = int(self.num1, 2)
        n2 = int(self.num2, 2)
        print(n1, "*", n2, "=", int(n1) * int(n2))

    def binary_div(self):
        n1 = int(self.num1, 2)
        n2 = int(self.num2, 2)
        print(n1, "/", n2, "=", int(n1) / int(n2))

    def binary_rem(self):
        n1 = int(self.num1, 2)
        n2 = int(self.num2, 2)
        print(n1, "%", n2, "=", int(n1) % int(n2))

    def octal_add(self):
        n1 = int(self.num1, 8)
        n2 = int(self.num2, 8)
        print(n1, "+", n2, "=", int(n1) + int(n2))

    def octal_sub(self):
        n1 = int(self.num1, 8)
        n2 = int(self.num2, 8)
        print(n1, "-", n2, "=", int(n1) - int(n2))

    def octal_mul(self):
        n1 = int(self.num1, 8)
        n2 = int(self.num2, 8)
        print(n1, "*", n2, "=", int(n1) * int(n2))

    def octal_div(self):
        n1 = int(self.num1, 8)
        n2 = int(self.num2, 8)
        print(n1, "/", n2, "=", int(n1) / int(n2))

    def octal_rem(self):
        n1 = int(self.num1, 8)
        n2 = int(self.num2, 8)
        print(n1, "%", n2, "=", int(n1) % int(n2))

    def hexadecimal_add(self):
        n1 = int(self.num1, 16)
        n2 = int(self.num2, 16)
        print(n1, "+", n2, "=", int(n1) + int(n2))

    def hexadecimal_sub(self):
        n1 = int(self.num1, 16)
        n2 = int(self.num2, 16)
        print(n1, "-", n2, "=", int(n1) - int(n2))

    def hexadecimal_mul(self):
        n1 = int(self.num1, 16)
        n2 = int(self.num2, 16)
        print(n1, "*", n2, "=", int(n1) * int(n2))

    def hexadecimal_div(self):
        n1 = int(self.num1, 16)
        n2 = int(self.num2, 16)
        print(n1, "/", n2, "=", int(n1) / int(n2))

    def hexadecimal_rem(self):
        n1 = int(self.num1, 16)
        n2 = int(self.num2, 16)
        print(n1, "%", n2, "=", int(n1) % int(n2))

class conversion:

    def __init__(self, category, num):
        self.category = category
        self.num = num
        if category == "d" or category == 'D':
            self.decimal_to_binary()
            self.decimal_to_hexadecimal()
            self.decimal_to_octal()

        if category == "b" or category == "B":
            self.binary_to_decimal()
            self.binary_to_hexadecimal()
            self.binary_to_octal()

        if category == "o" or category == "O":
            self.octal_to_binary()
            self.octal_to_decimal()
            self.octal_to_hexadecimal()

        if category == "h" or category == "H":
            self.hexadecimal_to_binary()
            self.hexadecimal_to_decimal()
            self.hexadecimal_to_octal()

    def decimal_to_binary(self):
        decimal = int(self.num)
        print(decimal, " in Binary      : ", bin(decimal))

    def decimal_to_hexadecimal(self):
        decimal = int(self.num)
        print(decimal, " in Hexadecimal : ", hex(decimal))

    def decimal_to_octal(self):
        decimal = int(self.num)
        print(decimal, " in Octal       : ", oct(decimal))

    def binary_to_decimal(self):
        bi = self.num
        print(bi, " in Decimal     : ", int(bi, 2))

    def binary_to_octal(self):
        bi = self.num
        print(bi, " in Octal       : ", oct(int(bi, 2)))

    def binary_to_hexadecimal(self):
        bi = self.num
        print(bi, " in Hexadecimal : ", hex(int(bi, 2)))

    def octal_to_decimal(self):
        oc = self.num
        print(oc, "in decimal    :", int(oc, 8))

    def octal_to_binary(self):
        oc = self.num
        print(oc, "in binary     :", bin(int(oc, 8)))

    def octal_to_hexadecimal(self):
        oc = self.num
        print(oc, "in hexadecimal:", hex(int(oc, 8)))

    def hexadecimal_to_binary(self):
        he = self.num
        print(he, "in Binary :", bin(int(he, 16)))

    def hexadecimal_to_octal(self):
        he = self.num
        print(he, "in Octal  :", oct(int(he, 16)))

    def hexadecimal_to_decimal(self):
        he = self.num
        print(he, "in Decimal:", int(he, 16))

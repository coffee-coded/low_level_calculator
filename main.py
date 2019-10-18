import sys

def decimal_to_binary(dec): 
    decimal = int(dec) 
    print(decimal, " in Binary      : ", bin(decimal)) 
   
def decimal_to_octal(dec): 
    decimal = int(dec)  
    print(decimal, " in Octal       : ", oct(decimal)) 
  
def decimal_to_hexadecimal(dec): 
    decimal = int(dec)  
    print(decimal, " in Hexadecimal : ", hex(decimal)) 

def binary_to_decimal(bi): 
    print(bi, " in Decimal     : ", int(bi,2)) 

def binary_to_octal(bi): 
    print(bi, " in Octal       : ", oct(int(bi,2))) 

def binary_to_hexadecimal(bi): 
    print(bi, " in Binary      : ", hex(int(bi,2))) 

if sys.argv[1]=='c':
    if(sys.argv[2]=='d' or sys.argv[2]=='D'):
        x = int(sys.argv[3])
        decimal_to_binary(x)
        decimal_to_hexadecimal(x)
        decimal_to_octal(x)

    if(sys.argv[2]=='b' or sys.argv[2]=='B'):
        x = sys.argv[3]
        binary_to_decimal(x)
        binary_to_hexadecimal(x)
        binary_to_octal(x)
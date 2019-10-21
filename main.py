import sys

from classes.conversion import conversion
from classes.operation import operation

if __name__ == '__main__':

    if sys.argv[1] == 'c' or sys.argv[1] == 'C':
        if sys.argv[2] == 'd' or sys.argv[2] == 'D':
            conversion(sys.argv[2], sys.argv[3])
        if sys.argv[2] == 'b' or sys.argv[2] == 'B':
            conversion(sys.argv[2], sys.argv[3])
        if sys.argv[2] == 'o' or sys.argv[2] == 'O':
            conversion(sys.argv[2], sys.argv[3])
        if sys.argv[2] == 'h' or sys.argv[2] == 'H':
            conversion(sys.argv[2], sys.argv[3])

    if sys.argv[1] == 'o' or sys.argv[1] == 'O':
        if sys.argv[2] == 'd' or sys.argv[2] == 'D':
            operation(sys.argv[2], sys.argv[3], sys.argv[4])
        if sys.argv[2] == 'b' or sys.argv[2] == 'B':
            operation(sys.argv[2], sys.argv[3], sys.argv[4])
        if sys.argv[2] == 'o' or sys.argv[2] == 'O':
            operation(sys.argv[2], sys.argv[3], sys.argv[4])
        if sys.argv[2] == 'h' or sys.argv[2] == 'H':
            operation(sys.argv[2], sys.argv[3], sys.argv[4])


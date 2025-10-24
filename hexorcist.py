digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(number, in_base):
    out_num = 0
    place = 0
    for char in number[::-1]:
        buffer = digits.index(char) * (in_base ** place)

in_base = int(input("What base number system are you starting from? "))
out_base = int(input("What base number system are you converting to? "))
in_num = input("What's the number you want to convert? ")

to_decimal("C8A", 16)
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(number, in_base):
    out_num = 0
    place = 0
    for char in number[::-1]:
        out_num += digits.index(char) * (in_base ** place)
        place += 1
    return out_num

def from_decimal(number, out_base):
    out_num = ""
    while True:
        remainder = number%out_base
        out_num = digits[remainder] + out_num
        number //= out_base
        if number == 0:
            break
    return out_num

def num_handling(number):
    while True:
        try:
            int(number)
        except:
            print("That's not really a number. Please input a NUMBER: ", end="")
        else:
            if 2 <= int(number) <= 36:
                return int(number)
            else:
                print("That number's not in the range. Please input a number in the RANGE: ", end="")
        number = input("")

print("I am the HEXORCIST! Prepare to be HEXORCISED!\n")
in_base = num_handling(input("What base number system are you starting from? (2-36) "))
out_base = num_handling(input("What base number system are you converting to? (2-36) "))
in_num = input(f"What's the number you want to convert? (0-{digits[in_base - 1]} per digit) ").upper()
while True:
    exit = True
    for char in in_num:
        if char not in digits.split(digits[in_base])[0]:
            in_num = input("That's not valid in this base system. Please reenter a correct number: ").upper()
            exit = False
    if exit:
        break

dec_num = to_decimal(in_num, in_base)
out_num = from_decimal(dec_num, out_base)

print(f"\n{in_num} in base {in_base} is equal to {out_num} in base {out_base}")
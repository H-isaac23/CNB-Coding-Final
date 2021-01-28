def decimal_to_other(num, base):
    digits = "0123456789ABCDEF"
    num_digits = int(num)
    rems = []

    while num_digits != 0:
        rems.insert(0, digits[num_digits % int(base)])
        num_digits //= int(base)

    return "".join(rems)


def other_to_decimal(num, base):
    digits = "0123456789ABCDEF"
    digit_vals = [x for x in digits]
    num_digits = [x for x in num]
    exp = 0
    sum_digits = 0

    for i in range(len(num_digits) - 1, -1, -1):
        sum_digits += digit_vals.index(num_digits[i]) * (int(base) ** exp)
        exp += 1

    return sum_digits

def bin_to_other(num, base):
    digits = "0123456789ABCDEF"
    num_digits = [x for x in num]
    bits = []
    bit_group = []
    new_num_digits = []

    sig_bits = 4 if base == "16" else 3

    for i in range(len(num_digits)-1, -1, -1):
        bit_group.insert(0, num_digits[i])
        if len(bit_group) == sig_bits or i == 0:
            bits.insert(0, "".join(bit_group))
            bit_group = []

    for i in range(len(bits)-1, -1, -1):
        index = other_to_decimal(bits[i], 2)
        new_num_digits.insert(0, digits[index])

    new_digit = "".join(new_num_digits)

    return(new_digit)


def other_to_binary(num, base):
    digits = "0123456789ABCDEF"
    num_digits = [x for x in num]
    indices = []
    bits = []

    for x in num_digits:
        indices.append(digits.index(x))

    for i in range(len(indices)-1, -1, -1):
        sig_bits = 4 if base == "16" else 3
        bit = decimal_to_other(indices[i], 2)

        if len(bit) != sig_bits:
            touch = [x for x in bit]
            while len(touch) < sig_bits and i != 0:
                touch.insert(0, "0")
            bit = "".join(touch)
        bits.insert(0, bit)

    return "".join(bits)

def is_base(num, base):
    digits = "0123456789ABCDEF"
    sliced_digits = digits[:int(base)]
    for x in num:
        if x not in sliced_digits:
            print(f"The digit you entered is not in base {base}.")
            return False
    return True


from_base = input("What base do you want to convert from? ")
to_base = input("What base do you want to convert to? ")
num = input("Enter the number: ")
converted_digit = 0

if is_base(num, from_base):
    if from_base == "2":
        if to_base == "8" or to_base == "16":
            converted_digit = bin_to_other(num, to_base)
        else:
            converted_digit = other_to_decimal(num, from_base)
    elif from_base == "10":
        converted_digit = decimal_to_other(num, to_base)
    elif from_base == "8" or from_base == "16":
        if to_base == "10":
            converted_digit = other_to_decimal(num, from_base)
        else:
            converted_digit = other_to_binary(num, from_base)
    else:
        converted_digit = other_to_binary(num, to_base)

print(f"The converted digit is: {converted_digit}")


# decimal_to_other(111, 2)
# print(other_to_decimal("1101111", 2))
# bin_to_other("1010000001011100011", 16)
# print(other_to_binary("9F2", 16))
# print(is_base("1012", 2))

def decimal_to_other(num, base):
    digits = "0123456789ABCDEF"
    num_digits = int(num)
    rems = []

    while num_digits != 0:
        rems.insert(0, digits[num_digits % base])
        num_digits //= base

    print("".join(rems))
    return "".join(rems)


def other_to_decimal(num, base):
    digits = "0123456789ABCDEF"
    digit_vals = [x for x in digits]
    num_digits = [x for x in num]
    exp = 0
    sum_digits = 0

    for i in range(len(num_digits) - 1, -1, -1):
        sum_digits += digit_vals.index(num_digits[i]) * (base ** exp)
        exp += 1

    return sum_digits

def bin_to_other(num, base):
    digits = "0123456789ABCDEF"
    num_digits = [x for x in str(num)]
    bits = []
    bit_group = []
    new_num_digits = []

    sig_bits = 4 if base == 16 else 3

    for i in range(len(num_digits)-1, -1, -1):
        bit_group.insert(0, num_digits[i])
        if len(bit_group) == sig_bits or i == 0:
            bits.insert(0, "".join(bit_group))
            bit_group = []

    for i in range(len(bits)-1, -1, -1):
        index = other_to_decimal(bits[i], 2)
        new_num_digits.insert(0, digits[index])

    new_digit = "".join(new_num_digits)
    print(new_digit)
    return(new_digit)


# decimal_to_other(111, 2)
# other_to_decimal("1101111", 2)
bin_to_other(1010000001011100011, 16)

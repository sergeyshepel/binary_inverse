input_data = [1, 0, 0, 1]

def get_decimal_represent(binary_represent):
    decimal_represent = 0
    for i, digit in enumerate(binary_represent):
        decimal_represent = decimal_represent + digit * pow(-2, i)
    print "decimal value = %s" % decimal_represent
    return decimal_represent

def invert_decimal_represent(decimal_represent):
    inverted_decimal = decimal_represent * -1
    print "inverted value = %s" % (inverted_decimal)
    return inverted_decimal

def get_the_shortest_represent(inverted_decimal):
    digits = []
    if not inverted_decimal:
        digits = ['0']
    else:
        while inverted_decimal != 0:
            inverted_decimal, remainder = divmod(inverted_decimal, -2)
            if remainder < 0:
                inverted_decimal, remainder = inverted_decimal + 1, remainder + 2
            digits.append(str(remainder))
    print "output = %s" % map(int, digits)

get_the_shortest_represent(invert_decimal_represent(get_decimal_represent(input_data)))
def get_initial_data():
    """ Get initial data """
    input_string = ''
    while not input_string:
        input_string = raw_input('Enter sequence of digits separated by comma: ')
    input_data = map(int, input_string.split(','))
    print "input data: %s" % input_data
    return input_data

def binary_inverse(initial_data):
    # Convert initial data into decimal representation
    decimal_represent = 0
    for i, digit in enumerate(initial_data):
        decimal_represent = decimal_represent + digit * pow(-2, i)
    print "decimal value = %s" % decimal_represent
    # Invert decimal representation
    inverted_decimal = decimal_represent * -1
    print "inverted value = %s" % (inverted_decimal)
    # Convert inverted decimal representation into negabinary
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
    return map(int, digits)

# main
binary_inverse(get_initial_data())
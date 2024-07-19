def convert(unsigned_int_x, base):
    x_type = type(unsigned_int_x)
    base_type = type(base)

    if x_type != int:
        raise TypeError("x is not an integer")
    if base_type != int:
        raise TypeError("base is not an integer")
    if unsigned_int_x < 0:
        raise ValueError("x must be positive")
    if base < 2:
        raise ValueError("base cannot be less than 2")

    result_list = []

    while unsigned_int_x > 0:
        remainder = unsigned_int_x % base
        result_list.append(remainder)

        # Repeatedly divide the number x by the base b
        unsigned_int_x = unsigned_int_x // base

    # Reverse the list to get the highest-order coefficient first
    result_list.reverse()

    return result_list


# print(convert(1234, 10))
# print(convert(4660, 16))


def hexstring(x):
    """
    Converts an unsigned integer x into a string representing the hexadecimal representation of x
    """
    x_type = type(x)

    if x_type != int:
        raise TypeError("x is not an integer")
    if x < 0:
        raise ValueError("x must be positive")
    # Convert the integer to hexadecimal representation
    hex_digits = "0123456789ABCDEF"
    coefficients = convert(x, 16)  # Get base-16 (hexadecimal) coefficients
    print(coefficients)

    # Build the hexadecimal string
    hex_string = "0x" + "".join(hex_digits[digit] for digit in coefficients)

    return hex_string


# print(hexstring(1234))
def decodedate(x):
    # Extract the month
    month = (x & 0xF0000000) >> 28

    # Extract the day
    day = (x & 0x0F800000) >> 23

    # Extract the year
    year = x & 0x007FFFFF

    # Format the result as 'dd.mm.yyyy'
    return f"{day}.{month}.{year}"


# Example usage:
# print(decodedate(1375733729))  # Output: 4.5.2017


def encodedate(day, month, year):
    # Check validity of inputs
    if not (1 <= month <= 12):
        raise ValueError("invalid month")
    if not (1 <= day <= 31):
        raise ValueError("invalid day")
    if not (0 <= year <= 2**23 - 1):
        raise ValueError("invalid year")

    # Encode month (4 bits)
    m_encoded = (month & 0xF) << 28

    # Encode day (5 bits)
    d_encoded = (day & 0x1F) << 23

    # Encode year (23 bits)
    y_encoded = year & 0x7FFFFF

    # Combine all fields
    encoded_value = m_encoded | d_encoded | y_encoded

    return encoded_value


# Example usage
print(encodedate(4, 5, 2017))  # Example test

def sequence_length(n):
    """Computes the Collatz sequence length of a given positive integer
    The Collatz sequence-length of n is the number of numbers generated in the Collatz
    sequence starting from n up to 1(including n and 1)
    """
    # Take any natural number n
    # if n is even, divide by 2 to get n/2
    # If n is odd, multiply by 3 and add 1 to obtain 3n + 1
    # No matter what number you start with you will always eventuallly reach 1
    if n == 1:
        return 1  # Return 1 when n is 1, as it's the only element in the sequence
    else:
        if n % 2 == 0:
            return 1 + sequence_length(n // 2)  # Recursively call sequence_length
        else:
            return 1 + sequence_length(3 * n + 1)  # Recursively call sequence_length


print(sequence_length(22))


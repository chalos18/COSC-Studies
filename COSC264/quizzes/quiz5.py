def value_from_db(db_value):
    NV= 1*(10**(db_value/10))
    return NV


# print(value_from_db(10))
# print(f"{value_from_db(16):.2f}")
# print(f"{value_from_db(-16):.4f}")t = np.linspace(0, len('10110001') * bit_duration, len('10110001') * bit_duration * sampling_rate)

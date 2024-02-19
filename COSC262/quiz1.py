def concatenate_list(strings):
    if len(strings) == 0:
        return ""
    else:
        return strings[0] + concatenate_list(strings[1:])


result = concatenate_list(["a", "b", "c", "d"])
print(result)

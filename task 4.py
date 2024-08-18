def convert_list_of_strings_to_integers(strings):
    integers = []
    for s in strings:
        try:
            integers.append(int(s))
        except ValueError:
            continue
    return integers

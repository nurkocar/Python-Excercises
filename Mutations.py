def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    new_string = ''.join(string_list)
    return new_string

print(mutate_string('abracadabra', 5, 'k'))
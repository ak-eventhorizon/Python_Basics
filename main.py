def mutate_string(string, position, character):
    listed_string = list(string)
    listed_string[position] = character
    mutated_string = ''.join(listed_string)
    return mutated_string

print(mutate_string('abracadabra', 5, 'k'))
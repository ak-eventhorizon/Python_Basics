from itertools import permutations as it_permutations


def permutations(string):
    permutation_obj = it_permutations(string)
    all_combinations = [''.join(p) for p in permutation_obj]
    no_duplicates_combinations = set(all_combinations)

    return list(no_duplicates_combinations)



if __name__ == '__main__':
    print(permutations('aabb'))

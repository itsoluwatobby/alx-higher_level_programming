#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    sample = list(a_dictionary.keys())[0]
    highest = a_dictionary[sample]
    for key, value in a_dictionary.items():
        if value > highest:
            highest = value
            sample = key
    return (sample)

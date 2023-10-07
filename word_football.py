def load_words(words):
    pairs_letters = []
    for word in words:
        first_letter = word[0]
        last_letter = word[-1]
        pairs_letters.append((first_letter, last_letter))
    
    return pairs_letters


def test_football_words(pairs, first_letter=None):
    if not first_letter:
        suitable_pairs = set(pairs)
    else:
        suitable_pairs = []
        for pair in set(pairs):
            if first_letter == pair[0]:
                suitable_pairs.append(pair)
                
    for pair in suitable_pairs:
        copy_pairs = pairs[:]
        copy_pairs.remove(pair)
        if test_football_words(copy_pairs, pair[1]):
            return True
    
    if not pairs:
        return True
    else:
        return False
    
    
def football_words(words):
    pairs = load_words(words)
    return test_football_words(pairs)


words = ["slama", "oko", "auto"] #zde se můžou dát náhodně slova 

print(football_words(words))



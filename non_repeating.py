def non_repeating(str):
    str = str.replace(' ','').lower()
    char_count = {}

    for c in str:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    all_uniques = []
    sort_chars = sorted(char_count.items(), key=lambda x: x[1])

    for item in sort_chars:
        if item[1] == sort_chars[0][1]:
            all_uniques.append(item)
    return all_uniques

print(non_repeating('I Apple Ape Peels'))
print(non_repeating('The quick brown fox jumped over the lazy dog and ate the cat'))

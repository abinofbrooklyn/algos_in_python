def unique(string):
    string = string.replace(' ','')
    characters = set()

    for letter in string:
        if letter in characters:
            return False
        else:
            characters.add(letter)

    return True

print(unique('a bsx eda'))
print(unique('a bsx ed'))

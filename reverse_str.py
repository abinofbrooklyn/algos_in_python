def reverse(s):
    spaces = [' ']
    words = []
    i = 0
    while i < len(s):
        if s[i] not in spaces:
            word_start = i
            while i < len(s) and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return "".join(reversed(s))

print(reverse("My name is ..."));


def rev(s):
    return s.split()[::-1]

print(rev("Hi, I like to eat Chinese food"));

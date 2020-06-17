MAPPING = ('0','1','ABC','DEF','GHI','JKL','MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonics(phone_number):
    def helper(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mneonics))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mneonics[digit] = c
                helper(digit + 1)
    mnemonics, partial_mneonics = [], [0] * len(phone_number)
    helper(0)
    return mnemonics

print(phone_mnemonics("2276696"))

import itertools

with open('p059_cipher.txt', 'r') as f:
    chars = [int(c) for c in f.readline().split(',')]

    letters = range(ord('a'), ord('z') + 1)
    perms = itertools.permutations(letters, 3)

    for perm in perms:
        passwords = itertools.cycle(perm)
        deciphered = []
        for c in chars:
            test = passwords.next()
            deciphered.append(c ^ test)
        text = ''.join(chr(d) for d in deciphered)
        if 'that' in text and 'or' in text and 'or' in text:
            print text
            print sum(deciphered)

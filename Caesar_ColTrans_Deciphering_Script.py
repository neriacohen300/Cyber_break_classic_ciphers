from src.hacker_tools import *


def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base +shift) % 26 + base)
            elif char.islower():
                base = ord('a')
                result += chr((ord(char) - base +shift) % 26 + base)
        else:
            result += char

    return result


def split_into_columns(text, n=5):
    L = len(text)
    base_len = L // n
    extra = L % n

    lengths = [base_len + 1 if i < extra else base_len for i in range(n)]
    cols = []
    index = 0
    for l in lengths:
        cols.append(text[index:index+l])
        index += l
    return cols



with open("enc/Caesar_ColTrans.txt", 'r') as f:
    text = f.read()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

min_score = chi_squared_score(calculate_letters_frequencies(text), ENGLISH_FREQ)
min_shift = 0

print(min_score)

for i in range(1,26):
    score = chi_squared_score(calculate_letters_frequencies(caesar_encrypt(text, i)), ENGLISH_FREQ)
    if score<min_score:
        min_score = score
        min_shift = i


newText = caesar_encrypt(text, min_shift)

Col5 = split_into_columns(newText)


count = 0
max_shared = 0
max_text = ""
print(max_shared)

for a in Col5:
    for b in Col5:
        if b == a:
            continue
        for c in Col5:
            if c in (a, b):
                continue
            for d in Col5:
                if d in (a, b, c):
                    continue
                for e in Col5:
                    if e in (a, b, c, d):
                        continue

                    perm = [a, b, c, d, e]

                    max_len = max(len(col) for col in perm)
                    candidate_text = ""
                    for i in range(max_len):
                        for col in perm:
                            if i < len(col):
                                candidate_text += col[i]

                    sharedT = compare_trigrams(get_top_trigrams(candidate_text), get_brown_top_trigrams())

                    if sharedT > max_shared:
                        max_shared = sharedT
                        max_text = candidate_text




with open("enc/DE_Caesar_ColTrans.txt", 'w') as f:
    f.write(max_text)

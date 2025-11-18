from src.hacker_tools import *
from ColTrans_Deciphering_Script import *


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



def main():
    with open("enc/Caesar_ColTrans.txt", 'r') as f:
        text = f.read()

    min_score = chi_squared_score(calculate_letters_frequencies(text), ENGLISH_FREQ)
    min_shift = 0

    print(min_score)

    for i in range(1,26):
        score = chi_squared_score(calculate_letters_frequencies(caesar_encrypt(text, i)), ENGLISH_FREQ)
        if score<min_score:
            min_score = score
            min_shift = i


    newText = caesar_encrypt(text, min_shift)


    with open("enc/DE_Caesar_ColTrans.txt", 'w') as f:
        f.write(ColTrans(newText))


main()
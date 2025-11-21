from pycipher import SimpleSubstitution
from src.hacker_tools import *
from src.caesar import *
from subbreaker import Breaker
import pkgutil
import json



with open("enc/SimpleSubstitution.txt", "r") as f:
    text = f.read()





text_freq = calculate_letters_frequencies(text)


text_freq_sorted = dict(sorted(text_freq.items(), key=lambda item: item[1], reverse=True))
english_freq_sorted = dict(sorted(ENGLISH_FREQ.items(), key=lambda item: item[1], reverse=True))

print(f"Text Freq: \n\n {text_freq_sorted}")
print(f"\n\nEnglish Freq: \n\n {english_freq_sorted}")


LIST_text_freq_sorted = list(text_freq_sorted)
LIST_english_freq_sorted = list(english_freq_sorted)


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetKEY = ""

for i in range(0, len(alphabet)):
    letter = alphabet[i]
    index = LIST_english_freq_sorted.index(letter)
    alphabetKEY += LIST_text_freq_sorted[index]


print(alphabetKEY)

#cipher = SimpleSubstitution(alphabetKEY.upper())
cipher = SimpleSubstitution(alphabetKEY.upper())
plaintext = cipher.decipher(text)


with open("enc/DE1_SimpleSubstitution.txt", "w") as f:
    f.write(plaintext)

print(plaintext[:500])


# Top trigrams
print("\nTop 20 trigrams in sample text:")
top_trigrams = get_top_vgrams(plaintext, 3, 50)
for trigram, count in top_trigrams:
    print(f"  {trigram}: {count}")


    # Compare with Brown corpus
print("\nComparing with Brown corpus trigrams...")
brown_trigrams = get_brown_top_vgrams(3, 50)
shared = compare_trigrams(top_trigrams, brown_trigrams)
print(f"  Shared trigrams: {shared}")

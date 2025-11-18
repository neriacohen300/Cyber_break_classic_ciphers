from src.hacker_tools import *
from pycipher import Autokey
from src.caesar import *

def decipher(text):
    count = 0
    parent_key = "AAAAA"

    for i in range(0,5):
        cipher = Autokey(parent_key)
        min_score = chi_squared_score(calculate_letters_frequencies(cipher.decipher(text)), ENGLISH_FREQ)
        bestKey = "AAAAA"
    
        for j in range(1,26):
            new_first = caesar_encrypt(text[i], j)  # encrypt first letter with shift i
            new_key = parent_key[:i] + new_first + parent_key[i+1:]  # combine with remaining letters
            cipher = Autokey(new_key)
            score = chi_squared_score(calculate_letters_frequencies(cipher.decipher(text)), ENGLISH_FREQ)
            count+=1
            print(count)

            if score<min_score:
                min_score = score
                bestKey = new_key

        parent_key = bestKey

        print(parent_key)

    return parent_key
                
    




def main():
    with open ("enc/Autokey.txt", "r") as f:
        text = f.read()

    # אם רוצים לעבור על הטקסט יותר מהר (יש סיכוי שזה יהיה פחות מדויק) אפשר לקחת רק חלק מהטקסט ולהריץ את זה עליו, ממה שאני בדקתי אפילו להריץ על ה500 אותיות הראשונות של הטקסט אפשר למצוא את המפתח, אבל בקוד השארתי את זה כרגע כלעבור על הכל
    key = decipher(text)
    cipher = Autokey(key)

    with open ("enc/DE_Autokey.txt", "w") as f:
        f.write(cipher.decipher(text))






    




main()
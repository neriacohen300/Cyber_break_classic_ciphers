from src.hacker_tools import *

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



def ColTrans(text):

    Col5 = split_into_columns(text)


    max_shared = 0
    max_text = ""

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

    return max_text

    



def main():
    with open("enc/ColTrans.txt", 'r') as f:
        text = f.read()

    with open("enc/DE_ColTrans.txt", 'w') as f:
        f.write(ColTrans(text))
    
    

main()




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
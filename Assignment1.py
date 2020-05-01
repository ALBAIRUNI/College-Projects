import sys


## Shift Cipher ##

def shift_enc(text, s):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result

def shift_dec(cipher_text, key):
    result = ""

    # transverse the plain text
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) - key - 65 + 26) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - key - 97 + 26) % 26 + 97)
        return result


## Affine Cipher ##

def affine_enc(text, a, b):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr(((ord(char) - 65) * a + b) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr(((ord(char) - 97) * a + b) % 26 + 97)
        return result


def affine_dec(text, a, b):
    result = ""

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Dncrypt uppercase characters in plain text

        if char.isupper():
            result += chr((((ord(char) - 65) - b) / a) % 26 + 65)
        # Dncrypt lowercase characters in plain text
        else:
            result += chr((((ord(char) - 97) - b) / a) % 26 + 97)
        return result


## vigenere Cipher ##


def vigenere_enc(text, key):
    cipher_text = []

    key = list(key)
    if len(text) == len(key):
        return (key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])

    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def vigenere_dec(cipher_text, key):
    orig_text = ""

    key = list(key)
    if len(cipher_text) == len(key):
        return (key)
    else:
        for i in range(len(cipher_text) - len(key)):
            key.append(key[i % len(key)])

    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)











def main():
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
    file1 = open(inputfile, "r")
    text = file1.read()

    if sys.argv[1] == "shift":
        if sys.argv[2] == "encrypt":
            s = int(sys.argv[5])
            file1 = open(outputfile, "w")
            file1.write(shift_enc(text, s))
            file1.close()
        elif sys.argv[2] == "decrypt":
            s = int(sys.argv[5])
            file1 = open(outputfile, "w")
            file1.write(shift_dec(text, s))
            file1.close()
    elif sys.argv[1] == "affine":
        if sys.argv[2] == "encrypt":
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            file1 = open(outputfile, "w")
            file1.write(affine_enc(text, a, b))
            file1.close()
        elif sys.argv[2] == "decrypt":
            a = int(sys.argv[5])
            b = int(sys.argv[6])
            file1 = open(outputfile, "w")
            file1.write(affine_dec(text, a, b))
            file1.close()
    elif sys.argv[1] == "vigenere":
        if sys.argv[5].isalpha():

            if sys.argv[2] == "encrypt":
                key = sys.argv[5]
                file1 = open(outputfile, "w")
                file1.write(vigenere_enc(text, key))
                file1.close()
            elif sys.argv[2] == "decrypt":
                key = sys.argv[5]
                file1 = open(outputfile, "w")
                file1.write(vigenere_dec(text, key))
                file1.close()


if __name__ == '__main__':
    main()

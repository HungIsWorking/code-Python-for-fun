def decrypt(alphabet, text, shift):
    print("Here is the encoded result: ", end = "")
    for i in text:
        indexAlphabet = alphabet.index(i)
        indexAlphabet -= shift
        if (indexAlphabet < 0):
            indexAlphabet += len(alphabet)
        print(alphabet[indexAlphabet], end ="")
    
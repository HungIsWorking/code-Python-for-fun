def encrypt(alphabet, text, shift):
    print("Here is the encoded result: ", end = "")
    for i in text:
        indexAlphabet = alphabet.index(i)
        indexAlphabet += shift
        if (indexAlphabet >= len(alphabet)):
            indexAlphabet -= len(alphabet)
        print(alphabet[indexAlphabet], end ="")
    
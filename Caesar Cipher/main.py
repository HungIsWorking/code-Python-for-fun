import TuanHung
import Encryption
import Decryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Encryption and Decryption tool!")
question = "yes"
def encryptAndDecrypt():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    if (direction == 'encode'):
        Encryption.encrypt(alphabet, text, shift)
    else:
        Decryption.decrypt(alphabet, text, shift)
    print("\n")   
    question = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()

while(question == "yes"):
    encryptAndDecrypt()
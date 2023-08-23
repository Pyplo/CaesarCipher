alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_word = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        shifted_letter = alphabet[letter_index + shift]
        encrypted_word += shifted_letter
    print(encrypted_word)

def decrypt(text, shift):
    decrypted_word = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        shifted_letter = alphabet[letter_index - shift]
        decrypted_word += shifted_letter
    print(decrypted_word)


if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text=text, shift=shift)



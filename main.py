from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
print(len(alphabet))
print(logo)


def caesar(text, shift, direction):
    final_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            shifted_index = letter_index + shift
            if shifted_index > len(alphabet):
                shifted_index %= len(alphabet)
            shifted_letter = alphabet[shifted_index]
            final_text += shifted_letter
        else:
            final_text += letter
    print(f"The {direction}d text is {final_text}")


end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text=text, shift=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

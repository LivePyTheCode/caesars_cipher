# Caesar Cipher
# Shifting Letters in the alphabet to encrypt a message
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d result is: {end_text}")


should_continue = True
while should_continue is True:
    direction = input("Type 'encode' to encrypt a message, type 'decode' to to decrypt a message:\n").lower()
    text = input("Type Your Message:\n").lower()
    shift = int(input("Type The Shift Number:\n"))
    shift = shift % 26
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Would you like to continue? type 'yes' to continue, or 'no' to stop.\n ")
    if result == 'no':
        should_continue = False
        print("Thanks for using Caesars Cipher. Goodbye.")

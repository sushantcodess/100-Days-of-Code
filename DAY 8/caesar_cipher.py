from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift > 26:
    shift = shift % 26

def caesar(direction, text, shift):
    caesar_text = ""
    if direction == "encode":
        shift = shift
    elif direction == "decode":
        shift = shift * - 1
    for i in text:
        if i not in alphabet:
            new_text = i
        else:
            text_index = alphabet.index(i) 
            text_position = text_index + shift
            new_text = alphabet[text_position]
        caesar_text += new_text
    print(f"The {direction}d text is {caesar_text}")
    

##################################################################################################################
caesar(direction=direction, shift=shift, text=text)

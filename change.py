alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def casear(start_text, shift_number, cipher_direction):
    end_text = ""
    if cipher_direction == "d":
        shift_number *= -1
        
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {cipher_direction} resoult {end_text}: ")

final = False
while not final:
    direction = input("Enter 'e' to encrypt, Enter 'd' to decrypt: ").lower()

    text = input("Enter massage: ").lower()
    #text = str('encoding=utf-8')
    shift = int(input("Enter cover number: "))

    shift = shift % 26
    
    casear(start_text=text, shift_number=shift, cipher_direction=direction)    

    restart = input("Enter 'Y' continue, Enter 'e' finish: ")
    if restart == 'e':
        final = True
        print("Bye")
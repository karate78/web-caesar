def alphabet_position(letter):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    lower_letter = letter.lower()
    for i in alpha:
        if lower_letter != i:
            count += 1
        else:
            return count
    return count
def rotate_character(char,rot):
    new_char = ""
    character = char.lower()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if character not in alpha:
        return character
    else:
        position =  alphabet_position(character)
        new_position = (position + (rot % 26)) % 26
        new_char += alpha[new_position]
        if char >= "A" and char <= "Z":
            new_char = new_char.upper()
            return new_char
        else:
            return new_char



def encrypt(text, rot):
    new_encrypt = ""
    for char in text:
        new_encrypt += rotate_character(char,rot)
    return new_encrypt

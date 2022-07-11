import string


def rotate_character(character, key):
    if character not in string.ascii_letters:
        return character

    alphalist = string.ascii_uppercase if\
        character.isupper() else\
        string.ascii_lowercase
    character_number = (alphalist.index(character) + key) % 26
    return alphalist[character_number]


def rotate(text, key):
    return ''.join([rotate_character(character, key) for character in text])

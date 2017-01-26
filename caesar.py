'''
Created on Jan 26, 2017

@author: Tax
'''
from string import ascii_uppercase


def alpha(indx):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_alpha = alpha.index(indx)
    return new_alpha


def encrypt(text, rot):
    encrypted_text = ''
    
    for char in text:
        encrypted_text += rotate_character(char, rot)
        
    return encrypted_text

def alphabet_position(letter):
    lower_letter = letter.lower()
    letter_index = alpha.index(lower_letter)
    
    return letter_index


def rotate_character(char, rot):
    alpha_key = 'abcdefghijklmnopqrstuvwxyz'
    is_upper = False
    
    try:
        upper_check = ascii_uppercase.index(char)
        is_upper = True
    except ValueError:
        pass
    
    char = char.lower()
    
    try:
        char_index = alpha(char)
    except ValueError:
        pass
        
    
    try:
        new_char_index = (char_index + rot) % 26
        new_char = alpha_key[new_char_index]
    except:
        new_char = char
        
    if is_upper:
        new_char = new_char.upper()
        
    return new_char
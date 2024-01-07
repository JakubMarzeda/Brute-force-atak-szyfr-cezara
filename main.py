import string
from config import english_alphabet_frequencies

def cesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr(((ord(char) - shift - 65) % 26) + 65)
            else:
                plaintext += chr(((ord(char) - shift - 97) % 26) + 97)
        else:
            ciphertext += char
    return ciphertext


def cesar_decrypt(ciphertext, shift):
    plaintext= ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr(((ord(char) - shift - 65) % 26) + 65)
            else:
                plaintext += chr(((ord(char) - shift - 97) % 26) + 97)
        else: 
            plaintext += char
    return plaintext


def letter_frequency(l, text):
    return text.count(l)


def cesar_brute_force(ciphertext):
    min_difference = float("inf")
    shift = 0
    alfabet = string.ascii_uppercase + string.ascii_lowercase

    for i in range(1, 26):
        plaintext = cesar_decrypt(ciphertext, i)
        total_difference = 0
        for letter in alfabet:
            observed_frequency = letter_frequency(letter, plaintext)
            excepted_frequency = english_alphabet_frequencies.get(letter, 0)
            difference = abs(observed_frequency / len(plaintext) - excepted_frequency)
            total_difference += difference
        if total_difference < min_difference:
            min_difference = total_difference
            shift = i
    return shift


ciphertext = "Kvtyez Jtyffcj Gzvinjqv Kvtyezbld Gifxirdzjkptqev n Gfcjtv qrgvnezrartv girbkptqev erltqrezv"
shift = cesar_brute_force(ciphertext)
print("Zaszyfrowany text: ", ciphertext)
print("Złamano szyfr klucz to: ", shift)
print("Odszyfrowany text: ", cesar_decrypt(ciphertext, shift))
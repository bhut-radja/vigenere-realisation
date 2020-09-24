#!/usr/bin/python3
import os
import modules.ecrypt as ecrypt

KEY_FILE = "./sources/key.ini"
INPUT_FILE = "./sources/input.txt"
OUTPUT_FILE = "./sources/output.txt"
ALPHABET = "./sources/alphabet.txt"
FORMAT_LIST = [' ', '\n', '\t', "", " ", '', '!', '?', '.', ',']


def clear():
    os.system("cls" if os.name == "nt" else "clear")
    return


# please, use basic English alphabet.
# Otherwise i really don't know. Just don't.
def get_alphabet():

    with open(ALPHABET, "r") as f:
        alphabet = f.read()

    return list(alphabet)


# for those who really likes read code and math: yes, it is not a matrix as is.
# i named it that way because for **me** it's more understandable. Thank you!
def alphabet_matrix(alphabet):

    matrix = dict()

    for letter in alphabet:
        matrix[str(letter)] = alphabet.index(letter)

    return matrix


def format_input(file):

    with open(file, "r") as f:
        message = f.read()

    message_list = list(message)

    for letter in message_list:
        if letter in FORMAT_LIST:
            message_list.remove(letter)

    return message_list


def to_integers(matrix, input_get):

    integers = list()

    for item in input_get:
        integers.append(matrix[str(item)])

    return integers


def input_to_key(input_int, key_int):

    l_i, l_k = len(input_int), len(key_int)

    if l_i == l_k:
        return input_int, key_int

    elif l_i > l_k:
        dif = l_i - l_k

        for i in range(dif):
            key_int.append(key_int[i])

        return input_int, key_int

    elif l_i < l_k:
        dif = l_k - l_i

        for i in range(dif):
            input_int.append(input_int[i])

        return input_int, key_int

    else:
        return False


# same case here.
def number_matrix(alphabet):
    num_matrix = dict()
    alpha_list = list(alphabet)

    for i in range(len(alphabet)):
        num_matrix[str(i)] = alpha_list[i]

    return num_matrix


def format_output(int_crypt, alphabet, num_matrix):

    crypt_list = list()
    letters = list()
    message = str()

    for item in int_crypt:
        if int(item) >= len(alphabet):
            item = item - len(alphabet)
        elif int(item) < 0:
            item = item + len(alphabet)
        crypt_list.append(item)

    for item in crypt_list:
        letters.append(num_matrix[str(item)])

    message = message.join(letters)
    return message


if __name__ == "__main__":

    clear()
    print("~ Vizhener")
    mode = int(input("~ decrypt[0]; crypt[1];\n~> "))

    if mode not in [0, 1]:
        quit("Invalid input.")

    alphabet = get_alphabet()
    matrix = alphabet_matrix(alphabet)
    num_matrix = number_matrix(alphabet)

    input_get = format_input(INPUT_FILE)
    key = format_input(KEY_FILE)

    word_crypt = to_integers(matrix, input_get)
    key_crypt = to_integers(matrix, key)

    to_key = input_to_key(word_crypt, key_crypt)

    if type(to_key) == tuple:
        int_input, int_key = to_key
    else:
        quit("Unexpected error in line (63 or 143)")

    if mode == 0:
        final = ecrypt.decrypt(int_key, int_input)
    else:
        final = ecrypt.crypt(int_key, int_input)

    crypto_output = format_output(final, alphabet, num_matrix)

    with open(OUTPUT_FILE, "w") as f:
        f.write(crypto_output)
    print("~> {}".format(crypto_output))
    exit()

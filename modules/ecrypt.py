# module for encryption and decryption


def crypt(int_key, int_input):

    message = list()
    for i, j in zip(int_key, int_input):
        message.append(j + i)

    return message


def decrypt(int_key, int_crypt):

    message = list()
    for i, j in zip(int_key, int_crypt):
        message.append(j - i)

    return message


if __name__ == "__main__":
    pass

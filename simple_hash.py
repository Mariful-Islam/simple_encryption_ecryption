# Very simple encryption and decryption function

encrypt_code = {
    'a': 45, 'b': 23, 'c': 21, 'd': 67, 'e': 54, 'f': 56, 'g': 13, 'h': 12, 'i': 17, 'j': 89, 'k': 31, 'l': 24, 'm': 25, 'n': 26, 'o': 27, 'p': 28, 'q': 29, 'r': 30, 's': 41, 't': 40, 'u': 42, 'v': 43, 'w': 44, 'x': 77, 'y': 46, 'z': 47,
    'A': 11, 'B': 15, 'C': 16, 'D': 18, 'E': 19, 'F': 20, 'G': 22, 'H': 32, 'I': 33, 'J': 34, 'K': 35, 'L': 36, 'M': 37, 'N': 38, 'O': 39, 'P': 48, 'Q': 49, 'R': 50, 'S': 51, 'T': 52, 'U': 53, 'V': 55, 'W': 57, 'X': 58, 'Y': 59, 'Z': 60, ' ': 99

}

decrypt_code = {
    '45': 'a', '23': 'b', '21': 'c', '67': 'd', '54': 'e', '56': 'f', '13': 'g', '12': 'h', '17': 'i', '89': 'j', '31': 'k', '24': 'l', '25': 'm', '26': 'n', '27': 'o', '28': 'p', '29': 'q', '30': 'r', '41': 's', '40': 't', '42': 'u', '43': 'v', '44': 'w', '77': 'x', '46': 'y', '47': 'z', '11': 'A', '15': 'B', '16': 'C', '18': 'D', '19': 'E', '20': 'F', '22': 'G', '32': 'H', '33': 'I', '34': 'J', '35': 'K', '36': 'L', '37': 'M', '38': 'N', '39': 'O', '48': 'P', '49': 'Q', '50': 'R', '51': 'S', '52': 'T', '53': 'U', '55': 'V', '57': 'W', '58': 'X', '59': 'Y', '60': 'Z', '99': ' '
}


def encryption(string):
    result = []
    for i in string:
        result.append(encrypt_code[i])

    result = "".join(map(str, result))
    return result

print(encryption())


def decryption(num):
    d_c = []
    result = []
    code = []
    for i in str(num):
        result.append(int(i))

    for i, j in zip(result[0::2], result[1::2]):
        code.append((i, j))

    ab = ["".join(map(str, a)) for a in code]
    for i in ab:
        d_c.append(decrypt_code[i])

    print("".join(d_c))


print(decryption())

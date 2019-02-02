# !/usr/bin/python3
import numpy as np
import string

def encrypt(msg):
    # Zastąp spacje nicością
    msg = msg.replace(" ", "X")#zamian wszystkich spacji na X w stringu msg
    msg = msg.replace(".", "Q")#zamiana wszystkich . na Q w stringu msg
    
    
    # Poproś o słowo kluczowe i zdobądź matrycę szyfrowania
    C = make_key()
    # Dopisz zero, jeśli wiadomość nie jest podzielna przez 2
    len_check = len(msg) % 2 == 0#ilość elementów
    if not len_check:
        msg += "0"
    # Wypełnij matrycę wiadomości
    P = create_matrix_of_integers_from_string(msg)
    # Oblicz długość wiadomości
    msg_len = int(len(msg) / 2)
    # Oblicz P * C
    encrypted_msg = ""


    for i in range(msg_len):
        # Dot product
        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
        # Modulate and add 65 to get back to the A-Z range in ascii
        '''row_0.append(" ")
        row_0.append("." )
        row_0.append("?")

        row_0.append(26)
        row_0.append(27)
        row_0.append(28)'''
        integer = int(row_0 % 29 + 65)
        
        # Change back to chr type and add to text
        encrypted_msg += chr(integer)
        # Repeat for the second column
        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(row_1 % 29 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg

def decrypt(encrypted_msg):
    # Ask for keyword and get encryption matrix
    C = make_key()
    # Inverse matrix
    determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]#wyznacznik macierzy
    determinant = determinant % 29#wyznacznik mod 29
    multiplicative_inverse = find_multiplicative_inverse(determinant)
    C_inverse = C
    # Swap a <-> d
    C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
    # Replace
    C[0][1] *= -1
    C[1][0] *= -1
    for row in range(2):
        for column in range(2):
            C_inverse[row][column] *= multiplicative_inverse
            C_inverse[row][column] = C_inverse[row][column] % 29

    P = create_matrix_of_integers_from_string(encrypted_msg)
    msg_len = int(len(encrypted_msg) / 2)
    decrypted_msg = ""
    
    for i in range(msg_len):
        # Dot product
        column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
        # Modulate and add 65 to get back to the A-Z range in ascii
        integer = int(column_0 % 29 + 65)
        # Change back to chr type and add to text
        decrypted_msg += chr(integer)
        # Repeat for the second column
        column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
        integer = int(column_1 % 29 + 65)
        decrypted_msg += chr(integer)
    if decrypted_msg[-1] == "0":
        decrypted_msg = decrypted_msg[:-1]
    return decrypted_msg

def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(29):
        inverse = determinant * i
        if inverse % 29 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse


def make_key():
     # Make sure cipher determinant is relatively prime to 26 and only a/A - z/Z are given
    determinant = 0
    C = None
    while True:
        cipher = input("Podaj min. 4 znakowy klucz: ")
        C = create_matrix_of_integers_from_string(cipher)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 29
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 29, uninvertible key")
        elif np.amax(C) > 29 and np.amin(C) < 0:
            print("Akceptowane są tylko znaki a-z")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C

def create_matrix_of_integers_from_string(string):
    # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M
    
def chr_to_int(char):
    # Uppercase the char to get into range 65-90 in ascii table
    char = char.upper()
    # Cast chr to int and subtract 65 to get 0-25
    integer = ord(char) - 65
    return integer

if __name__ == "__main__":
    msg = input("Text Jawny: ")
    encrypted_msg = encrypt(msg)
    print(encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg)
    decrypted_msg.replace("X", " ")
    decrypted_msg.replace("Q", ".")
    print(decrypted_msg.replace("X"," "))

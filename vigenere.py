def encrypt_vigenere(plaintext, shift):
    ciphertext = ""
    j = 0
    for i in plaintext:
        if ord(shift[j % len(shift)]) >= 65 and ord(shift[j % len(shift)]) <= 90:
            key = ord(shift[j % len(shift)]) - 65
        elif ord(shift[j % len(shift)]) >= 97 and ord(shift[j % len(shift)]) <= 122:
            key = ord(shift[j % len(shift)]) - 97
        if ord(i)>=65 and ord(i)<=90:
            i = chr((((ord(i) - 65) + key) % 26) + 65)
        if ord(i)>=97 and ord(i)<=122:
            i = chr((((ord(i) - 97) + key) % 26) + 97)
        ciphertext = ciphertext + i
        j = j + 1
    return ciphertext

def decrypt_vigenere(ciphertext, shift):
    plaintext = ""
    j = 0
    for i in ciphertext:
        if ord(shift[j % len(shift)]) >= 65 and ord(shift[j % len(shift)]) <= 90:
            key = ord(shift[j % len(shift)]) - 65
        elif ord(shift[j % len(shift)]) >= 97 and ord(shift[j % len(shift)]) <= 122:
            key = ord(shift[j % len(shift)]) - 97
        if ord(i)>=65 and ord(i)<=90:
            i = chr((((ord(i) - 65) - key) % 26) + 65)
        if ord(i)>=97 and ord(i)<=122:
            i = chr((((ord(i) - 97) - key) % 26) + 97)
        plaintext = plaintext + i
        j = j + 1
    return plaintext

user_choice = int(input("Press 0 to encrypt and 1 to decrypt message\n"))
user_text = input("Please input your text\n")
user_shift = input("Please input your shift\n")


if user_choice == 0:
    print (encrypt_vigenere(user_text,user_shift))
elif user_choice == 1:
    print(decrypt_vigenere(user_text,user_shift))
else:
    print("Wrong choice")

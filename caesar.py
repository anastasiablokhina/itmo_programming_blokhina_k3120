def encrypt_caesar(plaintext, shift):
    ciphertext = ""
    for i in plaintext:
        if ord(i)>=65 and ord(i)<=90:
            i = chr((((ord(i) - 65) + shift) % 26) + 65)
        if ord(i)>=97 and ord(i)<=122:
            i = chr((((ord(i) - 97) + shift) % 26) + 97)
        ciphertext = ciphertext + i
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    plaintext = ""
    for i in ciphertext:
        if ord(i)>=65 and ord(i)<=90:
            i = chr((((ord(i) - 65) - shift) % 26) + 65)
        if ord(i)>=97 and ord(i)<=122:
            i = chr((((ord(i) - 97) - shift) % 26) + 97)
        plaintext = plaintext + i
    return plaintext

user_choice = int(input("Press 0 to encrypt and 1 to decrypt message\n"))
user_text = input("Please input your text\n")
user_shift = int(input("Please input your shift\n"))

if user_choice == 0:
    print(encrypt_caesar(user_text,user_shift))
elif user_choice == 1:
    print(decrypt_caesar(user_text,user_shift))
else:
    print("Wrong choice")

import string

alphabet = string.ascii_lowercase
print(alphabet)

# eve wants to steal my password

# make my password secret

def decrypt(secret_message, key):
    decryption = ""
    for letter in secret_message:
        old_position = alphabet.find(letter)
        if old_position == -1:
            decryption += " "
        else:
            new_position = old_position - key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            decryption += new_letter
    print(key)
    return decryption

secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"

for key in range(26):
    print(decrypt(secret_message, key))
# Your task:
# figure out what key I used to encrypt this message:


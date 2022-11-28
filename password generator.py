#Pingluk GEN
import random
import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars
password_length = input ("longeur du mot de passe:")
while True:
    password = ''
    for i in range (int(password_length)):
        password +=''.join(secrets.choice(alphabet))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
            break

print(password)

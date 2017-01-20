"""
Simple implementation of symmetric-key encryption
Relies on cryptography's Fernnet
Docs: https://cryptography.io/en/latest/fernet/
"""
from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()

f = Fernet(secret_key)
# Binds input to raw_input to handle backwards compability between Python 2.x
# and 3.x
try:
    input = raw_input
except NameError:
    pass

message = input('Type a message you want to encrypt here: \n')

encrypted = f.encrypt(message)
print("Your message was: {}".format(message))
print("This became encrypted to: \n {}".format(encrypted))

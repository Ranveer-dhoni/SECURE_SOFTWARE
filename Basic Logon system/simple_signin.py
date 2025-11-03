#Import required modules 
import hashlib

def login():
    email = input("Please enter your email")
    pwd = input("Please enter a password: ")
    enc = pwd.encode()
    hash2 = hashlib.md5(enc).hexdigest()
    with open("credentials.txt", "r") as creds:
        stored_email, stored_pwd = creds.read().split("\n")
    if email == stored_email and hash2 == stored_pwd:
        print("Logon Successful!")
    else:
        print("Logon failed. \n")

login()
#Import required modules 
import hashlib

def sign_up():
    email = input("Please enter an email address: ")
    pwd = input("Please enter a password: ")
    conf_pwd = input("Enter the password again: ")
    if pwd == conf_pwd:
        enc = pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt","w",) as creds:
            creds.write(email + "\n")
            creds.write(hash1)
        print("You have successfully registered! ")
    else:
        print("The passwords do not match. \n")
        input("Press Enter To Continue.")
        sign_up()

sign_up()
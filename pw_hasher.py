import bcrypt

#Stored Password
password = input('Ranveer please reenter your password')

#Convert password into an array of bytes 
bytes = password.encode('utf-8')

#Generate the salt
salt = bcrypt.gensalt()

#Hash the password and salt
hash = bcrypt.hashpw(bytes, salt)

#Entered Password
entPassword = 'Password000'

#Convertent password into an array of bytes
entBytes=entPassword.encode('utf-8')

#Compare the passwords
result = bcrypt.checkpw(entBytes,hash)
print(result)


#Output the result/hash
#print(hash)

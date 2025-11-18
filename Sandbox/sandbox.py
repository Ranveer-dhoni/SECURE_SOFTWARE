#Create a restricted environment with limited 
#built in functions (whitelist)
restricted_env = {'__builtin__': {'print': print}}

#Safe code 
safe_code = 'print("Hello World")'

#Unsafe Code 
unsafe_coden = 'open("credentials.txt", "r")'

#Attempt to run safe code 
exec(safe_code, restricted_env)

#Attempt to run unsafe code 
try:
    exec(unsafe_code, restricted_env)
except NameError as e:
    print(f"Error: {e}")
import re
MAX_INPUT_LENGTH = 20


def sanitise_input(name):
    return re.sub(r"[^a-zA-Z\s-]","",name).strip()

while True:
    try:
        num = int(input('Please enter an integer betweeen 1-10: '))
        if num <1 or num >10:
            print('Please enter an integer between 1-10')
        else:
            break
    except ValueError:
        print('Please input a valid integer')

while True:
    try:
        user_name = input('Please enter your username: ')
        san_name = sanitise_input(user_name)
        if len(san_name) > MAX_INPUT_LENGTH:
            print(f'Exceeds the max length of {MAX_INPUT_LENGTH} characters.')
        elif not san_name.strip():
            print('Username cannot be blank or whitespace.')
        else:
            break
    except ValueError:
        print('Please input a valid string.')

print(f'VaLid number {num}')
print(f'Valid name {san_name}')


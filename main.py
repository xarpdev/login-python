"""
Login Python Project using input, print, and conditionals by Santiago Fabián Quispe
"""

import time

username = 'xarpdev'
password = 'freesoftware'

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print("Access Granted")
    print('Please Wait')
    time.sleep(5)
    print('Ok... Loading...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    print('Alright you have security clearance. Pulling up the secret mainframe.')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('You might wanna check both fields...')
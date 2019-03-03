#!/bin/python3

import random

print('''
====================================
Secure Password Generator

A Recommded Password length is 8 characters
====================================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*():;.,?0123456789'

number = input('How many passwords would you like?')
number = int(number)

length = input('How long would you like it?')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)

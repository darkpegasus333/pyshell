#I'm bored. I'm going to write a python shell.
import os
import sys


def help():
    print('''This thing doesn't do a whole lot yet. We'll fix that.
          This is the only function available currently''')

#first things first, we need a prompt.
#fix later so that I can edit it from a config file
prompt = ">"
PATH = "/usr/bin/"

try:
    while True:
        command = input(prompt)
        if command:
            if command == 'help':
                help()
except EOFError:
    #exit gracefully if user ctrl+D
    pass

#I'm bored. I'm going to write a python shell.
import os
import sys
from subprocess import call

#we'll hardcode these for right now
prompt = ">"
PATH = "/usr/bin/"
#####

#this is apparently useless with 'call' get rid of it soon?
#changed my mind. Keeping it. Could be useful.
#maybe for the first run ever? Cache the PATH afterwards?
programs = {}
dirs_in_path = PATH.split(":")
for dir in dirs_in_path:
    for item in os.listdir(dir):
        programs[item] = dir + item



def help():
    print('''This thing doesn't do a whole lot yet. We'll fix that.
          This is the only function available currently''')

try:
    while True:
        curr_dir = os.getcwd()
        command = input(curr_dir + prompt)
        if command:
            pieces = command.split(" ")

            #replace some shell builtins
            if pieces[0] == 'help':
                help()
            elif pieces[0] == 'cd':
                os.chdir(pieces[1])
            else:
                try:
                    if pieces[0] in programs:
                        pieces[0] = programs[pieces[0]] #do a switcheroo for the full path.
                    call(pieces)
                except FileNotFoundError:
                    print("This is not a command I recognize.")
                    #raise
                except KeyboardInterrupt:
                    print("\n")
                    print("You killed it :(")
except (EOFError,KeyboardInterrupt):
    #exit gracefully if user ctrl+D/ctrl+C
    print("\n")

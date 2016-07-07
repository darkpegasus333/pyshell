#I'm bored. I'm going to write a python shell.
import os
import sys
from subprocess import call
import subprocess


#we'll hardcode these for right now
prompt = ">"
PATH = "/usr/bin/"
PWD = os.getcwd() #previous working directory
#####

#this is apparently useless with 'call' get rid of it soon?
#changed my mind. Keeping it. Could be useful.
#maybe for the first run ever? Cache the PATH afterwards?
programs = {}
dirs_in_path = PATH.split(":")
for dir in dirs_in_path:
    for item in os.listdir(dir):
        programs[item] = dir + item

def cd(dir):
    if dir.startswith('~'):
        dir = dir.replace('~', os.path.expanduser('~'))

    if os.path.isdir(dir):
        PWD = os.getcwd()
        os.chdir(dir)
    else:
        print('That directory does not exist')

def forloop(stuff):
    stuff.remove('in') #we don't need it
    var = stuff[0]
    sub_proc=[]
    for x in stuff[1:]:
        if x != ":":
            sub_proc.append(x)
        else:
            break
    print(sub_proc)




def execute(command, stdout=None):
    command = command.split(" ")

    #replace some shell builtins
    if command[0] == 'help':
        help()
    elif command[0] == 'cd':
        cd(command[1])
    elif command[0] == 'for':
        forloop(command[1:]) #get rid of 'for' and send the rest.
    elif command[0] == "echo":
        print(command[1:])
    else:
        try:
            if command[0] in programs:
                command[0] = programs[command[0]] #do a switcheroo for the full path.
            call(command)
        except FileNotFoundError:
            print("This is not a command I recognize.")
            #raise
        except KeyboardInterrupt:
            print("\n")
            print("You killed it :(")

def help():
    print("""This thing doesn't do a whole lot yet. So far you can run programs
    like you normally would in, say, Bash. Right now only basic commands work. I
    mean *basic*, basic. There is no piping, looping, or flow control (if-then statements).
    That's coming (probably)! Also, no tab-completion.

    Why am I spending all my time writing a help that no one will use? I'm desperately
    avoiding working on the functions in the previous paragraph, of course!
    """)



if __name__ == '__main__':
    try:
        while True:
            curr_dir = os.getcwd()
            command = input(curr_dir + prompt)
            if command:
                execute(command)
    except (EOFError,KeyboardInterrupt):
        #exit gracefully if user ctrl+D/ctrl+C
        print("\n")

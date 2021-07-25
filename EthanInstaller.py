#iiClient Installer for 1.16.5

# Imports
import sys
import os
from os import path
import shutil

# Instructions
print('iiClient Installer for 1.17.1')
print('Modpack by Agent256#2000')

# Asks for installation path
destPath = ''
if len(sys.argv) == 2:
    destpath = sys.argv[1]
else:
    print('Please type in the full filepath of your .minecraft folder:')
    destpath = input()

# Verifies installation path legitimacy
isdir = os.path.isdir(destpath)
if not isdir:
    print(f'[ERROR]\tLooks like \"{destpath}\" is not a valid folder. Please check for any typos!')
    print('[INPUT]\tPress any key to exit...')
    input()
    sys.exit()
else:
    print('[LOG]\t' + destpath + ' is a valid directory')

    # User confirms install path
    confirmedDir = False
    while confirmedDir == False:
        print(f'\n[INPUT]\tAre you sure you want to install to \"{destpath}\"? (Y\\N)')
        choice = input().lower()
        if choice == 'y':
            confirmedDir = True
        elif choice == 'n':
            print('\n[INPUT]\tPress any key to exit...')
            input()
            sys.exit()
        else:
            print('[ERROR]\tNot a valid choice, please try again!')

# Makes sure the resources folder exists
sourcepath = path.abspath(path.join(path.dirname(__file__), 'resources'))
if not os.path.isdir(sourcepath):
    print('[ERROR]\tCan\'t find the resources folder, make sure it\'s in the same folder as the installer or try redownloading the package.')
    print('\n[INPUT]\tPress any key to exit...')
    input()
    sys.exit()
else:
    print('[LOG]\tValidated resource directory')

# Copies files from resources folder to install path
print('\n')
for subdir, dirs, files in os.walk(sourcepath):
    for filename in files:
        filepath = subdir + os.sep + filename
        destination = subdir.replace(sourcepath, '')
        os.makedirs(destpath + destination, exist_ok=True)
        fulldestpath = destpath + destination + os.sep + filename
        shutil.copyfile(filepath, fulldestpath)
        print(f'[LOG]\tCopied {destination} to {fulldestpath}')

# success message
print('\n[LOG]\tiiClient has been installed, enjoy!')
print('\n[CREDIT]\tInstaller made by ablazingeboy#7375')
print('\n[INPUT]\tPress any key to exit...')
input()
sys.exit()

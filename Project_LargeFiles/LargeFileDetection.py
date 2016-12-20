#! python3
# LargeFileDetection.py - walks through a directory looking for files larger than 100MB and prints them to the screen.

import os
import sys

# Get the directory from the user
while True:
    userInput = input('Enter the directory to search:\n')
    if userInput.lower() == 'quit':
        sys.exit(1)
    else:
        userInput = os.path.abspath(userInput)
        if os.path.isdir(userInput):
            break
        else:
            print('Invalid path. Please try again. Type "quit" to stop program.')
            continue

# Walks the directory adds files to list after comparing.
largeFiles = []
number = 1
for folder, subfolders, filenames in os.walk(userInput):
    for filename in filenames:
        if os.path.getsize(os.path.join(folder, filename)) > 100e6:
            largeFiles.append((number,
                               '{} MB'.format(round(os.path.getsize(os.path.join(folder, filename)) / 1e6, 0)),
                               os.path.join(folder, filename)
                               ))
            number += 1

for file in largeFiles:
    print(file)
print('Done.')

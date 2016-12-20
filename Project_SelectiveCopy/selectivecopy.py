#! python3
# selectivecopy.py - copies all files of a specified extension (i.e. .jpg or .pdf) through a directory tree to a
# given directory.

import os
import shutil
import pprint

# TODO: Check for files paths that would exceed maximum length in future version.

# Get the extension from the user
extensionInput = input('Enter the extension (ex: .pdf): ').strip('.')

# Get the source and destination folder from the user
while True:
    sourceInput = os.path.abspath(input('Enter the path of the folder to copy:\n'))
    if os.path.exists(sourceInput):
        break
    else:
        print('The path entered was not valid. Try again. Press ctrl-c to quit')
        continue
while True:
    destinationInput = os.path.abspath(input('Enter the path of the destination:\n'))
    if os.path.exists(destinationInput):
        break
    else:
        print('The path entered was not valid. Try again. Press ctrl-c to quit')
        continue

# Build list of file paths to copy
copyList = []

for foldername, subfolders, filenames in os.walk(sourceInput):
    for filename in filenames:
        if str(filename).endswith(extensionInput):
            copyList.append(os.path.join(foldername, filename))

# Loop through list moving files.
print('Copying these files:')
pprint.pprint(copyList, width=200)


# Get the number and size of all files to be copied (not required in project description)
totalSize = 0
for file in copyList:
    totalSize += os.path.getsize(file)
print(str(len(copyList)) + ' files will be copied. {} KB Total Do you wish to continue? [y/n]'.format(round(
    totalSize/1000, 0
)))
confirmInput = input()

if confirmInput.lower() in ['y', 'yes']:
    # Copy the list of files to destination
    for file in copyList:
        shutil.copy(file, destinationInput)
    print('Done.')
elif confirmInput.lower() in ['n', 'no']:
    print('Canceled. No files were copied.')
else:
    print('Input not understood. Cancelling operation.')


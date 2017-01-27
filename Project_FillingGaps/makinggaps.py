#! python3
# makinggaps.py - Creates a gap in file suffix number at user chosen integer.
# to close the gap.

import os
import sys
import re
import pprint
import shutil

# Get prefix from user
userPrefix = input('Enter prefix to search: ')

# Get the gap number from user
while True:
    try:
        userGap = int(input('Enter an integer for gap: '))
    except ValueError:
        print('That was not an integer. Try again.')
        continue
    if type(userGap) == int:
        break


# Create number suffix regex
numRegex = re.compile('({})(?P<num>\\d+)(\\..*)'.format(userPrefix), re.IGNORECASE)

# Get directory to search from user
while True:
    searchPath = input('Enter the directory path to search:\n')
    if searchPath.lower() == 'quit': 	# option to exit the program
        sys.exit(1)
    else:				# error handling
        searchPath = os.path.abspath(searchPath)
        if os.path.isdir(searchPath):
            break
        else:
            print('The path was invalid. Try again or enter "quit" to exit the program.')
            continue

# Search for matching files
fileList = []
for item in os.listdir(searchPath):
    if os.path.isfile(os.path.join(searchPath, item)):
        mo = numRegex.search(item)
        if mo is not None:
            fileList.append([int(mo.group('num')), item])

fileList.sort(key=lambda pairs: pairs[0])   # to sort properly when number does not have leading zeros

# Print out the list to see search results
print('Matching files:')
pprint.pprint(fileList)

# Increment the file numbers for userGap and afterward by one
for i, x in enumerate(fileList):
    if fileList[i][0] >= userGap:
        fileList[i][0] += 1

# Print to check the renumbered list
print('Renumbered fileList:')
pprint.pprint(fileList)

# Create list of new names
renamedFileList = []
for item in fileList:
    renamedFileList.append(numRegex.sub(r'\g<1>{:03}\g<3>'.format(item[0]), item[1]))

# compare before and after names
print('\n{:*^45}'.format(' FILES TO BE RENAMED '))
for n in range(len(renamedFileList)):
    print('{:>15}{:^15}{:<15}'.format(fileList[n][1], '>>>>>>>', renamedFileList[n]))

# Confirm then proceed with renaming files
while True:
    userConfirm = input('\nDo you wish to proceed? [y/n]: ')
    if userConfirm.lower() == 'n':
        sys.exit(1)
    elif userConfirm.lower() == 'y':
        break
    else:
        print('Try again. Enter "n" to exit.')
        continue

# Rename the files
print('Renaming files...')
for n in range(len(renamedFileList)):
    shutil.move(os.path.join(searchPath, fileList[n][1]), os.path.join(searchPath, renamedFileList[n]))

print('Done.')

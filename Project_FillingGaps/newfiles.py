#! python3
# newfiles.py - creates txt files with sequential number ending for use in fillinggaps.py

for i in [x for x in range(20) if x not in [2, 4, 5, 15, 16, 19]]:
    filename = open('spam{}.txt'.format(i), 'w')
    filename.close()

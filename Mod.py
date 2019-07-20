#Purpose of this is to edit text files to create more organized structure.
#Following code capitalizes and saves to txt file.

import os
import numpy as np

os.chdir('D:\\Programming related\\Python Projects\\ProperNounFinder\\texts')
comNounList = []
nouns = []
modified = []

file2 = open('names.txt', 'r')
file3 = open('common nouns.txt', 'a+')

for word in file2:
    nouns.append(word)


modified = np.setdiff1d(comNounList, nouns)

for word in modified:
    file3.write('%s\n'% word)

removed = len(comNounList) - len(modified)
print ('original length', len(comNounList))
print ('took out ', removed)

# for word in file:
#     newword = word.lower()
#     file2.write('%s\n'% newword.capitalize())


#
# file = open('commonNoun.txt').read().splitlines()
#
# new = open('comNoun.txt', 'a+')
# for word in file:
#     new.write('%s\n'% word.capitalize())


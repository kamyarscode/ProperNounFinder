import numpy as np
import urllib.request
import re
import os

noNumbers = []
joinedList = []

def number_finder(wordList):                        #true if number in word
    return any(char.isdigit() for char in wordList)

def non_words(wordList):                            #true if entry has multiple uppercase letters
    return (sum(1 for word in wordList if word.isupper()))

def duplicate_finder(wordList):                     #function that will sort input list in alphabetical order
    no_doubles = list(set(wordList))
    sorted_list = sorted(no_doubles, key = str.lower)
    return sorted_list

#add as many links as desired
links = ['https://en.wikipedia.org/wiki/Timeline_of_Russian_interference_in_the_2016_United_States_elections',
         'https://en.wikipedia.org/wiki/Saudi_Arabian-led_intervention_in_Yemen',
         'https://en.wikipedia.org/wiki/2016%E2%80%9317_ISU_World_Standings_and_Season%27s_World_Ranking'
         ]
for link in links:
    page = urllib.request.urlopen(link)
    pageOpen = page.read().decode('utf-8')                      #used to decode wiki so we can scan through it
    found = re.findall(r'[a-zA-Z0-9]\s([A-Z]\w+)', pageOpen)    #finds any letter | number, then prints first word with
                                                                #cap letter after whitspace
    for word in found:
        joinedList.append(word)

outputSort = duplicate_finder(joinedList)


for word in outputSort:                                         #eliminate entries that aren't words
    if (non_words(word) == 1):
        if (number_finder(word) is False):
            noNumbers.append(word)

os.chdir('D:\\Programming related\\Python Projects\\ProperNounFinder\\texts')
nounList = open('common nouns.txt','r').read().splitlines()
comparedList = np.setdiff1d(noNumbers, nounList)
file = open('entries.txt', 'a+', encoding = 'utf-8')
for entry in comparedList:
   file.write('%s\n'% entry)


last = len(joinedList)
noNumberLength = len(noNumbers)
filteredOut = last - noNumberLength
finalLength = len(comparedList)

print ('This action is completed. Added a total of', finalLength, 'words.' )
print ('Filtered out a total of', filteredOut, 'entries')
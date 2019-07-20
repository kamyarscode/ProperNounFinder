<h1> Proper Noun Finder </h1>

Basically a very simple script that can look through websites and output any potential proper nouns into a text file.
The inspiration came from not knowing if a word needed to be capitalized. I looked for a massive list of proper nouns, but after not being able to find one I decided to try and make a script to do that for me. 


I attempted to minimalize false positives by ignoring any word that came after a period and white space, and only recorded words in the middle of sentences. I also used a giant list of common nouns to further filter any unwanted words. A huge portion of the list was from 
http://web.archive.org/web/20141205135208/http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt, but I ended up editing it for my specific needs. I tested the script by using the shortest Wikipedia articles I could find, then used the three biggest in the final phase and ended up with a little bit under 1800 words. 

The user is able to enter as many websites manually into the links variable in the SearchAndDestroy.py file. The words will be recorded in a entries.txt file. 


**NOTE:** This script is not yet able to output strings of more than one word, so some book titles, countries, companies, etc will be output with each word on a new line. ie United Arab Emirates will be: 

United

Arab

Emirates

<h1> To Do </h1>

* Add exceptions, make code more efficient, avoid errors!
* Create web crawler to automatically add entries 
* Compare results from this script to one that utilizes nltk.tag
* Create funtion to output strings longer than one word on same line. 

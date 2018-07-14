#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import inflect
s=inflect.engine()
total = 0

def characters(num):
    word = s.number_to_words(num)
    badchars = [","," ","-"]
    for i in badchars:
        word = word.replace(i, "")
    return len(word)
        
for i in range (1,1001):
    print(i, " - ", characters(i), " characters ")
    total += characters(i)
print(total, " Total Characters")

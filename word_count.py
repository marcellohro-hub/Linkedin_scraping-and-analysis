# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:39:21 2020

@author: marcellohro
"""
import os
os.chdir(r'C:\Users\marcellohro\Downloads\snippets')

import collections
import pandas as pd
import matplotlib.pyplot as plt

stopwords = open('stopwords_pt.txt', encoding='utf-8-sig', mode='r').read()
texto = open('texto.txt', encoding='utf-8-sig', mode='r').read()

#stopwords
stopwords=set(stopwords.split('\n'))
#stopwords = stopwords.union(set(['mr','mrs','one','two','said']))

# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in texto.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("!","")
    word = word.replace("...","")
    word = word.replace("/","")
    word = word.replace(";","")
    word = word.replace("?","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
            
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words 
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')
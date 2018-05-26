# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:22:03 2016

@author: surya

TO-DO
------
0.1 only handles rejected
0.2 url is there then remove url
0.3 replace all in between hashtags, #Q to Q 
0.4 english length less than threshold length rejected

//preprocessing
2.while checking in the text check
    2.1 if other than "not" from dictionary present as a word, discard tweet as
        that shows context(check for first three character)
3.check #A in last bunch of #tags 
    3.1 if not present in last bunch discard
    3.2 find the sentiment 
        3.2.1 if +ve and "not" is not present in the text then check for #A
        3.2.2 if -ve and "not" is present in the text then check for #A
        
"""

import nltk
sentence = """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
print tokens

tagged = nltk.pos_tag(tokens)
print tagged[0:6]

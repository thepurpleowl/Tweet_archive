# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 19:39:15 2016

@author: surya
"""
hashtag_dict = ['#kidding', '#not', '#notatall' , '#notreally' , '#joking' , 
         '#pretend', '#lying' ];
line="congrats to the proteas... win the test match and i will forgive you for 1999 world cup #kidding"
words=line.split()

print words

hashtag_dict_word_present=0

for j in range(len(words)):
    if words[j] in hashtag_dict:
        hashtag_dict_word_present=1
        break


print hashtag_dict_word_present  
            
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 22:20:59 2016

@author: surya
"""

import os
import json
import urllib

#sub_dir='/Documents'
filename ='demo.txt'
hashtag_dict = ['#kidding', '#not', '#notatall' , '#notreally' , '#joking' , 
         '#pretend', '#lying' ];
with open(filename) as f:
    for line in f:
        print line
        
        line=line[::-1]
        words=line.split()
        word_w_hashtag=0        
        
        tot_words=len(words)
        for index in range(tot_words):
            words[index] = words[index][::-1]

        for index in range(len(words)):
            print words[index]
            
        print 'no of words',words,'\n'
        print 'no of character',len(line),'\n'    
        
        tag_from_last=1
        #checking for hashtag_dict words at the end of tweet
        for index in range(tot_words-1):
            if words[index].startswith('#',0) and words[index+1].startswith('#',0) :
                word_w_hashtag += 1
                continue
            else:
                if(tag_from_last==1):
                    tag_from_last=0
                    word_w_hashtag += 1
                    continue
                else:
                    if words[index].startswith('#',0):
                        words[index] = words[index][1:]
        
        if words[tot_words-1].startswith('#',0):
            words[tot_words-1] = words[tot_words-1][1:]
        print words

        
        print word_w_hashtag
                
                
        
        
        
        
        

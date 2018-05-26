# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:15:15 2016

@author: surya
"""

from __future__ import division
import os
import json
import urllib
from textblob import TextBlob

#sub_dir='/Documents'
filename ='demo.txt'
hashtag_dict = ['#kidding', '#not', '#notatall' , '#notreally' , '#joking' , 
         '#pretend', '#lying', '#NotReally' ];
         
with open(filename) as f:
    for line in f:
        print line
        line = line.lower()
        words=line.split()
    
        #initializing numbers
        tot_words=len(words)
        
        hashtag_dict_word_present=0
        word_w_hashtag=0
        
        neg_word_exist=0
        
        negative_words=0
        positive_words=0
        neutral_words=0
        
        sarcastic_sent=0
        nsarcastic_sent=0
        rejected_sent=0
        
        #more than 140 character reject
        if len(line) > 140:
            rejected_sent +=1
            continue
        
        #reversing string wordwise
        line=line[::-1]
        words=line.split()
        
        for index in range(len(words)):
            words[index] = words[index][::-1]
        
        tag_from_last=1
        #checking for hashtag_dict words at the end of tweet
        for index in range(tot_words-1):
            if words[index].startswith('#',0) and words[index+1].startswith('#',0) :
                word_w_hashtag += 1
                continue
            else:
                if(tag_from_last==1):
                    tag_from_last=index
                    word_w_hashtag += 1
                    continue
                else:
                    if words[index].startswith('#',0):
                        words[index] = words[index][1:]
        
        if words[tot_words-1].startswith('#',0):
            words[tot_words-1] = words[tot_words-1][1:]
            
        #if english is less than threshold reject
        if tot_words-word_w_hashtag <4:
            rejected_sent +=1
            continue
            
        #checking for negation word
        never_='never' in words
        not_='not' in words
        if never_==True| not_==True:
            neg_word_exist=1
        else:
            neg_word_exist=0
            
        #checking in hashtag dictionary
        for j in range(len(words)):
            if words[j] in hashtag_dict:
                hashtag_dict_word_present=1
                break
            
        #sentiment analysis    
        
        #first approach fetching sentiment from online        
        """
            data = urllib.urlencode({"text": words[index]})     
            u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
            the_page = u.read()
            values = json.loads(the_page)
            label_ = values["label"]
        """
           
        for index in range(len(words)):
            testimonial = TextBlob(words[index])
            testimonial.sentiment
            label_=testimonial.sentiment.polarity

            if label_>0:
                positive_words +=1
            elif label_<0:
                negative_words +=1
            elif label_==0:
                neutral_words +=1
        
        if positive_words > negative_words:
            sentiment = 'positive'
        elif positive_words<negative_words:
            sentiment = 'negative'
        else :
            sentiment = 'neutral'
        
        
        print sentiment,'        '
        #checking for sarcasm
        if neg_word_exist==1:
            if sentiment=='positive':
                sentiment='negative'
            elif sentiment=='negative':
                sentiment='positive'
        
        sarcasm='not sarcastic'
        if sentiment=='positive':
            if hashtag_dict_word_present==1:
                sarcasm='sarcastic'
                sarcastic_sent +=1
            else:
                sarcasm='not sarcastic'
                nsarcastic_sent +=1
                
            
        #removing sentence with two pretend
        pretend_check= '#pretend' in words[0:tag_from_last+1]
        trendpretend_check= 'pretend' in words[tag_from_last+1:len(words)]
        
        if(pretend_check==True & trendpretend_check==True):
            sarcasm='not sarcastic'
            
        #print hashtag_dict_word_present            
        print sarcasm
        print "------------------------------------------------------------\n"
# with textblob
"""
with open(filename) as f:
    for line in f:
        print line
        words=line.split()
        for index in range(len(words)):
            testimonial= Textblob(words[index])
            print testimonial.sentiment.polarity
        print '\n'
"""

import re
import random
from nltk.corpus import wordnet
from nltk.tokenize import regexp_tokenize
import nltk.data
from textGenPython import TextGenPython
from genericpath import exists

class TextSpinGram():
    spinGram = TextGenPython()
    ''' this is an update of the text spin class
    
    This one will have the following qualities
        1. part of speech identification (so we only spin words of significance)
        tagset found at www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
        2. A conversation with an ngram model.
            NOTE: in practice, in chat, this model will probably be very large.
            For our purposes, testing will be done with crypto.txt
        3. No "spintax" generator because that is unnecessary
        
            
            
    Uses the Natural Language Toolkit (nltk)
        1. Uses the tokenizing library and pos identifier
        see www.nltk.org/book/ch05.html
        2. See TextGen, build similar beast
        
    Takes a line of text, and possibly an ngram model... Unsure
        
    '''
    

    
    def ngram(self, line):
        #Upon initialization, add the line to the ngram model
        self.spinGram.addline(line)
    
    
    def getSyns(self, word):
        synonyms = []
        #there needs to be a check here
        s = []
        try:
             #wordnet.synset(word[0]+'.'+word[1]+'.'+'01')
            syn = wordnet.synset(word[0]+'.'+word[1]+'.' +'01')
            #print syn
            for lemma in syn.lemma_names():
                if lemma != word[0]:
#                 since wordnet lemma.name will include _ for spaces, we'll replace these with spaces
                    w, n = re.subn("_", " ", lemma)
                #print lemma + " in side syn"
                    synonyms.append(w)
                s = list(set(synonyms))
        except Exception as e:
            print "Exception was: "+ str(e)
            #I don't actually want the exception
            #to print bc not every word combination
            #will have a lemma
        if len(s)==0:
            s = [word[0]]
        return s
          
          
    def splitToSentences(self, content):
        #tokenizes the message input into sentences
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        return tokenizer.tokenize(content)
    
    #will have to modify spin bc it takes the spintxed text
    
    #returns tuples containing the split words and their POS identification
    def splitToWords(self, content):
        tk  = nltk.tokenize.word_tokenize(content)
        pos = nltk.pos_tag(tk)
        return pos
    
    
    
    def spinIt(self, message):
        #MAIN USEFUL METHOD OF THE CLASS
        #SPLITS INTO SENTENCES< FOR EACH SENTENCE WORDS< 
        spunMes = ""
        a = self.splitToSentences(message)
        for i in range(len(a)):
            b = self.splitToWords(a[i])
            for j in range(len(b)):
                (x, y)=b[j]
                if(y.startswith('V')):
                    word = self.getSyns((x,'v'))
                    if len(word) > 1:
                        h = random.randint(0, len(word)-1)
                    else:
                        h = 0
                    word = ' '+word[h]
                    #verbs
                elif (y.startswith('J')):
                    word = self.getSyns((x, 'a'))
                    if len(word) > 1:
                        h = random.randint(0, len(word)-1)
                    else:
                        h = 0
                    print word
                    print h
                    word = ' '+word[h]
                    #adjectives
                elif (y.startswith('N')):
                    word = self.getSyns((x, 'n'))
                    h = random.randint(0, len(word)-1)
                    word = ' '+word[h]
                    #nouns
                elif (y == '.'):
                    word = x
                else:
                    word = ' '+x                
                spunMes = spunMes+ word
                #print spunMes
        return spunMes    
        
    
    


    
        
import string
import nltk
from nltk.corpus import stopwords
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer


def lower(row):

    '''A function that finds all uppercase letters in a row and converts them to lowercase.''' 
    
    return row.lower()

def remove_stopword(row):
    
    '''A function that finds all stopwords in a row and removes them.''' 
    row = row.translate(str.maketrans('', '', string.punctuation))
    stop = stopwords.words('english')
    new_row = []
    for i in row.split():
        if i not in stop:
            new_row.append(i)
    return ' '.join(new_row)

def remove_punctuation(row):

    '''A function that finds all punctuation a row and removes it.''' 

    return row.translate(str.maketrans('', '', string.punctuation))


def lemmatize(row):
        
    '''A function that replaces words with their base forms.''' 
    
    nlp = English()
    tokenize = Tokenizer(nlp.vocab)
    
    new_row = []
    for i in tokenize(row):
        new_row.append(i.lemma_)
    return ' '.join(new_row)

def remove_numbers(row):

    '''A function that finds all numbers a row and removes them.''' 
    
    return row.translate(str.maketrans('', '', string.digits))

class Process_Text_Data:
    
    def __init__(self):
        pass

    def transform(self, data, col='text', RNN=False):   
        
        data[col] = data[col].apply(lower)
        data[col] = data[col].apply(remove_punctuation)
        
        if RNN==False:
            data[col] = data[col].apply(remove_stopword)
            data[col] = data[col].apply(lemmatize)
            data[col] = data[col].apply(remove_numbers)


    
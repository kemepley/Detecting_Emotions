import string
import nltk
from nltk.corpus import stopwords
from spacy.lang.en import English
from spacy.tokenizer import Tokenizer

 # stopwords list modified from https://www.ranks.nl/stopwords
stopwords = ['a',
        'about',
        'above',
         'abst',
         'accordance',
         'according',
         'accordingly',
         'across',
         'actually',
         'added',
         'adj',
         'after',
         'afterwards',
         'again',
         'all',
         'almost',
         'also',
         'although',
         'am',
         'among',
         'amongst',
         'an',
         'and',
         'another',
         'any',
         'anybody',
         'anyhow',
         'anymore',
         'anyone',
         'anything',
         'anyway',
         'anyways',
         'anywhere',
         'apparently',
 'approximately',
 'are',
 'aren',
 'arent',
 'arise',
 'around',
 'as',
 'aside',
 'ask',
 'asking',
 'at',
 'auth',
 'available',
 'back',
 'be',
 'became',
 'because',
 'become',
 'becomes',
 'becoming',
 'been',
 'before',
 'beforehand',
 'being',
 'below',
 'beside',
 'besides',
 'between',
 'beyond',
 'both',
 'brief',
 'briefly',
 'but',
 'by',
 'ca',
 'came',
 'can',
 'com',
 'come',
 'comes',
 'contain',
 'containing',
 'contains',
 'could',
 'couldnt',
 'did',
 "didn't",
 'do',
 'does',
 "doesn't",
 'doing',
 'done',
 "don't",
 'down',
 'due',
 'during',
 'each',
 'edu',
 'eg',
 'eight',
 'eighty',
 'either',
 'else',
 'elsewhere',
 'et',
 'et-al',
 'etc',
 'even',
 'ever',
 'every',
 'everybody',
 'everyone',
 'everything',
 'everywhere',
 'ex',
 'except',
 'far',
 'few',
 'fifth',
 'first',
 'five',
 'followed',
 'following',
 'follows',
 'for',
 'former',
 'formerly',
 'forth',
 'found',
 'four',
 'from',
 'further',
 'furthermore',
 'go',
 'goes',
 'gone',
 'got',
 'gotten',
 'had',
 'happens',
 'has',
 "hasn't",
 'have',
 "haven't",
 'having',
 'he',
 'hed',
 'hence',
 'her',
 'here',
 'hereafter',
 'hereby',
 'herein',
 'heres',
 'hereupon',
 'hers',
 'herself',
 'hes',
 'hi',
 'him',
 'himself',
 'his',
 'hither',
 'how',
 'howbeit',
 'however',
 'hundred',
 'i',
 'id',
 'ie',
 'if',
 'i\'ll',           
 'im',
 'in',
 'inc',
 'indeed',
 'index',
 'information',
 'instead',
 'into',
 'invention',
 'is',
 "isn't",
 'it',
 'itd',
 "it'll",
 'its',
 'itself',
 "i've",
 'just',
 'keep',
 'keeps',
 'kept',
 'kg',
 'km',
 'know',
 'known',
 'knows',
 'largely',
 'last',
 'lately',
 'later',
 'latter',
 'latterly',
 'least',
 'less',
 'lest',
 'let',
 'lets',
 'like',
 'liked',
 'likely',
 'line',
 'little',
 "'ll",
 'look',
 'looking',
 'looks',
 'ltd',
 'made',
 'mainly',
 'make',
 'makes',
 'many',
 'may',
 'maybe',
 'me',
 'mean',
 'means',
 'meantime',
 'meanwhile',
 'mg',
 'might',
 'million',
 'ml',
 'more',
 'moreover',
 'mostly',
 'mr',
 'mrs',
 'much',
 'must',
 'my',
 'myself',
 'na',
 'name',
 'namely',
 'nd',
 'near',
 'nearly',
 'necessarily',
 'neither',
 'nine',
 'ninety',
 'nobody',
 'non',
 'none',
 'nonetheless',
 'noone',
 'nor',
 'normally',
 'nos',
 'noted',
 'nothing',
 'now',
 'nowhere',
 'obtain',
 'obtained',
 'obviously',
 'of',
 'off',
 'often',
 'oh',
 'old',
 'on',
 'once',
 'one',
 'ones',
 'only',
 'onto',
 'or',
 'ord',
 'other',
 'others',
 'otherwise',
 'ought',
 'our',
 'ours',
 'ourselves',
 'out',
 'outside',
 'over',
 'overall',
 'own',
 'page',
 'pages',
 'part',
 'particular',
 'past',
 'per',
 'perhaps',
 'placed',
 'plus',
 'pp',
 'predominantly',
 'present',
 'previously',
 'primarily',
 'probably',
 'provides',
 'put',
 'que',
 'quickly',
 'qv',
 'ran',
 'rather',
 'rd',
 're',
 'recent',
 'recently',
 'ref',
 'refs',
 'regarding',
 'regardless',
 'related',
 'relatively',
 'respectively',
 'resulted',
 'resulting',
 'results',
 'run',
 'said',
 'same',
 'saw',
 'say',
 'saying',
 'says',
 'sec',
 'section',
 'see',
 'seeing',
 'seem',
 'seemed',
 'seeming',
 'seems',
 'seen',
 'self',
 'selves',
 'sent',
 'seven',
 'several',
 'shall',
 'she',
 'shed',
 "she'll",
 'shes',
 'show',
 'showed',
 'shown',
 'showns',
 'shows',
 'similar',
 'similarly',
 'since',
 'six',
 'slightly',
 'so',
 'some',
 'somebody',
 'somehow',
 'someone',
 'somethan',
 'something',
 'sometime',
 'sometimes',
 'somewhat',
 'somewhere',
 'sorry',
 'specifically',
 'specified',
 'specify',
 'specifying',
 'still',
 'stop',
 'sub',
 'substantially',
 'sufficiently',
 'suggestsup',
 'sure',
 'take',
 'taken',
 'taking',
 'tell',
 'tends',
 'th',
 'than',
 'thanx',
 'that',
 "that'll",
 'thats',
 "that've",
 'the',
 'their',
 'theirs',
 'them',
 'themselves',
 'then',
 'thence',
 'there',
 'thereafter',
 'thereby',
 'thered',
 'therefore',
 'therein',
 "there'll",
 'thereof',
 'therere',
 'theres',
 'thereto',
 'thereupon',
 "there've",
 'these',
 'they',
 'theyd',
 "they'll",
 'theyre',
 "they've",
 'think',
 'this',
 'those',
 'thou',
 'though',
 'thoughh',
 'thousand',
 'throug',
 'through',
 'throughout',
 'thru',
 'thus',
 'til',
 'tip',
 'to',
 'together',
 'too',
 'took',
 'toward',
 'towards',
 'tried',
 'tries',
 'try',
 'trying',
 'ts',
 'twice',
 'two',
 'un',
 'under',
 'unfortunately',
 'unless',
 'unlike',
 'unlikely',
 'until',
 'unto',
 'up',
 'upon',
 'ups',
 'us',
 'use',
 'used',
 'usefully',
 'usefulness',
 'uses',
 'using',
 'usually',
 'various',
 "'ve",
 'via',
 'viz',
 'vol',
 'vols',
 'vs',
 'want',
 'wants',
 'was',
 'wasnt',
 'way',
 'we',
 'wed',
 'welcome',
 "we'll",
 'went',
 'were',
 'werent',
 "we've",
 'what',
 'whatever',
 "what'll",
 'whats',
 'when',
 'whence',
 'whenever',
 'where',
 'whereafter',
 'whereas',
 'whereby',
 'wherein',
 'wheres',
 'whereupon',
 'wherever',
 'whether',
 'which',
 'while',
 'whither',
 'who',
 'whod',
 'whoever',
 'whole',
 "who'll",
 'whom',
 'whomever',
 'whos',
 'whose',
 'why',
 'widely',
 'with',
 'within',
 'without',
 'wont',
 'would',
 'wouldnt',
 'www',
 'yet',
 'you',
 'youd',
 "you'll",
 'your',
 'youre',
 'yours',
 'yourself',
 'yourselves',
 "you've",
 'zero']


def lower(row):

    '''A function that finds all uppercase letters in a row and converts them to lowercase.''' 
    
    return row.lower()

def remove_stopword(row):
    
    '''A function that finds all stopwords in a row and removes them.''' 

    new_row = []
    
    for i in row.split():
        if i not in stopwords:
            new_row.append(i)
    return ' '.join(new_row)

def remove_punctuation(row):

    '''A function that finds punctuation a row and removes it, but keeps ? and !.''' 
    
    words = []
    punct = []

    for i in row.split():
        if '?' in i:
            punct.append('?')
        if '!' in i:
            punct.append('!')
        i_temp = i
        for j in "~`!@#$%^&*()_-+=/\,.<>?!":
            if j in i:
                i_temp = i_temp.replace(j, '')
        words.append(i_temp)
        
    return ' '.join(words + punct)


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


    
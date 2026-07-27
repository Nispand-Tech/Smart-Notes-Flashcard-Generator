from nltk.tokenize import sent_tokenize,word_tokenize

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer, WordNetLemmatizer


from nltk import pos_tag

import string

def split_into_sentences(text):
    sentences=sent_tokenize(text)
    return sentences


def clean_sentences(sentences):
    cleaned_sentences=[]

    for sentence in sentences:
        sentence=sentence.strip()

        if sentence:## equal to if sentence !="";
            ## checks whether the string is not empty
            cleaned_sentences.append(sentence)
        
    return cleaned_sentences

## make notes at last of this project and learned technologies


def tokenize_words(sentence):
    words=word_tokenize(sentence)
    return words


def remove_stopwords(words):
    stop_words=set(stopwords.words("english"))

    filtered_words=[]


    for word in words:
        if word.lower() not in stop_words:
            filtered_words.append(word)

    return filtered_words

    
def remove_punctuation(words):
    cleaned_words=[]


    for word in words:
        if word not in string.punctuation:
            cleaned_words.append(word)


    return cleaned_words
 


def stem_words(words):


    stemmer=PorterStemmer()

    stemmed_words=[]

    for word in words:

        stemmed_word=stemmer.stem(word)
        stemmed_words.append(stemmed_word)

    
 
    return stemmed_words


def lemmatize_words(words):

    lemmatizer=WordNetLemmatizer()

    lemmatized_words=[]

    
    for word in words:
        lemma=lemmatizer.lemmatize(word)
        lemmatized_words.append(lemma)



    return lemmatized_words



def pos_tag_words(words):

    tagged_words=pos_tag(words)
   
    return tagged_words




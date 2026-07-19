from nltk.tokenize import sent_tokenize,word_tokenize



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

from src.file_handler import read_text_file
from src.text_cleaner import (split_into_sentences,clean_sentences,tokenize_words,remove_stopwords,
remove_punctuation,stem_words,lemmatize_words, pos_tag_words)
from src.flashcard_generator import generate_flashcards
from src.entity_recognizer import extract_entities
from src.tfidf_keywords import extract_tfidf_keywords

def main():
    file_path="data/sample_notes.txt"

   ## Step1: Read the text file
    text=read_text_file(file_path)
  ##  Step 2: Split text into sentences
    sentences=split_into_sentences(text)

    ## Step 3: Clean the sentences
    cleaned_sentences=clean_sentences(sentences)

    ## Generate TF-IDF Keywords for all sentences
    tfidf_keywords_list=extract_tfidf_keywords(
         cleaned_sentences,
         top_n=3
    )
   
    print("\n ===========NLP PROCESSING ==========\n")

    for index, sentence in enumerate(cleaned_sentences):

         # Word Tokenization
         words=tokenize_words(sentence)
         # Stop-Word Removal
         filtered_words=remove_stopwords(words)
         # Remove Punctuation
         keywords=remove_punctuation(filtered_words)
         # Stemming
         stemmed_keywords=stem_words(keywords)
         # Lemmatization
         lemmatized_keywords=lemmatize_words(keywords)
         #POS Tagging
         tagged_keywords=pos_tag_words(lemmatized_keywords)
         
         ## Named Entity Recognition(spaCy)
         entities=extract_entities(sentence)

         ## Get TF-IDF Keywords of current sentence

         tfidf_keywords=tfidf_keywords_list[index]

         
         ## Display Processing Results
         print("Sentence:")
         print(sentence)

         print("\n Original Keywords:",keywords)

         print("\n Stemmed Keywords:",stemmed_keywords)

         print("\n Lemmatized Keywords:",lemmatized_keywords)

         print("\n POS Tags:",tagged_keywords)
         
         print("\n Named Entities:")
         
         if entities:
              for entity in entities:
                   print(f"{entity['text']}--->{entity['label']}")
         else:
            print("No named entites found.")


         print("\n Top TF-IDF Keywords:")
         print(tfidf_keywords)

         print("-"* 70)

      ## Use TF-IDF keywords for flashcards

    flashcards=generate_flashcards(
          cleaned_sentences,
          tfidf_keywords_list
          )



    print("\n Generate Flashcards:\n")

    
    for index, flashcard in enumerate(flashcards,start=1):
        print(f"Flashcard {index}")
        print(f"Question:{flashcard['question']}")
        print(f"Answer:{flashcard['answer']}")
        print(f"Keywords:{', '.join(flashcard['keywords'])}")
        print("-"*60)



if __name__=="__main__":
     main()
       
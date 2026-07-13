# def generate_flashcards(cleaned_sentences):
#     flashcards=[]

#     for sentence in cleaned_sentences:
#         flashcard= {
#             "question": "Explain the following sentence.",
#             "answer": sentence
#         }

#         flashcards.append(flashcard)


#     return flashcards


def generate_flashcards(cleaned_sentences):
    flashcards=[]

    for sentence in cleaned_sentences:
        #rule based NLP
        
        ## check if the sentence follows the pattern "X is Y"

        if " is " in sentence:
            subject,definition=sentence.split(" is ",1)

            flashcard={
                "question": f"What is {subject}?",
                "answer": definition.capitalize()
            }

        
        ## check if the sentence follows the pattern "X are Y"

        elif "are" in sentence:
            subject,definition=sentence.split("are",1)

            flashcard={
                "question":f" What are {subject}?",
                "answer":definition.capitalize()
            }

        
        ## Fallback for all other sentences

        else:
            flashcard= {
                "question":"Explain the following sentence:",
                "answer":sentence
            }


        flashcards.append(flashcard)

    return flashcards
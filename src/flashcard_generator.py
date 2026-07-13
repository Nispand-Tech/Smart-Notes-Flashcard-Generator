def generate_flashcards(cleaned_sentences):
    flashcards=[]

    for sentence in cleaned_sentences:
        flashcard= {
            "question": "Explain the following sentence.",
            "answer": sentence
        }

        flashcards.append(flashcard)


    return flashcards

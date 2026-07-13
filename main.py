from src.file_handler import read_text_file
from src.text_cleaner import split_into_sentences,clean_sentences
from src.flashcard_generator import generate_flashcards


def main():
    file_path="data/sample_notes.txt"


    text=read_text_file(file_path)
    sentences=split_into_sentences(text)
    cleaned_sentences=clean_sentences(sentences)
    flashcards=generate_flashcards(cleaned_sentences)


    print("\n Generate Flashcards:\n")

    
    for index, flashcard in enumerate(flashcards,start=1):
        print(f"Flashcard {index}")
        print(f"Question:{flashcard['question']}")
        print(f"Answer:{flashcard['answer']}")
        print("-"*50)




if __name__=="__main__":
       main()
       
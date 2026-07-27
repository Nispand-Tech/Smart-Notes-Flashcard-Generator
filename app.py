import streamlit as st
import csv
import io

## canvas, write on it,draw lines and place text while letter a pdf needs a paze size
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from src.text_cleaner import (
    split_into_sentences,
    clean_sentences
)


from src.tfidf_keywords import extract_tfidf_keywords

from src.flashcard_generator import generate_flashcards




def main():

    ## Configure Streamlit page
    st.set_page_config(
        page_title="Smart Notes Flashcard Generator",
        page_icon="🗃️",
        layout="wide"
    )

    st.markdown("""
    
    <style>
    /* Main Page */
     .main{
     padding-top:20px;
     }

     /* Title */

     h1{
        color:#0F62FE;
        text-align:center;
        font-weight:bold;
        }

    h2,h3
    {
    color:#1F2937;
    }
    /* Sidebar */

      section[data-testid="stSidebar"]
      {
      background-color:#F5F7FA;
      
      }

      /* Buttons */

      .stButton>button{
      
      width:100%;
      border-radius:12px;
      font-weight:bold;
      padding:12px;
      background-color:#0F62FE;
      color:white;
      }

      /* Download buttons */

      .stDownloadButton>button{
      width:100%
      border-radius:12px;
      font-weight:bold;
      }
     
     /* Expander */

     div[data-testid="stExpander"]summary{
     font-size:18px;
     font-weight:bold;
     }


     </style>
     """,unsafe_allow_html=True)
     
     
     
     
    

    ## CREATE SIDEBAR

    st.sidebar.title("🗃️ Smart Notes")

    st.sidebar.markdown("---")

    st.sidebar.header("🗄️About")

    st.sidebar.write(
        """
        This application generates intelligent flashcards from
        study notes using NLP techniques.
         Technologies Used:
          
        - Python
        - Streamlit
        - NLTK
        - spaCy
        - Scikit-learn
         """
    )


    ## ADD PROJECT STATISTICS

    st.sidebar.markdown("---")

    st.sidebar.header("📊Project Stastics")

    st.sidebar.metric(
        "NLP Techniques",
        "5"
    )

    st.sidebar.metric(
        "Libraries Used",
        "4"
    )

    st.sidebar.metric(
        "Supported File Type",
        ".txt"
    )

    ## ADD INSTRUCTIONS

    st.sidebar.markdown("---")

    st.sidebar.header("💡 Instructions")

    st.sidebar.write(
        """
        1. Paste Notes

        **OR**

        2. Upload a .txt file

        3. Click Generate Flashcards

        4. View generated flashcards
        """
    )

    ## ADD FOOTER

    st.sidebar.markdown("---")

    st.sidebar.caption(
        "Developed using 💗 with Python & Streamlit"
    )


    st.sidebar.markdown("---")

    ## Title

    st.title("🗃️ Smart Notes Flashcard Generator")

     ## Description

    st.write(
        "Generate intelligent flashcards using NLP techniques" 
        " such as Tokenization, POS Tagging, NER and TF-IDF."
    )

    st.divider()

    ## Text input

    st.subheader("📂 Paste your Notes")

    notes=st.text_area("Enter your notes here:",
                       height=250,
                       placeholder=("Example:\n Python is a programming language.\n"
                        " NLP is a branch of Artificial Intelligence."
                       )
                    )

    st.write("### OR")

    ## File Upload

    uploaded_file=st.file_uploader(
        "Choose a text file",
        type=["txt"]
    )

    st.divider()

   ## Generate Button

    generate=st.button("🛩️ Generate Flashcards")

    if generate:

       text=""

       ## Read text from Text Area

       if notes.strip():
           text=notes

       ## Read text from Uploaded File

       elif uploaded_file is not None:
           text=uploaded_file.read().decode("utf-8")

        ## No Input

       else:
           st.warning("Please enter notes or upload a text file.")
           st.stop()


        ## NLP Processing Pipeline

       

       with st.spinner("Generating flashcards ..."):

           sentences=split_into_sentences(text)

           cleaned_sentences=clean_sentences(sentences)

           tfidf_keywords_list=extract_tfidf_keywords(
               cleaned_sentences,
               top_n=3
           )

           flashcards=generate_flashcards(
              cleaned_sentences,
              tfidf_keywords_list
       )


       ## Display Results


       st.success("✅ Flashcards Generated Successfully!")

       st.divider()
       st.subheader("📝 Processing Summary")

       col1,col2,col3=st.columns(3)

       with col1:
           st.metric(
               "Sentences",
               len(cleaned_sentences)
           )

       with col2:
           st.metric(
               "Flashcards",
               len(flashcards)
           )

       with col3:

           total_keywords=sum(
               len(words)
               for words in tfidf_keywords_list
           )

           st.metric(
               "Keywords",
               total_keywords
           )


       st.divider()

       ## Display Flashcards

       st.header("🗃️ Generated Flashcards")


       for index, flashcard in enumerate(flashcards,start=1):

           with st.expander(f"🗒️ Flashcard {index}"):

               
               st.markdown(
                   "###  ❓ Question "
               )

               st.write(
                   flashcard["question"]
               )

               st.markdown(
                #    f"** Answer: ** { flashcard['answer']}"
                    "### ✅ Answer"
               )

               st.write(
                   flashcard["answer"]
               )


               st.markdown(
                #    f"** Keywords:**{','.join(flashcard['keywords'])}"
                    "### 🔑 keywords"
               )

               st.write(
                   " 🟠".join(flashcard["keywords"])

               )


       st.divider()

       st.header("📩 Download Flashcards")

      ## TXT CONTENT

       txt_content= ""

       for index,flashcard in enumerate(flashcards, start=1):

                   txt_content+=f"Flashcard{index}\n"
                   txt_content+=f"Question: {flashcard['question']}\n"
                   txt_content+=f"Answer:{flashcard['answer']}\n"
                   txt_content+="Keywords:"+",".join(flashcard["keywords"])+"\n"
                   txt_content+="-"*40+"\n\n"

      ## CSV CONTENT

       csv_buffer=io.StringIO()

       csv_writer=csv.writer(csv_buffer)



       csv_writer.writerow(
            [
                 "Flashcard Number",
                 "Question",
                 "Answer",
                 "Keywords"
            ]
        )


       for index,flashcard in enumerate(flashcards, start=1):

            csv_writer.writerow(
                 [
                      index,
                      flashcard["question"],
                      flashcard["answer"], ",".join(flashcard["keywords"])

                ]
            )


       pdf_buffer=io.BytesIO()

       pdf=canvas.Canvas(pdf_buffer,pagesize=letter)

       width,height=letter

       y=height-50

       pdf.setFont("Helvetica-Bold",18)
       pdf.drawString(150,y,"Smart Notes Flashcards")

       y-=40

       pdf.setFont("Helvetica",12)

       for index,flashcard in enumerate(flashcards,start=1):
            
                 pdf.drawString(50,y,f"Flashcard{index}")
                 y-=20

                 pdf.drawString(50,y,f"Question:{flashcard['question']}")
                 y-=20

                 pdf.drawString(50,y,f"Answer:{flashcard['answer']}")
                 y-=20

                 pdf.drawString(
                      50,
                      y,
                      "Keywords: "+",".join(flashcard["keywords"])
                 )

                 y-=30

                 pdf.line(50,y,550,y)

                 y-=30

                 ## Create a new page if the current one is full

                 if y<80:
                      pdf.showPage()
                      pdf.setFont("Helvetica",12)
                      y=height-50

       pdf.save()

       pdf_buffer.seek(0)
            
        ## DOWNLOAD BUTTONS

       col1,col2,col3=st.columns(3)

       with col1:
            st.download_button(
                 label="📊 Download as TXT",
                 data=txt_content,
                 file_name="flashcards.txt",
                 mime="text/plain",
                 key="download_txt",
                 use_container_width=True
                 )
       with col2:
            
            st.download_button(
            label="📊 Download as CSV",
            data=csv_buffer.getvalue(),
            file_name="flashcards.csv",
            mime="text/csv",
            key="download_csv",
            use_container_width=True
        )

       with col3:
            st.download_button(
                 label="📊 Download as PDF",
                 data=pdf_buffer,
                 file_name="flashcards.pdf",
                 mime="application/pdf",
                 key="download_pdf",
                 use_container_width=True
            )



            
            
       
             



        

   


if __name__=="__main__":
    main()



from sklearn.feature_extraction.text import TfidfVectorizer


def extract_tfidf_keywords(sentences,top_n=3):

    # Create TF-IDF Vectorizer

    vectorizer=TfidfVectorizer(stop_words="english")

    # Learn vocabulary and calculate TF-IDF scores
    tfidf_matrix=vectorizer.fit_transform(sentences)

    # Get all words(features)

    feature_names=vectorizer.get_feature_names_out()

   # Store keywords for every sentence
   

    keywords_list=[]

   # Process every sentence

    for row in range(tfidf_matrix.shape[0]):

        ## Convert sparse matrix into a normal array

        scores=tfidf_matrix[row].toarray().flatten()

        # Pair each word with its TF-IDF score

        word_scores=list(zip(feature_names,scores))

        # Remove words with score 0

        word_scores =[
            (word,score)
            for word, score in word_scores
            if score > 0
        ] 

        ## Sort words according to score (Highest--> Lowest)

        word_scores=sorted(
            word_scores,
            key=lambda x:x[1],
            reverse=True
        )    

        ## Keep only top N words

        top_keywords=[
            word
            for word,score in word_scores[:top_n]
        ]

        keywords_list.append(top_keywords)


    return keywords_list



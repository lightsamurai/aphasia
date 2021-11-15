Aim of this work is to automatically rank the severeness of **anomic aphasia** by applying Word2Vec tasks to our corpus, manually collected from the **Aphasia Bank online database** (https://aphasia.talkbank.org/) from diagnostic protocols. We analyze the transcriptions of aphasic patients' productions collected in Aphasia Talkbank, which were produced by the patients by accomplishing specific and standardized tasks of the Aphasia Bank Protocol (i.e. to describe the scene portraited in a picture the interviewer shows the patient). Word2vec uses a neural network model to learn word associations from a large corpus of text.

We collect our **input data** from the Aphasia Bank online database. We organise our input data in a **3-columns .csv file** where the first column is the patient-ID, whereas the second and third column are target/response word pairs. The target is the word which exactly describes the scene (e.g. "ball") and the response is the word the patient produces (e.g. "sphere").

Since the automatic diagnosing algorithm works for each language, a suited **language model** has to be uploaded (e.g. for the English language we use the pre-trained 'word2vec-google-news-300' vectors). The cosine similarity task is ran by the built-in **wv.similarity function of Word2Vec**, which takes as input our word pairs and gives as output their cosine similarity.

Finally, we compute the mean across all the patient's score, in order to get a single index of severeness for that patient.

More details on the project: https://drive.google.com/file/d/1IQ8PDOVlTTNE6CscvI70yfJL8G-CYuM5/view?usp=sharing

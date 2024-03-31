Naïve Search Engine Utilizing MapReduce

Overview:
This repository contains the implementation of a Naïve Search Engine utilizing MapReduce technology. The search engine processes text data, tokenizes it, and generates a sparse representation of the data using TF/IDF weights.

Files Included:
map_reduce.exe: Executable file for MapReduce functionality.
preprocessing.py: Python script for text preprocessing.
sparse_representation.txt: Text file containing the sparse representation of the data.
tokenized_text_by_id.txt: Text file containing tokenized text grouped by ARTICLE_ID.

Preprocessing:

The preprocessing.py script performs the following preprocessing steps on the input text data:

Cleaning: Removal of extra whitespace, newline characters, special characters, and digits. Conversion of text to lowercase.
Lemmatization and Tokenization: Lemmatization and tokenization of text using SpaCy's English language model.
Tokenization: Tokenization of cleaned text.

Usage:
To utilize the Naïve Search Engine, follow these steps:

Ensure that map_reduce.exe, preprocessing.py, and the input dataset are available.
Run the preprocessing.py script to preprocess the text data.
Use the MapReduce functionality provided by map_reduce.exe to generate the sparse representation of the data.
Access the generated sparse_representation.txt file to obtain TF/IDF weights for the documents.

Example:
An example of using the TF/IDF weights calculation is provided in the script. Adjust the input sparse representation accordingly and calculate the TF/IDF weights using the calculate_tf_idf function.

Dependencies:
The following dependencies are required to run the preprocessing script:

pandas
numpy
spacy
Ensure these dependencies are installed in your Python environment.

Contributors
SM ABDULLAH - SHEHARYAR BHATTI

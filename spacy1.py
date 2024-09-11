# Import necessary libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Initialize spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to perform tokenization with spaCy
def spacy_tokenization(text):
    doc = nlp(text)
    tokens_spacy = [token.text for token in doc if not token.is_punct and not token.is_space]
    return tokens_spacy

# Function to perform stemming with spaCy (spaCy does not have built-in stemming, so we use lemmatization as a substitute)
def spacy_stemming(words):
    stemmed_words_spacy = [nlp(word)[0].lemma_ for word in words]
    return stemmed_words_spacy

# Function to perform lemmatization with spaCy
def spacy_lemmatization(text):
    doc = nlp(text)
    lemmatized_words_spacy = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
    return lemmatized_words_spacy

# Function to remove stopwords with spaCy
def spacy_remove_stopwords(words):
    tokens_without_stopwords = [token for token in words if token.lower() not in STOP_WORDS]
    return tokens_without_stopwords

# Predefined paragraph
paragraph = """
Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful. Techniques in NLP often involve tasks such as text analysis, sentiment analysis, machine translation, and more. With advances in machine learning and deep learning, NLP has become increasingly sophisticated and integral to many applications in technology and industry.
"""

# Main function for processing
def main():
    print("Welcome to Text Processing with spaCy!")
    
    # Use predefined paragraph
    text = paragraph
    
    # spaCy tokenization
    tokens_spacy = spacy_tokenization(text)
    
    # spaCy stemming (using lemmatization as a substitute)
    stemmed_words_spacy = spacy_stemming(tokens_spacy)
    
    # spaCy lemmatization
    lemmatized_words_spacy = spacy_lemmatization(text)
    
    # spaCy stopword removal
    tokens_without_stopwords_spacy = spacy_remove_stopwords(tokens_spacy)
    
    # Print spaCy results
    print("\nTokenization with spaCy:")
    print(tokens_spacy)
    print("\nStemming (using lemmatization) with spaCy:")
    print(stemmed_words_spacy)
    print("\nLemmatization with spaCy:")
    print(lemmatized_words_spacy)
    print("\nStopwords Removed with spaCy:")
    print(tokens_without_stopwords_spacy)

# Execute the main function
if __name__ == "__main__":
    main()

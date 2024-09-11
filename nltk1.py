# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

# Initialize NLTK resources (if not already done)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Function to perform tokenization with NLTK
def nltk_tokenization(text):
    words_nltk = word_tokenize(text)
    return words_nltk

# Function to perform stemming with NLTK
def nltk_stemming(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words

# Function to perform lemmatization with NLTK
def nltk_lemmatization(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return lemmatized_words

# Function to remove stopwords with NLTK
def nltk_remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

# Predefined paragraph
paragraph = """
Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful. Techniques in NLP often involve tasks such as text analysis, sentiment analysis, machine translation, and more. With advances in machine learning and deep learning, NLP has become increasingly sophisticated and integral to many applications in technology and industry.
"""

# Main function for processing
def main():
    print("Welcome to Text Processing with NLTK!")
    
    # Use predefined paragraph
    text = paragraph
    
    # NLTK tokenization
    words_nltk = nltk_tokenization(text)
    
    # NLTK stemming
    stemmed_words_nltk = nltk_stemming(words_nltk)
    
    # NLTK lemmatization
    lemmatized_words_nltk = nltk_lemmatization(words_nltk)
    
    # NLTK stopword removal
    filtered_words_nltk = nltk_remove_stopwords(words_nltk)
    
    # Print NLTK results
    print("\nTokenization:")
    print(words_nltk)
    print("\nStemming:")
    print(stemmed_words_nltk)
    print("\nLemmatization:")
    print(lemmatized_words_nltk)
    print("\nStopwords Removed:")
    print(filtered_words_nltk)

# Execute the main function
if __name__ == "__main__":
    main()

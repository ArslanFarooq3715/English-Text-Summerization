# Text Processing and Analysis of "Metamorphosis"

## Overview

This project involves the text processing and analysis of Franz Kafka's "Metamorphosis." Using various natural language processing (NLP) techniques, the project demonstrates how to clean, tokenize, and vectorize text data, enabling further analysis and insights.

## Dataset

The primary dataset used in this project is the cleaned text of "Metamorphosis," stored in the file `metamorphosis_clean.txt`. This text file contains the full content of the novella, preprocessed to remove extraneous elements.

## Steps and Techniques

### 1. Loading the Dataset

The text is loaded from `metamorphosis_clean.txt` using Python's built-in file handling.

```python
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
```

### 2. Basic Text Processing

- **Word Splitting**: The text is split into individual words using basic string operations and regular expressions.

```python
words = text.split()
import re
words = re.split(r'\W+', text)
```

- **Removing Punctuation**: Punctuation is removed to clean the text further.

```python
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
```

- **Lowercasing**: All words are converted to lowercase for uniformity.

```python
words = [word.lower() for word in words]
```

### 3. Tokenization

Sentences and words are tokenized using the NLTK library, allowing for more granular analysis.

```python
from nltk.tokenize import sent_tokenize, word_tokenize
sentences = sent_tokenize(text)
tokens = word_tokenize(text)
```

### 4. Filtering Tokens

- **Removing Non-Alphabetic Tokens**: Tokens that are not alphabetic are filtered out.

```python
words = [word for word in tokens if word.isalpha()]
```

- **Removing Stop Words**: Common stop words in English are removed to focus on more meaningful words.

```python
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
```

### 5. Stemming

Stemming is applied to reduce words to their base forms using the Porter Stemmer.

```python
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
```

### 6. Vectorization

- **Count Vectorization**: The text is converted into a matrix of token counts.

```python
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(text)
vector = vectorizer.transform(text)
```

- **TF-IDF Vectorization**: A more advanced vectorization technique that reflects the importance of words in the document relative to the corpus.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(text)
vector = tfidf_vectorizer.transform([text[0]])
```

## Results

The various processed outputs, including tokenized words, cleaned text, and vector representations, can be utilized for further text analysis, such as sentiment analysis, topic modeling, or classification tasks.

## Conclusion

This project provides a comprehensive framework for processing and analyzing text data using NLP techniques. By utilizing various methods for text cleaning, tokenization, and vectorization, it lays the groundwork for deeper textual analysis of "Metamorphosis."

## Requirements

To run the scripts, ensure you have the following libraries installed:

- NLTK
- scikit-learn
- Python 3.x

You can install the required libraries using pip:

```bash
pip install nltk scikit-learn
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to add any additional sections or details specific to your project!

#!/usr/bin/env python
# coding: utf-8

# In[90]:



filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()


# In[18]:


filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

words = text.split()
print(words)


# In[6]:



filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

import re
words = re.split(r'\W+', text)
print(words)


# In[10]:


filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

words = text.split()


import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped)


# In[12]:


filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

words = text.split()

words = [word.lower() for word in words]
print(words)


# In[1]:


import nltk
nltk.download()


# In[4]:



filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

from nltk import sent_tokenize
sentences = sent_tokenize(text)
print(sentences)


# In[6]:


# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens)


# In[7]:


# load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

words = [word for word in tokens if word.isalpha()]
print(words[:100])


# In[8]:


from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)


# In[10]:



filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

tokens = [w.lower() for w in tokens]

import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

words = [word for word in stripped if word.isalpha()]

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words)


# In[12]:



filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
print(stemmed)


# In[103]:


from sklearn.feature_extraction.text import CountVectorizer
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# list of text documents
text=[text]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
vectorizer.vocabulary_
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(type(vector))
print(vector.toarray())


# In[91]:


vectorizer.vocabulary_


# In[100]:


from sklearn.feature_extraction.text import TfidfVectorizer

filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

text = [text]

vectorizer = TfidfVectorizer()

vectorizer.fit(text)

print(vectorizer.vocabulary_)
print(vectorizer.idf_)

vector = vectorizer.transform([text[0]])

vector.shape
vector.toarray()


# In[ ]:





# In[ ]:





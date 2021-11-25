import string
import nltk
from nltk.corpus import stopwords

def message_features_bow1(message):
    '''Generates features for given message content
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    for word in set(nltk.word_tokenize(message)):
        features[f'contains({word})'] = True

    return features

def message_features_bow2(message):
    '''Generates features for given message content
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    for word in set(nltk.word_tokenize(message)):
        if word not in string.punctuation:
            features[f'contains({word})'] = True

    return features

def message_features_bow3(message):
    '''Generates features for given message content
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    for word in set(nltk.word_tokenize(message)):
        if word not in string.punctuation and word.lower() not in stopwords.words('norwegian'):
            features[f'contains({word})'] = True

    return features

def message_features_bow4(message): # Veldig lav nøyaktighet
    '''Generates features for given message content
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    for word in set(nltk.word_tokenize(message)):
        if word not in string.punctuation and word.lower() not in stopwords.words('norwegian'):
            features[f'contains({word})'] = True

    for bigram in nltk.bigrams([nltk.word_tokenize(sent) for sent in nltk.word_tokenize(message)]):
        features[f'contains({bigram})'] = True

def message_features_bow5(message):
    '''Generates features for given message content
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    tokens = nltk.word_tokenize(message)
    for word in set(tokens):
        if word not in string.punctuation and word.lower() not in stopwords.words('norwegian'):
            features[f'count({word})'] = tokens.count(word)

    return features

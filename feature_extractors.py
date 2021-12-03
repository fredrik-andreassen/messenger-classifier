# Fredrik Aas Andreassen
# fredaan@ifi.uio.no

import string
import nltk
from nltk.corpus import stopwords

def message_features_bow1(message):
    '''Generates features for given message content
    BOW only
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
    BOW, no punctuation
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
    BOW, no punctuation, no norwegian stopwords
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    for word in set(nltk.word_tokenize(message)):
        if word not in string.punctuation and word.lower() not in stopwords.words('norwegian'):
            features[f'contains({word})'] = True

    return features



def message_features_bow4(message):
    '''Generates features for given message content
    BOW (lowered), no punctuation, no norwegian stopwords
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    for word in set(nltk.word_tokenize(message.lower())):
        if word not in string.punctuation and word not in stopwords.words('norwegian'):
            features[f'contains({word})'] = True

    return features

def message_features_bow5(message):
    '''Generates features for given message content
    BOW (lowered), no punctuation, no norwegian stopwords + bigrams
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    for word in set(nltk.word_tokenize(message.lower())):
        if word not in string.punctuation and word not in stopwords.words('norwegian'):
            features[f'contains({word})'] = True

    sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(message)]
    for sentence in sentences:
        for bigram in nltk.bigrams(sentence, pad_left = True, pad_right = True, left_pad_symbol='<s>', right_pad_symbol='</s>'):
                features[f'contains({" ".join(bigram)})'] = True

    return features

def message_features_bow6(message):
    '''Generates features for given message content
    bigrams
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(message)]
    for sentence in sentences:
        for bigram in nltk.bigrams(sentence, pad_left = True, pad_right = True, left_pad_symbol='<s>', right_pad_symbol='</s>'):
            features[f'contains({" ".join(bigram)})'] = True

    return features

def message_features_bow7(message):
    '''Generates features for given message content
    bigrams (lowered)
    Args:
        `message` (`str`)
    Returns:
        `features` (`dict`)'''

    features = {}
    sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(message.lower())]
    for sentence in sentences:
        for bigram in nltk.bigrams(sentence, pad_left = True, pad_right = True, left_pad_symbol='<s>', right_pad_symbol='</s>'):
            features[f'contains({" ".join(bigram)})'] = True

    return features

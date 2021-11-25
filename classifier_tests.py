import os, json, random, string
from collections import defaultdict
import nltk
from nltk.corpus import stopwords

from utilities import *
from feature_extractors import *

def train_and_evaluate(features):
    random.shuffle(features)
    train_set, test_set = split_data(features, test_ratio = 0.2)
    print(f'len(train_set) = {len(train_set)}\tlen(test_set) = {len(test_set)}')
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print('Accuracy on test_set:', round(nltk.classify.accuracy(classifier, test_set) * 100, 4), '%')
    classifier.show_most_informative_features(10)
    print()

def print_messages(n = 20):
    messages = get_messages('ikkemittslips_fdy4dcsvdq')
    messages = clean_messages(messages)
    random.shuffle(messages)
    print('Antall meldinger:', len(messages))
    for message in messages[:n]:
        print(f'{abreviate_name(message[0])} ({message[1]}): {message[2]}')

def main():
    messages = remove_rare_participants(get_messages('ikkemittslips_fdy4dcsvdq'))
    messages = clean_messages(messages)
    show_message_distribution(messages)



    print(' BAG OF WORDS')
    features = []
    for message in messages:
        features.append((message_features_bow1(message[2]), abreviate_name(message[0])))
    train_and_evaluate(features)


    print(' BAG OF WORDS, INGEN TEGNSETTING')
    features = []
    for message in messages:
        features.append((message_features_bow2(message[2]), abreviate_name(message[0])))
    train_and_evaluate(features)


    print(' BAG OF WORDS, INGEN TEGNSETTING, INGEN NORSKE STOPPORD')
    features = []
    for message in messages:
        features.append((message_features_bow3(message[2]), abreviate_name(message[0])))
    train_and_evaluate(features)

if __name__ == '__main__':
    main()
    #print_messages()

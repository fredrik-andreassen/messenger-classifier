import nltk
import random
from utilities import *
from feature_extractors import *

def main():
    conversation_name = input('Conversation: ')
    print('Loading messages...')
    messages = get_messages(conversation_name)
    print('Cleaning messages...\n')
    messages = clean_messages(messages)

    show_message_distribution(messages)

    print('Generating features...')
    features = []
    for message in messages:
        features.append((message_features_bow3(message[2]), message[0]))
    random.shuffle(features)

    print('Training classifier...\n')
    classifier = nltk.NaiveBayesClassifier.train(features)

    print('Ready!\nExit with input \'q\'.\n')
    while True:
        query = input('Input: ')
        if query.lower() == 'q':
            break
        query_features = message_features_bow3(query)
        print('Features:', ',  '.join([f'{description}: {value}' for description, value in query_features.items()]))
        print('Predicted class:', classifier.classify(query_features), '\n')

if __name__ == '__main__':
    main()

import os, sys, random

import nltk

from utilities import *
from feature_extractors import *

def get_conversation_name():
    conversation_name = None
    while not conversation_name:
        search_query = input('Søk etter samtalenavn: ')
        search_results = [file for file in os.listdir('inbox') if search_query in file.split('_')[0]]

        if not search_results:
            print('\nIngen samtale funnet\n')

        elif len(search_results) == 1:
            conversation_name = search_results[0]
            print(f'\nFant samtale \'{conversation_name}\'')

        else:
            print('\nFant flere samtaler')
            for i, result in enumerate(search_results):
                print(f'{i+1}: {result}')
            try:
                selection = input(f'Valg (1-{len(search_results)}): ')
                conversation_name = search_results[int(selection) - 1]
                print(f'\nValgt samtale \'{conversation_name}\'')
            except:
                print('\nFeil. Prøv igjen\n')

    return conversation_name

def generate_features(messages):
    return [(message_features_bow3(message[2]), message[0]) for message in messages]


def main():
    conversation_name = get_conversation_name()
    print('Leser inn meldinger...')
    messages = get_messages(conversation_name)
    print('Fjerner sjeldne deltakere...')
    messages = remove_rare_participants(messages)
    print('Fjerner systemgenererte meldinger...\n')
    messages = clean_messages(messages)

    show_message_distribution(messages)

    print('Genererer trekk...')
    features = []
    for message in messages:
        features.append((message_features_bow3(message[2]), message[0]))
    random.shuffle(features)

    print('Trener klassifiserer...\n')
    classifier = nltk.NaiveBayesClassifier.train(features)

    print('Klar!\nAvslutt med input \'/q\'.\n')
    while True:

        # Les inn melding fra bruker
        query = input('>>> ')

        # Sjekk om kommando
        if query.strip().startswith('/'):
            command = query[1:].lower().strip()
            if command in ['q', 'exit', 'quit']:
                sys.exit(0)
            elif command in ['clear', 'clean']:
                clear_screen()
            elif command in ['reset', 'restart']:
                clear_screen()
                main()
            elif command in ['dist', 'distribution']:
                show_message_distribution(messages)
            else:
                print(f'Gjenkjenner ikke kommando \'{command}\'\n')
            continue

        # Hent ut trekk
        query_features = message_features_bow3(query)
        if not query_features:
            print('Ingen trekk å hente ut\n')
            continue

        # Skriv ut trekk
        print('Trekk:', ',  '.join([f'{description}: {value}' for description, value in query_features.items()]))

        # Skriv ut sannsynlighetsfordeling for topp tre avsendere
        prob_dist_dict = classifier.prob_classify(query_features)
        prob_dist = [(label, prob_dist_dict.prob(label)) for label in prob_dist_dict.samples()]
        prob_dist.sort(key = lambda x: x[1])
        longest_label = max([label for label in prob_dist_dict.samples()], key = len)
        for label, prob in prob_dist[-3:]:
            len_before_comma = len(str(prob).split('.')[0])
            print(' ' * (len(longest_label) - len(label)) + label + ':' + ' ' * (3 - len_before_comma) + str(round(prob * 100, 3)) + ' %')

        # Skriv ut estimert avsender
        print('Estimert klasse:', classifier.classify(query_features), '\n')


if __name__ == '__main__':
    main()

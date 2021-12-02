import os
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


if __name__ == '__main__':
    main()

import os

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

def get_feature_extractor():
    

def main():
    get_conversation_name()
    get_feature_extractor()



if __name__ == '__main__':
    main()

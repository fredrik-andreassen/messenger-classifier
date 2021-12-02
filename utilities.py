import os, json, re
from collections import defaultdict

def fix_unicode(text):
    '''Fixes special characters
    Args:
        `text` (`str`)
    Returns:
        `fixed_text` (`str`)'''
    fixed_text = text.encode('latin-1').decode('utf-8')
    return fixed_text

def get_messages(conversation_name):
    '''Gets messages with sender name and timestamp from conversation
    Args:
        `conversation_name` (`str`)
    Returns:
        `messages` (`list[tuple[str, str, str]]`)'''

    messages = []
    conversation_path = 'inbox/' + conversation_name + '/'

    for file_name in [file for file in os.listdir(conversation_path) if file.endswith('.json')]:
        with open(conversation_path + file_name, encoding = 'utf-8') as file_object:
            data = json.load(file_object)
            for message in data['messages']:
                if 'content' in message.keys():
                    sender_name = fix_unicode(message['sender_name'])
                    content = fix_unicode(message['content'])
                    messages.append((sender_name, message['timestamp_ms'], content))

    return messages

def remove_rare_participants(messages, limit = 0.01):
    '''Gets messages with participant names from conversation
    Args:
        `messages` (`list[tuple[str, str, str]]`)
    Returns:
        `filtered_messages` (`list[tuple[str, str, str]]`)'''
    message_counts = defaultdict(lambda: 0)
    for message in messages:
        message_counts[message[0]] += 1

    filtered_messages = []
    total_message_counts = sum(message_counts.values())
    for message in messages:
        if message_counts[message[0]] / total_message_counts >= limit:
            filtered_messages.append(message)

    return filtered_messages

def sort_messages(messages):
    '''Sorts messages after timestamp expected in `messages[i][1]`
    Args:
        `messages` (`list[tuple[str, str, str]]`)
    Returns:
        `sorted_messages` (`list[tuple[str, str, str]]`)'''

    sorted_messages = messages.sort(key = lambda x: x[1])

    return sorted_messages

def clean_messages(messages):
    '''Removes messages that are not actually written by someone
    Args:
        `messages` (`list[tuple[str, str, str]]`)
    Returns:
        `cleaned_messages` (`list[tuple[str, str, str]]`)'''

    filtered_messages = []

    for message in messages:
        name, timestamp, content = message

        # MIDLERTIDIG FOR Å FINNE FLERE
        #if not content.endswith('.'):
        #    continue

        # SENDT NOE SPESIELT
        if re.search(r' har sendt et vedlegg\.', content):
            continue
        if re.search(r' har sendt en lenke\.', content):
            continue
        if re.search(r' har sendt sin nåværende posisjon\.', content):
            continue
        if re.search(r' har sendt et bilde til .+\.', content):
            continue


        # ENDRET CHAT-INNSTILLINGER
        if re.search(r'.+ har lagt til .+ i gruppen\.', content):
            continue
        if re.search(r'.+ har fjernet .+ fra gruppen\.', content):
            continue
        if re.search(r' har angitt emojien ', content):
            continue
        if re.search(r'.+ har endret chattemaet\.', content):
            continue
        if re.search(r' har gitt gruppen navnet ', content):
            continue
        if re.search(r' har endret gruppebildet\.', content):
            continue
        if re.search(r'.+ har gitt .+ kallenavnet .+\.', content):
            continue
        if re.search(r'.+ har fjernet kallenavnet til .+\.', content):
            continue
        if re.search(r'.+ har fjernet sitt eget kallenavn\.', content):
            continue

        # MENINGSMÅLING
        if content == 'Denne meningsmålingen er ikke lenger tilgjengelig.':
            continue

        # ANROP
        if re.search(r' har startet en samtale\.', content):
            continue
        if re.search(r'.+ har blitt med i samtalen\.', content):
            continue
        if re.search(r'.+ har startet en videochat\.', content):
            continue
        if re.search(r' ble med i videochatten\.', content):
            continue
        if content == 'Videochatten er avsluttet.':
            continue

        # SPILL
        if re.search(r'har fått \d+ (poeng )?i (.+|et spill)\.', content):
            continue

        # ANNET
        if re.search(r'.+ har startet en plan\.', content):
            continue
        if re.search(r'.+ har kalt planen .+\.', content):
            continue

        # FJERNE LENKER
        content = re.sub(r'(https?:\/\/)?(www)?\w+(\.\w+)+(:\w+)?(\/[\w\-%+&#,.()=?:~\']+)*', '', content)

        if content.strip() != '':
            filtered_messages.append((name, timestamp, content))

    return filtered_messages


def show_message_distribution(messages):
    message_counts = defaultdict(lambda: 0)
    for message in messages:
        message_counts[message[0]] += 1

    total_message_counts = sum(message_counts.values())
    longest_name = max(message_counts.keys(), key = len)
    print(f'MESSAGE DISTRIBUTION ({len(message_counts.keys())} participants)')
    for name, count in message_counts.items():
        percentage_text = str(round(count / total_message_counts * 100, 3))
        if len(percentage_text) == 5:
            print((' ' * (len(longest_name) - len(name))) + name + ':    ' + percentage_text + ' %   (' + str(count) + ')')
        else:
            print((' ' * (len(longest_name) - len(name))) + name + ':   ' + percentage_text + ' %   (' + str(count) + ')')
    print()

def split_data(data, test_ratio = 0.25):
    '''Splits data into `train_set` and `test_set`
    Args:
        `data` (`list`)
        `test_ratio` (`float`): Amount of data to use in `test_set`
    Returns:
        `train_set` (`list`)
        `test_set` (`list`)'''

    split_index = int(len(data) * (1 - test_ratio))
    train_set = data[:split_index]
    test_set = data[split_index:]

    return train_set, test_set

def abreviate_name(name):
    return name[:4] + ' ' + name.split()[-1][0]

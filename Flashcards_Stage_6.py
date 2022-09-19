# Flashcards - hyperskill
# STAGE 6

import json
import random


def add_card(dict_cards):
    print_and_log(logs, f'The card:\n')
    term = input_and_log(logs)
    while term in dict_cards.keys():
        print_and_log(logs, f'The term "{term}" already exists. Try again:\n')
        term = input_and_log(logs)
    print_and_log(logs, f'The definition of the card:\n')
    definition = input_and_log(logs)
    while definition in [x['definition'] for x in list(dict_cards.values())]:
        print_and_log(logs, f'The definition "{definition}" already exists. Try again:\n')
        definition = input_and_log(logs)
    dict_cards[term] = {'definition': definition, 'errors': 0}
    print_and_log(logs, f'The pair ("{term}":"{definition}") has been added.')
    return dict_cards


def remove_card(dict_cards):
    print_and_log(logs, 'Which card?\n')
    card = input_and_log(logs)
    try:
        del dict_cards[card]
        print_and_log(logs, 'The card has been removed.')
    except KeyError:
        print_and_log(logs, f'Can\'t remove "{card}": there is no such card.')
    return dict_cards


def check_knowledge(dict_cards):
    print_and_log(logs, 'How many times to ask?\n')
    n = int(input_and_log(logs))
    for n in range(n):
        t, d = random.choice(list(dict_cards.items()))
        de = d['definition']
        e = d['errors']
        print_and_log(logs, f'Print the definition of "{t}":\n')
        answer = input_and_log(logs)
        if de == answer:
            print_and_log(logs, 'Correct!')
        elif de != answer and answer in [x['definition'] for x in list(dict_cards.values())]:
            o_term = list(dict_cards.keys())[[x['definition'] for x in list(dict_cards.values())].index(answer)]
            print_and_log(logs, f'Wrong. The right answer is "{de}", but your definition is correct for "{o_term}".')
            e += 1
        else:
            print_and_log(logs, f'Wrong. The right answer is "{de}".')
            e += 1
        dict_cards[t]['errors'] = e
    return dict_cards


def export_cards(dict_cards):
    print_and_log(logs, 'File name:\n')
    file_name = input_and_log(logs)
    with open(file_name, 'w') as f:
        json.dump(dict_cards, f)
    print_and_log(logs, f'{len(dict_cards)} cards have been saved.')


def import_cards(dict_cards):
    try:
        print_and_log(logs, 'File name:\n')
        file_name = input_and_log(logs)
        with open(file_name, 'r') as f:
            file_cards = json.load(f)
    except FileNotFoundError:
        print_and_log(logs, 'File not found.')
    else:
        print_and_log(logs, f'{len(file_cards)} cards have been loaded.')
        for t, d in file_cards.items():
            dict_cards[t] = d  # czy error z add i z pliku sie sumuje? czy nadpisuwac ten z pliku?
    return dict_cards


def reset_stats(dict_cards):
    for k in dict_cards.keys():
        dict_cards[k]['errors'] = 0
    print_and_log(logs, 'Card statistics have been reset.')
    return dict_cards


def hardest_card(dict_cards):
    max_err = 0
    max_err_terms = []
    for k, v in dict_cards.items():
        if v['errors'] > max_err:
            max_err = v['errors']
    if max_err > 0:
        for k, v in dict_cards.items():
            if v['errors'] == max_err:
                max_err_terms.append(k)
    if len(max_err_terms) == 0:
        print_and_log(logs, 'There are no cards with errors.')
    elif len(max_err_terms) == 1:
        print_and_log(logs, f'The hardest card is "{max_err_terms[0]}". You have {max_err} errors answering it')
    else:
        print_and_log(logs, f'The hardest cards are, {max_err_terms}')  # to change!!!!!!!


def save_log():
    print_and_log(logs, 'File name:')
    file_name = input_and_log(logs)
    print_and_log(logs, 'The log has been saved.')
    with open(file_name, 'w') as file:
        for log in logs:
            file.write(str(log) + '\n')


def print_and_log(logs, string):
    logs.append(string)
    print(string)


def input_and_log(logs):
    string = input()
    logs.append(string)
    return string


def flashcards():
    dict_cards = {}
    logs = []
    while True:
        print_and_log(logs, 'Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
        act = input_and_log(logs)
        if act == 'add':  # OK
            dict_cards = add_card(dict_cards)
        elif act == 'remove':  # OK
            dict_cards = remove_card(dict_cards)
        elif act == 'import':  # OK
            dict_cards = import_cards(dict_cards)
        elif act == 'export':  # OK
            export_cards(dict_cards)
        elif act == 'ask':  # OK
            dict_cards = check_knowledge(dict_cards)
        elif act == 'log':  # !!!
            save_log()
        elif act == 'hardest card':  # !!!
            hardest_card(dict_cards)
        elif act == 'reset stats':
            dict_cards = reset_stats(dict_cards)
        elif act == 'exit':  # OK
            print_and_log(logs, 'Bye bye!')
            break


flashcards()


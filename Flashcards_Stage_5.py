# Flashcards - hyperskill
# STAGE 5
import json
import random


def add_card(dict_cards):
    term = input(f'The card:\n')
    while term in dict_cards.keys():
        term = input(f'The term "{term}" already exists. Try again:\n')
    definition = input(f'The definition of the card:\n')
    while definition in dict_cards.values():
        definition = input(f'The definition "{definition}" already exists. Try again:\n')
    dict_cards[term] = definition
    print(f'The pair ("{term}":"{definition}") has been added.')
    return dict_cards


def remove_card(dict_cards):
    card = input('Which card?\n')
    try:
        del dict_cards[card]
        print('The card has been removed.')
    except KeyError:
        print(f'Can\'t remove "{card}": there is no such card.')
    return dict_cards


def check_knowledge(dict_cards):
    n = int(input('How many times to ask?\n'))
    for n in range(n):
        t, d = random.choice(list(dict_cards.items()))
        answer = input(f'Print the definition of "{t}":\n')
        if d == answer:
            print('Correct!')
        elif d != answer and answer in dict_cards.values():
            o_term = list(dict_cards.keys())[list(dict_cards.values()).index(answer)]
            print(f'Wrong. The right answer is "{d}", but your definition is correct for "{o_term}".')
        else:
            print(f'Wrong. The right answer is "{d}".')


def export_cards(dict_cards):
    with open(input('File name:\n'), 'w') as f:
        json.dump(dict_cards, f)
    print(f'{len(dict_cards)} cards have been saved.')


def import_cards(dict_cards):
    try:
        with open(input('File name:\n'), 'r') as f:
            file_cards = json.load(f)
    except FileNotFoundError:
        print('File not found.')
    else:
        print(f'{len(file_cards)} cards have been loaded.')
        for t, d in file_cards.items():
            dict_cards[t] = d
    return dict_cards


def flashcards()
    dict_cards = {}
    while True:
        act = input('Input the action (add, remove, import, export, ask, exit):\n')
        if act == 'add':
            dict_cards = add_card(dict_cards)
        elif act == 'remove':
            dict_cards = remove_card(dict_cards)
        elif act == 'import':
            dict_cards = import_cards(dict_cards)
        elif act == 'export':
            export_cards(dict_cards)
        elif act == 'ask':
            check_knowledge(dict_cards)
        elif act == 'exit':
            print('Bye bye!')
            break


flashcards()

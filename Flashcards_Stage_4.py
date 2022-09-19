# Flashcards - hyperskill
# STAGE 4

class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition


def create_cards():
    n = int(input('Input the number of cards:\n'))
    dict_cards = {}
    for c in range(n):
        term = input(f'The term for card #{c+1}:\n')
        while True:
            if term in dict_cards.keys():
                term = input(f'The term "{term}" already exists. Try again:\n')
            else:
                break
        definition = input(f'The definition for card #{c+1}:\n')
        while True:
            if definition in dict_cards.values():
                definition = input(f'The definition "{definition}" already exists. Try again:\n')
            else:
                break
        dict_cards[term] = definition
    return dict_cards


def check_knowledge(dict_cards):
    for t, d in dict_cards.items():
        answer = input(f'Print the definition of "{t}":\n')
        if d == answer:
            print('Correct!')
        elif d != answer and answer in dict_cards.values():
            o_term = list(dict_cards.keys())[list(dict_cards.values()).index(answer)]
            print(f'Wrong. The right answer is "{d}", but your definition is correct for "{o_term}".')
        else:
            print(f'Wrong. The right answer is "{d}".')


def flashcards():
    list_cards = create_cards()
    check_knowledge(list_cards)


flashcards()

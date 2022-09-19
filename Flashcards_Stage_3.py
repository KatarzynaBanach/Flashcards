# Flashcards - hyperskill
# STAGE 3

class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition


def create_cards():
    print('Input the number of cards:')
    n = int(input())
    list_cards = []
    for c in range(n):
        print(f'The term for card #{c+1}:')
        term = input()
        print(f'The definition for card #{c+1}:')
        definition = input()
        list_cards.append(Card(term, definition))
    return list_cards


def check_knowledge(list_cards):
    for c in list_cards:
        print(f'Print the definition of "{c.term}":')
        answer = input()
        if c.definition == answer:
            print('Correct!')
        else:
            print(f'Wrong. The right answer is "{c.definition}".')


def flashcards():
    list_cards = create_cards()
    check_knowledge(list_cards)


flashcards()

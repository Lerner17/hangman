from random import randint
from sys import exit


HANGMANPICS = [
        '''
        +---+
        |   |
            |
            |
            |
            |
    =========
        ''',
        '''
        +---+
        |   |
        O   |
            |
            |
            |
    =========
        ''',
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
    =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
    =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
    =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
    =========
        ''',
        '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
    =========
        '''
        ]


word_list = ['чайка', 'камень']

def get_random_word(word_list):
    return word_list[randint(0, len(word_list)-1)]

def new_game():
    print('Привет! Правила простые: у вас есть ограничесное количество жизней. Вам нужно отгадать слово. Если вы вводите не правильную букву жизнь сгорает.\nВы можете ввести слово полностью, если догадались. Удачи!!!\n\n\n')
    print('=======================================')
    
    mistakes = 0
    word = get_random_word(word_list)
    used_letters = set() 
    secret = ['*' for i in word]
    #print(type(secret), secret)

    while mistakes < 7:
        print(' '.join(secret))
        letter = input('Введите букву: ')
        if letter in used_letters:
            print(f'Letter {letter} already used')
            continue
        used_letters.add(letter)
        secret = map(lambda x: x if x in used_letters else '*', list(word))            
        secret = list(secret)
        if letter not in word:
            print(HANGMANPICS[mistakes])
            mistakes += 1
            print('Неверено')
            print('Буквы: ', end='')
            print(', '.join(list(used_letters)))
            continue
        if '*' not in secret:
            print('U won')
            break


def start():
    answers_list = ['1', '2']

    while True:
        print('В И С И Л И Ц А')
        print('+=====================================+')
        print('| 1. Новая игра                       |')
        print('| 2. Выход                            |')
        print('+=====================================+')
        answer = input()
        if answer not in answers_list:
            print('Неизвестая команда')
            continue
        elif answer is '1':
            new_game()
        else:
            exit() 

if __name__ == '__main__':
    start()

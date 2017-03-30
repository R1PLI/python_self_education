def listmethod(variablelist):
    sequence = ''
    for i in range(len(variablelist) - 1):
        sequence += variablelist[i] + ', '
    sequence += 'and ' + variablelist[-1]
    return sequence


def gridmethod(variablegrid):
    for j in range(len(variablegrid[0])):
        for i in range(len(variablegrid)):
            print(variablegrid[i][j], end='')
        print('')


spam = ['apples', 'bananas', 'tofu', 'cats']

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


print(listmethod(spam))
gridmethod(grid)
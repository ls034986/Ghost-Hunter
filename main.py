import random

Tree = '*'
Ghost = 'G'
ForestSize = 5


def createForest(ForestSize):
    forest = []
    GhostPosition = random.randint(0, ForestSize-1)
    for x in range(ForestSize):
        if x == GhostPosition:
            forest.append(Ghost)
        else:
            forest.append(Tree)
    return [forest, GhostPosition]

def Start():
    guess = 0
    ForestSize = int(input('Size of forest? >> '))
    forest = createForest(ForestSize)
    print(f'Where is the ghost in the forest? 1-{ForestSize}?')
    guess = int(input('>> '))
    if not guess == forest[1]+1:
        while not guess == forest[1]+1:
            if not guess == forest[1]+1:
                print('You guessed wrong, try again.')
            guess = int(input('>> '))
    print('You guessed it!')
    print(forest[0])
    if input('Would you like to play again?(Y/N)>>').lower() == 'y':
        Start()

Start()

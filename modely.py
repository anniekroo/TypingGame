import pygame, random, unicodeGen, math


allUnicodeChoices = unicodeGen.get_all_unicode()


white = 255, 255, 255
green = 0, 255, 0

class Model:
    def __init__(self, hits=0, misses=0, wrongKey=0, gameOver=False):
        '''Defines hits misses and game over and initializes the class.
        When undefined, hits and misses equal zero and gameover is false.
        '''
        self.hits = hits
        self.misses = misses
        self.wrongKey = wrongKey
        self.gameover = gameOver

    def score(self):
        '''Defines score'''
        total = self.hits + self.misses + self.wrongKey
        if(total == 0):
            return 0
        return (self.hits / total) * 100

    def wpm(self):
        '''sets up a function in the class for there to be a words per minute.
        This does not yet actually portray words per minute but instead is a
        constant. We will change this once we have fully worked out exactly how
        the UI is interfacing with the model'''
        return 37

    def updateScore(self, event, curTime=0):
        '''updates score statistics by modifying values in the class model'''
        if event == 'h':
            self.hits += 1
        elif event == 'm':
            self.misses += 1
        else:
            self.wrongKey += 1
        if curTime >= 60:  # time is in seconds.
            self.gameover = True


class Letter:
    '''Letter objects include the letter to be typed, its location on the screen,
    and other similar information, and the random unicode string that follows it'''

    def __init__(self, font='ARIALUNI.TTF', value=None, x=None, y=None, surf=None):
        # arguments not passed in are randomly generated
        self.font = font
        self.textFont = pygame.font.Font(self.font, 40)
        self.tailFont = pygame.font.Font(self.font, 40)

        charWidth = 40  # self.textFont.size('X')[0]
        charHeight = self.textFont.size('X')[1]

        if(value == None):
            self.value = random.randint(97, 122)
        else:
            self.value = value

        self.tail = []
        self.tailLength = random.randint(3, 12)
        for i in range(self.tailLength):
            self.tail.append(random.choice(allUnicodeChoices))

        self.surf = pygame.Surface((charWidth, charHeight*(self.tailLength+1)))
        # self.surf = surf
        # self.surf.width = charWidth
        # self.surf.height = charHeight*(self.tailLength+1)
        lastChar = self.textFont.render(chr(self.value), 1, white)
        self.surf.blit(lastChar, (0, (self.tailLength)*charHeight))
        for i in range(len(self.tail)):
            uni = self.tailFont.render(self.tail[i], 1, green)
            self.surf.blit(uni, (0, ((i)*charHeight)))

        self.height = self.surf.get_height()

        if y == None:
            self.y = 0 - (random.randint(0, 600) + self.height)
        else:
            self.y = y
        if(x == None):
            self.x = random.randint(0, 19)
        else:
            self.x = x

    def getEnd(self):
        return self.y + self.height

import pygame, random


white = 255, 255, 255

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
    def __init__(self, value=None, x=None, y=None, surf=None):
        self.textFont = pygame.font.SysFont('ubuntumono', 40)
        if y == None:
            self.y = 0 - random.randint(0, 600)
        else:
            self.y = y
        if(value == None):
            self.value = random.randint(97, 122)
        else:
            self.value = value
        if(x == None):
            self.x = random.randint(0, 19)
        else:
            self.x = x
        self.surf = self.textFont.render(chr(self.value), 1, white)

class model:
    def __init__ (self, hits=0, misses=0, gameover=False):
        '''Defines hits misses and game over and initializes the class.
        When undefined, hits and misses equal zero and gameover is false.
        '''
        self.hits = hits
        self.misses = misses
        self.gameover = gameover
    def score(self):
        '''Defines score'''
        return (hits - misses)
    def wpm(self):
        '''sets up a function in the class for there to be a words per minute.
        This does not yet actually portray words per minute but instead is a
        constant. We will change this once we have fully worked out exactly how
        the UI is interfacing with the model'''
        return 37
def updateScore (model, hit, curTime):
    '''updates score statistics by modifying values in the class model'''
    if hit == True:
        model.hits += 1
    else:
        model.misses += 1
    if curTime >= 120: #currently time is in seconds.
        model.gameover = True

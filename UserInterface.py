import sys, pygame, time, random, unicodeGen
from modely import Model, Letter
pygame.init()

unicodeChoices = unicodeGen.get_all_unicode()
font = 'ARIALUNI.TTF'

size = width, height = 1200, 600
black = 0, 0, 0
white = 255, 255, 255
grey = 50, 50, 50
red = 255, 0, 0
textFont = pygame.font.Font(font, 40)
scoreFont = pygame.font.Font(font, 20)

screen = pygame.display.set_mode(size)
mod = Model()
letters = []
for i in range(10):
    h = 0 - random.randint(0, height)
    letters.append(Letter())

def randExclude(exclude, start, stop):
    '''returns a random letter in range (rang) excluding the letters given to exclude.
    '''
    r = None
    while r in exclude or r is None:
         r = random.randrange(start, stop)
    return r

def replaceLet(let, start, stop):
    xVals = []
    for i in range(len(let)):
        if let[i].x in xVals:
            a = randExclude(xVals, start, stop)
            let[i].x = a
            xVals.append(a)
        else:
            xVals.append(let[i].x)
    return(let)

letters = replaceLet(letters, 0, 19)
def xInLetters(l):
    xV = []
    for i in range(len(l)):
        xv = l[i]
        xV.append(xv.x)
    return xV
def replaceLet2(xValues):
    return randExclude(xValues, 0, 19)
letterSize = textFont.size('X')
targetStart = 100

target = pygame.Surface((width, 70))
startTime = time.clock()
# screen.fill(black)
curTime = time.clock() - startTime

#clock = pygame.time.Clock()
while not mod.gameover:
    # msElapsed = startTime.tick(30)
    screen.fill(black)
    target.fill(grey)
    screen.blit(target, (0, height - targetStart))
    potentials = []
    for i in range(len(letters)):
        thisLetter = letters[i]
        letters[i].y += .2 # letterSize[1]
        screen.blit(thisLetter.surf, ((width/20)*thisLetter.x, thisLetter.y))
        if thisLetter.y >= 600:
            xs = xInLetters(letters)
            letters[i] = Letter()
            letters[i].x = replaceLet2(xs)
            print('   X')
            curTime = time.clock() - startTime
            mod.updateScore('m', curTime)
        if thisLetter.y > height - targetStart - letterSize[1]/2:
            potentials.append(thisLetter.value)
    scoreboard = scoreFont.render(('Score:' + str(mod.score())), 1, red)
    screen.blit(scoreboard, (width - 100, 10))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keyPressed = event.key
            if keyPressed in potentials:
                print('X')
                curTime = time.clock() - startTime
                mod.updateScore('h', curTime)
                for i in range(len(letters)):
                    if (keyPressed == letters[i].value
                        and letters[i].y >= height - targetStart - letterSize[1]/2):
                        xs = xInLetters(letters)
                        letters[i] = Letter()
                        letters[i].x = replaceLet2(xs)
                        mod.gameOver = startTime - time.time()
            else:
                print('      X')
                mod.updateScore('w', curTime)
while mod.gameover == True:
    screen.fill(black)
    endFont = pygame.font.SysFont('ubuntumono', 100)
    endText = endFont.render(('Score:' + str(mod.score())), 1, red)
    screen.blit(endText, (width/2 -225, height/2 - 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

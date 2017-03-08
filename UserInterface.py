import sys, pygame, random
from modely import Model, Letter
pygame.init()

size = width, height = 1200, 600
black = 0, 0, 0
white = 255, 255, 255
grey = 50, 50, 50
red = 255, 0, 0
textFont = pygame.font.SysFont('ubuntumono', 40)
scoreFont = pygame.font.SysFont('ubuntumono', 20)

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

# screen.fill(black)

while not mod.gameOver:
    screen.fill(black)
    target.fill(grey)
    screen.blit(target, (0, height - targetStart))
    potentials = []
    for i in range(len(letters)):
        thisLetter = letters[i]
        letters[i].y += .1 # letterSize[1]
        screen.blit(thisLetter.surf, ((width/20)*thisLetter.x, thisLetter.y))
        if thisLetter.y >= 600:
            xs = xInLetters(letters)
            letters[i] = Letter()
            letters[i].x = replaceLet2(xs)
            print('   X')
            mod.updateScore('m')
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
                mod.updateScore('h')
                for i in range(len(letters)):
                    if (keyPressed == letters[i].value
                        and letters[i].y >= height - targetStart - letterSize[1]/2):
                        xs = xInLetters(letters)
                        letters[i] = Letter()
                        letters[i].x = replaceLet2(xs)
            else:
                print('      X')
                mod.updateScore('w')

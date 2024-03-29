import pygame
from pygame.constants import KEYDOWN
from board import Board
from shape import Shape
class GameControl():    
    def setupScreen(self):
        width,height = self.board.getDimensions()
        pygame.display.set_mode((width+150,height))#100 represents the menu to the side of the game board
        screen = pygame.display.get_surface()
        return screen
    
    def createBoard(self):
        self.board = Board()

    def setUpFont(self):
        return pygame.font.SysFont(None, 24)
        
        
    def scorer(self,lines,level):
        if(lines == 1):
            return 40 * (level + 1)
        elif(lines == 2):
            return 100 * (level + 1)
        elif(lines == 3):
            return 300 * (level + 1)
        elif(lines == 4):
            return 1200 * (level + 1)
        else:
            return 0


    def gameLoop(self):
        pygame.init()
        exitGame = False
        newShape = True

        #board and screen setup
        self.createBoard()
        surface = self.setupScreen()
        gameBoard = self.board
        width,height  = gameBoard.getDimensions()
        shape = Shape(width)
        loopNum = 0
        clearedRows = 0
        score = 0
        level = 0
        maxLoop = 500
        #font setup
        font = self.setUpFont()
        nextText = font.render('Next', True, (255,255,255))
        linesText = font.render('Lines:  0', True, (255,255,255))
        scoreText = font.render('Score:  0', True, (255,255,255))
        levelText = font.render('Level:  0', True, (255,255,255))

        while not exitGame:
            if (newShape == True):
                shape.popShapeBag()
                shape.resetShape()
                newShape = False
            if(loopNum>maxLoop):#game loops until shape moves down
                loopNum = 0
                shape.moveShapeDown()
            loopNum+=1
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    if (pygame.key.get_pressed()[pygame.K_LEFT]):#move left
                        if(not(gameBoard.collisionCheck(shape,-1,0)) and ((shape.x + shape.getLeftHeight(shape.getShapeData()))>0)):#check if legal
                            shape.moveShapeLeft()

                    if (pygame.key.get_pressed()[pygame.K_RIGHT]):#move right
                        if(not(gameBoard.collisionCheck(shape,1,0)) and ((shape.x - shape.getRightHeight(shape.getShapeData()))<10)):#check if legal
                            shape.moveShapeRight()

                    if (pygame.key.get_pressed()[pygame.K_UP]):#rotate shape
                        shape.setShapeData(shape.rotateShape(shape.getShapeData()))
                        if(gameBoard.collisionCheck(shape,0,0)):#check if legal
                            shape.setShapeData(shape.undoRotation(shape.getShapeData()))
                        elif ((shape.x - shape.getRightHeight(shape.getShapeData()))>10) or ((shape.x + shape.getLeftHeight(shape.getShapeData()))<0):
                            shape.setShapeData(shape.undoRotation(shape.getShapeData()))

                    if (pygame.key.get_pressed()[pygame.K_SPACE]):#hard drop
                        while(not(gameBoard.collisionCheck(shape,0,1))):
                            shape.moveShapeDown()
                        gameBoard.addPlacedShapesToBoard(shape)
                        newShape = True
            
            if(loopNum>maxLoop-1):
                if (gameBoard.collisionCheck(shape,0,1)):
                    gameBoard.addPlacedShapesToBoard(shape)
                    newShape = True
                    maxLoop = 500 - (level*10)
                    if (maxLoop < 40):
                        maxLoop = 42
            

            score += self.scorer(gameBoard.rowCheck(),level)
            level = clearedRows//10
            if(clearedRows != gameBoard.rowsCleared):
                clearedRows = gameBoard.rowsCleared
                linesText = font.render('Lines:  '+str(clearedRows), True, (255,255,255))
                scoreText = font.render('Score:  '+str(score), True, (255,255,255))
                levelText = font.render('Level:  '+str(level), True, (255,255,255))

            if(gameBoard.toppleCheck()):
                exitGame = True
            
            if(loopNum % 40 == 0):
                surface.fill((0,0,0))
                gameBoard.drawBoard(surface)
                pygame.draw.rect(surface, (102,102,102), (width,0,150,height))
                shape.drawNextShape(surface,width,height)
                surface.blit(nextText, (width + 35, 5))
                surface.blit(linesText, (width + 20, 150))
                surface.blit(scoreText, (width + 20, 170))
                surface.blit(levelText, (width + 20, 190))
            shape.drawShape(surface)
            pygame.display.flip()
        print("Rows cleared " +str(gameBoard.rowsCleared))
        return gameBoard.rowsCleared
GameControl().gameLoop()


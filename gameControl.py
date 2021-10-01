import pygame
from pygame.constants import KEYDOWN
from board import Board
from shape import Shape
class GameControl():    
    def setupScreen(self):
        width,height = self.board.getDimensions()
        pygame.display.set_mode((width,height))
        screen = pygame.display.get_surface()
        return screen
    
    def createBoard(self):
        self.board = Board()


    def gameLoop(self):
        exitGame = False
        newShape = True
        self.createBoard()
        self.surface = self.setupScreen()
        gameBoard = self.board
        width  = gameBoard.getDimensions()[0]
        shape = Shape(width)
        loopNum = 0
        while not exitGame:
            if (newShape == True):
                shape.popShapeBag()
                shape.resetShape()
                newShape = False
            if(loopNum>500):#game loops until shape moves down
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
                            shape.SetShapeData(shape.undoRotation(shape.getShapeData()))
                        elif ((shape.x - shape.getRightHeight(shape.getShapeData()))>10) or ((shape.x + shape.getLeftHeight(shape.getShapeData()))<0):
                            shape.setShapeData(shape.undoRotation(shape.getShapeData()))

                    if (pygame.key.get_pressed()[pygame.K_SPACE]):#hard drop
                        while(not(gameBoard.collisionCheck(shape,0,1))):
                            shape.moveShapeDown()
                        gameBoard.addPlacedShapesToBoard(shape)
                        newShape = True

            if (gameBoard.collisionCheck(shape,0,1)):
                gameBoard.addPlacedShapesToBoard(shape)
                newShape = True
            
            gameBoard.rowCheck()
            if(gameBoard.toppleCheck()):
                exitGame = True
            if(loopNum%40 == 0):
                self.surface.fill((0,0,0))
                gameBoard.drawBoard(self.surface)
            shape.drawShape(self.surface)
            pygame.display.flip()
        print("Rows cleared " +str(gameBoard.rowsCleared))
        return gameBoard.rowsCleared
GameControl().gameLoop()


import pygame
from pygame.constants import KEYDOWN
from board import Board
from shape import Shape
import sys
import time
class GameControl():    
    def setupScreen(self):
        width,height = self.board.getDimensions()
        window = pygame.display.set_mode((width,height))
        screen = pygame.display.get_surface()
        return screen
    
    def createBoard(self):
        #self.mainQueue = SingletonQueue()
        self.board = Board()
        #self.mainQueue.register(self.board,0)


    def gameLoop(self):
        exitGame = False
        softDrop = False
        hardDrop = False
        newShape = True
        self.createBoard()
        self.surface = self.setupScreen()
        gameBoard = self.board
        width,height = self.board.getDimensions()
        shape = Shape(width)
        shape.x = 0
        shape.y = 0
        loopNum = 0
        while not exitGame:
            if (newShape == True):
                shape.popShapeBag()
                newShape = False
            if(loopNum>500):#game loops until shape moves down
                loopNum = 0
                shape.moveShapeDown()
            loopNum+=1
            for event in pygame.event.get():
                
                if (event.type == KEYDOWN):
                    if (pygame.key.get_pressed()[pygame.K_LEFT]):
                        if(not(self.board.collisionCheck(shape,-1,0)) and ((shape.x + shape.getLeftHeight(shape.currentShape))>0)):#check if legal
                            shape.moveShapeLeft()

                    if (pygame.key.get_pressed()[pygame.K_RIGHT]):
                        if(not(self.board.collisionCheck(shape,1,0)) and ((shape.x - shape.getRightHeight(shape.currentShape))<10)):#check if legal
                            shape.moveShapeRight()

                    if (pygame.key.get_pressed()[pygame.K_UP]):
                        shape.currentShape = shape.rotateShape(shape.currentShape)
                        if(self.board.collisionCheck(shape,0,0)):#check if legal
                            shape.currentShape = shape.undoRotation(shape.currentShape)
                        elif ((shape.x - shape.getRightHeight(shape.currentShape))>10) or ((shape.x + shape.getLeftHeight(shape.currentShape))<0):
                            shape.currentShape = shape.undoRotation(shape.currentShape)

                    if (pygame.key.get_pressed()[pygame.K_SPACE]):
                        while(not(self.board.collisionCheck(shape,0,1))):
                            shape.moveShapeDown()
                        self.board.addPlacedShapesToBoard(shape)
                        newShape = True

            if (self.board.collisionCheck(shape,0,1)):
                self.board.addPlacedShapesToBoard(shape)
                newShape = True
            
            self.board.rowCheck()

            if(loopNum%40 == 0):
                self.surface.fill((0,0,0))
                self.board.drawBoard(self.surface)
            shape.drawShape(self.surface)
            pygame.display.flip()
GameControl().gameLoop()


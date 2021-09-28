import pygame
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
        while not exitGame:
            for event in pygame.event.get():
                if (newShape == True):
                    shape.popShapeBag()
                    newShape = False
                shape.moveShapeDown()
                if (pygame.key.get_pressed()[pygame.K_LEFT]):
                    #check if legal
                    shape.moveShapeLeft()
                    print("left")
                
                if (pygame.key.get_pressed()[pygame.K_RIGHT]):
                    #check if legal
                    shape.moveShapeRight()
                    print("right")
                if (pygame.key.get_pressed()[pygame.K_UP]):
                    #check if legal
                    shape.currentShape = shape.rotateShape(shape.currentShape)
                if (self.board.collisionCheck(shape)):
                    self.board.addPlacedShapesToBoard(shape)
                    newShape = True
                time.sleep(0.1)
                self.surface.fill((0,0,0))
                self.board.drawBoard(self.surface)
                shape.drawShape(self.surface)
                pygame.display.flip()
GameControl().gameLoop()


from colours import Colours
import numpy as np
import pygame
class Board:
    def __init__ (self):
        self.width = 10
        self.height = 24
        self.blockSize = 20
        self.board = np.zeros((self.height,self.width))
        self.Colours = Colours().returnList()
        self.currentShape = None
        self.rowsCleared = 0
    
    def setCurrentShape(self,shape):
        self.currentShape = shape

    def getDimensions(self):
        return (self.width * self.blockSize, self.height * self.blockSize)
    
    def getWidth(self):
        return (self.width)

    def rowCheck(self):
        lines = 0
        for row in range(0,len(self.board)):
            if 0 in self.board[row]:
                pass
                
            else:
                self.clearRow(row)
                lines+=1
        return lines
    
    def clearRow(self,row):
        self.board = np.delete(self.board, row, 0)
        self.board = np.insert(self.board, 0, np.zeros(10),0)
        self.rowsCleared+=1
    
    def toppleCheck(self):
        if any(self.board[0]):
            return True
    
    def addPlacedShapesToBoard(self,shape):
        shapeData = shape.getShapeData()
        x,y = shape.getPosition()
        posX = 0
        posY = 0
        for row in shapeData:
            for block in row:
                px = x + posX
                py = y + posY
                if block != 0:
                    self.board[py][px] = block
                posX += 1
            posX = 0
            posY +=1
    
    def collisionCheck(self,shape,xIncrement,yIncrement):
        shapeData = shape.getShapeData()
        x,y = shape.getPosition()
        posX = 0
        posY = 0
        for row in shapeData:
            for block in row:
                px = x + posX + xIncrement
                py = y + posY + yIncrement
                try:
                    if block != 0 and self.board[py][px] != 0:
                        return True
                    posX += 1
                except IndexError:
                    return True
            posX = 0
            posY +=1
        
    def drawBoard(self,surface):
        index = 0
        for row in self.board:
            for block in row:
                x = (index % self.width) * 20
                y = (index // self.width) * 20
                if block != 0:
                    pygame.draw.rect(surface,self.Colours[block.astype(int)-1], pygame.Rect(x,y,20,20))
                    pygame.draw.rect(surface, self.Colours[8], pygame.Rect(x,y,20,20),1)
                index += 1
    
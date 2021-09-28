import numpy as np
from colours import Colours
import random
import pygame
from pygame import *
class Shape():
    def __init__(self,width):
        self.lineShape = np.array([[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]])
        self.square = np.array([[2,2],[2,2]])
        self.tShape = np.array([[0,0,0],[3,3,3],[0,3,0]])
        self.lShape = np.array([[0,4,0],[0,4,0],[0,4,4]])
        self.jShape = np.array([[0,5,0],[0,5,0],[5,5,0]])
        self.sShape = np.array([[0,6,6],[6,6,0],[0,0,0]])
        self.zShape = np.array([[7,7,0],[0,7,7],[0,0,0]])
        self.shapes = [self.lineShape, self.square, self.tShape, self.lShape, self.jShape, self.sShape,self.zShape]
        self.shapePointerBag = np.arange(len(self.shapes))
        np.random.shuffle(self.shapePointerBag)
        self.currentShape = None
        self.blockSize = 20
        self.Colours = Colours().returnList()
        self.width = width
        self.x = (self.width-2)//2
        self.y = 0
        self.dx = 0
        self.dy = 1

    def popShapeBag(self):
        self.currentShape = self.shapes[self.shapePointerBag[0]]
        self.shapePointerBag = np.delete(self.shapePointerBag,0)
        self.resetShape()
        if (len(self.shapePointerBag)<1):
            self.shapePointerBag = np.arange(len(self.shapes))
            np.random.shuffle(self.shapePointerBag)

    def getShapeData(self):
        return self.currentShape

    def getPosition(self):
        return self.x,self.y

    def resetShape(self):
        self.x = 0#(self.width-2)//2
        self.y = 0
        self.dx = 0
        self.dy = 1

    def setAsNext(self):
        self.x = 0
        self.y = 0

    def setOffset(self,offset):
        self.offset = offset

    def rotateShape(self,shape):
        return np.rot90(shape,3)

    def undoRotation(self,shape):
        return np.rot90(shape)
    
    def moveShapeLeft(self):
        self.x -=1
    
    def moveShapeRight(self):
        self.x +=1
    
    def moveShapeDown(self):
        self.y +=1
    
    def moveShapeUp(self):
        self.y -=1
    
    def drawShape(self,surface):
        xIndex = 0
        yIndex = 0
        for row in self.currentShape:
            for block in row:
                x = (self.x + xIndex) * 20
                y = (self.y + yIndex) * 20
                if block != 0:
                    pygame.draw.rect(surface,self.Colours[block-1], pygame.Rect(x,y,20,20))
                    pygame.draw.rect(surface, self.Colours[8], pygame.Rect(x,y,20,20),1)
                xIndex += 1
            xIndex = 0
            yIndex +=1
            
        #self.y = 8
        """posX = 0
        posY = 0
        for row in self.currentShape:
            for block in row:
                px = self.x + posX
                py = self.y + posY
                if block != 0:
                    pygame.draw.rect(surface,self.Colours[block-1], pygame.Rect(px,py,20,20))
                    pygame.draw.rect(surface, self.Colours[8], pygame.Rect(px,py,20,20),1)
                posX += 1
            posX = 0
            posY +=1"""

    def test(self):
        pass
#s = Shape(10)


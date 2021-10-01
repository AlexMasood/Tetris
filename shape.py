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
        self.x = 0
        self.y = 0
        self.dx = 0

    def popShapeBag(self):
        self.currentShape = self.shapes[self.shapePointerBag[0]]
        self.shapePointerBag = np.delete(self.shapePointerBag,0)
        self.resetShape()
        if (len(self.shapePointerBag)<1):
            self.shapePointerBag = np.arange(len(self.shapes))
            np.random.shuffle(self.shapePointerBag)

    def getNextShape(self):
        return self.shapes[self.shapePointerBag[0]]

    def getShapeData(self):
        return self.currentShape
    
    def setShapeData(self,shapeData):
        self.currentShape = shapeData

    def getPosition(self):
        return self.x,self.y

    def resetShape(self):
        self.x = 4 - self.getLeftHeight(self.currentShape)
        self.y = 0
        self.dx = 0

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
    
    
    def getHeight(self,shapeData):
        height=0
        for row in shapeData:
            if any(row):
                break
            else:
                height+=1
        return height

    def getLeftHeight(self,shapeData):
        shapeDataLeft = self.rotateShape(shapeData)
        return self.getHeight(shapeDataLeft)
    
    def getRightHeight(self,shapeData):
        shapeDataRight = self.undoRotation(shapeData)
        return self.getHeight(shapeDataRight)

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
    
    def drawNextShape(self,surface,width,height):
        xIndex = 0
        yIndex = 0
        xOffset = 0
        yOffset = 0
        if self.shapePointerBag[0] in [0,1,3,4]:
            xOffset = 1
        if (self.shapePointerBag[0] == 2):
            yOffset = 1
        for row in self.getNextShape():
            for block in row:
                x = ((xIndex + (1 + xOffset - self.getLeftHeight(self.getNextShape()))) *20)+ width
                y = ((2 - yOffset + yIndex) * 20)
                if block != 0:
                    pygame.draw.rect(surface,self.Colours[block-1], pygame.Rect(x,y,20,20))
                    pygame.draw.rect(surface, self.Colours[8], pygame.Rect(x,y,20,20),1)
                xIndex += 1
            xIndex = 0
            yIndex +=1
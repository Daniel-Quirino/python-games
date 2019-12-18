import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
 
class cube(object):
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
       
    def move(self, dirnx, dirny):
        pass
 
    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass
 
    def move(self):
        pass
 
    def reset(self, pos):
        pass
 
    def addCube(self):
        pass
       
    def draw(self, surface):
        pass
 
def drawGrid(w, rows, surface):
    pass

def redrawWindow(surface):
    pass
 
 
def randomSnack(rows, item):
    pass
 
 
def message_box(subject, content):
    pass
 
 
def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    snack = cube(randomSnack(rows, s), color=(0,255,0))
    flag = True
    clock = pygame.time.Clock()
   
    pass
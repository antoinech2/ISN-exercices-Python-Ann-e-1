from tkinter import *
from random import randrange

def trace():
    global x_1,y_1,x_2,y_2,coul
    cadre.create_polygon(x_1,y_1,x_2,y_2,100,50,width,fill=coul)
    y_2,y_1=y_2+10,y_1-10
    x_2,x_1=x_2+10,x_1-10

def couleur():
    global coul
    palette=['red','blue','yellow','green','brown','black','orange','purple']

def dessine_croix():
    cadre.create_line(300,100,300,400,width=5,fill='red')
    cadre.create_line(100,250,500,250,width=5,fill='red')

x_1,y_1,x_2,y_2=100,290,390,100
coul='dark green'
fen=Tk()
czadre=Canvas(fen,bg=)

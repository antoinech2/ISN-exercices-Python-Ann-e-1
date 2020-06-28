from tkinter import *
from random import randrange
import time

fenetre = Tk()
text = Label(fenetre, text='Compte à rebours', fg='green')
text.pack(side=TOP)
quitter = Button(fenetre,text='Quitter',command=fenetre.destroy)
lancer = Button(fenetre,text='Démarrer',command=fenetre.quit)
quitter.pack()
lancer.pack()
fenetre.mainloop()

for i in range (5):
    text = Label(fenetre, text=5-i, fg='red')
    text.pack(side=TOP)
    #time.sleep(1)

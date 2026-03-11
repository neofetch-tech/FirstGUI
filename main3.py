from tkinter import *
def button_click():
    print('Guys, its working')

root=Tk()
root.tittle('My first GUI')
root.geometry('400x400')
Button(root,text='Click this shit man', command=button_click).pack()
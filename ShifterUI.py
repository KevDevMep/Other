import pandas as pd
import tkinter as tk
import Shifter as S

def load():
    try:
        S.df = pd.read_csv(filename.get().strip())
        loaded.set(True)
        print('Loaded')
    except:
        print('Error')

def shifter():
    if loaded.get():
        S.shifter(shift.get(), senBefore.get(), govBefore.get())
        print('Shifted')
    else:
        print('File not Loaded')

def reset():
    if loaded.get():
        S.reset()
        print('Reset')
    else:
        print('File not Loaded')

def stats():
    if loaded.get():
        S.stats(senBefore.get(), govBefore.get())
    else:
        print('File not Loaded')

def pres():
    if loaded.get():
        print(S.df[S.df['Type']=='Pres'])
    else:
        print('File not loaded')

def house():
    if loaded.get():
        print(S.df[S.df['Type']=='House'])
    else:
        print('File not loaded')

def senate():
    if loaded.get():
        print(S.df[S.df['Type']=='Senate'])
    else:
        print('File not loaded')

def gov():
    if loaded.get():
        print(S.df[S.df['Type']=='Gov'])
    else:
        print('File not loaded')

def pathToVictory():
    if loaded.get():
        S.pathToVictory()
    else:
        print('File not loaded')

def senGoTo():
    if loaded.get():
        S.senGoTo(senBefore.get(), senTarget.get())
    else:
        print('File not loaded')

def preset():
    match year.get():
        case '2024':
            filename.set('Election Data 24.csv')
            senBefore.set(28)
            govBefore.set(20)
        case '2022':
            filename.set('Election Data 22.csv')
            senBefore.set(35)
            govBefore.set(8)
        case '2020':
            filename.set('Election Data 20.csv')
            senBefore.set(36)
            govBefore.set(20)
        case '2018':
            filename.set('Election Data 18.csv')
            senBefore.set(23)
            govBefore.set(9)
        case '2016':
            filename.set('Election Data 16.csv')
            senBefore.set(36)
            govBefore.set(11)
        case '2014':
            filename.set('Election Data 14.csv')
            senBefore.set(34)
            govBefore.set(8)
        case '2012':
            filename.set('Election Data 12.csv')
            senBefore.set(29)
            govBefore.set(13)
        case '2010':
            filename.set('Election Data 10.csv')
            senBefore.set(39)
            govBefore.set(7)
        case '2008':
            filename.set('Election Data 08.csv')
            senBefore.set(39)
            govBefore.set(22)
        case '2006':
            filename.set('Election Data 06.csv')
            senBefore.set(27)
            govBefore.set(7)
        case '2004':
            filename.set('Election Data 04.csv')
            senBefore.set(30)
            govBefore.set(16)
        case _:
            print('Not a year with a preset')

def comp():
    if loaded.get():
        S.comp()
    else:
        print('File not loaded')

def search():
    if loaded.get():
        print(S.df[S.df['id'] == name.get()])
    else:
        print('File not loaded')

root = tk.Tk()
root.title('Shifter')
year = tk.StringVar()
filename = tk.StringVar()
name = tk.StringVar()
loaded = tk.BooleanVar()
shift = tk.IntVar()
senBefore = tk.IntVar()
govBefore = tk.IntVar()
senTarget = tk.IntVar(value=50)

tk.Label(root, text='Filename').grid(row=0, column=0)
tk.Entry(root, textvariable=filename).grid(row=1, column=0)
tk.Button(root, text='Load', command=load).grid(row=1, column=1)
tk.Label(root, text='Margin (%)').grid(row=2, column=0)
tk.Spinbox(root, from_=-100, to_=100, textvariable=shift).grid(row=3, column=0)
tk.Button(root, text='Shift', command=shifter).grid(row=3, column=1)
tk.Button(root, text='Stats', command=stats).grid(row=4, column=0)
tk.Button(root, text='Reset', command=reset).grid(row=4, column=1)
tk.Label(root, text='Senate Comp').grid(row=5, column=0)
tk.Label(root, text='Gov Comp').grid(row=5, column=1)
tk.Spinbox(root, textvariable=senBefore, from_=0, to_=100).grid(row=6, column=0)
tk.Spinbox(root, textvariable=govBefore, from_=0, to_=50).grid(row=6, column=1)
tk.Checkbutton(root, variable=loaded, text='Loaded', onvalue=True, offvalue=False, state='disabled').grid(row=7, column=0)


tk.Button(root, text='President', command=pres).grid(row=0, column=3)
tk.Button(root, text='House', command=house).grid(row=1, column=3)
tk.Button(root, text='Senate', command=senate).grid(row=2, column=3)
tk.Button(root, text='Governor', command=gov).grid(row=3, column=3)
tk.Button(root, text='Path To Victory', command=pathToVictory).grid(row=4, column=3)
tk.Label(root, text='Senate Target').grid(row=5, column=3)
tk.Spinbox(root, textvariable=senTarget, from_=0, to_=100).grid(row=6, column=3)
tk.Button(root, text='Target', command=senGoTo).grid(row=7, column=3)

tk.Label(root, text='Year').grid(row=0, column=4)
tk.Entry(root, textvariable=year).grid(row=1, column=4)
tk.Button(root, text='Historical Preset', command=preset).grid(row=2, column=4)
tk.Button(root, text='Comp', command=comp).grid(row=3, column=4)
tk.Label(root, text='Name').grid(row=4, column=4)
tk.Entry(root, textvariable=name).grid(row=5, column=4)
tk.Button(root, text='Search',command=search).grid(row=6, column=4)

root.mainloop()
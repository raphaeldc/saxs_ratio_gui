#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

# importando funções saxs_plot:
from saxs_ratio_analyser import *


from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from tkinter.filedialog import askopenfilename
import os

#from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

#name1 = ''
#file = open('null.txt')

'''
Inserir classe App para facilitar a construção da interface

'''


root = Tk.Tk()
root.wm_title("SAXS Data Crystallographic Analysis")

def callback():
      global name1
      samples = []
      name1 = askopenfilename(title = "Select file",filetypes = (("DAT files","*.dat"),("all files","*.*")))
      samples.append(os.path.split(name1)[1])
      n1.insert(END, sample)
      print(samples)
      #n1.insert(END, sample)
errmsg = 'Error!'

button_open = Tk.Button(master=root, text='Open data file', command=callback)
button_open.pack(side=Tk.TOP)

# chamando função saxs_plot

f = saxs_plot(['ra_10LA_1_norm_minus_agua_7_norm.dat','ra_10LH_1_norm_minus_agua_7_norm.dat'], ['Fd3m', 'Pn3m','Pn3m'], [0.91, 1.21, 1.3]   ,['0.05% C14','2% C14'])



# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)

def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

canvas.mpl_connect('button_press_event', onclick)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button_quit = Tk.Button(master=root, text='Quit', command=_quit)
button_quit.pack(side=Tk.BOTTOM)

#file.close()

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.

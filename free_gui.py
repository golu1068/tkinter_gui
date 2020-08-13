from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import ttk
######################################################################
def OnMap(fr,w,h,event):
    print('onmap')
    fr.config(width=w, height=h)
    
def OnUnmap(fr, w,h,event):
    print('OnUnmap')
#    fr.config(width=w-w/9, height=h-h/9)

def con(fr,w, h, event):
#    ww = event.width
#    hh = event.height
    print(w, h)
    print(fr['width'])
#    print('fr= ',fr.winfo_screenwidth(), fr.winfo_screenheight())
#    fr.config(width =w/2-w/30, height=h/2)
#    master.destroy()
def char2pixel(val):
    return int(val*0.125)

###############################################################################
master = Tk()
w, h = master.winfo_screenwidth(), master.winfo_screenheight()
master.geometry("%dx%d" % (w, h)) 
#master.state("zoomed")
#master.minsize(1000, 200) 

#master.protocol("WM_DELETE_WINDOW", partial(close, master))
master.bind('<Escape>', lambda e: master.destroy())
#master.bind('<Configure>', partial(close, master))
###############################################################################
main_frame = Frame(master, bg='gray',  bd=1, relief=RIDGE,  pady=13)
main_frame.grid(row=0, column=0, padx=0, pady=1)
main_frame.grid_propagate(False)
main_frame.config(width =w, height=h)
#########################################################################
frame1 = Frame(main_frame, bg='yellow',  bd=1, relief=RIDGE)
frame1.grid(row=0, column=0, padx=10, pady=1, sticky=N)
frame1.grid_propagate(False)
frame1.config(width =main_frame['width']*0.98, height=main_frame['height']*0.29)

print(frame1['width'])

fr11 = Frame(frame1, bg='white',  bd=1, relief=RIDGE)
fr11.grid(row=0, column=0)
fr11.grid_propagate(False)
fr11.config(width =frame1['width']*0.25, height=frame1['height']) 
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr11['width']*0.5), fr11['height']), Image.ANTIALIAS))
l1 = Label(fr11, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr11,  bg='white', height=int(char2pixel(fr11['height'])/2), width=int(char2pixel(fr11['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT,'vweiuf gfhnffrhrhrh bk')

print(char2pixel(fr11['width']))

fr12 = Frame(frame1, bg='white',  bd=1, relief=RIDGE)
fr12.grid(row=0, column=1)
fr12.grid_propagate(False)
fr12.config(width =frame1['width']*0.25, height=frame1['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr11['width']*0.5), fr11['height']), Image.ANTIALIAS))
l1 = Label(fr12, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr12,  bg='white', height=int(char2pixel(fr12['height'])/2), width=int(char2pixel(fr12['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT,'vweiwefwfufgbk')

fr13 = Frame(frame1, bg='white',  bd=1, relief=RIDGE)
fr13.grid(row=0, column=2)
fr13.grid_propagate(False)
fr13.config(width =frame1['width']*0.25, height=frame1['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr11['width']*0.5), fr11['height']), Image.ANTIALIAS))
l1 = Label(fr13, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr13,  bg='white', height=int(char2pixel(fr13['height'])/2), width=int(char2pixel(fr13['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT,'vweiwefwfufgbk')

fr14 = Frame(frame1, bg='white',  bd=1, relief=RIDGE)
fr14.grid(row=0, column=3)
fr14.grid_propagate(False)
fr14.config(width =frame1['width']*0.25, height=frame1['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr11['width']*0.5), fr11['height']), Image.ANTIALIAS))
l1 = Label(fr14, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr14,  bg='white', height=int(char2pixel(fr14['height'])/2), width=int(char2pixel(fr14['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT,'vweiwefwfufgbk')
##############################################################################
frame2 = Frame(main_frame, bg='white',  bd=1, relief=RIDGE,  pady=1)
frame2.grid(row=1, column=0, padx=10, pady=2, sticky=N)
frame2.grid_propagate(False)
frame2.config(width =main_frame['width']*0.98, height=main_frame['height']*0.29)


fr21 = Frame(frame2, bg='white',  bd=1, relief=RIDGE)
fr21.grid(row=1, column=0)
fr21.grid_propagate(False)
fr21.config(width =frame1['width']*0.3, height=frame1['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr21['width']*0.5), fr21['height']), Image.ANTIALIAS))
l1 = Label(fr21, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr21,  bg='white', height=int(char2pixel(fr21['height'])/2), width=int(char2pixel(fr21['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

fr22 = Frame(frame2, bg='white',  bd=1, relief=RIDGE)
fr22.grid(row=1, column=1)
fr22.grid_propagate(False)
fr22.config(width =frame1['width']*0.3, height=frame1['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr22['width']*0.5), fr22['height']), Image.ANTIALIAS))
l1 = Label(fr22, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr22,  bg='white', height=int(char2pixel(fr22['height'])/2), width=int(char2pixel(fr22['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

fr23 = Frame(frame2, bg='white',  bd=1, relief=RIDGE)
fr23.grid(row=1, column=2)
fr23.grid_propagate(False)
fr23.config(width =frame1['width']*0.15, height=frame1['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr23['width']*0.5), fr23['height']), Image.ANTIALIAS))
l1 = Label(fr23, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr23,  bg='white', height=int(char2pixel(fr23['height'])/2), width=int(char2pixel(fr23['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

fr24 = Frame(frame2, bg='white',  bd=1, relief=RIDGE)
fr24.grid(row=1, column=3)
fr24.grid_propagate(False)
fr24.config(width =frame1['width']*0.25, height=frame1['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr24['width']*0.5), fr24['height']), Image.ANTIALIAS))
l1 = Label(fr24, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr24,  bg='white', height=int(char2pixel(fr24['height'])/2), width=int(char2pixel(fr24['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

#########################################################################
#style = ttk.Style()
#style.element_create("RoundedFrame", "image", "frameBorder",
#     border=16, sticky="nsew")
#
#style.layout("RoundedFrame", [("RoundedFrame", {"sticky": "nsew"})])
#style.configure("TEntry", borderwidth=5)

frame3 = Frame(main_frame, bg='white',  bd=0, relief=RIDGE)
frame3.grid(row=2, column=0, padx=10, pady=2, sticky=N)
frame3.grid_propagate(False)
frame3.config(width =main_frame['width']*0.98, height=main_frame['height']*0.29)


frame30 = Frame(frame3,relief=SUNKEN, bd=0, bg='brown')
frame30.grid(row=0, column=0, padx=17, pady=9)
frame30.grid_propagate(False)
frame30.config(width =frame3['width']*0.95, height=frame3['height']*0.85)

fr31 = Frame(frame30, bg='white',  bd=1, relief=RIDGE)
fr31.grid(row=0, column=0)
fr31.grid_propagate(False)
fr31.config(width =frame30['width']*0.25, height=frame30['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr31['width']*0.5), fr31['height']), Image.ANTIALIAS))
l1 = Label(fr31, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr31,  bg='white', height=int(char2pixel(fr31['height'])/2), width=int(char2pixel(fr31['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

fr32 = Frame(frame30, bg='white',  bd=1, relief=RIDGE)
fr32.grid(row=0, column=1)
fr32.grid_propagate(False)
fr32.config(width =frame30['width']*0.25, height=frame30['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr32['width']*0.5), fr32['height']), Image.ANTIALIAS))
l1 = Label(fr32, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr32,  bg='white', height=int(char2pixel(fr32['height'])/2), width=int(char2pixel(fr32['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

fr33 = Frame(frame30, bg='white',  bd=1, relief=RIDGE)
fr33.grid(row=0, column=2)
fr33.grid_propagate(False)
fr33.config(width =frame30['width']*0.15, height=frame30['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr33['width']*0.5), fr33['height']), Image.ANTIALIAS))
l1 = Label(fr33, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr33,  bg='white', height=int(char2pixel(fr33['height'])/2), width=int(char2pixel(fr33['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

fr34 = Frame(frame30, bg='white',  bd=1, relief=RIDGE)
fr34.grid(row=0, column=3)
fr34.grid_propagate(False)
fr34.config(width =frame30['width']*0.35, height=frame30['height'])
image = Image.open("images_4.png")
photo = ImageTk.PhotoImage(image.resize((int(fr34['width']*0.5), fr34['height']), Image.ANTIALIAS))
l1 = Label(fr34, image=photo, bg='green')
l1.image = photo
l1.grid(row=0, column=0)    
l2 = Text(fr34,  bg='white', height=int(char2pixel(fr34['height'])/2), width=int(char2pixel(fr34['width'])/2)-1, relief=FLAT,
          wrap=WORD)
l2.grid(row=0, column=1)
l2.insert(INSERT, 'nagndrakjcbsdkjcsdc')

#############################################################################
#master.bind('<Configure>', partial(con, frame1, w, h))

#l1 = Label(frame1, text='vbklv')
#l1.pack(fill=BOTH, side=LEFT)



master.bind("<Unmap>", partial(OnUnmap, main_frame, w, h))
master.bind("<Map>", partial(OnMap, main_frame, w, h))
master.mainloop()
##################################################################################
#import tkinter
#import tkinter.scrolledtext as scrolledtext
#
#def close():
#    print('domne')
#
#class GUI(object):
#
#    def __init__(self):
#        root = self.root = tkinter.Tk()
#        root.title('Test')
#
#    # make the top right close button minimize (iconify) the main window
#        root.protocol("WM_DELETE_WINDOW", close)
#
#    # make Esc exit the program
#        root.bind('<Escape>', lambda e: root.destroy())
#
#    # create a menu bar with an Exit command
#        menubar = tkinter.Menu(root)
#        filemenu = tkinter.Menu(menubar, tearoff=0)
#        filemenu.add_command(label="Exit", command=root.destroy)
#        menubar.add_cascade(label="File", menu=filemenu)
#        root.config(menu=menubar)
#
#    # create a Text widget with a Scrollbar attached
#        txt = scrolledtext.ScrolledText(root, undo=True)
#        txt['font'] = ('consolas', '12')
#        txt.pack(expand=True, fill='both')
#
#gui = GUI()
#gui.root.mainloop()
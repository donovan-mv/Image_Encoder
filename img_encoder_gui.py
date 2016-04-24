#version 1.0 => with basic gui options and no file dialogs
#version 1.5 => Added browse buttons to enable file dialogs for chosing files
#version 2.0 => Addded fast encode option to take image from webcam and other GUI improovements

#refer gui3 module for most gui implementations
#all commented code was used for debugging
#as of 15-Oct-15, working with JPEGs shows inconsistency in the encoding-decoding process


from Tkinter import *
import tkMessageBox as mb
import tkFileDialog as fd
from cv2 import *
import numpy as np
import img_encode as ie


def enc(): #Function to encode; calls encode() method in img_encode module
    """print ent1.get()
    print ent2.get()
    print ent3.get()
    print ent4.get()"""
    try:
        img=ie.encode(imread(ent1.get(), 0), ent2.get(), int(ent4.get()))
        imwrite(ent3.get(), img)
    except:
        print "ERROR: Enter a valid file name"
        return
    print "encode complete"
    mb.showinfo(title="Complete", message="Encoding complete!")
    return

def dec(): #Function to decode; calls decode() method in img_encode module
    """print ent1.get()
    print ent2.get()
    print ent3.get()
    print int(ent4.get())"""
    if ie.decode(imread(ent1.get(), 0),ent3.get(), int(ent4.get())) == -2:
        print "ERROR: Enter a valide output file"
        return
    elif ie.decode(imread(ent1.get(), 0),ent3.get(), int(ent4.get())) == -1:
        return
    else:
        print "decode complete"
        mb.showinfo(title="Complete", message="Decoding complete!")
        return

def openf(): #method to create a file dialog for opening files
    return fd.askopenfilename(parent=root, defaultextension='.png', title='Open File', filetypes=[('Portable Network Graphics', '*.png'), ('JPEG', '*jpeg'), ('JPG', '*jpg'), ('Text File', '*.txt')])

def savef(): #method to create a file dialog for saving files
    return fd.asksaveasfilename(parent=root, defaultextension='.txt', title='Save File', filetypes=[('Portable Network Graphics', '*.png'), ('Text File', '*.txt')])

def brow_img(): #callback function for 1st browse button
    ent1.delete(0, END)
    ent1.insert(0, openf())
    return

def brow_input(): #callback function for 2nd browse button
    ent2.delete(0, END)
    ent2.insert(0, openf())
    return

def brow_output(): #callback function for 3rd browse button
    ent3.delete(0, END)
    ent3.insert(0, savef())
    return

def fast_en(): #function that implements fast encoding by capturing image from webcam
    cam=VideoCapture(0)
    ret, frame=cam.read() #It returns 2 object; the first is a boolean indicating if read was successful
    if ret is False:
        print "Error initialising webcam. Try again."
        return
    cam.release()
    photo=cvtColor(frame, COLOR_BGR2GRAY)
    #imshow("photo", photo)
    try:
        img=ie.encode(photo, ent2.get(), int(ent4.get()))
        imwrite(ent3.get(), img)
    except:
        print "ERROR: Enter a valid file name"
        return
    print "encode complete"
    mb.showinfo(title="Complete", message="Encoding complete!")
    return


root=Tk()
root.title("Image Encoder 2.0")
root.resizable(height=FALSE, width=FALSE)

fr=Frame(root, height=100, width=200, bd=1)
fr.grid(sticky=(N,S,E,W))
lb1=Label(fr, text="Image (.jpeg, .png)")
lb1.grid(padx=10, pady=5, row=0, column=0, sticky=(W))
lb2=Label(fr, text="Input (.txt)")
lb2.grid(padx=10, pady=5, row=1, column=0,sticky=(W))
lb3=Label(fr, text="Output (.png, .txt)")
lb3.grid(padx=10, pady=5, row=2, column=0, sticky=(W))
lb4=Label(fr, text="Key (11-99)")
lb4.grid(padx=10, pady=5, row=3, column=0, sticky=(W))
ent1=Entry(fr, width=60)
ent1.focus_set()
ent1.grid(row=0, column=1, padx=5, columnspan=2, sticky=(W))
ent2=Entry(fr, width=60)
ent2.grid(row=1, column=1, padx=5, columnspan=2, sticky=(W))
ent3=Entry(fr, width=60)
ent3.grid(row=2, column=1, padx=5, columnspan=2, sticky=(W))
ent4=Spinbox(fr, width=8, from_=11, to=99)
ent4.grid(row=3, column=1, padx=5, columnspan=2, sticky=(W))
but1=Button(fr, text="Encode",width=15, height=2, command=enc)
but1.grid(row=4, column=0, pady=15, ipadx=10, padx=10,)
but2=Button(fr, text="Decode", width=15, height=2, command=dec)
but2.grid(row=4, column=1, pady=15, padx=10, ipadx=10)

info=Label(fr, text="Select the image file name with which encoding is to be performed in the image box. Then select the text file whos data is to be encoded (input). Enter an output image name (.png) as output. Then enter a 2 digit key and click 'Encode'. To decode, select the file of encoded image as 'image', and enter an output file name (.txt). Then click 'Decode' after entering the right key. Fast encode captures a fram from the webcam so there is no need to select an image for encoding with. Simply select the input text and give an output file name and click 'Fast Encode'.\n\n Dev: Donovan Vaz",
           wraplength=625, justify=LEFT)
info.grid(row=5, column=0, columnspan=4,pady=5, padx=10, sticky=(W))

brow1=Button(fr, text="Browse", command=brow_img)
brow1.grid(row=0, column=3, ipadx=10, pady=5, sticky=(W), padx=10)
brow2=Button(fr, text="Browse", command=brow_input)
brow2.grid(row=1, column=3, ipadx=10, pady=5, sticky=(W), padx=10)
brow3=Button(fr, text="Browse", command=brow_output)
brow3.grid(row=2, column=3, ipadx=10, pady=5, sticky=(W), padx=10)

fen=Button(master=fr, text='Fast Encode', width=15, height=2, command=fast_en)
fen.grid(row=4, column=2, pady=15, padx=25, ipadx=10, sticky=(W))

root.mainloop()

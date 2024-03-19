import tkinter as tk 
from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os 

root=tk.Tk()
root.title("Color Picker")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False, False)

global filename

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="select image file",
                                        filetypes=(("PNG file", "*.png"),
                                                  ("JPG file", "*.jpg"), 
                                                  ("ALL file", ".")))

    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=310, height=270)
    lbl.image=img             


def Findcolor():
    global filename
    ct=ColorThief(filename)
    pallete=ct.get_palette(color_count=11)
    
    
    rgb1=pallete[0]
    rgb2=pallete[1]
    rgb3=pallete[2]
    rgb4=pallete[3]
    rgb5=pallete[4]
    
    rgb6=pallete[5]
    rgb7=pallete[6]
    rgb8=pallete[7]
    rgb9=pallete[8]
    rgb10=pallete[9]
    
    
    print(rgb1)
    #print(rgb2)
    
    color1=f"#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}"
    color2=f"#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}"
    color3=f"#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}"
    color4=f"#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}"
    color5=f"#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}"
    
    color6=f"#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}"
    color7=f"#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}"
    color8=f"#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}"
    color9=f"#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}"
    color10=f"#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}"
    
    colors.itemconfig(id1, fill=color1)
    colors.itemconfig(id2, fill=color2)
    colors.itemconfig(id3, fill=color3)
    colors.itemconfig(id4, fill=color4)
    colors.itemconfig(id5, fill=color5)
    
    colors2.itemconfig(id6, fill=color6)
    colors2.itemconfig(id7, fill=color7)
    colors2.itemconfig(id8, fill=color8)
    colors2.itemconfig(id9, fill=color9)
    colors2.itemconfig(id10, fill=color10)
    
    hex1.config(text=color1)
    hex2.config(text=color2)
    hex3.config(text=color3)
    hex4.config(text=color4)
    hex5.config(text=color5)
    hex6.config(text=color6)
    hex7.config(text=color7)
    hex8.config(text=color8)
    hex9.config(text=color9)
    hex10.config(text=color10)
    
    
tk.Label(root, width=120, height=10, bg="#4272f9").pack()
image_icon=tk.PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)
#FRAME

frame=Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)


logo=PhotoImage(file="logo.png")
tk.Label(frame, image=logo, bg="#fff").place(x=10,y=10)

tk.Label(frame, text="Color Finder", font="arial 25 bold", bg="white").place(x=100, y=20)


#COLOR 1 

colors=tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors.place(x=20, y=90)

id1=colors.create_rectangle((10,10,50,50), fill="#b8255f")
id2=colors.create_rectangle((10,50,50,100), fill="#b8255f")
id3=colors.create_rectangle((10,100,50,150), fill="#b8255f")
id4=colors.create_rectangle((10,150,50,200), fill="#b8255f")
id5=colors.create_rectangle((10,200,50,250), fill="#b8255f")


hex1=tk.Label(colors,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex1.place(x=60, y=15)
hex2=tk.Label(colors,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex2.place(x=60, y=65)
hex3=tk.Label(colors,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex3.place(x=60, y=115)
hex4=tk.Label(colors,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex4.place(x=60, y=165)
hex5=tk.Label(colors,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex5.place(x=60, y=215)

#COLOR2
colors2=tk.Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors2.place(x=180, y=90)

id6=colors2.create_rectangle((10,10,50,50), fill="#b8255f")
id7=colors2.create_rectangle((10,50,50,100), fill="#b8255f")
id8=colors2.create_rectangle((10,100,50,150), fill="#b8255f")
id9=colors2.create_rectangle((10,150,50,200), fill="#b8255f")
id10=colors2.create_rectangle((10,200,50,250), fill="#b8255f")


hex6=tk.Label(colors2,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex6.place(x=60, y=15)
hex7=tk.Label(colors2,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex7.place(x=60, y=65)
hex8=tk.Label(colors2,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex8.place(x=60, y=115)
hex9=tk.Label(colors2,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex9.place(x=60, y=165)
hex10=tk.Label(colors2,text="#b8255f", fg="#000", bg="#fff", font="arail 12 bold")
hex10.place(x=60, y=215)


# SELECT IMAGE
selectimage=tk.Frame(frame, width=340, height=350, bg="#d6dee5", relief=tk.GROOVE)
selectimage.place(x=350, y=10)

f=tk.Frame(selectimage, bd=3, bg="black", width=320, height=280)
f.place(x=10, y=20)

lbl=tk.Label(f, bg="black")
lbl.place(x=0, y=0)


tk.Button(selectimage, text="Select Image", width =12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
tk.Button(selectimage, text="Find Color", width =12, height=1, font="arial 14 bold", command=Findcolor).place(x=176, y=300)



root.mainloop()




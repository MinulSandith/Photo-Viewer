from tkinter.filedialog import askopenfilename
import pathlib
import os
import ctypes
import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER
import os
import pathlib
# i must stop over lapping,and disabling of buttons
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
global end
end = 1
root = tk.Tk()
time = "first"
root.title("The Infinite Viewer")
user32 = ctypes.windll.user32
pixel_x = user32.GetSystemMetrics(0)
pixel_y = user32.GetSystemMetrics(1)-75
x_cordinate = int((pixel_x/2) - (pixel_x/2))
y_cordinate = int((pixel_y/2) - (pixel_y/2))
global copy
global display_img
root.geometry("{}x{}+{}+{}".format(pixel_x, pixel_y, x_cordinate, y_cordinate))
display_img = Image.open(
    "photo.jpg")
copy = ImageTk.PhotoImage(display_img)

global index
global imagefiles
global image_area
copy_width = copy.width()
copy_height = copy.height()

def choose():

   global index
   global imagefiles
   xxxxxxxxxxxx = 0
   print(xxxxxxxxxxxx)
   path = askopenfilename()
   cwd = os.path.dirname(path)
   onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd)
                if os.path.isfile(os.path.join(cwd, f))]
   global xx
   xx = -1
   imagefiles = []
   for x in onlyfiles:
       extension = pathlib.Path(onlyfiles[xx + 1]).suffix
       xx = xx + 1
       if extension == '.jpeg' or extension == '.png' or extension == '.jpg':
           imagefiles.append(x)
   kkk = 0
   for l in imagefiles:
       imagefiles[kkk] = imagefiles[kkk].replace("\u005C", '/')
       kkk = kkk + 1
   selected_file = path
   index = imagefiles.index(path)
   print(imagefiles[index])
   action()


def action():

  global copy
  global display_img
  global image_area
  del copy
  del display_img
  image_area.destroy()
  display_img = Image.open(
      imagefiles[index])
  copy = ImageTk.PhotoImage(display_img)
  copy_width = copy.width()
  copy_height = copy.height()


  display()
frame_w=pixel_x*88/100
frame_h=pixel_y*87.5/100
def display():
  global display_img
  copy_width = copy.width()
  copy_height = copy.height()

  if copy_width > pixel_x:
    while copy_width > pixel_x:
       copy_width = copy_width/1.1111
       copy_height = copy_height/1.1111
    display_img = display_img.resize(
        (int(copy_width), int(copy_height)), Image.ANTIALIAS)
  if copy_height > pixel_y*87.5/100:
    while copy_height > pixel_y*87.5/100:
       copy_width = copy_width/1.1111
       copy_height = copy_height/1.1111
    display_img = display_img.resize(
        (int(copy_width), int(copy_height)), Image.ANTIALIAS)

  display_img = ImageTk.PhotoImage(display_img)
  image_area = tk.Label(root, image=display_img)
  global i_w,i_h
  i_w = display_img.width()
  frame_w=pixel_x*88/100
  x_center = pixel_x-frame_w
  x_center = x_center/2
  x_center = x_center/pixel_x

  i_h = display_img.height()
  frame_h=pixel_y*87.5/100
  y_center = pixel_y*87.5/100-frame_h
  y_center = y_center/2
  y_center = y_center/pixel_y*87.5/100

  choose_img_w = choose_img.width()
  c_x_center = pixel_x-choose_img_w

  c_zero_d = c_x_center/2
  c_l_x = c_zero_d/pixel_x
  i_w = display_img.width()
  x_center = pixel_x-i_w
  zero_d = x_center/2
  l_x = zero_d/pixel_x

  i_h = display_img.height()
  y_center = pixel_y*87.5/100-i_h
  zero_h = y_center/2
  l_y = zero_h/pixel_y*87.5/100

  image_area.place(relx=l_x, rely=l_y)


def forward():

   global index
   global imagefiles
   index = index+1
   if index == len(imagefiles):

       index = 0
   action()


def backward():
   global index
   global imagefiles
   index = index-1
   if index == -1:

       index = len(imagefiles)-1

   action()

def zoom_in():
    global display_img,imagefiles,index,i_h,i_w
    display_img = Image.open(
        imagefiles[index])
    display_img = display_img.resize(
        (int(i_w*1.3),int( i_h*1.3)), Image.ANTIALIAS)
    display()

def zoom_out():
    global display_img,imagefiles,index,i_h,i_w
    display_img = Image.open(
        imagefiles[index])
    display_img = display_img.resize((int(i_w/1.3), int(i_h/1.3)), Image.ANTIALIAS)
    display()
if copy_width > pixel_x:
    while copy_width > pixel_x:
       copy_width = copy_width/1.1111
       copy_height = copy_height/1.1111
    display_img = display_img.resize(
        (int(copy_width), int(copy_height)), Image.ANTIALIAS)
if copy_height > pixel_y*87.5/100:
    while copy_height > pixel_y*87.5/100:
       copy_width = copy_width/1.1111
       copy_height = copy_height/1.1111
    display_img = display_img.resize(
        (int(copy_width), int(copy_height)), Image.ANTIALIAS)

choose_img = Image.open("D:\Minul\python\developed\photo viewer\images.png")
choose_img = choose_img.resize(
    (int(pixel_y*12.5/100), int(pixel_y*12.5/100)), Image.ANTIALIAS)
choose_img = ImageTk.PhotoImage(choose_img)
choose_img_hw = pixel_y*12.5/100


copy_width = copy.width()
copy_height = copy.height()



display_img = ImageTk.PhotoImage(display_img)
choose_file = tk.Button(root, image=choose_img, border=0, command=choose)
forward = tk.Button(root, text="Forward" ,command=forward)
backward = tk.Button(root, text="Backward",command=backward)
image_area = tk.Label(root, image=display_img)



zoom_in=tk.Button(root,text="zoom in" ,command=zoom_in)
zoom_out=tk.Button(root,text="zoom out" ,command=zoom_out)

frame_w=pixel_x*88/100
frame_h=pixel_y*87.5/100

i_w = display_img.width()
i_h = display_img.height()

x_center = pixel_x-frame_w
x_center = x_center/2
x_center = x_center/pixel_x


y_center = pixel_y*87.5/100-frame_h
y_center = y_center/2
y_center = y_center/pixel_y*87.5/100

img_x_center = frame_w-i_w
img_x_center = img_x_center/2
#img_x_center = img_x_center/pixel_x

img_y_center = frame_h-i_h
img_y_center = img_y_center/2
#img_y_center = img_y_center/pixel_y*87.5/100











choose_img_w = choose_img.width()
c_x_center = pixel_x-choose_img_w

c_zero_d = c_x_center/2
c_l_x = c_zero_d/pixel_x




forward.place(relx=0.8, rely=0.9)
backward.place(relx=0.2, rely=0.9)
choose_file.place(relx=c_l_x, rely=0.875)
zoom_in.place(relx=0.6,rely=0.9)
zoom_out.place(relx=0.4,rely=0.9)

#here is the module now  i must make this for both hei..,width.then take the heighest t value an substact it from both to take a ratio
i_w = display_img.width()
x_center = pixel_x-i_w
zero_d = x_center/2
l_x = zero_d/pixel_x

i_h = display_img.height()
y_center = pixel_y*87.5/100-i_h
zero_h = y_center/2
l_y = zero_h/pixel_y*87.5/100
image_area.place(relx=l_x, rely=l_y)
print(pixel_y*87.5/100)
print("x",pixel_x,"\n","y",pixel_y)
print(1366*88/100)
root.mainloop()


#1300/227.666666666,590

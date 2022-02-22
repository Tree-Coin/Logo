

# Imports
# ------------------------------------------------------------------------------
import turtle
import os
from datetime import date, datetime
from PIL import Image, ImageTk, ImageSequence
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.animation as animation
# import io
import tkinter as tk
# import tkinter_gif

# import sys
# def split(word):
#     return [char for char in word]
#
# def numerologic_sum(word):
#     count = 0
#     for i in split(str(word)):
#         count += int(i)
#     # return split(str(word))
#     if(count > 9):
#         return numerologic_sum(str(count))
#     else:
#         return count
#
#     # return count
#
# year = int(datetime.today().strftime('%Y'))
# month = int(datetime.today().strftime('%m'))
# day = int(datetime.today().strftime('%d'))
# sum = year + month + day
# today_number = numerologic_sum(sum)

# class ImageLabel:
#     def __init__(self, canvas):
#         self.canvas = canvas
#
#     def load(self, im, x=0, y=0):
#         # create a canvas image item
#         self.image = self.canvas.create_image(x, y, image=None)
#         self.canvas.tag_lower(self.image)
#
#         if isinstance(im, str):
#             im = Image.open(im)
#
#         self.frames = []
#         try:
#             for i in count(1):
#                 self.frames.append(ImageTk.PhotoImage(im.copy()))
#                 im.seek(i)
#         except EOFError:
#             pass
#
#         try:
#             self.delay = im.info['duration']
#         except:
#             self.delay = 100
#
#         num_frames = len(self.frames)
#         if num_frames == 1:
#             self.canvas.itemconfig(self.image, image=self.frames[0])
#         else:
#             self.next_frame(0, num_frames)
#
#     def unload(self):
#         self.canvas.delete(self.image)
#         self.frames = None
#
#     def next_frame(self, loc, total):
#         if self.frames:
#             self.canvas.itemconfig(self.image, image=self.frames[loc])
#             loc = (loc + 1) % total
#             self.canvas.after(self.delay, self.next_frame, loc, total)
# ------------------------------------------------------------------------------


############################# DRAW ON THE SCREEN  ##############################

import colours
import roots
import tree

################################################################################

def numNodes(root):
    if root == None:
        return 0
    node = 1
    for child in root.children:
        node = node + numNodes(child)
    return node

def save(window):
    date = (datetime.now()).strftime("%Y-%m-%d")
    time = (datetime.now()).strftime("%H:%M:%S-%f")
    current_season = colours.get_current_season()

    sources_path = date + "/"
    files_path = date + "/" + current_season + "/"
    file_name = time + "_" + current_season + " - logo"

    if not os.path.exists(date):
        os.mkdir(date, 0o777)
    if not os.path.exists(sources_path + current_season):
        os.mkdir(sources_path + current_season, 0o777)

    canvas = window.getcanvas()

    # Save SVG file
    # --------------------------
    # svg = canvas.postscript(file=date + "/" + files_path + file_name + ".svg")
    # Save PostScript file
    # ps = canvas.postscript(file=sources_path + file_name + ".ps", colormode='color')
    ps = canvas.postscript(file = sources_path + file_name + ".ps", colormode='color')
    print("Saved img PS: ", files_path + file_name + ".eps")

    # Save EPS file
    # --------------------------
    # img = Image.open(sources_path + file_name + ".eps")
    # s.getcanvas().postscript(file=sources_path + file_name + ".eps")
    eps = canvas.postscript(file = files_path + file_name + ".eps", colormode='color')
    print("Saved img EPS: ", files_path + file_name + ".eps")

    # Save PNG file
    # --------------------------
    im = Image.open(sources_path + file_name + ".ps")
    # pen.getscreen().getcanvas().postscript(file= files_path + file_name+'.eps')
    os.remove(sources_path + file_name + ".ps")
    print("Saved img PNG: ", files_path + file_name + ".png")
    im.save(files_path + file_name + ".png")
    im.close()

    # Save JPG file
    # --------------------------
    # ps = canvas.postscript(colormode='color')
    # img = Image.open(io.BytesIO(ps.encode('utf-8')))

    # img.save(files_path + file_name + ".png", format="PNG")
    # Save PNG file
    # img = Image.open(io.BytesIO(ps.encode("utf-8")))
    # img.save(files_path + file_name + ".png", format="PNG")

    # gif_window = tkinter_gif.ImageLabel(canvas)
    # gif_window.load("giphy.gif", -200, -200) # 0, 0 is the center of canvas

    # x, y = [], []
    # line, = axis.plot(0, 0)
    # def animate(frame_number):
    #     x.append(frame_number)
    #     y.append(frame_number)
    #     line.set_xdata(x)
    #     line.set_ydata(y)
    #     return line,

    # gif_window = tkinter_gif.ImageLabel(canvas)
    # gif_window.load("giphy.gif", -200, -200)

def main():
    date = (datetime.now()).strftime("%Y-%m-%d")
    time = (datetime.now()).strftime("%H:%M:%S-%f")
    current_season = colours.get_current_season()
    files_path = date + "/" + current_season + "/"

    print("\nTREE DRAWER\n----------------------")
    print("Date and time:", date, time)
    print("Current season:", current_season[0].upper() + current_season[1:])
    print("Working directory:", files_path)
    print("")

    # Create 2 Turtle objects
    # 1 for roots and 1 for the tree
    tree_objects = [turtle.Turtle(), turtle.Turtle()]

    # window = (turtle
    # ._screen
    # .getcanvas()
    # .winfo_toplevel())
    window = turtle.Screen()
    window.colormode(255)
    window.setup(2500, 2500)

    # turtle.update()
    # window.tracer(1, 0)
    # window.onclick(lambda x, y: window.update())
    # window.bgcolor("white")

    for tree_object in tree_objects:
        tree_object.hideturtle()
        tree_object.speed('fastest')
        tree_object.fillcolor("")
        # print(tree_object)
        # pen.speed(10)

        #
        # ROOTS
        # Draw the roots
        # -----------------------------------
        roots.draw_roots(tree_object, window)
        # save(window)

        #
        # TREE
        # Draw the roots
        # -----------------------------------
        tree.draw_tree(tree_object, window)
        save(window)

    # update the whole screen now that the new positions have been calculated
    turtle.update()


    window.exitonclick()


# 1 second
s1 = 3600
# 10 seconds
s10 = 36000
# 30 seconds
s30 = 108000
# 60 seconds
s60 = 216000

# turtle = turtle.Turtle()
# sys.setExecutionLimit(s30)
# turtle.hideturtle()
# turtle.setup(1200, 1200)
# turtle.fillcolor("")


# root = tk.Tk()
# root.attributes("-alpha", 0.3)

# s = turtle.getscreen()
#####################################

# Save as file image
# forward(100)
# img_file = "logo.png"
# s.getcanvas().postscript(file="logo.eps")
# pen .getscreen().getcanvas().postscript(file= file_name+'.eps')

# img = Image.open("logo.eps")
# img.save("logo.jpg")

main()
turtle.done()

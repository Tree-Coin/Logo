
# A program that draw on screen the Tree Coin logo
#
# How to launch this program:
# $> cd /mnt/e44cf6f0-0b6d-424f-9f06-7fb57f1cfb2b/home/alessandro/\[\ In\ lavorazione\ \]/IEMO/__logo_generator/
# $> python3 logo_generator.py



import colours

import turtle
import os
from datetime import date, datetime
from PIL import Image, ImageTk, ImageSequence
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.animation as animation
import io
import tkinter as tk
# import tkinter
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

class ImageLabel:
    def __init__(self, canvas):
        self.canvas = canvas

    def load(self, im, x=0, y=0):
        # create a canvas image item
        self.image = self.canvas.create_image(x, y, image=None)
        self.canvas.tag_lower(self.image)

        if isinstance(im, str):
            im = Image.open(im)

        self.frames = []
        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        num_frames = len(self.frames)
        if num_frames == 1:
            self.canvas.itemconfig(self.image, image=self.frames[0])
        else:
            self.next_frame(0, num_frames)

    def unload(self):
        self.canvas.delete(self.image)
        self.frames = None

    def next_frame(self, loc, total):
        if self.frames:
            self.canvas.itemconfig(self.image, image=self.frames[loc])
            loc = (loc + 1) % total
            self.canvas.after(self.delay, self.next_frame, loc, total)

########################### ↓↓↓ DRAW THE SCREEN  ↓↓↓ ###########################

def tree(branchLen, pen, window, deep):
    # print("Tree", deep)
    current_season = colours.get_current_season()

    if branchLen > 1:
        # turtle.pencolor(240,160,80)
        if (branchLen > 60):
            pen.pencolor(colours.color_palette(branchLen))
            pen.width(branchLen/4)
        else:
            pen.pencolor(random.choice(colours.get_season_branch_colours()))
            pen.width(branchLen/5)

        pen.down()
        pen.forward(branchLen)
        pen.right(30) # +30
        tree(branchLen-10, pen, window, 2)

        pen.left(70) # -40
        tree(branchLen-10, pen, window, 3)
        pen.up()
        pen.right(20) # -20
        # pen.pencolor("#E8C995")

        # Frequency of leafs and roots
        tree(branchLen-8, pen, window, 4)
        pen.up()
        # pen.pencolor("#aeff8b")-

        # print(branchLen, pen.pencolor())
        # if(branchLen == 1):
        if(int(branchLen) <= 10):
            tree_colours = colours.get_season_tree_colours()
            today_number = int((datetime.now()).strftime("%d"))

            # if(current_season != "winter"):
            #     # pen.right(80) # +100
            #     # tree(random.choice([
            #     #     branchLen-5,
            #     #     branchLen-3,
            #     #     branchLen-1,
            #     # ]), pen, window, 5)
            #     # pen.left(60) # +40
            #     pen.right(20)
            #     pen.width(random.choice([0.1, 0.8, 1, 2, 4]))
            if(current_season == "winter"):
                pen.right(20)
                pen.width(random.choice([today_number/5, today_number/6, today_number/7]))
            elif(current_season == "autumn"):
                pen.right(20)
                pen.width(random.choice([today_number/8, today_number/9, today_number/10]))
            else:
                pen.right(20)
                pen.width(random.choice([1, 2, 3, 4]))
            # if(current_season == "summer"):
                # This increases the number of leafs but requires a lot of processor
                # ----------------------------------
                # pen.left(60)
                # tree(random.choice([
                #     branchLen-1
                # ]), pen, window, 6)
                # pen.right(60)
                # ----------------------------------

            # pen.pencolor("#E8C995")
            # pen.pencolor("#c2c5aa")
            pen.pencolor(random.choice(tree_colours))
            pen.down()
        else:
            pen.right(20)

            pen.width(0.1)
            pen.pencolor("#AACC00")
            pen.down()


        pen.backward(branchLen)
        pen.up()

#
# TREE
# Draw the tree
# -----------------------------------
def draw_tree(tree_object, window):
    tree_object.left(180)
    tree_object.up()
    tree_object.forward(-90)
    tree_object.down()
    # print(numNodes(pen))
    print("-> Drawing tree...")
    tree(90, tree_object, window, 1)
    # save(window)
    print("   Done")
    # -----------------------------------

# ------------------------------------------------------------------------------

def roots(branchLen, pen, window):
    # if branchLen == 90:
    #     print("ok")
    #     tree(90, pen)
    if branchLen > 1:
        #
        # Generate the first branch
        # ----------------------------------
        #
        pen.pencolor(colours.grey_colours(branchLen))


        # pen.pencolor(214, 255, 196, 0)
        # bg = (255,255,255)
        # fg = (0 / 255, 255 / 255, 0 / 255, 100 / 255)
        #
        # r = int(max(min(((1 - fg[3]) * bg[0]) + (fg[3] * fg[0]), 1), 0))
        # g = int(max(min(((1 - fg[3]) * bg[1]) + (fg[3] * fg[1]), 1), 0))
        # b = int(max(min(((1 - fg[3]) * bg[2]) + (fg[3] * fg[2]), 1), 0))
        # for i in range (75):
        #     pen.pencolor(r,g,b)

        # turtle.pencolor(240,160,80)
        if (branchLen > 60):
            pen.width(branchLen/4)
        else:
            pen.width(branchLen/5)

        if (branchLen < 90):
            pen.forward(branchLen)

        pen.right(30)

        #
        # > Commands to execute on each single branch
        # ----------------------------------
        #
        # Save the branch as image file
        # save(window)

        #
        # ----------------------------------
        #

        #
        # Generate the second branch
        # ----------------------------------
        #
        roots(branchLen-10, pen, window)

        pen.left(60)
        pen.pencolor(254, 254, 254)

        #
        # Generate the third branch
        # ----------------------------------
        #
        roots(branchLen-10, pen, window)

        pen.right(30)
        if(branchLen <= 10):
            pen.width(2)
            pen.down()
        else:
            pen.width(1)
            pen.down()

        pen.backward(branchLen)

#
# ROOTS
# Draw the roots
# -----------------------------------
def draw_roots(tree_object, window):
    tree_object.width(80/3)
    tree_object.pencolor("#fff")
    tree_object.left(-90)
    tree_object.forward(100)
    tree_object.down()
    print("-> Drawing roots...")
    roots(90, tree_object, window)
    print("   Done")
    # -----------------------------------

########################### ↑↑↑ DRAW THE SCREEN  ↑↑↑ ###########################

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
    # window.getcanvas().postscript(file=date + "/" + files_path + file_name + ".svg")

    # name = asksaveasfile(mode='w', defaultextension='.ps')
    ps = canvas.postscript(file = sources_path + file_name + ".ps", colormode='color')
    eps = canvas.postscript(file = files_path + file_name + ".eps", colormode='color')
    print("Saved img PNG: ", files_path + file_name + ".eps")
    im = Image.open(sources_path + file_name + ".ps")
    # pen.getscreen().getcanvas().postscript(file= files_path + file_name+'.eps')

    os.remove(sources_path + file_name + ".ps")
    print("Saved img PNG: ", files_path + file_name + ".png")
    im.save(files_path + file_name + ".png")
    im.close()
    # ps = canvas.postscript(colormode='color')
    # img = Image.open(io.BytesIO(ps.encode('utf-8')))

    # Save PostScript file
    # ps = window.getcanvas().postscript(file=sources_path + file_name + ".ps", colormode='color')
    # Save EPS file
    # img = Image.open(sources_path + file_name + ".eps")
    # s.getcanvas().postscript(file=sources_path + file_name + ".eps")

    # Save JPG file
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

    tree = [turtle.Turtle(), turtle.Turtle()]

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

    for tree_object in tree:
        tree_object.hideturtle()
        tree_object.speed('fastest')
        tree_object.fillcolor("")
        # print(tree_object)
        # pen.speed(10)

        #
        # ROOTS
        # Draw the roots
        # -----------------------------------
        draw_roots(tree_object, window)
        save(window)

        #
        # TREE
        # Draw the roots
        # -----------------------------------
        draw_tree(tree_object, window)
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

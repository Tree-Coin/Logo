
import colours




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


from datetime import date, datetime
import random
import colours


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

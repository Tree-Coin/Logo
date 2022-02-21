
from datetime import date, datetime
import random

def grey_colours(branchLen):
    # COLORS = [(139, 0, 0),
    #       (0, 100, 0),
    #       (0, 0, 139)]
    # if (branchLen == 120):
    #     r = random.randint(180,180)-branchLen
    #     g = 255 - random.randint(70,75) - branchLen
    #     b = random.randint(60,60)
    # else:
    rand = random.randint(250,255);
    r = rand - int((branchLen/4))
    g = rand - int((branchLen/4))
    b = rand - int((branchLen/4))
    rgb = [r,g,b]
    # print("root", r, g, b, branchLen)
    return rgb

# Color palette
def color_palette(branchLen):
    # ---------------
    #  URL: https://coolors.co
    if(branchLen == 1):
        hex = "#eae4e9"
    if(branchLen == 10) :
        # LEAF
        # ---------------------
        # Sage
        # hex = "#a4ac86"
        #
        # hex = random.choice(["#ccd5ae", "#e9edc9", "#e9edc9", "#fefae0", "#faedcd", "#9e2a2b"])
        #
        hex = random.choice(get_season_tree_colours())
    elif(branchLen <= 30) :
        # Spanish Bistre
        hex = "#788e2f"
    elif(branchLen > 30 and branchLen <= 40) :
        # Dark Olive Green
        hex = "#566d2e"
    elif(branchLen > 40 and branchLen <= 60) :
        # Hunter Green
        hex = "#45613d"
    elif(branchLen > 60 and branchLen <= 70) :
        # Kombu Green
        hex = "#334729"
    elif(branchLen > 70 and branchLen <= 80) :
        # Rifle Green
        hex = "#454524"
    elif(branchLen > 80) :
        # Dark Liver Horses
        hex = "#4b3830"
    return hex

def get_season_tree_colours():
    current_season = get_current_season()
    # print(current_season)

    if (current_season == "winter"):
        # Winter palette
        # https://coolors.co/dfe7fd-cddafd-eae4e9-fff1e6-fde2e4-fad2e1-f0efeb-e2ece9-d0e7e8-bee1e6
        tree_colours = [
            "#dfe7fd",
            "#eae4e9",
            "#fcf7f8",
            "#f0efeb",
            "#e2ece9",
            "#d0e7e8",
            "#bee1e6",
            "#cfdbcc",
            "#eff2ef",
            "#e7ede6"
        ]
    elif (current_season == "spring"):
        tree_colours = [
            "#007f5f",
            "#2b9348",
            "#55a630",
            "#80b918",
            "#aacc00",
            "#bfd200",
            "#d4d700",
            "#dddf00",
            "#eeef20",
            "#ffff3f"
        ]
    elif (current_season == "summer"):
        tree_colours = [
            "#ff4800",
            "#ff5400",
            "#ff6000",
            "#ff6d00",
            "#ff7900",
            "#ff8500",
            "#ff9100",
            "#ff9e00",
            "#ffaa00",
            "#ffb600",
            "#dddf00",
            "#eeef20",
            "#ffff3f"
        ]
    elif (current_season == "autumn"):
        tree_colours = [
            "#b1150c",
            "#970f08",
            "#7c0903",
            "#6a1609",
            "#4b1101",
            "#652c18",
            "#773c07",
            "#a46728",
            "#d69c52",
            "#daa562"
        ]
    return tree_colours

def get_season_branch_colours():
    current_season = get_current_season()
    # print(current_season)

    if (current_season == "winter"):
        branch_colours = [
            "#45613d",
            "#334729",
            "#454524",
            "#4b3830"
        ]
    elif (current_season == "spring"):
        branch_colours = [
            "#788e2f",
            "#566d2e",
            "#45613d",
            "#334729",
            "#454524",
            "#4b3830"
        ]
    elif (current_season == "summer"):
        branch_colours = [
            "#566d2e",
            "#45613d",
            "#334729",
            "#454524",
            "#4b3830"
        ]
    elif (current_season == "autumn"):
        branch_colours = [
            "#45613d",
            "#334729",
            "#454524",
            "#4b3830"
        ]

    return branch_colours

def get_current_season():
    Y = int((datetime.now()).strftime("%Y"))
    seasons = [
        ("winter", (date(Y,  1,  1), date(Y,  3, 20))),
        ("spring", (date(Y,  3, 21), date(Y,  6, 20))),
        ("summer", (date(Y,  6, 21), date(Y,  9, 22))),
        ("autumn", (date(Y,  9, 23), date(Y, 12, 20))),
        ("winter", (date(Y, 12, 21), date(Y, 12, 31)))
    ]
    now = date.today()
    now = now.replace(year=Y)

    # return next(season for season, (start, end) in seasons
    #         if start <= now <= end)
    return "autumn"

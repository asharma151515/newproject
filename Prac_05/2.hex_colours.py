COLOURS = {"aquamarine1": "#7fff d4", "DarkOrange": "#ff8c00", "DarkOrchid3": "#9a32cd", "cyan1": "#00ffff",
           "OrangeRed1": "#ff4500", "SeaGreen2": "#4eee94", "SpringGreen1": "#00ff7f", "purple": "#a020f0",
           "plum3": "#cd96cd", "PeachPuff1": "#ffdab9"}

for colour_name, colour_code in COLOURS.items():
    print("{:<12} - {:<8}".format(colour_name, colour_code))

enter_colour_name = input("Please enter a colour name: ")
while enter_colour_name != "":
    if enter_colour_name in COLOURS:
        print("{} is {}".format(enter_colour_name, COLOURS[enter_colour_name]))
    else:
        print("The colour you have entered is invalid.")
    enter_colour_name = input("Please enter a colour name: ")

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
all_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(all_fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in all_fonts:
        f = sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


figlet.setFont(font=f)


user = input("Input: ")
print(figlet.renderText(user))



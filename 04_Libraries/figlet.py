import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) < 2:
    user_font = random.choice(fonts)
elif len(sys.argv) == 2:
    sys.exit("Too few arguments")
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("not font word")
    elif sys.argv[2] not in fonts:
        sys.exit("not in fonts")
    user_font = sys.argv[2]
else:
    sys.exit("Too many arguments")

user_input = str(input("Input: "))
figlet.setFont(font=user_font)
print(f"Output:\n {figlet.renderText(user_input)}")
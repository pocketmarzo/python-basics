import time
from colorama import Fore, Style, init
init(autoreset=True)

text = input("Input your text: ")
direction = input("Direction: R or L?").upper().strip()
speed = float(input("Enter speed: "))
window_size = 30

if len(text) < window_size:
    text = text + " " * (window_size - len(text) + 5)

color = input("Do you like add some color('Yes' or 'Not')").strip().lower()
choosen_color = ""

if color == "yes":
    color_choice = input("Choise: 'G' - green, 'R' - red, 'Y' - yellow : ").upper().strip()
    
    if color_choice == "G":
        choosen_color = Fore.GREEN
    elif color_choice == "R":
        choosen_color = Fore.RED
    elif color_choice == "Y":
        choosen_color = Fore.YELLOW


try:
    print("\n--- Running! Press Ctrl+C to stop ---\n")    

    while True:

        if direction == "R":
            text = text[-1] + text[:-1]
        else:        
            text = text[1:] + text[0]
        print(choosen_color + text[:window_size] + Style.RESET_ALL, end="\r", flush=True)
        time.sleep(speed)

except KeyboardInterrupt:
    print("")
    print("Program finished")
    
    
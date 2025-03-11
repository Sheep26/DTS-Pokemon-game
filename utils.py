import os

def clear():
    # Clear the console
    # Windows uses the command cls to clear and linux uses the command clear
    os.system('cls' if os.name == 'nt' else 'clear')
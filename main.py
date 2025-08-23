# main.py
import os
import subprocess
from colorama import Fore, Back, Style, init

init(autoreset=True)

# ===========================================
# Banner
# ===========================================
def banner():
    print(Fore.CYAN + Style.BRIGHT + """
╔════════════════════════════════════════╗
║       Welcome to RH Professional CLI   ║
║       Developed by RH Hasan            ║
║       Telegram: t.me/Romzan_99        ║
╚════════════════════════════════════════╝
""")

# ===========================================
# List files in current directory
# ===========================================
def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(Fore.YELLOW + "\nAvailable files to run:")
    for f in files:
        print(Fore.GREEN + " - " + f)
    print(Fore.MAGENTA + "\nType the file name (without extension) to run it, or 'back' to return.\n")

# ===========================================
# Run selected file
# ===========================================
def run_file(file_name):
    file_executed = False
    # Check for Python file
    if os.path.exists(file_name + ".py"):
        subprocess.run(["python3", file_name + ".py"])
        file_executed = True
    # Check for Bash file
    elif os.path.exists(file_name + ".sh"):
        subprocess.run(["bash", file_name + ".sh"])
        file_executed = True
    else:
        print(Fore.RED + "File not found!")

    if file_executed:
        print(Fore.CYAN + "\nTask completed. Type 'back' to return to main menu.\n")
        while True:
            back_input = input(Fore.YELLOW + ">>> ").strip().lower()
            if back_input == "back":
                break

# ===========================================
# Main loop
# ===========================================
def main():
    while True:
        os.system('clear')
        banner()
        list_files()
        choice = input(Fore.CYAN + "Enter file name or 'back': ").strip()
        if choice.lower() == 'back':
            print(Fore.GREEN + "\nReturning to main menu...\n")
            continue
        else:
            run_file(choice)

if __name__ == "__main__":
    main()

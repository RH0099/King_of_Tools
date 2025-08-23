import os
import subprocess
from colorama import Fore, Back, Style, init

init(autoreset=True)

# ===========================================
# Banner
# ===========================================
def banner():
    print(Fore.CYAN + Style.BRIGHT + """
╔══════════════════════════════════╗
║      Welcome to My Tool v1.0     ║
║   Developed by RH Hasan          ║
║   Telegram: t.me/Romzan_99       ║
╚══════════════════════════════════╝
    """)

# ===========================================
# List files in current directory
# ===========================================
def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print(Fore.YELLOW + "\nAvailable files to run:")
    for f in files:
        print(" - " + f)
    print(Fore.GREEN + "\nType the file name (without extension) to run it, or 'back' to return.\n")

# ===========================================
# Run selected file
# ===========================================
def run_file(file_name):
    # Search for .py or .sh
    if os.path.exists(file_name + ".py"):
        subprocess.run(["python3", file_name + ".py"])
    elif os.path.exists(file_name + ".sh"):
        subprocess.run(["bash", file_name + ".sh"])
    else:
        print(Fore.RED + "File not found!")
    input(Fore.MAGENTA + "\nPress Enter to go back to main menu...")

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
            continue  # stays in main loop
        else:
            run_file(choice)

if __name__ == "__main__":
    main()
             

import time
import ctypes
from colorama import init, Fore, Style

init() # initialising colorama module-

def main():
    
    mutex = ctypes.windll.kernel32.CreateMutexW(None, True, "ROBLOX_singletonMutex") # locking thread

    print(Fore.GREEN + "Running multi-intance\n")
    print(Fore.RED + "Please do not close this window.")
    print(Fore.WHITE + Style.RESET_ALL)
    
    try:
        while True: # keeps program running
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting program...")

if __name__ == "__main__":
    main()

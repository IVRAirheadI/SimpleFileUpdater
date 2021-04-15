import urllib.request
from urllib.request import urlopen, Request
import requests
import colorama
import time
import os
import ctypes
from colorama import init,Fore
init()
ctypes.windll.kernel32.SetConsoleTitleW(f' FILE | UPDATER')

print(f'''{Fore.LIGHTBLUE_EX}
                                ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗
                                ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
                                ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
                                ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
                                ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
                                 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
''' + Fore.RESET)
print(f'{Fore.LIGHTBLUE_EX}' '━' * os.get_terminal_size().columns)
print(f"{Fore.LIGHTBLUE_EX}[1] Update/Download All Files\n[2] File.exe\n[3] AnotherFile.json")


choice = input(f"Selection: ")
if choice == "1":
    print(f"{Fore.LIGHTBLUE_EX}Downloading All Files, This May Take Awhile...")
    PASTYBOY = urlopen(Request("RAWPASTEBINLINK1")).read().decode() # raw pastebin links are used so you can upload direct file links you want to it, and it reads that file link
    PASTYBOY2 = urlopen(Request("RAWPASTEBINLINK2")).read().decode()
    PASTYBOY3 = urlopen(Request("RAWPASTEBINLINK3")).read().decode()
    File1 = f'{PASTYBOY}' # These are whats gonna be used to make the requests
    File2 = f'{PASTYBOY2}'
    File3 = f'{PASTYBOY3}'
    File_r = requests.get(File1, allow_redirects=True) # makes the request to the given link, to then download that file
    File2_r = requests.get(File2, allow_redirects=True)
    File3_r = requests.get(File3, allow_redirects=True)
    open('File.exe', 'wb').write(File_r.content) # overwrites/downloads the file
    open('AnotherFile.json', 'wb').write(File2_r.content)
    open('MoreFile.zip', 'wb').write(File3_r.content)
    print(f'{Fore.GREEN}All Files Downloaded Successfully')
    time.sleep(1)
    choice = input(f"{Fore.WHITE}Selection: ")
if choice == "2":
    print(f"{Fore.LIGHTBLUE_EX}Fetching File.exe...")
    PASTYBOY = urlopen(Request("RAWPASTEBINLINK1")).read().decode()
    File8 = f'{PASTYBOY}'
    File8_r = requests.get(File8, allow_redirects=True)
    open('File.exe', 'wb').write(selfbot8_r.content)
    print(f'{Fore.GREEN}Successfully Downloaded File.exe')
    time.sleep(1)
    choice = input(f"{Fore.WHITE}Selection: ")
if choice == "3":
    print(f'{Fore.LIGHTBLUE_EX}Fetching AnotherFile.json...')
    time.sleep(1)
    PASTYBOY2 = urlopen(Request("RAWPASTEBINLINK3")).read().decode()
    File2 = f'{PASTYBOY2}'
    File2_r = requests.get(File2, allow_redirects=True)
    open('AnotherFile.json', 'wb').write(selfbot9_r.content)
    print(f'{Fore.LIGHTBLUE_EX}Downloading AnotherFile.json')
    time.sleep(2)
    print(f'{Fore.GREEN}Successfully Downloaded AnotherFile.json')
    time.sleep(1)
    choice = input(f"{Fore.WHITE}Selection: ")

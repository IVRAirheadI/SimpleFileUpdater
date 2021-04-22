import os
from colorama import init, Fore
from requests import get
init()
print("\33]0; FILE | UPDATER\a")


# Easily add filenames with their url here #
data = {
    "File.exe": {"url": "RAW PASTEBIN HERE"},
    "AnotherFile.json": {"url": "RAW PASTEBIN HERE"},
    "MoreFile.zip": {"url": "RAW PASTEBIN HERE"},
    "methods": []
}

for x in list(data.keys())[:-1]:
    data["methods"] += [f"{x}"]


def main():
    print(f'''{Fore.LIGHTBLUE_EX}
                    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██████╗
                    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
                    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██████╔╝
                    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗
                    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██║  ██║
                     ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    ''')
    print('━' * os.get_terminal_size().columns)
    counter = 2
    print("[1] Update/Download All Files")
    for x in data["methods"]:
        print(f"[{counter}] {x}")
        counter += 1
    print(Fore.RESET)
    choice = int(input(f"Selection: "))
    menu(choice)


def menu(choice):
    os.system('cls')
    if choice == 1:
        downloadAll()
        main()
    else:
        try:
            choice -= 2
            downloadFile(choice)
            main()
        except:
            print(f'{Fore.YELLOW}Choose a valid option!')
            main()


# FUNCTIONS #


def downloadAll():
    print(f"{Fore.LIGHTBLUE_EX}Downloading All Files, This May Take Awhile...\n")
    # raw pastebin links are used so you can upload direct file links you want to it, and it reads that file link
    fails = 0
    success = True
    for file in data:
        if file != "methods":
            urlFile = data[file]["url"]
            try:
                fileDownload = get(urlFile).content.decode()
                # overwrites/downloads the file
                open(file, 'w').write(fileDownload)
            except:
                success = False
                fails += 1
                print(
                    f"{Fore.RED}Failed to download {file}, is the URL correct?\nURL: {urlFile}\n")
    if success:
        print(f'{Fore.GREEN}All Files Downloaded Successfully')
    else:
        print(f'{Fore.YELLOW}Failed to download {fails} files')


def downloadFile(pos: int):
    file = list(data.keys())[pos]
    urlFile = data[file]["url"]
    success = True
    print(f"{Fore.LIGHTBLUE_EX}Fetching {file}...")
    try:
        fileDownload = get(urlFile).content.decode()
        open(file, 'w').write(fileDownload)
    except:
        success = False
        print(
            f"{Fore.RED}Failed to download {file}, is the URL correct?\nURL: {urlFile}\n")
    if success:
        print(f'{Fore.GREEN}Successfully Downloaded {file}')


if __name__ == "__main__":
    main()

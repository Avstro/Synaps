import os
import time
import pyautogui
import webbrowser
import subprocess

print("Synaps Beta-Test.")
print("Enter Command.")

while True:
    cmd = input("")

    if cmd == "get.version":
        print("Synaps 0.0.5")

    if cmd == "system.hotkey()":
        print("cmd address: system")
        print("enter Hotkey 1.")
        hotkey1 = input("")

        print("enter Hotkey 2.")
        hotkey2 = input("")

        pyautogui.hotkey(hotkey1, hotkey2)

    if cmd == "system.site()":
        print("cmd address: site")
        print("enter URL to open.")
        url = input("")
        webbrowser.open(url, new=0, autoraise=True)

    if cmd == "folder.create()":
        print("Enter folder path:")
        folder_path = input("")
        os.makedirs(folder_path, exist_ok=True)
        print("Folder created.")

    if cmd == "file.info()":
        print("Enter file path:")
        file_path = input("")
        file_info = os.stat(file_path)
        print("Size:", file_info.st_size, "bytes")
        print("Created:", file_info.st_ctime)
        print("Modified:", file_info.st_mtime)

    if cmd == "synaps.open()":
        print("Enter file path:")
        file_path = input("")
        subprocess.call(["start", file_path], shell=True)

    if cmd == "synaps.delete()":
        print("synaps address: delete")
        print("enter file to delete.")
        print("warning: this command in beta test!")
        file = input("")
        cur_file = file
        os.remove(cur_file)

    if cmd == "cmd.import()":
        print("Importing cmd to Synaps...")
        time.sleep(2)
        print("Enter command:")
        command = input("")
        os.system(command)

    if cmd == "python.execute()":
        print("Enter path to Python script:")
        script_path = input("")
        subprocess.call(["python", script_path])

    if cmd == "folder.open()":
        print("Enter folder path:")
        folder_path = input("")
        subprocess.call(["explorer", folder_path])

    if cmd == "file.search()":
        print("Enter search path:")
        search_path = input("")
        print("Enter file name to search:")
        file_name = input("")

        for root, dirs, files in os.walk(search_path):
            for file in files:
                if file_name in file:
                    print(os.path.join(root, file))

    if cmd == "system.shutdown()":
        confirm = input("enter code to confirm: 9120")
        if confirm.lower() == "9120":
            os.system("shutdown /s /t 0")
            break

    if cmd == "system.restart()":
        confirm = input("enter code to confirm: 9120")
        if confirm.lower() == "9120":
            os.system("shutdown /r /t 0")
            break

    if cmd == "file.info()":
        print("Enter file path:")
        file_path = input("")
        file_info = os.stat(file_path)
        print("Size:", file_info.st_size, "bytes")
        print("Created:", file_info.st_ctime)
        print("Modified:", file_info.st_mtime)

    else:
        print("Command not found.")
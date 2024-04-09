import subprocess
import os
import getpass

def search_for_python_exe():
    try:
        User = getpass.getuser()
        for root, dirs, files in os.walk(f"C:\\Users\\{User}\\AppData\\Local\\Programs\\Python"):
            if "python.exe" in files:
                python_path = os.path.join(root, "python.exe")
                return python_path

        print("Python executable not found.")
        return None
    except Exception as e:
        print("Error occurred during Python executable search:", e)
        return None

def get_directories():
    try:
        result = subprocess.run('wmic logicaldisk get name', shell=True, check=True, capture_output=True, text=True)
        output = result.stdout
        lines = output.split('\n')[1:]
        directories = [line.strip() + '\\' for line in lines if line.strip()]
        return directories
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return []

def search_for_application(app_name, max_depth=5):
    try:
        root_directories = get_directories()
        for root_dir in root_directories:
            for root, dirs, files in os.walk(root_dir):
                for file in files:
                    if file.endswith(os.path.basename(app_name)):
                        full_path = os.path.join(root, file)
                        if full_path.endswith(app_name):
                            return full_path
        print(f"Application Broke while Searching for {app_name}")
        return None
    except Exception as e:
        print("Error occurred during application search:", e)
        return None

def check_create_txt_file():
    file_path = os.path.join(os.path.dirname(__file__), "SteamPath.txt")
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            steam_path = search_for_application("steam.exe")
            file.write(steam_path)
    else:
        print("SteamPath.txt already exists.")

def print_welcome():
    print("\n ")
    print(r"_____/\\\\\\\\\\\___________________________________________________________________")
    print(r" ___/\\\/////////\\\_________________________________________________________________")
    print(r"  __\//\\\______\///______/\\\________________________________________________________")
    print(r"   ___\////\\\__________/\\\\\\\\\\\_____/\\\\\\\\___/\\\\\\\\\_______/\\\\\__/\\\\\___ ")
    print(r"    ______\////\\\______\////\\\////____/\\\/////\\\_\////////\\\____/\\\///\\\\\///\\\_")
    print(r"     _________\////\\\______\/\\\_______/\\\\\\\\\\\____/\\\\\\\\\\__\/\\\_\//\\\__\/\\\_")
    print(r"      __/\\\______\//\\\_____\/\\\_/\\__\//\\///////____/\\\/////\\\__\/\\\__\/\\\__\/\\\_")
    print(r"       _\///\\\\\\\\\\\/______\//\\\\\____\//\\\\\\\\\\_\//\\\\\\\\/\\_\/\\\__\/\\\__\/\\\_")
    print(r"        ___\///////////_________\/////______\//////////___\////////\//__\///___\///___\///__")
    print(r"__/\\\\\\\\\\\\\____/\\\\\\______________________________________________")
    print(r" _\/\\\/////////\\\_\////\\\_________________________________/\\\_________")
    print(r"  _\/\\\_______\/\\\____\/\\\________________________________\/\\\_________")
    print(r"   _\/\\\\\\\\\\\\\\_____\/\\\________/\\\\\________/\\\\\\\\_\/\\\\\\\\____")
    print(r"    _\/\\\/////////\\\____\/\\\______/\\\///\\\____/\\\//////__\/\\\////\\\__")
    print(r"     _\/\\\_______\/\\\____\/\\\_____/\\\__\//\\\__/\\\_________\/\\\\\\\\/___")
    print(r"      _\/\\\_______\/\\\____\/\\\____\//\\\__/\\\__\//\\\________\/\\\///\\\___")
    print(r"       _\/\\\\\\\\\\\\\/___/\\\\\\\\\__\///\\\\\/____\///\\\\\\\\_\/\\\_\///\\\_")
    print(r"        _\/////////////____\/////////_____\/////________\////////__\///____\///__")
    print("\nby Fish")
def start_steamcuck():
    print_welcome()
    check_create_txt_file()
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = current_directory + r"\SteamBlockButBetter.py"
    pythonpath = search_for_python_exe()
    powershell_command = f'Start-Process -Verb RunAs {pythonpath} "{path}"'
    try:
        subprocess.run(['powershell', '-Command', powershell_command], check=True)
        print("PowerShell command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing PowerShell command: {e}")

start_steamcuck()

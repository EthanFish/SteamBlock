import subprocess
import os
def print_header():
    print(r"  ___ _                  ")
    print(r" / __| |_ ___ __ _ _ __  ")
    print(r" \__ \  _/ -_) _` | '  \ ")
    print(r" |___/\__\___\__,_|_|_|_|")
    print(r"  ___ _         _        ")
    print(r" | _ ) |___  __| |__     ")
    print(r" | _ \ / _ \/ _| / /     ")
    print(r" |___/_\___/\__|_\_\     ")
    print(r"==========================")

def get_valid_input(valid_inputs):
    while True:
        user_input = input(">")
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input. Please try again.")

def clear_screen():
    try:
        subprocess.run(['cls'], shell=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)


def add_firewall_rule(rule_name):
    try:
        subprocess.run(
            f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=block program="{steam_path}" enable=yes profile=Any')
        subprocess.run(
            f'netsh advfirewall firewall add rule name="{rule_name}" dir=out action=block program="{steam_path}" enable=yes profile=Any')
        print("Firewall rule added successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        exit()

def check_firewall_rule_existence(rule_name):
    try:

        output = subprocess.check_output(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=' + rule_name], stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

def delete_firewall_rule(rule_name):
    try:
        subprocess.run(f'netsh advfirewall firewall delete rule name="{rule_name}"', shell=True, check=True)
        print(f"Firewall rule '{rule_name}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        exit()

def read_steam_path():
    file_path = os.path.join(os.path.dirname(__file__), "SteamPath.txt")
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            steam_path = file.readline().strip()
        return steam_path
    else:
        print("SteamPath.txt does not exist.")
        return None

if __name__ == "__main__":
    rule_name = "FishSteamBlock"
    steam_path = read_steam_path()
    while True:
        os.system(f'mode con: cols={75} lines={20}')
        clear_screen()
        print_header()
        if check_firewall_rule_existence(rule_name) == True:
            print("Status")
            print("\033[1;32m Active \n")
            print("\033[1;37m\n[1] - Disable block\n\n[2] - Exit\n")
            valid_inputs = ["1", "2"]
            user_input = get_valid_input(valid_inputs)
            if user_input == "1":
                delete_firewall_rule(rule_name)
            if user_input == "2":
                exit()
            clear_screen()
            print_header()

        if check_firewall_rule_existence(rule_name) == False:
            print("Status")
            print("\033[1;31m Inactive \n")
            print("\033[1;37m\n[1] - Enable block\n\n[2] - Exit\n")
            valid_inputs = ["1", "2"]
            user_input = get_valid_input(valid_inputs)
            if user_input == "1":
                add_firewall_rule(rule_name)
            if user_input == "2":
                exit()


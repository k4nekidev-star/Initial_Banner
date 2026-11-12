
import json
from os import system
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    COLORS = {
        "red": "RED",
        "green": "GREEN",
        "blue": "BLUE",
        "cyan": "CYAN",
        "yellow": "YELLOW"
    }

    SHELLS = {
        "fish": "fish",
        "bash": False
    }

    YES_NO = {
        "yes": True,
        "y": True,
        "no": False,
        "n": False
    }

    def __init__(self):
        self.json_config = BASE_DIR / "config" / "config.json"
        self.banner_config = BASE_DIR / "config" / "banner.txt"

    def Read_file(self):
        with open(self.json_config, "r", encoding="utf-8") as file:
            return json.load(file)

    def Save_file(self, config):
        with open(self.json_config, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)

    def ask(self, message, options):
        while True:
            user = input(message).strip().lower()

            if user in options:
                return options[user]

            print("Invalid option. Try again.")

    def Realize_changes(self):

        while True:
            config = self.Read_file()

            print("Configurations")

            config["animation"] = self.ask(
                "ANIMATION [yes/no]: ",
                self.YES_NO
            )

            config["banner_color"] = self.ask(
                "BANNER COLOR [Red/Green/Blue/Cyan/Yellow]: ",
                self.COLORS
            )

            config["shell"] = self.ask(
                "SHELL [fish/bash]: ",
                self.SHELLS
            )
            
            user = input("Banner text: ")
            system(f"figlet {user} > {self.banner_config}")

            system("clear")

            print("Configuration summary")
            print("---------------------")

            for key, value in config.items():
                if key != "open_for_first_time":
                    print(f"{key}: {value}")

            save = self.ask(
                "Save changes? [yes/no]: ",
                self.YES_NO
            )

            if save:
                self.Save_file(config)
                print("Saved...")
                return

            system("clear")


import json
import subprocess
from os import system
from pathlib import Path
from shutil import which


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

    DEPENDENCIES = {
        "packages": [
            "figlet",
            "fish"
        ],
        "python": [
            "colorama"
        ]
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

    
    def Install_dependencies(self):
        import sys
        from importlib.util import find_spec
    
        missing_packages = [
            dependency
            for dependency in self.DEPENDENCIES["packages"]
            if which(dependency) is None
        ]
    
        missing_python = [
            dependency
            for dependency in self.DEPENDENCIES["python"]
            if find_spec(dependency) is None
        ]
    
        if missing_packages:
            print("Installing system dependencies...")
    
            try:
                subprocess.run(
                    ["pkg", "install", "-y", *missing_packages],
                    check=True
                )
            except (subprocess.CalledProcessError, FileNotFoundError) as error:
                print(f"System installation error: {error}")
                return False
    
        if missing_python:
            print("Installing Python dependencies...")
    
            try:
                subprocess.run(
                    [
                        sys.executable, "-m", "pip",
                        "install", *missing_python
                    ],
                    check=True
                )
            except (subprocess.CalledProcessError, FileNotFoundError) as error:
                print(f"Python installation error: {error}")
                return False
    
        print("All dependencies are installed.")
        return True


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

            with open(self.banner_config, "w", encoding="utf-8") as file:
                subprocess.run(
                    ["figlet", user],
                    stdout=file,
                    check=True
                )

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

    def Initial_setup(self):
        config = self.Read_file()

        if config.get("open_for_first_time", False):

            if not self.Install_dependencies():
                return False

            self.Realize_changes()

            config = self.Read_file()
            config["open_for_first_time"] = False
            self.Save_file(config)

        return True

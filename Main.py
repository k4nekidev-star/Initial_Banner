
import sys, time, json, shutil, os
from colorama import init, Fore
from os import system
import configfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Banner:
    def __init__(self, default_velocity, banner_velocity, borders_velocity):
        init(autoreset=True)
        self.version = 2.10
        self.default_velocity = default_velocity
        self.banner_velocity = banner_velocity
        self.borders_velocity = borders_velocity
        self.path = BASE_DIR / "config" / "banner.txt"
        self.json_config = BASE_DIR / "config" / "config.json"
        self.banner_color = self.color()

    def print_banner(self, args, args2=str):

        size = shutil.get_terminal_size()
        size = size.columns

        if os.path.exists(args):

            with open(args, 'r') as file:
                j = []
                for i in file.read().split("\n"):
                    j.append(i)
                banner_len = len(j[0])

            banner = []
            with open(args, 'r') as file:
                for i in file.read().split("\n"):
                    a = int((size-banner_len) / 2)
                    banner = " "*a+i+" "*a
                    self.write(banner, velocity=self.banner_velocity, color=self.banner_color)

        else:
            banner_size = int((size - len(args)) / 2)
            banner = args2*banner_size+args+args2*banner_size+"\n"
            self.write(banner, velocity=self.borders_velocity, color=Fore.GREEN)

    def Read_file(self):
        with open(self.json_config, 'r') as file:
            return json.loads(file.read())

    def Save_file(self, config):
        with open(self.json_config, 'w') as file:
            json.dump(config, file, indent=4)

    def first_time(self):
        file_conf = self.Read_file()

        if file_conf["open_for_first_time"]:
            config = configfile.Config()

            # Install dependencies
            if not config.Install_dependencies():
                return False

            # Initial configuration
            config.Realize_changes()

            # Update first execution status
            file_conf = config.Read_file()
            file_conf["open_for_first_time"] = False
            config.Save_file(file_conf)

        return True

    def color(self):
        colors = {
            "RED": Fore.RED,
            "GREEN": Fore.GREEN,
            "YELLOW": Fore.YELLOW,
            "CYAN": Fore.CYAN,
            "BLUE": Fore.BLUE
        }

        config = self.Read_file()
        color = config["banner_color"]

        if color in colors.keys():
            return colors[color]
        else:
            return Fore.WHITE

    def write(self, text, velocity, color=Fore.WHITE):
        for i in text:
            sys.stdout.write(color + i)
            sys.stdout.flush()
            time.sleep(velocity)
        print()

    def banner(self):

        system("clear")
        self.print_banner("CTR+C_to_skip", "_")
        self.print_banner("Iniciando Ajustes...", " ")
        self.print_banner("_", "_")
        self.print_banner("Bienvenido_Señor", " ")

        self.print_banner(self.path)

        self.print_banner("_", "_")

    def cmds(self):
        fish = self.Read_file()

        if fish["shell"] == "fish":
            system("fish")
        else:
            pass

    def run(self):

        if not self.first_time():
            return

        self.banner_color = self.color()

        try:
            self.banner()
            self.cmds()

        except KeyboardInterrupt:
            self.default_velocity = 0
            self.banner_velocity = 0
            self.borders_velocity = 0
            self.banner()
            self.cmds()


if __name__ == "__main__":

    with open(BASE_DIR / "config" / "config.json", "r", encoding="utf-8") as animation:
        if json.load(animation)["animation"]:
            banner = Banner(
                default_velocity=0.02,
                banner_velocity=0.005,
                borders_velocity=0.007
            )
        else:
            banner = Banner(
                default_velocity=0.0,
                banner_velocity=0.0,
                borders_velocity=0.0
            )

        banner.run()

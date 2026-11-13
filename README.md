Initial Banner

<p align="center">
  <b>A customizable terminal startup banner for Termux.</b>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Version-2.10-red?style=for-the-badge" />
</p>---

About

Initial Banner is a Python-based startup customization project designed for Termux.

It displays a personalized ASCII banner whenever a new Bash session starts, providing a customizable terminal welcome experience.

The project includes configurable text animations, banner colors, shell selection and startup settings.

Features

- ASCII Banner: Displays a custom banner when starting the terminal.
- Text Animation: Enables or disables character-by-character printing.
- Custom Colors: Choose between red, green, blue, cyan and yellow.
- Shell Selection: Choose between Fish and the default Bash behavior.
- Configuration System: Stores user preferences in a JSON file.
- First Startup Configuration: Automatically launches the initial configuration when needed.
- Keyboard Interruption: Press "CTRL + C" to skip the startup animation.
- Automatic Updates Setting: Includes a configuration option for automatic updates.

Installation

1. Update Termux

pkg update && pkg upgrade -y

2. Install dependencies

pkg install git python -y

Install the Python dependency:

pip install colorama

If you want to use Fish:

pkg install fish -y

3. Clone the repository

git clone https://github.com/k4nekidev-star/Initial_Banner.git

4. Enter the project directory

cd Initial_Banner

5. Check the project structure

Make sure the files are organized as follows:

Initial_Banner/
│
├── Main.py
├── configfile.py
├── banner.txt
│
└── config/
    └── config.json

6. Test the program

Before adding it to your startup configuration, run:

python Main.py

On the first launch, the configuration wizard will ask you to customize the program.

Automatic startup with Bash

To display Initial Banner whenever you open a new Bash session, add it to your ".bashrc".

1. Open your Bash configuration

nano ~/.bashrc

2. Add the following code at the end

# Initial Banner
if [[ $- == *i* ]] && [[ -f "$HOME/Initial_Banner/Main.py" ]]; then
    python "$HOME/Initial_Banner/Main.py"
fi

3. Save the changes

In Nano:

- "CTRL + O" to save.
- "ENTER" to confirm.
- "CTRL + X" to exit.

4. Reload Bash

source ~/.bashrc

You can also close and reopen your Termux session.

Note: This configuration assumes that you cloned the repository inside your Termux home directory.

Configuration

Initial Banner uses a JSON configuration file located at:

config/config.json

Example:

{
    "animation": true,
    "banner_color": "RED",
    "shell": "fish",
    "auto_update": true,
    "open_for_first_time": false
}

Available options

Option| Description
"animation"| Enables or disables text animation.
"banner_color"| Sets the banner color.
"shell"| Selects Fish or default Bash behavior.
"auto_update"| Stores the automatic update preference.
"open_for_first_time"| Controls the initial configuration wizard.

Banner colors

Available colors:

- "RED"
- "GREEN"
- "BLUE"
- "CYAN"
- "YELLOW"

Shell selection

Fish: Launches Fish after displaying the banner.

Bash: Leaves the current Bash session running without launching another Bash process.

Controls

Key| Action
"CTRL + C"| Interrupts the startup animation and displays the banner immediately.

Troubleshooting

The banner does not appear

Check that the startup code is present in your ".bashrc" and that the project is located at:

~/Initial_Banner/

Missing Python dependencies

pip install colorama

Fish does not start

Check that Fish is installed:

pkg install fish

Configuration problems

Check that "config/config.json" exists and contains valid JSON.

Author

k4nekidev-star

GitHub: https://github.com/k4nekidev-star

License

Check the repository for the project's license and usage conditions.

---

<p align="center">
  <b>Initial Banner</b><br>
  Customize your terminal, your way.
</p>
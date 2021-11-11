[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/TStickers.svg?style=for-the-badge)](../../)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/TStickers.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/TStickers.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/TStickers.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/TStickers.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/TStickers.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/tstickers.svg?style=for-the-badge)](https://pypistats.org/packages/tstickers)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Ftstickers)](https://pepy.tech/project/tstickers)
[![PyPI Version](https://img.shields.io/pypi/v/tstickers.svg?style=for-the-badge)](https://pypi.org/project/tstickers)

<!-- omit in TOC -->
# TStickers - Telegram Sticker Downloader

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Download sticker packs from Telegram

NOTE: You need a telegram bot token to make use of the script. Generate a bot
token and paste in a file called 'env'. Send a message to @BotFather to get started.

- [Docs](#docs)
- [Using](#using)
	- [Help](#help)
- [Formats](#formats)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Docs

See the [Docs](/DOCS/) for more information.

## Using

- Create a file called 'env' (or env.txt) and paste your token
- Get the URL of the telegram sticker pack
- Run the program `python -m tstickers`
- Enter the URL of the sticker pack
- Get the output in the `downloads` folder.

### Help

```sh
usage: Welcome to TStickers, providing all of your sticker needs [-h] [-t TOKEN] [-p PACK] [--frameskip FRAMESKIP]
                                                                 [--scale SCALE]

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Pass in a bot token inline
  -p PACK, --pack PACK  Pass in a pack url inline
  --frameskip FRAMESKIP
                        Set frameskip. default=1
  --scale SCALE         Set scale. default=1.0
```

## Formats

| Format | Static | Animated |
| ------ | ------ | -------- |
| .gif   | ✔      | ✔        |
| .png   | ✔      | ✔+       |
| .tgs   | ❌      | ✔        |
| .webp  | ✔      | ✔        |

```txt
+ First frame of animated image only
```

Note that static images can fail to save as .gif occasionally in testing

## Documentation

See the [Docs](/DOCS/) for more information.

## Install With PIP

```python
pip install tstickers
```

Head to https://pypi.org/project/tstickers/ for more info

## Language information

### Built for

This program has been written for Python versions 3.7 - 3.10 and has been tested with both 3.7 and
3.10

## Install Python on Windows

### Chocolatey

```powershell
choco install python
```

### Windows - Python.org

To install Python, go to https://www.python.org/downloads/windows/ and download the latest
version.

## Install Python on Linux

### Apt

```bash
sudo apt install python3.x
```

### Dnf

```bash
sudo dnf install python3.x
```

## Install Python on MacOS

### Homebrew

```bash
brew install python@3.x
```

### MacOS - Python.org

To install Python, go to https://www.python.org/downloads/macos/ and download the latest
version.

## How to run

### Windows

- Module
	`py -3.x -m [module]` or `[module]` (if module installs a script)

- File
	`py -3.x [file]` or `./[file]`

### Linux/ MacOS

- Module
	`python3.x -m [module]` or `[module]` (if module installs a script)

- File
	`python3.x [file]` or `./[file]`

## Download Project

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2

	```bash
	git clone https://github.com/FHPythonUtils/TStickers
	```

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files

### Licence

MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog

See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale

The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.

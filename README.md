[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/TStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/TStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/TStickers.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/TStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/TStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/tstickers.svg?style=for-the-badge&cacheSeconds=28800)](https://pypistats.org/packages/tstickers)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi%2Epepy%2Etech%2Fapi%2Fv2%2Fprojects%2Ftstickers)](https://pepy.tech/project/tstickers)
[![PyPI Version](https://img.shields.io/pypi/v/tstickers.svg?style=for-the-badge&cacheSeconds=28800)](https://pypi.org/project/tstickers)

<!-- omit in toc -->
# TStickers - Telegram Sticker Downloader

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

The `tstickers` package provides functionality for downloading and converting sticker packs from https://t.me/addstickers. Download stickers, and convert them to multiple formats, with caching the converted stickers for faster retrieval.

- [Basic Use](#basic-use)
- [Using](#using)
- [Help](#help)
- [Documentation](#documentation)
- [Formats](#formats)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Windows - Python.org](#windows---pythonorg)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
	- [Dnf](#dnf)
- [Install Python on MacOS](#install-python-on-macos)
	- [Homebrew](#homebrew)
	- [MacOS - Python.org](#macos---pythonorg)
- [How to run](#how-to-run)
	- [Windows](#windows)
	- [Linux/ MacOS](#linux-macos)
- [Building](#building)
- [Testing](#testing)
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

## Basic Use

https://t.me/addstickers/DonutTheDog

- NOTE: You need a telegram bot token to make use of the script. Generate a bot
token and paste in a file called 'env'. Send a message to @BotFather to get started.
- Create a file called 'env' (or env.txt) and paste your token
- Get the URL of the telegram sticker pack
- Run the program `python -m tstickers`
- Enter the URL of the sticker pack
- Get the output in the `downloads` folder.

More info at [Tutorials](/documentation/tutorials)

## Using

1. Get the URL of the Signal sticker pack. In the form https://t.me/addstickers

2. Pass in multiple packs from the commandline with `-p/--pack`

	```bash
	$ tstickers --pack https://t.me/addstickers/DonutTheDog
	INFO     | ============================================================
	INFO     | Starting to scrape "DonutTheDog" ..
	INFO     | Time taken to scrape 31 stickers - 0.044s
	INFO     |
	INFO     | ------------------------------------------------------------
	INFO     | Starting download of "donutthedog" into downloads\donutthedog
	INFO     | Time taken to download 31 stickers - 0.157s
	INFO     |
	INFO     | ------------------------------------------------------------
	INFO     | -> Cache miss for DonutTheDog!
	INFO     | Converting stickers "DonutTheDog"...
	INFO     | Time taken to convert 31 stickers (tgs) - 60.970s
	INFO     |
	INFO     | Time taken to convert 31 stickers (webp) - 0.447s
	INFO     |
	INFO     | Time taken to convert 62 stickers (total) - 61.434s
	INFO     |

	```

3. OR. Enter the URL of the sticker pack when prompted

	```bash
	$ python -m tstickers
	Enter sticker_set URL (leave blank to stop): https://t.me/addstickers/DonutTheDog
	Enter sticker_set URL (leave blank to stop):
		INFO     | ============================================================
	INFO     | Starting to scrape "DonutTheDog" ..
	INFO     | Time taken to scrape 31 stickers - 0.044s
	INFO     |
	INFO     | ------------------------------------------------------------
	INFO     | Starting download of "donutthedog" into downloads\donutthedog
	INFO     | Time taken to download 31 stickers - 0.157s
	INFO     |
	INFO     | ------------------------------------------------------------
	...
	```

4. Get the output in the `downloads` folder.

	```powershell
	$ ls .\downloads\donutthedog\

	Mode                 LastWriteTime         Length Name
	----                 -------------         ------ ----
	d-----        17/03/2024     17꞉00                apng
	d-----        17/03/2024     17꞉01                gif
	d-----        17/03/2024     17꞉06                png
	d-----        17/03/2024     17꞉00                tgs
	d-----        17/03/2024     17꞉02                webp
	```

## Help

```bash
$ python -m tstickers --help
usage: Welcome to TStickers, providing all of your sticker needs [-h] [-t TOKEN] [-p PACK [PACK ...]]
																[--frameskip FRAMESKIP] [--scale SCALE]
																[-b {rlottie-python,pyrlottie}]

options:
-h, --help            show this help message and exit
-t TOKEN, --token TOKEN
						Pass in a bot token inline
-p PACK [PACK ...], --pack PACK [PACK ...]
						Pass in a pack url inline
--frameskip FRAMESKIP
						Set frameskip. default=1
--scale SCALE         Set scale. default=1.0
-b {rlottie-python,pyrlottie}, --backend {rlottie-python,pyrlottie}
						Specify the convert backend
```

## Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
- The [Technical Reference](/documentation/reference) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software.
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Formats

| Format | Static | Animated | Animated (webm) |
| ------ | ------ | -------- | --------------- |
| .gif   | ✔      | ✔        | ❌               |
| .png   | ✔      | ✔+       | ❌               |
| .tgs   | ❌      | ✔        | ❌               |
| .webp  | ✔      | ✔        | ❌               |
| .webm  | ❌      | ❌        | ✔               |

```txt
+ First frame of animated image only
```

Note that static images can fail to save as .gif occasionally in testing

## Install With PIP

```python
pip install tstickers
```

Head to https://pypi.org/project/tstickers/ for more info

## Language information

### Built for

This program has been written for Python versions 3.8 - 3.11 and has been tested with both 3.8 and
3.11

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

## Building

This project uses https://github.com/FHPythonUtils/FHMake to automate most of the building. This
command generates the documentation, updates the requirements.txt and builds the library artefacts

Note the functionality provided by fhmake can be approximated by the following

```sh
handsdown  --cleanup -o documentation/reference
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements_optional.txt
poetry build
```

`fhmake audit` can be run to perform additional checks

## Testing

For testing with the version of python used by poetry use

```sh
poetry run pytest
```

Alternatively use `tox` to run tests over python 3.8 - 3.11

```sh
tox
```

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

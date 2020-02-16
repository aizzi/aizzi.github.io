---
title: "How to setup a laptop for ML exploration"
description: "In this tutorial I describe how I configured a laptop for my learning of ML related topics."
last_update: "2020-02-02"
published: false
---
# How to setup a laptop for Machine Learning exploration
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

After a very long time spent sharing my personal Windows 10 laptop among *pleasure* and *study*, I decided to dedicate one spare laptop exclusively to development tasks (either for learning and practicing).

My requirements for this build were:
- Supported by major machine learning frameworks
- Support C/C++ development
- Support Python development
- Support Docker containers
- Maintain clear and separate development spaces by using virtual environments and containers.

This tutorial is for future reference of what I installed, why and *how* (if any customization should be required).

---
## Installing Ubuntu

Ubuntu 18.04.3 LTE is the operating system of choice. It is well supported and documented, easy to install, free and all the major libraries and tools support Linux out of the box.

1. Reboot your computer from the installation media
2. At the `Install` panel select `English` and `Install Ubuntu`
3. Select the appropriate keyboard layout. My choice is `English (US)` with `English (US)`. Other layout can be added later if needed.
4. Connect to the Wireless network of your choice
5. On the `Updates and other software` panel select
  - Minimal installation (we want to keep the machine the cleanest it's possible)
  - Download updates while installing Ubuntu
  - Install third-party software for graphics and Wi-Fi hardware and additional media formats
6. On the `Installation Type` select `Erase disk and install Ubuntu` (we want only development done here)
7. Complete the installation and restart your computer
8. Install the updates and restart the system. On the `What's new in Ubuntu` panel select:
  - Do not install `Livepatch`
  - Do not send system info
9. In `Settings\Region & Language\Input sources` add the following keyboards:
  - `Italian (Winkeys)` input source (this is because I use an Italian keyboard at home)
  - `Czech (QWERTY)` since my laptop provides also the Czech keyboard
10. I like as well to format dates and currencies the Italian way. So, in the same panel, select `Manage Installed Languages` and install the support for Italian.
11. Restart the computer and you're ready to go.

---
## Browser

The browser of choice is `Firefox`. The version which comes pre-installed when I installed is the **72.0.2 (64 bit)**.

To customize it, let's start with installing `Lastpass` for password management.
Visit [LastPass](https://www.lastpass.com/misc_download2.php) to download the plugin.

Then activate the `Firefox Sync` feature to get all your links.

---
## Prerequisite libraries

Install the following libraries, which will be needed in the following steps:

- sudo apt-get install build-essential
- sudo apt-get install checkinstall
- sudo apt-get install libreadline-gplv2-dev
- sudo apt-get install libncursesw5-dev
- sudo apt-get install libssl-dev
- sudo apt-get install libsqlite3-dev
- sudo apt-get install tk-dev
- sudo apt-get install libgdbm-dev
- sudo apt-get install libc6-dev
- sudo apt-get install libbz2-dev
- sudo apt-get install libffi-dev
- sudo apt-get install zliblg-dev


---
## Python

Ubuntu comes with Python 3.6.9 preinstalled. You can verify this by executing the command:

```
aizzi@PC02-ML:~$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

Although this is generally fine, we may want to install other versions too. For example, we are going to install Python 3.8

1. From [Python.org/downloads](https://www.python.org/downloads/) download the latest source release (Python 3.8.1 at the moment of writing)
2. Move into `~/Downloads` and install Python
```
> cd ~/Downloads
> sudo tar -xf Python-3.8.1.tar.xz
> cd Pyhton-3.8.1
> sudo ./configure --enable-optimizations
> sudo make altinstall
```

Verify that both version of Python exists on the system:

```
> python3
> python 3.8
> which python3
> which python3.8
```

---
## C/C++ Compiler
[GCC](https://gcc.gnu.org/install/) and C++ compiler should be already installed, as a result of the `build-essential` library. Verify by running `gcc --version` and `g++ --version` commands.

---
## Git

Install Git following instructions at the following page [https://git-scm.com/download/linux](https://git-scm.com/download/linux)

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
```

Verify the installation went fine:

```
aizzi@PC02-ML:~$ git --version
git version 2.17.1
```

A powerful guide to use Git is the [Pro Git](https://git-scm.com/book/en/v2) book. Follow the [First-Time Git Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

```
git config --global user.name "<your name here>"
git config --global user.email <your email here>
```

---
## Editor

Install [Visual Studio Code](https://code.visualstudio.com). Download the package, then:

```
> cd ~/Downloads
> sudo apt install ./<file>.deb
```

Launch `Visual Studio Code` and install the following Extensions:
- Python
- C/C++
- Docker

---
## Docker

To install Docker, head to [Docker Quick Start](https://hub.docker.com/?overlay=onboarding) and follow the instructions.

```
> sudo apt-get update
> sudo apt-get install apt-transport-https
> sudo apt-get install ca-certificates
> sudo apt-get install curl
> sudo apt-get install gnupg2
> sudo apt-get install software-properties-common
> curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
> sudo apt-key fingerprint 0EBFCD88
> sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
> sudo apt-get update
> sudo apt-get install docker-ce
> sudo apt-get install docker-ce-cli
> sudo apt-get install containerd.io
```
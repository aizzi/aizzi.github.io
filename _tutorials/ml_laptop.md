---
title: "How to setup a laptop for ML exploration"
description: "In this tutorial I describe how I configured a laptop for my learning of ML related topics."
last_update: "2020-02-02"
published: true
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

### Installing support for MX Master 2S

> sudo add-apt-repository ppa:bluetooth/bluez
> sudo apt install bluez
> sudo service bluetooth restart

Good level of details about bluetooth on Ubuntu is availabel [here](https://medium.com/@overcode/fixing-bluetooth-in-ubuntu-pop-os-18-04-d4b8dbf7ddd6)

A useful tool to check in case of bluetooth problems is `bluetoothctl`

I'm still not able to have my Logitech MX Master 2S reliably working with this setup. Bluetooth on Ubuntu appears to be very unstable. My suggestion is to use corded mouse and keyboards.

**Note** : I still had problems even after these actions. I solved by intalling [ltunify](https://git.lekensteyn.nl/ltunify/) and using the Logitech Unify Dongle provided with the mouse.

### Virtual Environment Management

It will be extremely probable that you will end up with a lot of different virtual environments to play with, so you want to organize them in a good way. This is how I do it.

1. All my source code will go into a single repository:
`~/Programming/SourceCode`
2. All virtual environments will be stored in the folder `~/Programming/envs`, each one in its specific folder.
3. To create a new environment use the following code:
```
> python -m venv --prompt <unique_promp> ~/Programming/envs/<environment_identifier> 
```
4. Modify `~/.bashrc` by adding the following code at the end of the file:

```
# Custom Functions definitions.
# You may want to put all your custom functions into a separate file like
# ~/.bash_functions, instead of adding them here directly.

if [ -f ~/.bash_functions ]; then
    . ~/.bash_functions

```

5. Create the file `~/.bash_functions` and add the following code:
```
activate_env() {
    # Activate a virtual environment
    if [ "$1" = "" ]; then
        echo "This are the available environments"
        ls ~/Programming/envs
    else
        echo "Activating environment $1"
        . ~/Programming/envs/$1/bin/activate
    fi
}
```
6. Source the `~./bashrc` or logoff and logon.
7. Now you can use `activate_env` from the command line to activate your virtual environment. Just type `activate_env` to get a list of available environments, or `activate_env <name of the environment>` to activate a specific environment.

  > **Disclaimer**: I know the function is really crude, but I'm working on functionality over fanciness here. You can make it better for yourself.

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

> **Note**: You can skip this passage if you are going to use *Anaconda*, because it will take care to install Python using *Conda*. See below for instructions.

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

You may want to set an alias to easily execute different versions of Python. To do so, move to your home directory and create a file called `.bash_aliases` with the following entries:

```
alias p36='python3'
alias p38='python3.8'
alias pip38='pip3.8'
```

Now logoff and logon and you will be able to use the short aliases to execute the different versions of Python.

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
> git config --global core.editor "code --wait"
```

Launch `Visual Studio Code` and install the following Extensions:
- Python
- C/C++
- Docker

---
## Docker

To install Docker, head to [Get Docker Engine - Community for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu) and follow the instructions.

```
> sudo apt-get update
> sudo apt-get install apt-transport-https
> sudo apt-get install ca-certificates
> sudo apt-get install curl
> sudo apt-get install gnupg-agent
> sudo apt-get install software-properties-common
> curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
> sudo apt-key fingerprint 0EBFCD88
> sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
> sudo apt-get update
> sudo apt-get install docker-ce
> sudo apt-get install docker-ce-cli
> sudo apt-get install containerd.io
> sudo docker run hello-world
```

Now follow the instructions on [Post-installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/) in order to manage Docker as a non-root user and be able to interface it from Visual Studio Code.

```
> sudo groupadd docker
> sudo usermod -aG docker $USER
> newgrp docker
> docker run hello-world
```

You need to restart your machine in order to have Visual Studio Code to connect to the Docker engine.

---
## PyTorch

We will install [PyTorch] (https://pytorch.org/get-started/locally/) in a virtual environment.

Move to the directory you want to create the virtual environment into and run the following command

```
> python -m venv --prompt MLE01 .venv
> . ./venv/bin/activate
> pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

---
## Miniconda

`Miniconda` is a free minimal installer for `conda`. It includes just the bare minimum to get started and this is exactly why I like it. The following instructions will guide through the `Miniconda` installation.

Detailed instructions on which this guide is based are available [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda).

1. Download the Linux installer from [here](https://docs.conda.io/en/latest/miniconda.html#linux-installers). Be sure to download the appropriate version. In my case, I installed the `Python 3.7 Miniconda Linux 64-bit`.

2. Verify the cryptographic hash of the downloaded file:
`> sha256sum Miniconda3-latest-Linux-x86_64.sh`

3. Follow the [installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
`> bash Miniconda3-latest-Linux-x86_64.sh`

4. Choose to install into `~/Programming/Tools/miniconda3`

5. Let the installer initialize Miniconda3

6. Close and re-open your shell. You will see that your prompt was modified to include `(base)` in order to show you are on the root environment.

7. Update `conda` with 
`> conda update conda`

8. Verify your Python installation:
```
(base) aizzi@PC02-ML:~$ python
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
(base) aizzi@PC02-ML:~$ which python
/home/aizzi/Programming/Tools/miniconda3/bin/python
(base) aizzi@PC02-ML:~$ which python3.8
/usr/local/bin/python3.8
(base) aizzi@PC02-ML:~$ which python3.6
/usr/bin/python3.6
```

---
## Jupyter Lab

[`JupyterLab`](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) is the successor of `Jupyter Notebook`. It has a modern interface while preserving the features of Notebooks. If you're starting with Notebooks, I think it's worth to start learning `JupyterLab` instead of `Jupyter Notebook`.

To install `JupyterLab` in your base environment using `conda`:

```
> conda search jupyterlab
> conda install jupyterlab=1.2.6
> conda install nb_conda
> jupyter lab
```

The command `conda install nb_conda` will install modules to manage your environments. This way, you will be able to execute kernels in different environment while using `JupyterLab` in the *(base)* environment.

Let's say you have created a conda environment named `MLE01`. Now, you activate the environment and then run the following command in it to install the kernel:

```
(MLE01) aizzi@PC02-ML:~$ conda install ipykernel
```

Now, when you execute `jupyter lab` from the `(base)` environment, you will see the `MLE01` kernel available to execute in the `JupyterLab` console.
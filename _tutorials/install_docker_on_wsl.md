---
title: "How to setup a development environment in wsl with Docker and Git"
description: "In this tutorial I describe the steps needed to create a development environment in a WSL2 environment, installing Docker in it without the need of installing Docker Desktop"
last_update: "2022-07-20"
published: true
---
# How to setup a development environment in a WSL2 virtual machine
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

1. [Install the WSL distribution](#install-the-wsl-distribution)
2. [Install and set up Windows Terminal](#install-and-set-up-windows-terminal)
3. [Configure Git](#configure-git)
4. [Install Docker into the WSL](#install-docker-into-the-wsl)

## Install the WSL distribution

A nice step to step guide is available [here](https://docs.microsoft.com/en-us/windows/wsl/setup/environment). This is what I followed, noting everything strange happening during the installation.

```
PS C:\Users\your_uid> wsl --install -d Ubuntu
Downloading: Ubuntu
Installing: Ubuntu
Ubuntu has been installed.
Launching Ubuntu...
```

You may be requested to restart your machine. I was not, but I already had a `WSL Ubuntu` distribution running.

At the end of the installation, the Ubuntu shell should start.

You can check what is installed on your WSL using the following command in a PowerShell console:

```
PS C:\Users\your_uid> wsl -l -v
  NAME                   STATE           VERSION
* Ubuntu-20.04           Running         2
  docker-desktop         Running         2
  docker-desktop-data    Running         2
  Ubuntu                 Running         2
```

Note how you can install multiple distributions (in the example above, I have both "Ubuntu-20.04" and "Ubuntu").

## Install and set up Windows Terminal

Follow the instructions at [this page](https://docs.microsoft.com/en-us/windows/terminal/install).

If you already have the terminal installed and running, restart it in order to load the new distribution. Then add the new profile in the settings to have it listed among the choices.

## Configure Git

Follow the instructions at [this page](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git) to install (if needed) and configure `Git` in your environment.

As a minimum, configure the following keys:

* user.name
* user.email
* credential.helper

```
your_id@your_hostname:~$ git config -l
user.name=Name Surname
user.email=your_email@your_provider
credential.helper=/mnt/c/Program\ Files/Git/mingw64/libexec/git-core/git-credential-manager-core.exe
```

## Install Docker into the WSL

Follow [this article](https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9) to install Docker on the WSL without `Docker Desktop` (skip this step if you are using `Docker Desktop`).

```
your_uid@your_hostname:~$ sudo apt update && sudo apt upgrade
 
your_uid@your_hostname:~$ sudo apt install --no-install-recommends apt-transport-https ca-certificates curl gnupg2
 
your_uid@your_hostname:~$ source /etc/os-release
 
your_uid@your_hostname:~$ curl -fsSL https://download.docker.com/linux/${ID}/gpg | sudo apt-key add -
 
your_uid@your_hostname:~$ echo "deb [arch=amd64] https://download.docker.com/linux/${ID} ${VERSION_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/docker.list
 
your_uid@your_hostname:~$ sudo apt update
 
your_uid@your_hostname:~$ sudo apt install docker-ce docker-ce-cli containerd.io
 
your_uid@your_hostname:~$ sudo usermod -aG docker $USER
 
# This is to share the dockerd across WSL distros <<< START
your_uid@your_hostname:~$ getent group | grep 36257 || echo "Yes, that ID is free"
 
your_uid@your_hostname:~$ sudo groupmod -g 36257 docker
 
your_uid@your_hostname:~$ getent group | grep 36257 || echo "Yes, that ID is free"
 
your_uid@your_hostname:~$ DOCKER_DIR=/mnt/wsl/shared-docker
 
your_uid@your_hostname:~$ mkdir -pm o=,ug=rwx "$DOCKER_DIR"
 
your_uid@your_hostname:~$ sudo chgrp docker "$DOCKER_DIR"
 
your_uid@your_hostname:~$ sudo mkdir /etc/docker/
 
your_uid@your_hostname:~$ sudo vi /etc/docker/daemon.json
 
your_uid@your_hostname:~$ cat /etc/docker/daemon.json
{
        "hosts": ["unix:///mnt/wsl/shared-docker/docker.sock"]
}
# This is to share the dockerd across WSL distros <<< END
```

Edit `.bashrc` and add the following at the end to automatically start `Docker`:

```
# Automatically start the docker service at startup
DOCKER_DISTRO="Ubuntu"
DOCKER_DIR=/mnt/wsl/shared-docker
DOCKER_SOCK="$DOCKER_DIR/docker.sock"
export DOCKER_HOST="unix://$DOCKER_SOCK"
if [ ! -S "DOCKER_SOCK" ]; then
        mkdir -pm o=,ug=rwx "$DOCKER_DIR"
        chgrp docker "$DOCKER_DIR"
        /mnt/c/Windows/System32/wsl.exe -d $DOCKER_DISTRO sh -c "nohup sudo -b dockerd < /dev/null > $DOCKER_DIR/dockerd.log 2>&1"
fi
```

Now, edit the `~/.docker/config.json` and add all the configurations you need.

Restart the terminal to activate `Docker`.

Finally, verify that `Docker` is working:

```
your_uid@your_hostname:~/.docker$ docker -H unix:///mnt/wsl/shared-docker/docker.sock run --rm hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:2498fce14358aa50ead0cc6c19990fc6ff866ce72aeb5546e1d59caac3d0d60f
Status: Downloaded newer image for hello-world:latest
 
Hello from Docker!
This message shows that your installation appears to be working correctly.
 
To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
 
To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash
 
Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/
 
For more examples and ideas, visit:
 https://docs.docker.com/get-started/
 ```

 Next, tell `sudo` to grant passwordless access to `dockerd`, as long as the user is a member of the `docker` group. To do so, enter `sudo visudo` and add the following lines to it:

 ```
 # Allow members of docker group to start dockerd without password
%docker ALL=(ALL)  NOPASSWD: /usr/bin/dockerd
```

That's it. You are now ready to use `Docker` in your `WSL2` environment on Windowsw, without having to install `Docker Desktop`.

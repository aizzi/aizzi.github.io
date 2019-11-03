---
title: "How to backup using rsync in a container"
description: "In this tutorial I describe the steps needed to create a container to run rsync and use it to backup a FreeNAS server on a local USB external disk. This tutorial assume you have the same level of expertise about container I have when I wrote it: **PRACTICALLY NOTHING**"
last_update: "2019-11-03"
published: true
---
# How to backup a FreeNAS server using rsync running in a container
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

1. [History and Infrastructure](#history-and-infrastructure)
2. [Choose the linux image](#choose-the-linux-image)
3. [Install rsync](#install-rsync)
4. [Mounting the directories to backup](#mounting-the-directories-to-backup)
5. [Mounting the USB disk to backup to](#mounting-the-usb-disk-to-backup-to)
6. [Execute the backup](#execute-the-backup)


## History and Infrastructure
My backup strategy is based on two backup images. The first one is a local backup executed periodically on an external USB disk. The second one is a remote cloud backup.

For the cloud backup I have a Crashplan for Small Business subscription. The local backup is executed using an rsync command.

My storage infrastructure is based on a FreeNAS server which serves all the family needs. Each family member has his own home-directory on this server, where he can store all the files he wants saved. Other directories serve as media repository for family pictures, videos, movies, books, etc. Local PC are not backed-up by choice. We are mostly a Windows 10 shop, with a couple of Linux images.

My first requirement was to have a full backup of the FreeNAS server in both images. A daily backup is more than enough.

The second requirement was to shield the backup images from a ransomware attack. This is accomplished locally by switching off the external USB disk when a backup is not running.

This strategy cannot be used with Crashplan because it is continuously running in background. These presented two problems to me:
* Crashplan consume resources while running in background and I don't really need a 15 minute recovery point. A daily or weekly backup is more than enough.
* If my PC get infected by a ransomware virus, it will propagate to the Crashplan cloud backup, rendering one of my backup images useless.

So, I decided to create a virtual machine to run the backup. Both the rsync and Crashplan were installed on it. The VM has also access to the FreeNAS server. Whenever I want to run a backup, I start the VM and execute the rsync or just let Crashplan sync the cloud repository. When the VM is closed, there is no way to access the backup images, which are effectively shielded.

The VM was created using VirtualBox and saved to be easily restored in case I should ever need to recreate it.

When I started playing with Docker, I had to switch to HyperV which rendered my VirtualBox useless. So I have to recreate the same architecture on HyperV and decided to go and see if I can make it run both in separate containers.

The first step was to create the rsync container to backup locally.

## Choose the linux image
First of all, we need a linux image to run the rsync command from. So, let's hop to [Docker Hub](https://hub.docker.com/search?q=&type=image) and see what's there we can use. [Alpine](https://hub.docker.com/_/alpine) seems to be a good candidate for our test.

Let's start by creating a very basic Dockerfile

```
# Use the official Alpine image
FROM alpine:3.10.2

# Define environment variable
ENV NAME local-backup
```

and let's build the image with `docker build --tag=rsync_backup:0.1.0 .`. Pay attention at that last '.': do not miss it! If everything goes fine you should see something like this:

```
C:\Programming\SourceCode\Containers\rsync>docker build --tag=rsync_backup:0.1.0 .
Sending build context to Docker daemon  4.096kB
Step 1/2 : FROM alpine:3.10.2
3.10.2: Pulling from library/alpine
9d48c3bd43c5: Pull complete
Digest: sha256:72c42ed48c3a2db31b7dafe17d275b634664a708d901ec9fd57b1529280f01fb
Status: Downloaded newer image for alpine:3.10.2
 ---> 961769676411
Step 2/2 : ENV NAME local-backup
 ---> Running in 43cb9c77ddba
Removing intermediate container 43cb9c77ddba
 ---> c19ecbf6593b
Successfully built c19ecbf6593b
Successfully tagged rsync_backup:0.1.0
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.
```

A `docker image ls` command should confirm your new image is in your local repository and you should be able to lunch the container using `docker run rsync_backup`. The command should run and immediately complete - without any error - because of course we gave it nothing to do. So, let's remediate. Open your Dockerfile and modify it in the following way:

```
# Use the official Alpine image
FROM alpine:3.10.2

# Define environment variable
ENV NAME local-backup

# Run a command to say hello
CMD ["echo", "hello"]
```

and build the v0.2.0 of the image with `docker build --tag=rsync_backup:0.2.0 .`. A `docker image ls` should now show you both image and you can execute the new one with `docker run rsync_backup:0.2.0`. This time you should see the following:

```
C:\Programming\SourceCode\Containers\rsync>docker run rsync_backup:0.2.0
hello
```

Hurra! Give yourself a path on the shoulder and move to the next step.

## Install rsync
Now we want to check that rsync is there to be executed. The easiest way is to execute it. So, get back to to the Docker file and modify it like this:

```
# Use the official Alpine image
FROM alpine:3.10.2

# Define environment variable
ENV NAME local-backup

# Run a command to say hello
CMD ["rsync", "--version"]
```

Go on and create the v0.3.0 of your container.

```
C:\Programming\SourceCode\Containers\rsync>docker build --tag=rsync_backup:0.3.0 .
Sending build context to Docker daemon  4.096kB
Step 1/3 : FROM alpine:3.10.2
 ---> 961769676411
Step 2/3 : ENV NAME local-backup
 ---> Using cache
 ---> c19ecbf6593b
Step 3/3 : CMD ["rsync", "--version"]
 ---> Running in 98bd64169127
Removing intermediate container 98bd64169127
 ---> 76f31b352aec
Successfully built 76f31b352aec
Successfully tagged rsync_backup:0.3.0
SECURITY WARNING: You are building a Docker image from Windows against a non-Windows Docker host. All files and directories added to build context will have '-rwxr-xr-x' permissions. It is recommended to double check and reset permissions for sensitive files and directories.

C:\Programming\SourceCode\Containers\rsync>docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
rsync_backup        0.3.0               76f31b352aec        8 seconds ago       5.58MB
rsync_backup        0.2.0               cd6933b22f8e        20 minutes ago      5.58MB
rsync_backup        0.1.0               c19ecbf6593b        29 minutes ago      5.58MB
alpine              3.10.2              961769676411        10 days ago         5.58MB

C:\Programming\SourceCode\Containers\rsync>docker run rsync_backup:0.3.0
docker: Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "exec: \"rsync\": executable file not found in $PATH": unknown.
```

So, rsync is not there to run. Let's install it. Modify the Dockerfile to look like this

```
# Use the official Alpine image
FROM alpine:3.10.2

# Install any needed package
RUN apk update
RUN apk add rsync

# Define environment variable
ENV NAME local-backup

# Run a command to say hello
CMD ["rsync", "--version"]
```

and build your `rsync_backup v0.4.0` (you know how to do it now, don't you?). Now, when you execute your container you get the following:

```
C:\Programming\SourceCode\Containers\rsync>docker run rsync_backup:0.4.0
rsync  version 3.1.3  protocol version 31
Copyright (C) 1996-2018 by Andrew Tridgell, Wayne Davison, and others.
Web site: http://rsync.samba.org/
Capabilities:
    64-bit files, 64-bit inums, 64-bit timestamps, 64-bit long ints,
    socketpairs, hardlinks, symlinks, IPv6, batchfiles, inplace,
    append, ACLs, xattrs, iconv, symtimes, prealloc

rsync comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
are welcome to redistribute it under certain conditions.  See the GNU
General Public Licence for details.
```

## Mounting the directories to backup
Now, it is time to mount the FreeNAS filesystems we want to backup. The idea here is to have the filesystem mounted automatically during when the container starts.

First of all, let's check that the container can reach the FreeNAS server. I have it configured with a static IP address, so we can try pinging it using the following Dockerfile:

```
# Use the official Alpine image
FROM alpine:3.10.2

# Install any needed package
RUN apk update
RUN apk add rsync

# Define environment variable
ENV NAME local-backup

# Run a command to say hello
CMD ping -c 4 <your_own_ip_address_here>
```

If everything is fine, you should receive back something like this:

```
PS C:\programming\sourcecode\Containers\rsync> docker run rsync_backup:0.5.3
PING 192.168.1.8 (192.168.1.8): 56 data bytes
64 bytes from 192.168.1.8: seq=0 ttl=37 time=7.877 ms
64 bytes from 192.168.1.8: seq=1 ttl=37 time=2.827 ms
64 bytes from 192.168.1.8: seq=2 ttl=37 time=2.929 ms
64 bytes from 192.168.1.8: seq=3 ttl=37 time=3.089 ms

--- 192.168.1.8 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 2.827/4.180/7.877 ms
```

When we are sure that we can connect to the FreeNAS server, let's mount the filesystem from FreeNAS.

Let's start by creating an `fstab` file with all the CIFS shares we want to backup (replace `<MOUNT_USER>` and `<MOUNT_PWD>` with your own credentials here):

```
/dev/cdrom      /media/cdrom    iso9660 noauto,ro 0 0
/dev/usbdisk    /media/usb      vfat    noauto,ro 0 0
//192.168.1.8/backup /mnt/fs01/backup cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/ebook /mnt/fs01/ebook cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/film /mnt/fs01/film cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/fotografie /mnt/fs01/fotografie cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/homedirs /mnt/fs01/homedirs cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/it /mnt/fs01/it cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/ITunesMedia /mnt/fs01/ITunesMedia cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/Kodi /mnt/fs01/Kodi cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/music /mnt/fs01/music cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/series /mnt/fs01/series cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
//192.168.1.8/video /mnt/fs01/video cifs uid=0,gid=0,user=<MOUNT_USER>,password=<MOUNT_PWD>,_netdev 0 0
```

The mounting points must be created at build time, so modify the `Dockerfile` to create them by adding the following lines:

```
RUN mkdir /mnt/fs01
RUN mkdir /mnt/fs01/backup
RUN mkdir /mnt/fs01/ebook
RUN mkdir /mnt/fs01/film
RUN mkdir /mnt/fs01/fotografie
RUN mkdir /mnt/fs01/homedirs
RUN mkdir /mnt/fs01/it
RUN mkdir /mnt/fs01/ITunesMedia
RUN mkdir /mnt/fs01/Kodi
RUN mkdir /mnt/fs01/music
RUN mkdir /mnt/fs01/series
RUN mkdir /mnt/fs01/video
```

and replace the `fstab` with our own one:

```
COPY --chown=root:root fstab /etc/fstab
```

I had problems in having the files mounted at startup, so I worked around that by mounting everything at runtime:

```
CMD mount -a && sh
```

This command will execute the `mount -a` and start a shell to verify that everything is effectively mounted. Let's build the image and run the container. If everything gets correctly mounted, you should see something like this:

```
C:\Programming\SourceCode\Containers\rsync>docker run -it --privileged rsync_backup:0.5.4
/ # df -k | grep 192.168.1.8
//192.168.1.8/backup 959344780 539284752 343312448  61% /mnt/fs01/backup
//192.168.1.8/ebook  959344780 539284752 343312448  61% /mnt/fs01/ebook
//192.168.1.8/film   946031668 864028928   6320208  99% /mnt/fs01/film
//192.168.1.8/fotografie
//192.168.1.8/homedirs
//192.168.1.8/it     959344780 539284752 343312448  61% /mnt/fs01/it
//192.168.1.8/ITunesMedia
//192.168.1.8/Kodi   946031668 864028928   6320208  99% /mnt/fs01/Kodi
//192.168.1.8/music  959344780 539284752 343312448  61% /mnt/fs01/music
//192.168.1.8/series 946031668 864028928   6320208  99% /mnt/fs01/series
//192.168.1.8/video  1920752504 1335633124 431459180  76% /mnt/fs01/video
```

## Mounting the USB disk to backup to

Since the USB is seen on the host as a local disk, we can use a bind mount to connect the container to it. In my case, the disk is mounted as `D:\`, so I can run the container with the `--mount` option to connect it:

```
C:\Programming\SourceCode\Containers\rsync>docker run -it --privileged --mount type=bind,source=D:,target=/media/LocalBackup rsync_backup:0.5.4
/ # df -k | grep LocalBackup
//10.0.75.1/D        2930265084 2757963708 172301376  94% /media/LocalBackup
/ # ls /media/LocalBackup
$RECYCLE.BIN               fs01bck_2018-12-30         fs01bck_2019-03-09         fs01bck_2019-06-01
System Volume Information  fs01bck_2018-12-31         fs01bck_2019-03-17         fs01bck_2019-06-08
found.000                  fs01bck_2019-01-13         fs01bck_2019-03-23         fs01bck_2019-06-15
fs01                       fs01bck_2019-01-20         fs01bck_2019-03-31         fs01bck_2019-06-22
fs01bck_2018-12-02         fs01bck_2019-01-26         fs01bck_2019-04-06         fs01bck_2019-06-23
fs01bck_2018-12-16         fs01bck_2019-01-27         fs01bck_2019-04-07         fs01bck_2019-06-28
fs01bck_2018-12-17         fs01bck_2019-02-02         fs01bck_2019-04-18         fs01bck_2019-07-07
fs01bck_2018-12-21         fs01bck_2019-02-09         fs01bck_2019-04-22         fs01bck_2019-07-13
fs01bck_2018-12-26         fs01bck_2019-02-10         fs01bck_2019-04-27         fs01bck_2019-08-04
fs01bck_2018-12-27         fs01bck_2019-02-16         fs01bck_2019-05-05         fs01bck_2019-08-08
fs01bck_2018-12-28         fs01bck_2019-02-23         fs01bck_2019-05-11         fs01bck_2019-08-21
fs01bck_2018-12-29         fs01bck_2019-03-02         fs01bck_2019-05-18         fs01bck_2019-08-24
```

## Execute the backup
What we  really want to have is a way to double-click an icon on the desktop to start the container and execute the backup. We are not there yet!

First of all, I do not like the idea to put the userid and password for the mount into a file `embedded` into the container. I want to specify them at launch time. This means I cannot use fstab and I have to mount the filesystems from inside a script that will be executed at start time.

The `run_backup.sh` script is the following one:

``` bash
#!/bin/sh

# Verify that the user is set
if [ "$RSYNC_USER" == "" ]; then
  echo "The user is not set"
  exit 1
fi

# Verify that the password is set
if [ "$RSYNC_PWD" == "" ]; then
  echo "The password is not set"
  exit 1
fi

# Verify that BCKROOT is set
if [ "$BCKROOT" == "" ]; then
  echo "BCKROOT is not set"
  exit 1
fi

# Verify that BCKFS is set
if [ "$BCKFS" == "" ]; then
  echo "BCKFS is not set"
  exit 1
fi

# Verify that REMOTE is set
if [ "$REMOTE" == "" ]; then
  echo "REMOTE is not set"
  exit 1
fi

echo "RSYNC_USER = $RSYNC_USER"
echo "RSYNC_PWD = $RSYNC_PWD"
echo "BCKROOT = $BCKROOT"
echo "BCKFS = $BCKFS"
echo "REMOTE = $REMOTE"

# Verify that the receiving backup filesystem exists
echo "Checking for /media/LocalBackup"
findmnt /media/LocalBackup
if [ ! $? -eq 0 ]; then
  echo "The receiving filesystem is not mounted"
  exit 1
else
  echo "/media/LocalBackup is mounted"
fi

# Create the root directory
if [ ! -d /mnt/$BCKROOT ]; then
  echo "Creating /mnt/$BCKROOT"
  mkdir /mnt/$BCKROOT
  if [ ! $? -eq 0 ]; then
    echo "Unable to create /mnt/$BCKROOT"
    exit 1
  fi
fi
echo "/mnt/$BCKROOT created"

# Create the log directory
if [ ! -d /media/LocalBackup/logs/`date +%F` ]; then
  echo "Creating /media/LocalBackup/logs/`date +%F`"
  mkdir /media/LocalBackup/logs/`date +%F`
  if [ ! $? -eq 0 ]; then
    echo "Unable to create /media/LocalBackup/logs/`date +%F`"
    exit 1
  fi
fi

# Looping through the directories to backup
IFS=,
for fs in $BCKFS; do
  echo
  echo "***** BACKUP $fs *****"
  if [ ! -d /mnt/$BCKROOT/$fs ]; then
    echo "Creating /mnt/$BCKROOT/$fs"
    mkdir /mnt/$BCKROOT/$fs
    if [ ! $? -eq 0 ]; then
      echo "Unable to create /mnt/$BCKROOT/$fs"
      exit 1
    fi
  fi
  echo "/mnt/$BCKROOT/$fs created"
  echo "mounting remote filesystem"
  findmnt /mnt/$BCKROOT/$fs
  if [ ! $? -eq 0 ]; then
    mount.cifs //$REMOTE/$fs /mnt/$BCKROOT/$fs -o user=$RSYNC_USER,password=$RSYNC_PWD,uid=0,gid=0,iocharset=utf8
    if [ ! $? -eq 0 ]; then
      echo "Unable to mount //$REMOTE/$fs"
      exit 1
    fi
  fi
  echo "//$REMOTE/$fs mounted. Executing rsync"
  rsync -abqpEAog --backup-dir=/media/LocalBackup/bck_`date +%F`/$fs --delete-during /mnt/$BCKROOT/$fs/ /media/LocalBackup/$BCKROOT/$fs/ --log-file=/media/LocalBackup/logs/`date +%F`/$fs.log
done
```

The idea behind it is that at runtime I'll pass the following variables:

* RSYNC_USER = the user to mount the remote filesystems
* RSYNC_PWD = the password for the above user
* BCKROOT = the root directory for the backup
* BCKFS = the list of filesystem to backup (comma separated)
* REMOTE = the ip address of the remote server

All the filesystem in the `BCKFS` list will be mounted from the `REMOTE` server using `RSYNC_USER` and `RSYNC_PWD` credentials. These filesystems will be backed up in `/media/LocalBackup`, which is be bound to the USB disk. Everything is grouped into /media/LocalBackup/`BCKROOT`. The differences will be saved in a date identified directory `/media/LocalBackup/bck_<current_date>`. Logs will be stored into `/media/LocalBackup/logs/<current_date>`.

We can build the container with the followind Dockerfile:

```
# Use the official Alpine image
FROM alpine:3.10.2

# Set the working directory
WORKDIR /root

# Install any needed package
RUN apk update
RUN apk add openrc
RUN apk add rsync
RUN apk add cifs-utils
RUN rc-update add netmount default
RUN apk add findmnt

# Copy the script to execute the backup
COPY --chown=root:root run_backup.sh .
RUN chmod 755 ./run_backup.sh

# Define environment variable
ENV NAME local-backup

# Run the following command when starting the container
CMD run_backup.sh
```

and execute it in the following way:

`docker run -it --privileged --mount type=bind,source=D:,target=/media/LocalBackup -e RSYNC_USER=<your_user> -e RSYNC_PWD=<your_pwd> -e BCKROOT=fs01 -e BCKFS=backup,ebook,film,fotografie,homedirs,it,ITunesMedia,Kodi,music,series,video -e REMOTE=192.168.1.8 rsync_backup:1.0`

In the command above replace `D:` with the drive letter of your USB disk. Insert the command into a `cmd` file, associate an icon to it on your desktop and you're ready to execute your rsync backup.

## Conclusion
I hope you'd find this tutorial instructive. It certainly was for me. When I started I knew nothing about docker: I installed it for the first time to build this project and proceeded step-by-step. That's why I recorded in this article my flow of thoughts, issues and resolutions. Feel free to reuse the above instructions to build your own containers.

Learn smart, code hard, have fun!

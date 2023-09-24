---
title: "01 - Install Proxmox"
description: "How to install and maintain Proxmox"
last_update: "2023-09-09"
published: false
---
# How to install and maintain webmin in the containers/vm
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

1. [Overview](#overview)
2. [Installation](#installation)
3. [Create a Container](#create-a-container)

## Overview
> [Proxmox Virtual Environment](https://www.proxmox.com/en/proxmox-virtual-environment/overview) is a complete, open-source server management platform for enterprise virtualization. It tightly integrates the KVM hypervisor and Linux Containers (LXC), software-defined storage and networking functionality, on a single platform. 

## Installation
To Do

## Create a Container
1. Launch the `Proxmox UI`
2. Click on `Create CT`. The dialog `Create: LXC Container` opens.
3. In the `General` tab insert the following:
    * Node: <select the node to use>
    * CT ID: <automatic>
    * Hostname: <the hostname of the container>
    * Password: <the root password for the container>
    * Confirm password: <the root password for the container>
    * SSH public key: <your public key for SSH login. Use the `Load SSH Key File`.>
4. In the `Template` tab:
    * Storage: <select the storage with the template to use>
    * Template: <select the template to use>
5. In the `Disks` tab add the disk you want to have in the container
6. In the `CPU` tab define the CPU and limit you want to use for the container
7. In the `Memory` tab define the amount of memory you want to use in the container
8. In the `Network` tab define the network settings for the container
9. In the `DNS` tab:
    * DNS domain: <your.domain>
    * DNS servers: <ip address of your nameserver>
10. In the `Confirm` tab, review the options and click on `Finish`

The creation of the container starts. You should see a log. If everything is fine, you should receive a `TASK OK` message.

You can now close the `Task Viewer: CT xxx - Create` dialog and start your container.

Assuming you have provided your ssh key durig the creation, you can now connect to the container with the following command: `ssh root@<hostname.your.domain>`.

Update your newly installed system

1. apt update
2. apt upgrade

---
title: "Setting up a kubernetes learning environment"
description: "In this tutorial I describe how I configured my kubernetes learning environment."
last_update: "2020-04-30"
published: false
---
# How to setup a Kubernetes environment for learning purposes
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

So, you decided to give Kubernetes a go eh? You brave fool!

I made the same decision once, not exactly for pleasure but because I needed to. Here is how I set up my first k8s environment on a virtual machine.

## 1 - References
To completed this tutorial I consulted the following documentation:
* [Setting a Kubernetes cluster on Ubuntu VirtualBox: The lost guide](https://medium.com/@dcarrascal75/setting-a-kubernetes-cluster-on-ubuntu-virtualbox-the-lost-guide-73706e28bc5b) by [David Carrascal](https://medium.com/@dcarrascal75?source=post_page-----73706e28bc5b----------------------)
* [Kubernetes Documentation](https://kubernetes.io/docs/home/)


## 2 - Environment
My environment consist of a Lenovo T490, equipped with an Intel Core i7-8665U CPU and 40 GB of RAM.

The hypervisor used to run K8S is 'Oracle VirtualBox 6.1'.

The host OS is Windows 10.

The guest OS for K8S is Ubuntu Server 18.04 LTS.

[Putty](http://www.putty.org/) will be use to SSH login into the VMs.

> **Note**: You can choose to install any other OS versions, including a Desktop one. But since this is a learning environment, I think it is best to keep it as similar as possible to a production one (which include learning how to use the OS environment).

In this tutorial I assume you have the hypervisor installed and that you know how to create a VM in VirtualBox. I'll report only details about configuration of such VMs.

## 3 - Create the base VM
The first step is to create a base VM from which we'll later clone the K8S nodes. This basically means to create the VM and configure some features that will be useful later. I'll call this first VM `k8sBase`. My base machine has the following characteristics:

* Memory size = 1024 MB
* Create a virtual hard disk now
    * Hard Disk type : VDI
    * Dynamically allocated
    * Size 10GB

Now, start the newly created VM, load your ISO image and completed a basic configuration of the server. When presented with the option, `Install OpenSSH server` so that you will be able to remotely connect to this machine. Do not install any of the popular snaps: we are learning!

Once finished, restart your server and update/upgrade:

```
sudo apt-get update && sudo apt-get upgrade -y
```

### 3.1 - Install Docker
Instructions about how to install Docker for a Kubernetes environment are available at the official Kubernetes documentation page [Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#docker). They also point to the [Official Docker Documentation](https://docs.docker.com/engine/install/ubuntu/).

```
# Install Docker CE
## Set up the repository:
### Install packages to allow apt to use a repository over HTTPS
sudo apt-get update && sudo apt-get install -y \
  apt-transport-https ca-certificates curl software-properties-common gnupg2

### Add Docker’s official GPG key
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

### Add Docker apt repository.
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"

## Install Docker CE.
sudo apt-get update && sudo apt-get install -y \
  containerd.io=1.2.13-1 \
  docker-ce=5:19.03.8~3-0~ubuntu-$(lsb_release -cs) \
  docker-ce-cli=5:19.03.8~3-0~ubuntu-$(lsb_release -cs)

# Setup daemon.
sudo cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF

sudo mkdir -p /etc/systemd/system/docker.service.d

# Restart docker.
sudo systemctl daemon-reload
sudo systemctl restart docker

# Verifyt that Docker Engine is installed correctly
sudo docker run hello-world
```

### 3.2 - Configure the Kubernetes repositories

Add kubernetes to the apt repository list and add the Google's official pgp key

```
$ sudo sh -c "echo 'deb https://apt.kubernetes.io/ kubernetes-xenial main' >> /etc/apt/sources.list.d/kubernetes.list"

$ sudo sh -c "curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -"

$ sudo apt-get update
```

## 4 - Create your Kubernetes VM
Now that you have your base machine, you can close it to create your first kubernetes nodes. Name them "k8sMaster" and "k8sNode1" respectively.

![Fig. 1.1 - Cloning k8sMaster](/assets/img/k8s_learning/img01_1.png)
![Fig. 1.2 - Cloning k8sMaster](/assets/img/k8s_learning/img01_2.png)

## 5 - Setting up the Network configuration
We are going to provide each of the kubernetes nodes with a static host-only ip address to use for kubernetes, in addition to the one provided by the NAT that they will use to reach the internet.

This way, they will be able to talk to each other and we can reach them from the host machine.

Check the ip addresses you are using in your environment, because you don't want to overlap with your production environment.

If you don't have one already (or if you want to use a dedicated one for your kubernetes cluster), got to **Virtualbox > File > Host Network Manager > Create** and create an adapter. Let all the default values and check the DHCP checker.

![Fig. 2.1 - Creating the Host Adapter](/assets/img/k8s_learning/img02_1.png))
![Fig. 2.2 - Creating the Host Adapter](/assets/img/k8s_learning/img02_2.png))

Now enable the `Host-only Adapter` for `k8sMaster` and `k8sNode1`.

![Fig. 3 - Enable the Host Adapter](/assets/img/k8s_learning/img03.png))

Now start `k8sMaster` and check the network interfaces with `ifconfig -a`. Identify the one attached to the Host Adapter. If you are in doubt, note that when you created the adapter it provided you with a MAC Address you can use for this task. In my configuration, the right one is called `enp0s8`.

![Fig. 4 - Identify the interface](/assets/img/k8s_learning/img04.png))

Let's configure it with the static ip address `192.168.56.10` (check your configuration to know what address use in your configuration).

```
$ ls /etc/netplan
50-cloud-init.yaml

$ sudo vi /etc/netplan/50-cloud-init.yaml
```

Modify the content of the file as follows:

```
network:
    ethernets:
        enp0s3:
            dhcp4: true
        enp0s8:
            addresses:
                - 192.168.56.10/24
    version: 2
```

Then apply the configuration with `sudo netplan apply`. More examples about netplan are available [here](https://netplan.io/examples).

Do the same for `k8sNode1` configuring the ipaddress `192.168.56.11`.

Now, verify that:

1. you can reach internet from both the VM: `ping 1.1.1.1` - `ping google.com`
2. you can reach both VM from your host: `ping 192.168.56.10` `ping 192.168.56.11`
3. the two VM can ping each other

Now change the hostname of the two VM to reflect their role. On each VM run the following commands (using the appropriate hostname for each one):

```
$ sudo hostnamectl set-hostname k8sMaster
aizzi$ sudo reboot
```

## Generate keys to login from host
On the host, create a key-pair using `ssh-keygen`. It will be stored in `id_rsa` and `id_rsa.pub`.

Now ssh to `k8sMaster`:

```
$ sudo mkdir ~/.ssh
$ sudo chmod 700 ~/.ssh
$ sudo vi ~/.ssh/authorized_keys
    <paste the public key you copied in the clipboard and save the file. You can use the right mouse button to paste.>
$ sudo chmod 600 ~/.ssh/authorized_keys
$ sudo chown -R $(whoami):$(whoami) ~/.ssh/
```

Now you can login directly into the machines without providing the password: `ssh aizzi@192.168.56.10`.


Spiegare come connettersi usando SSH e Continuare da [Installing k8s master](https://medium.com/@dcarrascal75/setting-a-kubernetes-cluster-on-ubuntu-virtualbox-the-lost-guide-73706e28bc5b)
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

## Installing Ubuntu
I choose to install Ubuntu Server 18.04.4 in a VM on VirtualBox. I assume you'll do the same or solve your one issues.

## Installing Minikube
My starting point with K8S was the [official documentation](https://kubernetes.io/docs/setup/). It suggest to start your exploration of Kubernetes with [Minikube](https://kubernetes.io/docs/setup/learning-environment/minikube/). It runs a single-node Kubernetes cluster in the VM.

Detailed information about how to install `Minikube` are available on the [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) page. I followed those instructions and report here the problems I faced and how I solved them.

1. Start your VM with Ubuntu Server
2. Install and set up kubectl following the instruction [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-linux)

```
$> curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl

$> chmod +x ./kubectl

$> sudo mv ./kubectl /usr/local/bin/kubectl

$> kubectl version --client
```

> **Note**: Pay attention to that `LO`. That's the letter `O` not the number `0`.


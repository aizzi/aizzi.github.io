---
title: "01 - Webmin"
description: "Webmin help and references"
last_update: "2023-09-09"
published: false
---
# How to install and maintain webmin in the containers/vm
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

1. [Overview](#overview)
2. [Installation](#installation)

## Overview
> [Webmin](https://webmin.com/) is a web-based system administration tool for Unix-like servers, and services. Using it, it is possible to configure operating system internals, as well as modify, and control open-source apps.

## Installation
Reference: [Downloading and Installing](https://webmin.com/download/)

1. curl -o setup-repos.sh https://raw.githubusercontent.com/webmin/webmin/master/setup-repos.sh
2. sh setup-repos.sh
3. apt-get install --install-recommends webmin

Now you can connect to the web interface at the address `hostname.your.domain:10000`.
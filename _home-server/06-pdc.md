---
title: "05 - Primary Domain Controller"
description: "Install and Maintain the PDC"
last_update: "2023-09-09"
published: false
---
# How to install and maintain the Primary Domain Controller
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

## Overview
This section covers configuring Samba as a `Primary Domain Controller (PDC)`.

## References
- [Setting Up Samba as an Active Directory Domain Controller](https://wiki.samba.org/index.php/Setting_up_Samba_as_an_Active_Directory_Domain_Controller)

## Installation

For the remainder the following information are used:

- Hostname = `dc1`
- DC local IP Address = `192.168.1.7`
- Authentication Domain = `antmar.home.arpa`
- Top Level Domain = `home.arpa`




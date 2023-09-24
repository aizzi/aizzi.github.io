---
title: "04 - DHCP"
description: "DHCP help and references"
last_update: "2023-09-09"
published: false
---
# How to install and maintain Bind
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

## Overview


## Installation

1. Use `Webmin` to install the DHCP server
2. Modify the configuration file to look like this

```
default-lease-time 604800;
allow client-updates;
allow unknown-clients;
use-host-decl-names on;
ddns-updates on;
ddns-update-style interim;
authoritative;
log-facility local7;
key rndc-key {
	secret ZdJ32quZBh0mCsqiVBzPw65F/eZv4xeC1Gt2R5jMxAU=;
	algorithm hmac-sha256;
	}
zone antmar.home.arpa. {
	primary 192.168.4.2;
	key rndc-key;
	}
zone 4.168.192.in-addr.arpa. {
	primary 192.168.4.2;
	key rndc-key;
	}

# Personal Computers
subnet 192.168.4.0 netmask 255.255.255.0 {
	# ddns-updates on;
	option domain-search "antmar.home.arpa";
	option domain-name-servers ns1.antmar.home.arpa;
	option domain-name "antmar.home.arpa";
	option subnet-mask 255.255.255.0;
	ddns-rev-domainname "in-addr.arpa";
	ddns-domainname "antmar.home.arpa";
	range 192.168.4.100 192.168.4.199;
	option routers 192.168.4.1;
	}
```
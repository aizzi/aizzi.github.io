---
title: "03 - Bind"
description: "Bind help and references"
last_update: "2023-09-09"
published: false
---
# How to install and maintain Bind
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

1. [Overview](#overview)

## Overview
> [Bind9](https://www.isc.org/bind/) is a flexible, full-featured DNS system.

## Installation
References:
* [Installing and upgrading Bind](https://kb.isc.org/docs/aa-00648)
* [Running Bind9 and ISC-DHCP](https://blog.bigdinosaur.org/running-bind9-and-isc-dhcp/)

1. Use `Webmin` to install `Bind`
2. Generate the cryptographic hash to use with both DHCP and DNS
    `/usr/sbin/rndc-confgen -a`
3. Copy the content of the `rndc.key` file into the `/etc/bind/named.conf`

```
include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";
key rndc-key {
	algorithm hmac-sha256;
	secret "ZdJ32quZBh0mCsqiVBzPw65F/eZv4xeC1Gt2R5jMxAU=";
	};
controls {
	inet 127.0.0.1 port 953 allow { 127.0.0.1; } keys { rndc-key; };
	};
```

4. Edit the `/etc/bind/named.conf.options`

```
options {
        directory "/var/cache/bind";

        dnssec-validation auto;

        listen-on-v6 { any; };
        forwarders {
                1.1.1.1;
                1.0.0.1;
                };
        allow-query {
                192.168.1/24;
                192.168.4/24;
                127.0.0.1;
                };
        allow-transfer {
                192.168.1/24;
                192.168.4/24;
                127.0.0.1;
                };
};
```

5. Edit the `/etc/bin/named.conf.local` adding all the zones you need:

```
zone "1.168.192.in-addr.arpa" {
        type master;
        file "/var/lib/bind/192.168.1.rev";
        allow-update { key rndc-key; };
        };
zone "antmar.home.arpa" {
        type master;
        file "/var/lib/bind/antmar.home.arpa.hosts";
        allow-update {
                key rndc-key;
                };
        };
zone "4.168.192.in-addr.arpa" {
        type master;
        file "/var/lib/bind/192.168.4.rev";
        allow-update {
                key rndc-key;
                };
        };
```

6. The file `/etc/bind/named.conf.default-zones` should look like this already:

```
// prime the server with knowledge of the root servers
zone "." {
	type hint;
	file "/usr/share/dns/root.hints";
};

// be authoritative for the localhost forward and reverse zones, and for
// broadcast zones as per RFC 1912

zone "localhost" {
	type master;
	file "/etc/bind/db.local";
};

zone "127.in-addr.arpa" {
	type master;
	file "/etc/bind/db.127";
};

zone "0.in-addr.arpa" {
	type master;
	file "/etc/bind/db.0";
};

zone "255.in-addr.arpa" {
	type master;
	file "/etc/bind/db.255";
};
```

7. You can use the `Webmin` Ui to define the zones and the hosts, but the final configuration should look like this.
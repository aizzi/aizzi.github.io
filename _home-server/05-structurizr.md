---
title: "05 - Structurizr"
description: "Structurizr help and references"
last_update: "2023-09-09"
published: false
---
# How to install and maintain Bind
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

## Overview
> We use [Structurizr](https://docs.structurizr.com/onpremises) to store our architectural documentation.

## Installation

References
    * [How to install Java with Apt on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-22-04)
    * [A complete guide to install Tomcat on Linux](https://www.digitalocean.com/community/tutorials/install-tomcat-on-linux)

1. Create a container  to host the application (`structurizr.antmar.izzi.net`)

2. Install Java 17+  (wi install the version 19)
```
$ java -version
$ apt install openjdk-19-jre-headless
$ java -version
$ javac -version
$ apt install openjdk-19-jdk-headless
$ javac -version
```

3. Install and configure [Apache Tomcat 9.0.80](https://www.digitalocean.com/community/tutorials/install-tomcat-on-linux)
    * Setup the Tomcat User
    ```
    $ sudo useradd -r -m -U -d /opt/tomcat -s /bin/false tomcat
    ```
    * Download the Tomcat package
    ```
    $ wget -c https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.80/bin/apache-tomcat-9.0.80.tar.gz
    ```
    * Unpack the package in the /opt/tomcat
    ```
    $ tar xf apache-tomcat-9.0.80.tar.gz -C /opt/tomcat
    ```
    * Create a symbolic link to the installation directory. To update, unpack the new archive and modify the link:
    ```
    $ ln -s /opt/tomcat/apache-tomcat-9.0.80 /opt/tomcat/updated
    ```
    * Provide access to the tomcat user:
    ```
    $ chown -R tomcat: /opt/tomcat/*
    ```
    * Provide all executable flags to all scripts within the bin directory:
    ```
    $ sh -c 'chmod +x /opt/tomcat/updated/bin/*.sh'
    ```
    * Create the folder to store structurizr data:
    ```
    $ mkdir /structurizr/data
    $ chown tomcat:tomcat /structurizr/data
    ```
    * Create the `tomcat.service` unit for `systemd`
    ```
    $ vi /etc/systemd/system/tomcat.service
    ```
    enter the following and save (remember to check your JAVA_HOME)
    ```
    [Unit]
    Description=Apache Tomcat Web Application Container
    After=network.target

    [Service]
    Type=forking

    Environment="JAVA_HOME=/usr/lib/jvm/java-1.19.0-openjdk-amd64"
    Environment="CATALINA_PID=/opt/tomcat/updated/temp/tomcat.pid"
    Environment="CATALINA_HOME=/opt/tomcat/updated/"
    Environment="CATALINA_BASE=/opt/tomcat/updated/"
    Environment="CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC"
    Environment="JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom"
    Environment="STRUCTURIZR_DATA_DIRECTORY=/structurizr/data"

    ExecStart=/opt/tomcat/updated/bin/startup.sh
    ExecStop=/opt/tomcat/updated/bin/shutdown.sh

    User=tomcat
    Group=tomcat
    UMask=0007
    RestartSec=10
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
    * Reload the daemon
    ```
    $ systemctl daemon-reload
    ```
    * Start the Tomcat service
    ```
    $ systemctl start tomcat
    ```
    * Check the status with
    ```
    $ systemctl status tomcat
    ```
    * Enable the service to run on startup
    ```
    $ systemctl enable tomcat
    ```
    * If `ufw` is enabled, open the port 8080:
    ```
    $ ufw allow 8080/tcp
    ```
    * Check that Tomcat is running
    ```
    $ http://<YourIPAddress>:8080
    ```

4. Install `graphviz`:
```
$ apt install graphviz
```

5. Install `Structurizr`
    * Stop Tomcat
    ```
    $ systemctl stop tomcat
    ```
    * Delete the ROOT web application
    ```
    $ rm /opt/tomcat/updated/webapps/ROOT.war
    $ rm -r /opt/tomcat/updated/webapps/ROOT
    ```
    * Download the application
    ```
    $ cd /opt/tomcat/updated/webapps
    $ wget -c https://github.com/structurizr/onpremises/releases/download/v3142/structurizr-onpremises.war
    $ mv structurizr-onpremises.war ROOT.war
    $ chown tomcat:tomcat ROOT.war
    ```
    * Restart tomcat
    ```
    $ systemctl start tomcat
    ```
    * Verify that Structurizr is running:
    ```
    $ http:<YourIPAddress>:8080
    ```
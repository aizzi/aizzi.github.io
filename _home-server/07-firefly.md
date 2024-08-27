---
title: "07 - Firefly III "
description: "Install and Maintain Firefly III"
last_update: "2024-08-25"
published: false
---
# How to install and maintain Firefly III, a personal finance manager
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

## Install Firefly III

1. Create the container to host the application (`firefly.antmar.home.arpa`)
```
- Hostname = firefly
- Unprivileged Container = True
- Select a password for the root user
- Load the public key for ssh connection

- Template = ubuntu-22.04-standard

- Disk size = 50 GB

- Cores = 1

- Memory = 1024
- Swap = 512

- IPv4 = 192.168.1.15/24
- Gateway = 192.168.1.1

- DNS domain = antmar.home.arpa
- DNS server = 192.168.1.10
```

2. ssh into the new host

```
Host    firefly
        Hostname        firefly.antmar.home.arpa
        IdentityFile    ~/.ssh/id_ed25519
        User            root
```

3. Update the system and install the language packs. This may take a while.

```
apt update && apt upgrade -y
apt install language-pack-en-base
apt install language-pack-it-base
apt install language-pack-cs-base
locale-gen
```

4. Install `Nginx` and enable it to run on boot.

```
apt install nginx -y
systemctl start nginx
sudo systemctl enable nginx
```

If everything went fine, you should be able to connect to `http://firefly.antmar.home.arpa` and receive the `Welcome to nginx` message.

5. Install `MariaDB`, the DB used by `Firefly` to store data.

```
apt install mariadb-server -y
```

6. Secure `MariaDB` by running the provided security script:

```
mysql_secure_installation
```

Use the following answers:

```
- Enter current password for root: (Enter your SSH root user password)
- Switch to unix_socket authentication [Y/n]: Y
- Change the root password? [Y/n]: Y
- It will ask you to set new MySQL root password at this step. This can be different from the SSH root user password.
- Remove anonymous users? [Y/n] Y
- Disallow root login remotely? [Y/n] Y
- Remove test database and access to it? [Y/n] Y
- Reload privilege tables now? [Y/n] Y
```

7. Now log in to `MariaDB` and create a database and user for Firefly III

```
mysql -u root -p
CREATE DATABASE firefly;
GRANT ALL ON firefly.* TO 'firefly_user'@'localhost' IDENTIFIED BY 'strong_password';
FLUSH PRIVILEGES;
SELECT User FROM mysql.global_priv;
SHOW DATABASES;
EXIT;
```

Verify that the user `firefly` can access the database with the intended password:

```
mysql -u firefly -p
SHOW GRANTS FOR CURRENT_USER;
EXIT;
```

8. Now install `PHP 8.3`

```
apt install software-properties-common -y
add-apt-repository ppa:ondrej/php # Press enter when prompted.
apt update
apt install php8.3-common php8.3-cli php8.3-fpm php8.3-{curl,bz2,mbstring,intl}
apt install php8.3-{xml,mysql,bcmath,gd,curl,zip,ldap,gmp} -y
```

9. Configure `PHP 8.3` by setting the following options in `/etc/php/8.3/fpm/php.ini`

```
short_open_tag = On
cgi.fix_pathinfo = 0
memory_limit = 256M
upload_max_filesize = 100M
max_execution_time = 360
max_input_vars = 1500
date.timezone = Europe/Prague
```

Apply the new settings by restarting the PHP 8.3-FMP service:

```
systemctl restart php8.3-fpm
```

Finally, verify that PHP is installed and it's working:

```
php -v

PHP 8.3.10 (cli) (built: Aug  2 2024 15:31:15) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.3.10, Copyright (c) Zend Technologies
    with Zend OPcache v8.3.10, Copyright (c), by Zend Technologies
```

10. Install `Firefly III`

Check the latest version on https://version.firefly-iii.org/. We will be installing v6.1.19 here.

```
apt install curl

curl -LO https://github.com/firefly-iii/firefly-iii/releases/download/v6.1.19/FireflyIII-v6.1.19.tar.gz

curl -LO https://github.com/firefly-iii/firefly-iii/releases/download/v6.1.19/FireflyIII-v6.1.19.tar.gz.sha256

sha256sum -c FireflyIII-v6.1.19.tar.gz.sha256

mkdir /var/www/firefly-iii

tar -xvf FireflyIII-v6.1.19.tar.gz -C /var/www/firefly-iii

chown -R www-data:www-data /var/www/firefly-iii

chmod -R 775 /var/www/firefly-iii/storage
```

11. Configure `Firefly III`

```
cd /var/www/firefly-iii
sudo -u www-data cp .env.example .env
nano .env
```

Set the following parameters:

```
TZ=Europe/Prague
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=firefly
DB_USERNAME=firefly
DB_PASSWORD="<password set in point 7 above>"
```

12. Initialize the database

```
cd /var/www/firefly-iii/
php artisan firefly-iii:upgrade-database
php artisan firefly-iii:correct-database
php artisan firefly-iii:report-integrity
php artisan firefly-iii:laravel-passport-keys
```

13. Configure `Nginx`

```
cd /etc/nginx/sites-available
nano firefly.conf
ln -s /etc/nginx/sites-available/firefly.conf /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

Now, you should be able to navigate to `http://firefly.antmar.home.arpa` and finalize the setup.

## Install the Data Importer

You can check the latest version [here](https://version.firefly-iii.org/). We will be installing v1.5.4.

```
curl -LO https://github.com/firefly-iii/data-importer/releases/download/v1.5
.4/DataImporter-v1.5.4.tar.gz

curl -LO https://github.com/firefly-iii/data-importer/releases/download/v1.5.4/DataImporter-v1.5.4.tar.gz.sha256

sha256sum -c DataImporter-v1.5.4.tar.gz.sha256

mkdir /var/www/data-importer

tar -xvf DataImporter-v1.5.4.tar.gz -C /var/www/data-importer

chown -R www-data:www-data /var/www/data-importer
chmod -R 775 /var/www/data-importer/storage

cd /var/www/data-importer

cp .env.example .env

nano .env
FIREFLY_III_URL=http://firefly.antmar.home.arpa  << Modify this line and save the file>>

chown -R www-data:www-data /var/www/data-importer
chmod -R 775 /var/www/data-importer/storage

cd /etc/nginx/sites-available

nano importer.conf
```

Copy the following code:

```
server {
       listen       80;
       listen       [::]:80;
       server_name  firefly-importer.antmar.home.arpa;
       root         /var/www/data-importer/public;
       index index.html index.htm index.php;
       location / {
               try_files $uri /index.php$is_args$args;
               proxy_buffer_size          128k;
               proxy_buffers              4 256k;
               proxy_busy_buffers_size    256k;
               autoindex on;
               sendfile off;
      }
       location ~ \.php$ {
       fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
       fastcgi_index index.php;
       fastcgi_read_timeout 240;
       fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
       include fastcgi_params;
       fastcgi_split_path_info ^(.+.php)(/.+)$;
       fastcgi_buffers 16 32k;
       fastcgi_buffer_size 64k;
       fastcgi_busy_buffers_size 64k;
       }
   }
```

Save the file and exit and restart nginx:

```
ln -s /etc/nginx/sites-available/importer.conf /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

Now, connect to `http://firefly-importer.antmar.home.arpa` and follow the instructions on screen.
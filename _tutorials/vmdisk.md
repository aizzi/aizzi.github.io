---
title: "How to expand the disk of a VM guest"
description: "How to expand the disk available to a VirtualBox VM guest"
last_update: "2020-08-03"
published: true
---
# How to expand the disk of a VirtualBox VM guest
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}


aizzi@k8sMaster:~$ sudo apt-get install cloud-guest-utils
Reading package lists... Done
Building dependency tree
Reading state information... Done
cloud-guest-utils is already the newest version (0.30-0ubuntu5).
cloud-guest-utils set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

---

aizzi@k8sMaster:~$ sudo swapoff -a

---

aizzi@k8sMaster:~$ sudo parted
GNU Parted 3.2
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print all
Warning: Not all of the space available to /dev/sda appears to be used, you can fix the GPT to use all of the space (an extra 20971520 blocks) or continue
with the current setting?
Fix/Ignore? F
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name  Flags
 1      1049kB  2097kB  1049kB                     bios_grub
 2      2097kB  10.7GB  10.7GB  ext4


Warning: Unable to open /dev/sr0 read-write (Read-only file system).  /dev/sr0 has been opened read-only.
Error: /dev/sr0: unrecognised disk label
Model: VBOX CD-ROM (scsi)
Disk /dev/sr0: 59.8MB
Sector size (logical/physical): 2048B/2048B
Partition Table: unknown
Disk Flags:

(parted) quit

---

aizzi@k8sMaster:~$ df -k .
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda2       10252564 8128736   1583312  84% /

---

aizzi@k8sMaster:~$ sudo parted
GNU Parted 3.2
Using /dev/sda
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print all
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name  Flags
 1      1049kB  2097kB  1049kB                     bios_grub
 2      2097kB  10.7GB  10.7GB  ext4


Warning: Unable to open /dev/sr0 read-write (Read-only file system).  /dev/sr0 has been opened read-only.
Error: /dev/sr0: unrecognised disk label
Model: VBOX CD-ROM (scsi)
Disk /dev/sr0: 59.8MB
Sector size (logical/physical): 2048B/2048B
Partition Table: unknown
Disk Flags:

(parted) quit

---

aizzi@k8sMaster:~$ sudo growpart /dev/sda 2
CHANGED: partition=2 start=4096 old: size=20965376 end=20969472 new: size=41938911,end=41943007

---

aizzi@k8sMaster:~$ sudo resize2fs /dev/sda2
resize2fs 1.44.1 (24-Mar-2018)
Filesystem at /dev/sda2 is mounted on /; on-line resizing required
old_desc_blocks = 2, new_desc_blocks = 3
The filesystem on /dev/sda2 is now 5242363 (4k) blocks long.

---

aizzi@k8sMaster:~$ df -k .
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda2       20574780 8306584  11308344  43% /
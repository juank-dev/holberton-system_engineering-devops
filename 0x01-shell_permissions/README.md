# **0x01. Shell, permissions**
> ## Foundations - System engineering & DevOps ― Bash

![Alt](https://www.oreilly.com/library/view/learning-linux-shell/9781788993197/assets/99c02f63-3014-4df0-8990-b9474944f298.jpg)

## Permissions

* What do the commands chmod, sudo, su, chown, chgrp do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why can’t a normal user chown a file
* How to run a command with root privileges
* How to change user ID or become superuser

## Other Man Pages

* How to create a user
* How to create a group
* How to print real and effective user and group IDs
* How to print the groups a user is in
* How to print the effective userid

This repository will cover the following commands:

* **chmod** - modify file access rights
* **su** - temporarily become the superuser
* **sudo** - temporarily become the superuser
* **chown** - change file ownership
* **chgrp** - change a file's group ownership

### File Permissions

On a Linux system, each file and directory is assigned access rights for the owner of the file, the members of a group of related users, and everybody else. Rights can be assigned to read a file, to write a file, and to execute a file (i.e., run the file as a program).


* 777 | **(rwxrwxrwx)** No restrictions on permissions. Anybody may do anything. Generally not a desirable setting.
* 755 | **(rwxr-xr-x)** The file's owner may read, write, and execute the file. All others may read and execute the file. This setting is common for programs that are used by all users.
* 700 | **(rwx------)** The file's owner may read, write, and execute the file. Nobody else has any rights. This setting is useful for programs that only the owner may use and must be kept private from others.
* 666 | **(rw-rw-rw-)** All users may read and write the file.
* 644 | **(rw-r--r--)** The owner may read and write a file, while all others may only read the file. A common setting for data files that everybody may read, but only the owner may change.
* 600 | **(rw-------)** The owner may read and write a file. All others have no rights. A common setting for data files that the owner wants to keep private.

